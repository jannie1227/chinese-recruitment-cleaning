"""Check this release's file boundary; not a general-purpose data-loss scanner."""
import ast
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_EXAMPLES = {'examples/metadata_v1211_synthetic.csv', 'examples/descriptions_synthetic.csv'}
FORBIDDEN = {'.gz', '.zip', '.sqlite', '.db', '.parquet', '.dta', '.xlsx', '.pem', '.key', '.jsonl'}


def main():
    tracked = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, check=False)
    if tracked.returncode == 0 and tracked.stdout:
        paths = [ROOT / x.decode('utf-8') for x in tracked.stdout.split(b'\0') if x]
    else:
        paths = [p for p in ROOT.rglob('*') if p.is_file() and not any(x in {'.git', '__pycache__', '.venv'} for x in p.relative_to(ROOT).parts)]
    errors = []
    secrets = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{24,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
    local_paths = re.compile(r'/(?:Users|Volumes)/[A-Za-z0-9\u3400-\u9fff]')
    for path in paths:
        name = path.relative_to(ROOT).as_posix()
        if path.suffix in FORBIDDEN or any(x in {'private', 'data', 'outputs', 'output', 'private_resources'} for x in path.relative_to(ROOT).parts):
            errors.append(name + ': excluded data or credential path')
            continue
        if path.stat().st_size > 1024 * 1024:
            errors.append(name + ': unexpected large file')
            continue
        try:
            text = path.read_text(encoding='utf-8-sig')
        except UnicodeError:
            errors.append(name + ': unexpected binary file')
            continue
        if secrets.search(text):
            errors.append(name + ': credential marker')
        if local_paths.search(text):
            errors.append(name + ': developer filesystem path')
        if path.suffix == '.csv' and name not in ALLOWED_EXAMPLES:
            errors.append(name + ': CSV is not an approved synthetic fixture')
    tree = ast.parse((ROOT / 'job_description_cleaning.py').read_text(encoding='utf-8'))
    resources = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(x, ast.Name) and x.id == 'BUNDLED_RESOURCES' for x in n.targets))
    if resources != {'r10_reviews': [], 'v5_reviews': [], 'v7_reviews': []}:
        errors.append('description: private adjudications embedded in source')
    source_manifest = json.loads((ROOT / 'docs/source_manifest.json').read_text(encoding='utf-8'))
    for name, expected in source_manifest['metadata_sources'].items():
        actual = hashlib.sha256((ROOT / 'metadata_rules' / name).read_bytes()).hexdigest()
        if actual != expected:
            errors.append('metadata_rules/' + name + ': frozen-source checksum mismatch')
    modules = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(x, ast.Name) and x.id == 'MODULE_SOURCES' for x in n.targets))
    actual_modules = {name: hashlib.sha256(text.encode('utf-8')).hexdigest() for name, text in sorted(modules.items())}
    if actual_modules != source_manifest['description_rule_sources']:
        errors.append('description: frozen semantic modules changed')
    for filename in ALLOWED_EXAMPLES:
        with (ROOT / filename).open(encoding='utf-8-sig', newline='') as handle:
            rows = list(csv.DictReader(handle))
        if 'metadata_' in filename and not all(r['record_id'].startswith('SYNTH_') for r in rows):
            errors.append(filename + ': non-synthetic identity')
        if 'descriptions_' in filename and not all(r['来源'] == '人工构造示例' for r in rows):
            errors.append(filename + ': non-synthetic source')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('PASS_PUBLIC_FILE_BOUNDARY_AND_FROZEN_RULE_HASHES', len(paths), 'files')


if __name__ == '__main__':
    main()
