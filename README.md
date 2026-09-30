# Chinese Recruitment Cleaning

面向中文招聘数据的两条可追溯清洗流程：一条整理职位名称与分类元数据，供后续职业匹配使用；另一条从职位描述中提取职责正文，供后续文本分析使用。两条流程分别保留原记录身份、版本信息与质量证据。

Chinese job-metadata revisions and responsibility-text cleaning, with preserved record identities, synthetic examples, local audit-resource interfaces, and explicit quality limits.

公开软件版本：**0.1.0**。研究采用版本分别为 **v1.2.12** 与 **R12 V7**。运行环境为 **CPython 3.12.x**，仅使用标准库，无须安装第三方 Python 包。

## 两条流程

| 模块 | 当前研究采用版本 | 输入 | 主要输出 | 方法文档 |
| --- | --- | --- | --- | --- |
| 职位匹配前清洗 | v1.2.12 常规清洗交付版 | v1.2.11 封存格式的 31 列元数据表 | 修订主表、匹配任务字典、record_id 桥接表、匹配输入分流 | [职位元数据清洗](docs/job-metadata-cleaning.md) |
| 岗位描述清洗 | R12 V7，2026-09-29 定稿 | 原始 2.0 CSV 中的职位描述与记录身份 | responsibility_text、原文哈希与记录身份 | [岗位描述清洗](docs/job-description-cleaning.md) |

职位匹配前清洗保留技术词、产品材料和实际职能限定，记录招聘噪声处理及分类证据的允许用途。岗位描述清洗区分实际任务、应聘要求、招聘宣传和来源损伤，保留可回查的正文与原文对应关系。

## 研究规模与连接方式

两条研究流程均覆盖 4,073,781 条招聘记录。职位匹配前清洗交付字典包含 2,112,545 个去重匹配项；岗位描述 R12 V7 包含 3,754,886 条非空职责正文和 318,895 条空正文。

使用 `record_id` 回连原记录。职位字典通过 `final_match_item_id` 连接桥接表，字典中的 `freq` 表示招聘记录频数。岗位描述中的空正文保留记录身份，并在下游记录文本缺失。精确相同正文可以共用计算结果，但原记录及其权重仍须保留。

## 公开内容与数据获取

公开内容为实际采用的修订／清洗实现、自建规则、方法说明、依赖配置、测试和人工构造示例。真实原始招聘数据、清洗后的全量记录、企业级结果、私有复核原文及凭据不随公开仓库分发。使用者自行准备有权处理的数据。

Python 源代码（含代码中的规则实现）使用 [MIT](LICENSE)；人工示例与独立自建规则表使用 [CC BY 4.0](LICENSE-DATA)，文档可在两者中任选其一。第三方数据不因代码开源而获得上述许可。

## 快速运行人工示例

在仓库根目录运行，输出目录使用尚不存在的新路径：

```sh
python3.12 job_metadata_cleaning.py --input examples/metadata_v1211_synthetic.csv --output-dir outputs/metadata-example
python3.12 job_description_cleaning.py --input examples/descriptions_synthetic.csv --output-dir outputs/description-example --allow-other-input --workers 2
```

Windows 上可将 `python3.12` 替换为 `py -3.12`。所有示例均为人工构造，不是从真实招聘记录抽样得到的。

元数据入口生成 `cleaned_metadata.csv.gz`（37 列）、`job_match_dictionary.csv.gz`（25 列）、`record_match_bridge.csv.gz`（5 列）和 `provenance.json`。公开桥接表只保存本次连接所需字段；私有研究交付中的旧版桥接追溯列不在这一入口中重建。`ruleset_hash` 记录公开入口、冻结规则和本地待讨论配置的指纹，与私有研究交付哈希分别记录。

岗位描述入口生成 `cleaned/part_*.csv.gz`、`manifest.json` 和 `progress.json`。示例及其他输入标记为 `COMPLETE_OTHER_INPUT`，不会被标记为研究语料全量复现通过。岗位描述入口支持 `--resume`；更换代码、输入或本地定案资源后不能继续使用旧目录。

## 复现条件

R12 V7 的私有研究包曾在原始语料上完成六个研究字段的全量逐条一致性检查。公开版保留规则实现，将 19 项真实原文定案资源改为通过 `--review-resources` 从本地 JSON 加载；这些资源不在本仓库内。原始研究语料的完整复现同时需要原始 CSV 和对应私有定案配置。提供自有 CSV 时可使用 `--allow-other-input`，结果不认证为原研究语料。

v1.2.12 公开入口提供从 v1.2.11 封存表到 v1.2.12 的末轮修订及分流，包含实际调用的九个规则模块。研究语料还需通过 `--pending-rules` 加载对应 27 项待讨论组合。该入口不包含原始招聘数据至 v1.2.11 的早期清洗与私有企业证据链，不能称为原始数据到终版的独立复现。

详细输入契约、私有配置格式和版本来源见两份方法文档及 [源码指纹清单](docs/source_manifest.json)。

## 验证与目录结构

```sh
python3.12 scripts/check_public_files.py
python3.12 -m unittest discover -s tests -v
```

七项公开回归检查覆盖原字段与记录保留、稳定匹配 ID、字典频数、疑难岗位分流、禁用分类证据、并发加载本地资源、续跑身份及输出篡改检查。GitHub Actions 在 Linux、Windows 和 macOS 上运行人工示例。

另在本地对全部 19 项私有定案原文及 4 项人工输入比较公开版和原程序，正文与生效阶段差异为 0。对应的 [封装验证摘要](docs/release_validation.json) 只包含聚合结果，不包含原文。这不是新一轮全量清洗或准确率评估。

```text
job_metadata_cleaning.py       # v1.2.11 → v1.2.12 修订入口
metadata_rules/               # 九个原始规则模块
job_description_cleaning.py    # R12 V7 公开清洗入口
examples/                     # 两套人工输入
docs/                         # 方法、质量和源码指纹
tests/                        # 公开回归检查
scripts/check_public_files.py # 公开文件边界检查
.github/workflows/ci.yml       # 跨平台自动检查
```

## 质量与适用范围

v1.2.12 是常规清洗工作基线，尚无新版独立样本外准确率。历史 v1.2.11 的两个 AI 复核随机组联合正确率为 87.5% 和 86.0%，不能作为 v1.2.12 的准确率。进入候选匹配路线也不代表已经确定最终 SOC 编码。

R12 V7 最近一次 200 条 AI 辅助随机抽查中，146 条未见问题、8 条轻微问题、40 条实质错误、6 条边界争议；保守记录级无实质错误率为 77.0%，95% 抽样区间为 70.7%—82.3%。用户在保留这些质量结论的前提下停止继续清洗，相关新发现没有在定稿后修复。

复现结果一致与文本内容准确是两项不同检验。上述复核均不属于人工金标准。本仓库的拟公开范围止于清洗，不包含已完成的 SOC 赋码、向量生成或语义漂移指标计算。

## 文档组织参考

沿用既有 `Chinese Job Title Cleaning` 开源设计中的输入输出契约、字段字典、规则说明、人工示例、测试和许可边界，并更新到实际采用的两套流程。具体冻结源码及公开封装调整在源码指纹清单中记录。

另参考 [Job Posting Salary Prediction](https://github.com/nginyc/job-posting-salary-prediction) 的 README 组织方式，分别介绍项目目标、清洗、预处理、复现与来源。该链接是本轮另行检索获得的排版参考；两套流程的规则和质量结论仍以本项目材料为准。

## 引用

作者账号：[@jannie1227](https://github.com/jannie1227)。引用信息见 [CITATION.cff](CITATION.cff)。引用时请同时说明公开软件版本和所采用的研究规则版本。
