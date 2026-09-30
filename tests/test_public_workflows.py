import csv
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import job_metadata_cleaning as metadata


def read_csv(path):
    opener = gzip.open if Path(path).suffix == '.gz' else Path.open
    with opener(path, 'rt' if Path(path).suffix == '.gz' else 'r', encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


class PublicWorkflows(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write_metadata(self, rows, filename='input.csv'):
        path = self.directory / filename
        with path.open('w', encoding='utf-8-sig', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=metadata.HEADERS, lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
        return path

    def description_run(self, output, *extra, success=True):
        command = [sys.executable, str(ROOT / 'job_description_cleaning.py'), '--input', str(ROOT / 'examples/descriptions_synthetic.csv'), '--output-dir', str(output), '--allow-other-input', '--workers', '2', *extra]
        result = subprocess.run(command, text=True, capture_output=True, timeout=60)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def test_metadata_identity_dictionary_and_conservative_routes(self):
        before = read_csv(ROOT / 'examples/metadata_v1211_synthetic.csv')
        out = self.directory / 'metadata'
        manifest = metadata.run(ROOT / 'examples/metadata_v1211_synthetic.csv', out)
        after = read_csv(out / 'cleaned_metadata.csv.gz')
        self.assertEqual(len(after), len(before))
        for old, new in zip(before, after):
            for index in metadata.PROTECTED:
                self.assertEqual(old[metadata.HEADERS[index]], new[metadata.HEADERS[index]])
        self.assertEqual(after[2]['clean_title'], '组装工')
        self.assertEqual(after[2]['soc_input_route'], 'REVIEW_REQUIRED')
        self.assertEqual(after[3]['soc_input_route'], 'MULTI_OCCUPATION')
        self.assertEqual(after[3]['match_title_core'], '')
        self.assertEqual(after[4]['soc_input_route'], 'NO_OCCUPATION')
        dictionary = read_csv(out / 'job_match_dictionary.csv.gz')
        bridge = read_csv(out / 'record_match_bridge.csv.gz')
        self.assertEqual(sum(int(row['freq']) for row in dictionary), len(before))
        self.assertEqual(len(bridge), len(before))
        self.assertEqual(after[0]['final_match_item_id'], after[1]['final_match_item_id'])
        self.assertEqual(manifest['rows'], 5)
        ids = {row['final_match_item_id'] for row in dictionary}
        self.assertTrue(all(row['final_match_item_id'] in ids for row in bridge))
        reversed_input = self.write_metadata(list(reversed(before)))
        other = self.directory / 'reversed'
        metadata.run(reversed_input, other)
        reversed_rows = read_csv(other / 'cleaned_metadata.csv.gz')
        self.assertEqual({r['record_id']:r['final_match_item_id'] for r in after}, {r['record_id']:r['final_match_item_id'] for r in reversed_rows})

    def test_metadata_duplicate_ids_abort_without_publishing(self):
        rows = read_csv(ROOT / 'examples/metadata_v1211_synthetic.csv')
        rows[1]['record_id'] = rows[0]['record_id']
        path = self.write_metadata(rows)
        out = self.directory / 'invalid'
        with self.assertRaisesRegex(ValueError, 'Duplicate record_id'):
            metadata.run(path, out)
        self.assertFalse(out.exists())
        self.assertFalse(list(self.directory.glob('.metadata-publish-*')))

    def test_private_pending_rules_change_route_and_identity(self):
        rows = read_csv(ROOT / 'examples/metadata_v1211_synthetic.csv')
        raw = rows[0]
        key = metadata.canonical([raw[name] for name in ['招聘岗位_raw','招聘类别_raw','初级分类_raw','上市公司行业_raw']])
        config = self.directory / 'local.json'
        config.write_text(json.dumps({key:'AI_KNOWN_UNRESOLVED'}, ensure_ascii=False), encoding='utf-8')
        out = self.directory / 'pending'
        metadata.run(ROOT / 'examples/metadata_v1211_synthetic.csv', out, config)
        after = read_csv(out / 'cleaned_metadata.csv.gz')
        self.assertEqual(after[0]['known_pending_issue'], 'AI_KNOWN_UNRESOLVED')
        self.assertEqual(after[0]['soc_input_route'], 'REVIEW_REQUIRED')
        self.assertEqual(after[1]['final_match_item_id'], after[0]['final_match_item_id'])

    def test_conflicting_category_hints_remain_disabled(self):
        row = read_csv(ROOT / 'examples/metadata_v1211_synthetic.csv')[0]
        row.update(category_use_status='conflict', occupation_hint_soc_use='disabled', occupation_category_hint='人工反例提示')
        out = self.directory / 'conflict'
        metadata.run(self.write_metadata([row]), out)
        after = read_csv(out / 'cleaned_metadata.csv.gz')[0]
        self.assertEqual(after['occupation_hint_auxiliary'], '')
        self.assertEqual(after['occupation_hint_candidates_only'], '')

    def test_description_extracts_tasks_preserves_empty_records_and_resume(self):
        out = self.directory / 'description'
        self.description_run(out)
        rows = read_csv(out / 'cleaned/part_00001.csv.gz')
        self.assertEqual([r['record_id'] for r in rows], [f'R2_{i:010d}' for i in range(1, 6)])
        self.assertEqual(rows[0]['responsibility_text'], '负责设备安装与维护')
        self.assertEqual(rows[1]['responsibility_text'], '编制项目进度计划,协调项目实施')
        self.assertEqual(rows[2]['responsibility_text'], rows[0]['responsibility_text'])
        self.assertEqual(rows[3]['responsibility_text'], '')
        self.assertEqual(rows[4]['responsibility_text'], '')
        manifest = json.loads((out / 'manifest.json').read_text())
        self.assertEqual(manifest['status'], 'COMPLETE_OTHER_INPUT')
        self.assertFalse(manifest['frozen_reference_match'])
        self.assertFalse(manifest['private_reviews_loaded'])
        self.assertEqual(manifest['unique_originals_computed'], 4)
        original = (out / 'cleaned/part_00001.csv.gz').read_bytes()
        result = self.description_run(out, '--resume')
        self.assertIn('no new reconstruction performed', result.stdout)
        self.assertEqual(original, (out / 'cleaned/part_00001.csv.gz').read_bytes())
        self.description_run(out, success=False)

    def test_description_spawn_loads_local_resources_and_resume_checks_identity(self):
        raw = read_csv(ROOT / 'examples/descriptions_synthetic.csv')[0]['职位描述']
        config = self.directory / 'reviews.json'
        resources = {'r10_reviews':[{'raw':raw,'raw_sha256':hashlib.sha256(raw.encode()).hexdigest(),'decisions':[]}], 'v5_reviews':[], 'v7_reviews':[]}
        config.write_text(json.dumps(resources, ensure_ascii=False), encoding='utf-8')
        out = self.directory / 'with-private'
        self.description_run(out, '--review-resources', str(config))
        manifest = json.loads((out / 'manifest.json').read_text())
        self.assertTrue(manifest['private_reviews_loaded'])
        self.assertEqual(manifest['review_resources_sha256'], hashlib.sha256(config.read_bytes()).hexdigest())
        self.assertEqual(read_csv(out / 'cleaned/part_00001.csv.gz')[0]['responsibility_text'], '负责设备安装与维护')
        resources['r10_reviews'].clear()
        config.write_text(json.dumps(resources), encoding='utf-8')
        result = self.description_run(out, '--review-resources', str(config), '--resume', success=False)
        self.assertIn('Existing output belongs to different code or input', result.stderr)

    def test_description_resume_rejects_tampered_outputs(self):
        out = self.directory / 'tampered'
        self.description_run(out)
        with (out / 'cleaned/part_00001.csv.gz').open('ab') as handle:
            handle.write(b'tampered')
        result = self.description_run(out, '--resume', success=False)
        self.assertIn('checksum failed', result.stderr)


if __name__ == '__main__':
    unittest.main()
