# 中文招聘清洗工具：分类导航

当前工具已拆为两个独立、可安装的公开仓库。两者默认只需要使用者自己的输入，规则随安装包提供。

| 清洗内容 | 独立仓库 | Python 调用 |
| --- | --- | --- |
| 职位名称及招聘类别、初级分类、行业元数据 | [chinese-job-title-cleaning](https://github.com/jannie1227/chinese-job-title-cleaning) | `clean_title`、`clean_record`、`clean_records` |
| 岗位描述中的职责正文 | [chinese-job-description-cleaning](https://github.com/jannie1227/chinese-job-description-cleaning) | `clean_description`、`clean_record`、`clean_records` |

## 安装

使用 Python 3.12.x：

```sh
python -m pip install "git+https://github.com/jannie1227/chinese-job-title-cleaning.git@v0.1.0"
python -m pip install "git+https://github.com/jannie1227/chinese-job-description-cleaning.git@v0.1.0"
```

也可从各自 Releases 下载 wheel 后本地安装。两个仓库分别提供普通 CSV 入口、代码注释、输入输出说明、人工示例及跨平台安装检查。

## 数据与研究版本

公开展示全部使用人工构造数据。原始招聘数据、真实逐记录输出和私有定案材料不在公开仓库内。输入只在调用者本地处理。

通用职位接口使用既有公开词法核心，原研究 v1.2.12 封存修订单独保留。岗位描述默认执行 R12 V7 公开规则；原语料严格复现还需数据持有者自己的原始 CSV 与本地定案配置。条件与历史质量结论分别在两个仓库中说明。

## 历史发布

本仓库首版 [v0.1.0](https://github.com/jannie1227/chinese-recruitment-cleaning/releases/tag/v0.1.0) 保留，供追溯原合并发布的代码和方法说明。当前可直接安装和调用的版本请使用上面的两个独立仓库。
