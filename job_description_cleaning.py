#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frozen R12 V7 cleaning, entirely contained in this file.

Run: python reproduce_cleaning.py
Public rules contain no private reviews. Exact corpus reproduction additionally
requires the separately held local review-resources JSON. No network or pip packages.
This reproduces cleaning, not embeddings or semantic-drift indicators.
"""
BUNDLED_RESOURCES = {'r10_reviews': [], 'v5_reviews': [], 'v7_reviews': []}
BUNDLED_PROVENANCE = [{'module': 'jdclean_unified.responsibility_repair_r11', 'original_file': '工作区/jdclean_unified/responsibility_repair_r11.py', 'original_sha256': '7933d94f0c28c40bf57a1ff0c5af1e304ff74317a10cfe8220abbdd54d7962e3', 'embedded_sha256': '7933d94f0c28c40bf57a1ff0c5af1e304ff74317a10cfe8220abbdd54d7962e3', 'packaging_changes': []}, {'module': 'tools.r11_io', 'original_file': '工作区/tools/r11_io.py', 'original_sha256': '69b2ff04d98f5e2c5c3cf80494ecb8258599421fe27197a77713324820c6aa04', 'embedded_sha256': '69b2ff04d98f5e2c5c3cf80494ecb8258599421fe27197a77713324820c6aa04', 'packaging_changes': []}, {'module': 'tools.r11_engine', 'original_file': '工作区/tools/r11_engine.py', 'original_sha256': '7e737ebe940d1767ff7d2ef427e4d142349529b26aeb23a8a4435469f9b4437e', 'embedded_sha256': 'ccc78232262a47e4653914228459f420cecbf6e5a1091157a3cb6fd9f0288213', 'packaging_changes': ['Replace a file read with the identical embedded frozen JSON resource; no decision contents changed.', 'Remove mutation of the host Python import path.']}, {'module': 'tools.r11_headings_v4', 'original_file': '工作区/tools/r11_headings_v4.py', 'original_sha256': '020f5c416dca01c994a24c6533fe6fef489b04e10b58155891552735ba2677e4', 'embedded_sha256': '020f5c416dca01c994a24c6533fe6fef489b04e10b58155891552735ba2677e4', 'packaging_changes': []}, {'module': 'tools.r11_policy_v2', 'original_file': '工作区/tools/r11_policy_v2.py', 'original_sha256': '552745856c2a317348cfeef4c21bd91a199789e9f03b1d1449f7096627bc5172', 'embedded_sha256': '552745856c2a317348cfeef4c21bd91a199789e9f03b1d1449f7096627bc5172', 'packaging_changes': []}, {'module': 'tools.r11_policy_v3', 'original_file': '工作区/tools/r11_policy_v3.py', 'original_sha256': 'dae4bd90fb022f093d1926cf11bd52f9c698c39e27e0073b264ee241fff5da19', 'embedded_sha256': 'dae4bd90fb022f093d1926cf11bd52f9c698c39e27e0073b264ee241fff5da19', 'packaging_changes': []}, {'module': 'tools.r11_policy_v4', 'original_file': '工作区/tools/r11_policy_v4.py', 'original_sha256': 'eb875a26e8f31d65622f006987a840a98355416c6a9a4907bfa39bece084b7bc', 'embedded_sha256': 'eb875a26e8f31d65622f006987a840a98355416c6a9a4907bfa39bece084b7bc', 'packaging_changes': []}, {'module': 'tools.r11_policy_v5', 'original_file': '工作区/tools/r11_policy_v5.py', 'original_sha256': '2fbd3088c4e58a82c6f6a8be3cd2416efbd612b296cefd7aee20f0c1c06d3a13', 'embedded_sha256': '2fbd3088c4e58a82c6f6a8be3cd2416efbd612b296cefd7aee20f0c1c06d3a13', 'packaging_changes': []}, {'module': 'tools.r11_verify_release', 'original_file': '工作区/tools/r11_verify_release.py', 'original_sha256': 'dd69ae64177824475ed3b4ac3508462c56195fc48e540e52f2af99c9fefe4417', 'embedded_sha256': '1799a6d1a9f8f062263660351765c8488fcb7fc33f30aa4d70c198ca1accb30a', 'packaging_changes': ['Only the unchanged pure replay() function is embedded; retired disk/database replay driver and Unix fcntl imports are not needed.']}, {'module': 'tools.r12_policy', 'original_file': '工作区/tools/r12_policy.py', 'original_sha256': 'a7f152c7f3d366b0ba4c6cb24d235e44e4864e4475615572bfd972867afcda2c', 'embedded_sha256': 'a7f152c7f3d366b0ba4c6cb24d235e44e4864e4475615572bfd972867afcda2c', 'packaging_changes': []}, {'module': 'tools.r12_policy_v2', 'original_file': '工作区/tools/r12_policy_v2.py', 'original_sha256': '380db6e2c14459d9b37c4038262e2b450ff0fced8313bab26260a269b1e94599', 'embedded_sha256': '380db6e2c14459d9b37c4038262e2b450ff0fced8313bab26260a269b1e94599', 'packaging_changes': []}, {'module': 'tools.r12_policy_v3', 'original_file': '工作区/tools/r12_policy_v3.py', 'original_sha256': 'e9f94516ac72b85e9ffbd43fa038dd01238146a5b90c3e4e41d3bb5fe08e1b63', 'embedded_sha256': 'e9f94516ac72b85e9ffbd43fa038dd01238146a5b90c3e4e41d3bb5fe08e1b63', 'packaging_changes': []}, {'module': 'tools.r12_policy_v4', 'original_file': '工作区/tools/r12_policy_v4.py', 'original_sha256': 'bdf279d3bcade6ddef27f996f202ced573f78a5c336c6f15f682afa58373cdba', 'embedded_sha256': 'bdf279d3bcade6ddef27f996f202ced573f78a5c336c6f15f682afa58373cdba', 'packaging_changes': []}, {'module': 'tools.r12_policy_v5', 'original_file': '工作区/tools/r12_policy_v5.py', 'original_sha256': 'bd00228b0fa3516951043ef9b24c3e81d7ddd71c9c053a0a7eb2d8c2a5b32448', 'embedded_sha256': 'c36cfdfdb58687a6a7060f869c2170b30504fa76850ec2d607fe2b4cebc0fede', 'packaging_changes': ['Replace a file read with the identical embedded frozen JSON resource; no decision contents changed.']}, {'module': 'tools.r12_policy_v6', 'original_file': '工作区/tools/r12_policy_v6.py', 'original_sha256': 'c01349c381bfd8a1caaa90a9d1b315b20c6397259c960e6441dc52cc699c117d', 'embedded_sha256': 'c01349c381bfd8a1caaa90a9d1b315b20c6397259c960e6441dc52cc699c117d', 'packaging_changes': []}, {'module': 'tools.r12_policy_v7', 'original_file': '工作区/tools/r12_policy_v7.py', 'original_sha256': 'bd972ae95653fda60749e9cb3f75d8f7d33ffb0f2afde3fa4ddcfeae321fcd55', 'embedded_sha256': '4c58e118de281da6d2bec1efff1c9e0f491dfeaa5dd114bd686e14a48031aff4', 'packaging_changes': ['Replace a file read with the identical embedded frozen JSON resource; no decision contents changed.']}]
EXPECTED = {'canonical_sha256': 'fcda9178d45a18c3f72516d08b073a1410a38ba239c326774a52dc299b0585d3', 'canonical_fields': ['record_id', 'stock_code', 'year', 'source', 'responsibility_text', 'raw_text_sha256'], 'records': 4073781, 'nonempty_records': 3754886, 'empty_records': 318895, 'input_sha256': 'dac38597ce68396fe0a06889b549e7f8a1a579fb443e38cadedbc5ee5870f620', 'source_release_manifest_sha256': '1e2d0d4a0a14aecf512e42f52e39e3b5ee0ccd7380868cae13c97e73959ed6f4'}
MODULE_SOURCES = {
'jdclean_unified.responsibility_repair_r11': r'''"""Terminal operational cleaning decisions over complete supplied descriptions.

R=literal task, N=non-task, S=syntax, X=unusable literal fragment. No U label.
Decisions express a documented extraction convention, not human gold labels.
Every output word is retained from the normalized supplied source; only recorded
format transformations and separators are permitted. No predicted missing text.
"""
import re,html,hashlib

HEADS={
 'R':('岗位职责 工作职责 职责描述 主要职责 工作内容 职位描述 职位职责 岗位描述 岗位工作内容 岗位主要工作内容 主要工作内容 主要工作任务 工作任务 工作概要 工作概述 岗位定位 工作责任 负责内容 职责说明 核心职责 你的工作 你需要做 需要你做 你将负责 你将会做 岗位职责描述 核心岗位职责描述 岗位职责与要求 工作职责及任职要求 岗位职责及任职要求 工作职责及内容 工作内容及要求').split()+['Job Responsibilities','Key Responsibilities','Main Responsibilities','Responsibilities','Job Duties','Job Description','Position Summary','The Role','Your Responsibilities'],
 'Q':('任职要求 任职资格 任职条件 职位要求 岗位要求 岗位需求 职责要求 职责资格 任职需求 资格条件 基本要求 岗位基本要求 招聘基本要求 加分要求 必备技能 专业知识及技能要求 相关经验和资质要求 应聘条件 招聘条件 招聘要求 学历要求 技能要求 工作经验 专业要求 教育背景 经验要求 能力要求 素质要求 其他要求 岗位人员要求 人员要求 用人要求').split()+['Position Qualifications','Qualifications','Requirements','Job Requirements','Qualification Criteria','Required Skills','Skills and Experience','Education and Experience','Your Profile','About You'],
 'B':('福利待遇 薪资待遇 薪资福利待遇 薪酬福利待遇 薪酬福利 工资待遇 工资福利待遇 岗位待遇 福利保障 员工福利待遇 员工福利 薪资构成 培训晋升 发展通道 职业发展规划 晋升空间 晋升方向 发展空间 福利 薪酬待遇 薪资 工作福利').split()+['Benefits','We Offer','What We Offer','Compensation and Benefits'],
 'A':('工作地点 工作地址 上班地点 面试地点 面试地址 面试时间 工作时间 上班时间 联系方式 联系电话 联系人 联系邮箱 简历请投递 简历投递 报名时间 投递方式 招聘程序 招聘需求 岗位名称 培养岗位 从事岗位 职能类别 关键字 关键词 温馨提示 乘车路线 招聘人数 招聘岗位 面试方式 备注 应聘方式').split()+['Location','How to Apply'],
 'C':('公司简介 企业简介 公司介绍 企业介绍 公司概况 部门介绍 职位介绍 项目背景介绍 项目介绍 团队背景 招聘面向人群 培训目标 关于我们').split()+['About Us','About the Company','Company Profile','Company Overview']}
HEADS['R']+=['主要工作职责','岗位工作职责','学习内容','实习内容','定岗职责','职责内容','工作内容/职位描述']
HEADS['A']+=['培养方向','发展方向','未来培养','招聘负责人','招聘联系方式','实习部门','实习岗位','实习地点','公司网址','官网']
HEADS['B']+=['公司亮点','公司优势','工作氛围','员工保障','员工培训','奖励机制','福利假期']
HEADS['R']+=['内容']
HEADS['Q']+=['技能','加分项','要求']
HEADS['B']+=['待遇']
HEADS['R']+=['关于该岗位','主要工作内容及职责','Responsibilities description','Responsibilities Description','Main Responsibilies']
HEADS['Q']+=['工作要求','具体要求','我们希望您','我们希望你','我们对您的期望','任职资格条件及技能要求','Position Requirements','Responsibility requirements','岗位任职要求','开发经验要求']
HEADS['B']+=['我们为您提供','我们为你提供','您对我们的期望','岗位培养及发展通道','明确职业发展通道','全面的发展路线','专业的培训','就职待遇']
HEADS['A']+=['培养城市','应聘邮箱']
HEADS['R']+=['职责表述','主要工作内容及时间','工作内容及时间','主要工作职责及要求','工作职责及要求','岗位职责及要求']
HEADS['Q']+=['面试条件','面试要求','岗位基本条件','技术要求']
HEADS['Q']+=['相关要求','实习要求','应聘要求','任职基本条件']
HEADS['B']+=['我们提供','我们可以提供','加入我们,您将获得','加入我们你将获得']
HEADS['R']+=['岗位说明','岗位工作说明','职位说明']
HEADS['R']+=['职责']
HEADS['Q']+=['其它要求','其他条件','优先经验和技能','优先条件','性别要求','年龄要求','英语能力','经历要求','经验要求']
HEADS['B']+=['公司福利关怀','公司福利','待遇福利','薪资待遇概述','薪资保障','工资福利','工作时间及薪资待遇']
HEADS['A']+=['Base地','BASE地','工 作 地点','数量']
HEADS['C']+=['公司业绩','企业业绩','寄语','企业荣誉','品牌介绍']
HEADS['Q']+=['业绩要求','我们的要求']
HEADS['B']+=['你能获得','实习生&管培生培养计划']
HEADS['R']+=['而你所需要做的事情是','你所需要做的事情是','你需要做的事情','工作主要内容','你的职责','您的职责','工作任务描述','Contractor的工作内容','主要任务和职责','岗位和职责','团队发展']
HEADS['Q']+=['任职学历、经历要求','任职资格要求','个人要求','专业技能','个人素质','岗位资格','技能与经验','Qualification','Competency','Basic Skills','Educational Background','Relevant Working Experience','任职要求与核心条件']
HEADS['Q']+=['我们需要怎样的人','我们希望怎样的你']
HEADS['C']+=['公司业务','我们是谁','我们的愿景和优势','公司背景','企业背景','公司情况','企业发展']
HEADS['A']+=['Network 主要工作联系','主要工作联系','原标题','职位关键词','职务名称','投递要求','工作制度']
HEADS['B']+=['我们能带给你','我们所提供的','其他你可能想知道的事情','工作时间与薪资福利','公司可提供以下待遇','公司提供以下待遇','上班地点与薪资待遇','薪资方面','福利方面','食宿情况']
HROLE={h.lower():r for r,hs in HEADS.items() for h in hs}
HEAD=re.compile('|'.join(sorted(map(re.escape,HROLE),key=len,reverse=True)),re.I)
SPACED_HEAD=re.compile('(?:'+'|'.join(r'\s*'.join(map(re.escape,h)) for h in sorted(HROLE,key=len,reverse=True) if re.fullmatch(r'[\u3400-\u9fff]{2,15}',h))+r')(?=\s*[:：])')
HTML=re.compile(r'</?(?:p|br|div|span|b|strong|i|em|u|font|ul|ol|li|table|tbody|tr|td|a|h[1-6])(?:\s+[^<>]*?)?\s*/?>',re.I)
ENTITY=re.compile(r'&(?:nbsp|amp|lt|gt|quot|apos|#\d{1,7}|#x[0-9a-fA-F]{1,6});',re.I)
CODE=re.compile(r'换行符|文件路径|转义|字面|字符串|字符集|正则|代码示例|源代码|HTML代码|HTML标记|代码片段|ASCII|Unicode',re.I)
MAC=r'(?:马[\s\-]*克[\s\-]*(?:数[\s\-]*据(?:[\s\-]*网)?|团[\s\-]*队)|(?:www\.)?macrodatas\.cn)'
SOURCE=re.compile(r'(?:\(\s*(?:来源|来自)?\s*'+MAC+r'\s*\)|(?:来源|来自|关注微信公众号|微信公众号|关注公众号|搜索|百度搜索|数据由|该数据由)\s*[:：]?\s*<?\s*'+MAC+r'\s*>?(?:整理|[-—]官网)?)',re.I)
ACTION_WORDS='负责 协助 参与 完成 编制 制定 制订 执行 处理 办理 回复 核算 审核 归档 登记 整理 寄送 报送 统计 巡查 检查 监控 跟踪 跟进 维护 开发 设计 指导 开展 承担 收集 搜集 接待 录入 监督 协调 核对 制作 组织 安排 检修 维修 清洁 配送 研究 策划 落实 建立 更新 对接 撰写 编写 测试 评估 操作 分析 优化 保管 安装 销售 开拓 拓展 推动 推进 搭建 完善 塑造 宣传 主持 配合 主导 履行 培养 提高 提升 培训 沟通 拟订 识别 改进 降低 增加 签订 签发 发放 发货 接听 收发 联系 带领 接收 发送 进行 督促 开具 调试 引导 统筹 生产 组装 打包 检验 转接 翻译 提供 增强 加强 训练 反馈 引入 填写 支持 使用 采购 协作 辅助 管理 总结 汇总 帮助 协同 传达 讲解 出具 报销 解释 验收 签署 保证 确保 关注 授课 教授 教学 装卸 分拣 编辑 确认 申请 整合 解决 优选 营销 推广 探索 优化 评审 评价 保障 掌控 把控 指挥 核查 调查 审计 发起 实施 遵守 服从'.split()
ACTION_WORDS+=['学习','从事','担任','争取','解答','寻找','保守','接洽','检索','审查','设定','打造','挖掘','做好','安抚','回访','招聘培训','招聘员工','招聘人员','回收','审批','巡检','防护','制止','领取','退还','维系','传递','预防','纠正','清理','转化','转换','挑货','下单','开具','报告','确定','收派','记录','建设','攻克','互动','实现','组建','孵化','布道','经营','接驳','宣传','促成','订货','备货','结算','梳理','检测','拍摄','剪辑','配送','搬运','核查','诊断','培养','保洁','送达','收取','查验','巡逻','保养','输出','报备','催收','汇报','修订','修理','执教','授课','回收','分配']
AW='(?:'+'|'.join(ACTION_WORDS)+')'
ACTION=re.compile(r'^(?:(?:主要|具体|日常|全面|独立|及时|定期|每日|每天|每周|每月|按时|认真|严格|积极|主动|共同|并且|并|同时|协同|持续|不断|深度|有效|耐心|热情|准确|熟练地|须|需|需要|应当|必须|将)\s*)*'+AW+r'(?!过|能力|经验|精神|人员必须|人职位|生毕业)(?=.{2,})')
ACT_ANY=re.compile(AW)
NOMINAL=re.compile(r'(?:工作|任务|管理|运营|维护|核对|报送|审核|统计|分析|研究|设计|开发|试验|检测|评估|规划|培训|接待|收集|整理|归档|考核|建设|检查|制作|编制|签发|盘点|处理|推进|执行|保障|沟通|洽谈|投标|实施|服务|支持|存档|报表|接收|申报|缴费|缴纳|发放|汇总|报账|密封|盘活|协调|跟进|保养|安装|调试|改善|填写|装订|解释|管控|交付|追踪|解决|编辑|寻源|比价|复核|风控|授课|生产|装卸|分拣|拍摄|剪辑|运营|上架|下架|排版|绘图|制图|控制|保密义务)(?:等|等工作|相关工作|工作事项|及完善)?[。;；]*$')
QUAL=re.compile(r'^(?:(?:要求|至少|必须|须|需|应|需要|基本|比较|较为)\s*)?(?:具有|具备|拥有|有着|有过|有(?:良好|较强|很强|丰富|一定|相关|\d|[一二两三四五六七八九十])|熟悉|熟练|精通|掌握|了解|懂|理解|能够|能独立|能熟练|能看懂|能承受|能接受|能适应|能完成|能处理|会用|会使用|会操作|会开车|善于|擅长|喜欢|热爱|愿意|乐于|认同|认可|良好|优秀|较强|扎实|丰富|性格|身体|为人|做事|工作态度|工作经验|学历|学位|教育|专业|年龄|性别|身高|体重|英语|英文|普通话|口语|证书|资格证|户口|居住在|家住|男女不限|不限|无刑事)')
HARDQUAL=re.compile(r'学历|学位|相关专业|专业毕业|专业优先|者优先|优先考虑|优先录用|优先录取|工作经验|行业经验|从业经验|相关经验|工作经历|从事过|负责过|参与过|做过|\d+年(?:以上|及以上)|[一二两三四五六七八九十]+年(?:以上|及以上)|(?:本科|大专|硕士|博士|高中|中专|专科)(?:及以上|以上)?|毕业生|\d+\s*[-~至到]\s*\d+\s*(?:周岁|岁)')
TRAIT=re.compile(r'^(?:工作|做事|为人|态度)?(?:认真负责|认真细致|细心|细致|耐心|勤奋|敬业|诚实|正直|踏实|严谨|积极|热情|开朗|责任心|执行力|沟通能力|表达能力|学习能力|形象|声音|思路|思维|逻辑|口齿|身体|五官|人品|品行|抗压能力|吃苦耐劳|遵纪守法)')
BENEFIT=re.compile(r'底薪|工资|薪资|薪酬|奖金|提成|五险|六险|社保|公积金|年假|年终奖|月薪|年薪|补助|补贴|津贴|包吃|包住|食宿|免费|双休|调薪|晋升|提拔|优惠|油卡|法定假期|法定节假日|团建|聚餐|年度旅游|节日|员工关怀|工作环境|商业保险|绩效奖金|带薪|两班倒|月休|加班费')
BENEFIT_START=re.compile(r'^(?:享受|入职|我们提供|公司提供|本公司提供|公司为|公司承担|可享|缴纳(?:社保|社会保险|五险|公积金)|按照国家及地方规定缴纳|购买(?:五险|社保)|提供(?:食宿|住宿|三餐|免费)|免费提供|免费|包吃|包住|五险|六险|社保|公积金|底薪|工资|薪资|月薪|年薪|综合工资|基本工资|年终奖|周末双休|双休|月休|带薪|法定节假日|节日福利|生日福利|晋升|完善的晋升)')
HR=re.compile(r'负责|协助|核算|审核|计算|办理员工|办理职工|办理.{0,15}(?:社保|公积金)|薪酬管理|缴费申报|制定|统计|编制|报表|申报|代缴|管理员工')
META=re.compile(r'^(?:联系电话|联系人|联系地址|手机|电话|传真|邮箱|邮件|网址|地址|地点|工作地|工作地址|上班地点|面试|应聘|简历|投递|报名|乘车|公交|地铁|招聘|诚聘|招收|招募|招聘岗位|职位名称|岗位名称|职能类别|关键字|关键词|详情请|请联系|有意者|欢迎|温馨提示|温馨提醒|友情提示|特别提醒|备注|备注说明)')
EMPLOYER=re.compile(r'^(?:公司|本公司|企业|集团|我们|本集团|本企业|本部门|该平台|本平台|目前公司|近年来公司)(?:目前|现|自|始终|长期|一直|主要|已经|已|于|均)?(?:成立|成立于|致力于|位于|坐落|专注|主要从事|是一家|是|拥有|总部|主营|提供|秉承|经营|占地|注册|发展|承担福利|执行[“"简单])')
ENQ=re.compile(r'^(?:at least|minimum|bachelor|master|ph\.?d|degree|diploma|education|experience|knowledge|proficien|familiar|fluent|fluency|excellent|strong|good|ability|able to|must have|should have|required|requirements|qualifications|you have|you are|we are looking|we seek|\d+\+?\s*(?:years|year))\b',re.I)
ENA=re.compile(r'^(?:(?:you|the candidate|the employee|he/she)\s+(?:will|shall|must|is to)\s+|(?:to|and|also|proactively|independently|effectively|regularly|timely)\s+)*(?:responsible for|assist|support|manage|develop|design|perform|conduct|execute|implement|deliver|provide|ensure|maintain|monitor|prepare|review|coordinate|lead|drive|analy[sz]e|create|build|plan|organize|organise|work|collaborate|communicate|collect|report|resolve|handle|identify|participate|establish|improve|process|track|test|evaluate|write|translate|train|operate|validate|check|control|supervise|follow|achieve|optimi[sz]e|take|be responsible|seek|promote|understand)\b',re.I)
TAIL=re.compile(r'^(?:负责|协助|包括|主要负责|负责相关|完成相关|负责公司|负责产品|协助完成|根据|按照|以及|并且|主要|工作|岗位|职位|任职|要求|职责|来源|关注)[:：。;；\s]*$')
PUNCT=' \t\n\r\xa0,，;；。!！:：[]【】"“”•·◆★●§'

def cleantext(t):return t.strip(PUNCT).lstrip('‐—·').strip()
def apply(s,events):
 events=sorted(events,key=lambda e:(e['a'],-e['b']));chosen=[]
 for e in events:
  if chosen and e['a']<chosen[-1]['b']:continue
  if e['old']!=e['new']:chosen.append(e)
 out=[];last=0
 for e in chosen:
  assert last<=e['a']<e['b']<=len(s) and s[e['a']:e['b']]==e['old'];out.extend([s[last:e['a']],e['new']]);last=e['b']
 out.append(s[last:]);return ''.join(out),chosen

def normalize(raw):
 s=raw;stages=[]
 def stage(es,name):
  nonlocal s
  s,es=apply(s,es)
  if es:stages.append(dict(name=name,edits=es))
 def events(rx,fn,why):return [dict(a=m.start(),b=m.end(),old=m[0],new=fn(m),rule=why) for m in rx.finditer(s)]
 stage(events(re.compile('[\uff01-\uff5e\u3000]'),lambda m:chr(ord(m[0])-65248) if m[0]!='\u3000' else ' ','WIDTH_NORMALIZATION'),'width')
 for _ in range(3):
  es=events(ENTITY,lambda m:html.unescape(m[0]),'COMPLETE_HTML_ENTITY')
  if not es:break
  stage(es,'entity')
 es=[]
 for m in HTML.finditer(s):
  if CODE.search(s[max(0,m.start()-25):m.end()+25]):continue
  es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n' if re.match(r'</?(?:p|br|div|li|ul|ol|tr|h[1-6])\b',m[0],re.I) else '',rule='HTML_LAYOUT'))
 stage(es,'html')
 if len(re.findall(r'br(?=\s*\d+[.、)]|岗位职责|任职要求|工作地点|入职)',s,re.I))>=3 and not CODE.search(s):
  stage(events(re.compile(r'br(?=\s*\d+[.、)]|岗位职责|任职要求|工作地点|入职)',re.I),lambda m:'\n','REPEATED_BARE_BR_LAYOUT'),'bare_br')
 stage(events(re.compile('[\u200b\ufeff\x00-\x08\x0b\x0c\x0e-\x1f\x7f]'),lambda m:'','FORMAT_CONTROL'),'control')
 stage(events(re.compile('[\uf0d8\uf0b7\uf0fc\uf06c\uf06e]'),lambda m:'\n','FONT_LIST_BULLET'),'font')
 es=[]
 for m in re.finditer(r'(?:\\+r\\+n|\\+[rn](?=[\s\d\u3400-\u9fff]|\\+[rn])|\\+t(?=[\u3400-\u9fff]))',s):
  ctx=s[max(0,m.start()-30):m.end()+30]
  if CODE.search(ctx) or re.search(r'802\.11[a-z\\/]+',ctx,re.I):continue
  es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n' if m[0][-1] in 'rn' else ' ',rule='ESCAPED_LAYOUT'))
 stage(es,'escaped_layout')
 stage(events(re.compile(r'[\u200c\u200d\u2060]'),lambda m:'' if (m.start()>0 and re.match(r'[A-Za-z0-9\u3400-\u9fff]',s[m.start()-1]) or m.end()<len(s) and re.match(r'[A-Za-z0-9\u3400-\u9fff]',s[m.end()])) else m[0],'CJK_LATIN_JOINER'),'joiner')
 stage(events(re.compile('\xa0'),lambda m:' ','NONBREAKING_SPACE'),'space')
 # Only heading letters separated by whitespace are joined, followed by a
 # caption colon. No task words are rewritten or joined across free prose.
 es=[]
 for m in SPACED_HEAD.finditer(s):
  if any(c.isspace() for c in m[0]):es.append(dict(a=m.start(),b=m.end(),old=m[0],new=re.sub(r'\s+','',m[0]),rule='SPACED_LITERAL_SECTION_CAPTION'))
 stage(es,'spaced_captions')
 return s,stages

def headings(s):
 hs=[];stack=[];enclosures=[]
 for i,c in enumerate(s):
  if c in '([【':stack.append((i,c))
  elif c in ')]】' and stack and {'(':')','[':']','【':'】'}[stack[-1][1]]==c:
   lo,op=stack.pop();enclosures.append((lo,i+1,op))
 for m in HEAD.finditer(s):
  a,b=m.span();pre=s[max(0,a-22):a];post=s[b:b+60]
  # Examples and task objects inside parentheses are not section transitions.
  if any(lo<a and b<hi and not (op=='[' and not s[:lo].strip() and not s[hi:].strip()) and s[lo+1:hi-1].strip(' :：')!=m[0] for lo,hi,op in enclosures):continue
  if m[0] in {'内容','技能','要求','待遇','职责'} and a and not (pre[-1:].isspace() or pre[-1:] in '[【。;；:：' or re.search(r'[一二三四五六七八九十][、.)]$',pre)):continue
  if re.search(r'(?:制定|编写|编制|发布|界定|定义|修订|完善|履行|根据|明确|熟悉|了解|执行|满足|符合|确认|梳理|优化|做好|开展|相关)(?:相关|各岗位|公司|员工|的)?$',pre) and not re.match(r'\s*[:：]\s*\(?[1-9][.、)]',post):continue
  if re.search('[A-Za-z]',m[0]) and ((a and s[a-1].isalpha()) or b<len(s) and s[b].isalpha()):continue
  anno=re.match(r'\s*\((?:详细说明|Job Responsibilities|Responsibilities|Requirements|教育|经验|技能)[^()]{0,80}\)\s*',s[b:],re.I)
  if anno:b+=anno.end();post=s[b:b+60]
  narrative=m[0] in {'我们需要怎样的人','我们希望怎样的你'} and re.match(r'\s*[?？]',post) or m[0]=='我们所提供的' and (a==0 or pre[-1:] in '-—\n。;；')
  if not (narrative or re.match(r'\s*(?:[:：;；]|[】\]【])',post) or re.match(r'\s*[1-9][.、)]',post) or m[0] in {'福利待遇','任职资格条件及技能要求','主要工作内容及职责'} or (a==0 or pre[-1:] in '\n\r\t。;；[【、)]') and (not post or post[:1].isspace()) or re.match(r'\s*'+HEAD.pattern,post,re.I)):continue
  if a and s[a-1] in '[【':a-=1
  close=re.match(r'\s*(?:[:：]\s*)?[】\]]?\s*(?:[:：])?',s[b:])
  if close:b+=close.end()
  if narrative and b<len(s) and s[b] in '?？':b+=1
  if narrative and a and s[a-1] in '-—':a-=1
  prefix=re.search(r'[一二三四五六七八九十]+[、.)]\s*$',s[:a])
  if prefix:a=prefix.start()
  if m[0] in {'公司业绩','企业业绩'}:
   prefix=re.search(r'[一二三四五六七八九十]+[、.)][^;；。\n]{0,45}$',s[:a])
   if prefix:a=prefix.start()
  if hs and a<hs[-1]['b']:continue
  hs.append(dict(a=a,b=b,role=HROLE[m[0].lower()],name=m[0]))
 return hs

def partitions(s):
 hs=headings(s);structures=[dict(a=h['a'],b=h['b'],label='S',reason='EXPLICIT_SECTION_HEADING',section=h['role'],heading=h['name']) for h in hs]
 for h in hs:
  m=re.match(r'[-•·●◆■▪▶►][ \t]+(?=[\u3400-\u9fffA-Za-z])',s[h['b']:])
  if m:structures.append(dict(a=h['b'],b=h['b']+m.end(),label='S',reason='EXPLICIT_FIRST_BULLET_AFTER_HEADING'))
 for m in SOURCE.finditer(s):structures.append(dict(a=m.start(),b=m.end(),label='S',reason='LITERAL_SOURCE_ATTRIBUTION'))
 # Known provider's bare domain at document edges is an attribution too.
 for m in re.finditer(MAC,s,re.I):
  if not s[:m.start()].strip(' \t\n\r([【。') or not s[m.end():].strip(' \t\n\r)]】。;；'):structures.append(dict(a=m.start(),b=m.end(),label='S',reason='EDGE_PROVIDER_ATTRIBUTION'))
 markers=[]
 rx=re.compile(r'(?<![A-Za-z0-9])(?:\(?([1-9]\d?)\s*([.,)、])|([一二三四五六七八九十]+)[、.)]|([a-zA-Z])[.)])\s*(?=\S)')
 for m in rx.finditer(s):
  a,b=m.span();pre=s[:a];rest=s[b:];value=int(m[1]) if m[1] else None
  if m[1] and rest[:1].isdigit() and not re.match(r'\d+(?:年以上|年及以上|年|[-~至到]\d+岁)',rest):continue
  boundary=not pre.strip() or pre[-1:] in '\n\r\t;；。:：[【' or pre[-1:].isspace() or any(h['b']==a for h in hs)
  if m[3] and not boundary:continue
  if m[4] and not boundary:continue
  if m[2]=='.' and not boundary and a>0 and s[a-1] in './\\':continue
  markers.append(dict(a=a,b=b,value=value,boundary=boundary,text=m[0]))
 for i,m in enumerate(markers):
  sibling=any(markers[j]['value'] is not None and m['value'] is not None and abs(markers[j]['value']-m['value'])<=2 for j in [i-1,i+1] if 0<=j<len(markers))
  if m['boundary'] or sibling:structures.append(dict(a=m['a'],b=m['b'],label='S',reason='EXPLICIT_LIST_MARKER'))
 cms=list(re.finditer(r'([一二三四五六七八九十])[、.)]\s*(?=[\u3400-\u9fffA-Za-z])',s))
 if len(cms)>=2:
  for i,m in enumerate(cms):
   value='一二三四五六七八九十'.index(m[1])
   if any('一二三四五六七八九十'.index(cms[j][1])-value==j-i for j in [i-1,i+1] if 0<=j<len(cms)):structures.append(dict(a=m.start(),b=m.end(),label='S',reason='COHERENT_INLINE_CHINESE_ORDINAL'))
 bare=list(re.finditer(r'(?:^|(?<=[;；。\n:]))\s*([1-9]\d?)(?=(?:配合|跟踪|根据|服从|负责|协助|完成|进行|操作|整理|维护|开发|设计|编制))',s))
 if len(bare)>=2 and any(int(y[1])==int(x[1])+1 for x,y in zip(bare,bare[1:])):
  for m in bare:structures.append(dict(a=m.start(1),b=m.end(1),label='S',reason='COHERENT_BARE_ORDINAL'))
 spaced=list(re.finditer(r'(?<!\d)([1-9]\d?)[ \t]+(?=(?:负责|协助|参与|要求|加分项|根据|完成|操作|设计|开发|维护|整理))',s))
 if len(spaced)>=2 and any(int(y[1])==int(x[1])+1 for x,y in zip(spaced,spaced[1:])):
  for m in spaced:structures.append(dict(a=m.start(),b=m.end(),label='S',reason='COHERENT_SPACED_ORDINAL'))
 for m in re.finditer(r'(?:^|(?<=[\n\r:：;；。]))[ \t]*[-•·●◆■▪▶►★☆█]+\s*|[•●◆■▪▶►█]',s):structures.append(dict(a=m.start(),b=m.end(),label='S',reason='DECORATIVE_LIST_MARKER'))
 # Delimiters inside brackets stay attached to the task's examples/objects.
 cut={0,len(s)};depth=0
 for i,c in enumerate(s):
  if c in '([【《':depth+=1
  elif c in ')]】》':depth=max(0,depth-1)
  if c in '\n\r;；。' and (depth==0 or c in '\n\r'):cut.add(i+1)
 for d in structures:cut.update((d['a'],d['b']))
 # Recover an explicit assignment following a qualification/skill tag without a
 # sentence separator; the former text is still independently excluded.
 for m in re.finditer(r'(?:负责(?!过|人|心)|协助)(?=.{3,})',s):
  a=m.start();line=max(s.rfind(';',0,a),s.rfind('。',0,a),s.rfind('\n',0,a))+1;pre=s[line:a]
  if (re.search(r'经验者$',pre) or re.search(r'技能要求.{0,65}销售$',pre)) and not re.search(r'能(?:够|独立)|参与过|曾|有过',pre):cut.add(a)
 for m in re.finditer(r'\s{2,}',s):cut.update(m.span())
 # Fixed headed records with a single outer wrapper must not suppress splits.
 if s.strip().startswith('[') and s.strip().endswith(']'):
  for m in re.finditer('[;；。]',s):cut.add(m.end())
 points=sorted(cut);out=[];hidx=-1
 for a,b in zip(points,points[1:]):
  while hidx+1<len(hs) and hs[hidx+1]['a']<=a:hidx+=1
  h=hs[hidx] if hidx>=0 else {'role':None,'name':None}
  st=next((d for d in structures if d['a']<=a and b<=d['b']),None)
  if st:out.append(dict(a=a,b=b,label='S',reason=st['reason'],section=h['role'],heading=h['name']));continue
  t=s[a:b]
  if not cleantext(t) or re.fullmatch(r'[\W\d_]+',t):out.append(dict(a=a,b=b,label='S',reason='SEPARATOR_OR_ISOLATED_NUMBER',section=h['role'],heading=h['name']));continue
  out.append(dict(a=a,b=b,section=h['role'],heading=h['name']))
 return out

def is_task(t):
 t=cleantext(t)
 if not t:return False
 if re.search(r'^(?:研究生|审核人员必须|设计思路|开拓精神|分析性思维|执行力|培养方向|发展方向)',t):return False
 if re.match(r'^(?:专业销售|销售|管理|多元化发展|职业发展)(?:路线|通道|方向)',t):return False
 if re.fullmatch(r'.{1,35}(?:工程师|经理|总监|主管|专员|技术员|顾问|助理|优化师|医师|岗位|职位)(?:\([^)]{0,20}\))?',t):return False
 if re.match(r'^(?:沟通|表达|协调|管理|组织|逻辑|思维|领导|执行|抗压|学习|创新)[^,，;；]{0,12}(?:能力|素质|意识|技巧|精神)',t):return False
 if re.search(r'(?:负责|参与|主导|从事|设计|开发|操作|完成|组织|使用|做)过(?!程)',t[:30]):return False
 if ACTION.match(t) or ENA.match(t):return True
 if re.match(r'^(?:不定期|定时|每季度|每年|每周|每月|提前|及时准确地)',t) and ACTION.match(re.sub(r'^(?:不定期|定时|每季度|每年|每周|每月|提前|及时准确地)','',t)):return True
 if caption_assignment(t):return True
 if re.match(r'^(?:主要|具体)?做(?!事|人|过|为).{2,}',t):return True
 if re.match(r'^(?:本岗位|本职位|你将|您将|你需要|您需要|我们需要你)',t) and ACT_ANY.search(t):return True
 if re.match(r'^(?:根据|按照|依据|在|对|为|与|向|通过|利用|借助|结合|基于|作为|就|将|围绕|按|针对|归属|所负责)',t) and ACT_ANY.search(t) and not QUAL.match(t) and not re.search(r'(?:有|具备|具有).{0,25}(?:经验|能力)|经验优先|者优先',t):return True
 return False

def qualification(t):
 if ENQ.match(t):return True
 if t.startswith('要求') and re.search(r'经验|熟悉|掌握|能力|学历|背景',t):return True
 if re.match(r'^(?:熟知|基本了解|善于|擅长)',t):return True
 if re.match(r'^有(?!权).{0,55}(?:能力|意识|精神|资格证|证者|证书|经验|经历)',t):return True
 if re.match(r'^(?:受过|接受过|参加过|经历过|曾经).{0,100}(?:培训|课程|工作|项目|学习)',t):return True
 if re.match(r'^(?:需|须|必须|请)?(?:持有|持本人|携带|持|提供本人).{0,20}(?:身份证|证件|资格证|健康证)|^(?:喜爱|对.{0,25}有.{0,20}(?:兴趣|热情))',t):return True
 if QUAL.match(t):return True
 if HARDQUAL.search(t) and not is_task(t):return True
 if re.search(r'(?:有|具有|具备).{0,60}(?:经验|能力|知识)|(?:相关|设计|工程|技术|学)专业[。;；]?$|(?:知识|理论)(?:扎实|丰富|良好)|经验(?:丰富|优先|为佳|尤佳)?[。;；]?$',t) and not is_task(t):return True
 if TRAIT.match(t) and not is_task(t):return True
 if re.fullmatch(r'.{0,30}(?:能力|精神|意识|素质|素养|责任心|执行力|亲和力)(?:强|佳|好|良好|较强)?',t) and not is_task(t):return True
 return False

def decide(t,role,previous=None):
 t=cleantext(t)
 if not t:return 'S','SEPARATOR'
 if role!='R' and re.fullmatch(r'(?:服从|听从).{0,18}(?:安排|管理|指挥|调配)(?:等)?',t):return 'N','GENERIC_APPLICANT_COMPLIANCE'
 if t.lower() in HROLE or t in {'微信分享','分享微信','分享到微信'}:return 'S','BARE_HEADING_OR_SHARE_UI'
 if role!='R' and re.fullmatch(r'(?:服从|听从)(?:公司|领导|上级)?(?:安排|指挥|管理)',t):return 'N','GENERIC_APPLICANT_COMPLIANCE'
 if len(t)<=2 and t in ACTION_WORDS:return 'X','INCOMPLETE_LITERAL_PREDICATE'
 if TAIL.fullmatch(t):return 'X' if re.search('负责|协助|完成|根据|按照',t) else 'S','INCOMPLETE_LITERAL_PREDICATE' if re.search('负责|协助|完成|根据|按照',t) else 'BARE_HEADING_TOKEN'
 # Literal encoding loss/masking stays in excluded-fragment ledger, never guessed.
 if re.search(r'\ufffd|锟斤拷|烫烫烫|屯屯屯',t):return 'X','LITERAL_ENCODING_LOSS'
 if re.search(r'(?<=[\u3400-\u9fff])\*+(?=[\u3400-\u9fff])|(?<=[\u3400-\u9fff])\?{2,}(?=[\u3400-\u9fff])',t) and not CODE.search(t):return 'X','SOURCE_MASK_WITHIN_WORD'
 if re.search(r'&(?:nbs?p?|quo?t?|am?p?|#\d*)$',t):return 'X','INCOMPLETE_LITERAL_ENTITY'
 if re.search(r'(?:\.{3,}|…+)',t) and not re.search(r'[,，、/].*(?:\.{3,}|…+)\s*(?:等)?[)）]',t) and not CODE.search(t):return 'X','SOURCE_ELLIPSIS_FRAGMENT_EXCLUDED'
 if re.search(r'[\ue000-\uf8ff]',t):return 'X','UNDECODABLE_PRIVATE_FONT_CHARACTER'
 if re.match(r'^(?:公司|我们|本公司).{0,12}(?:诚聘|招聘|直招)',t):return 'N','RECRUITMENT_ADVERTISEMENT'
 if re.match(r'^.{2,70}(?:有限公司|有限责任公司|股份公司|集团|设计院|研究院)(?:是|已|下设|成立|目前|主要|拥有|位于|创建|创立|以)',t):return 'N','NAMED_EMPLOYER_DESCRIPTION'
 if EMPLOYER.match(t) and not re.search(r'你将|您将|你负责|您负责|你的职责|您的职责',t):return 'N','EMPLOYER_SUBJECT_DESCRIPTION'
 if re.match(r'^(?:电话|网络|微信)(?:推广|销售|邀约|拜访|沟通|回访)',t) and role not in {'B','A','C'}:return 'R','EXPLICIT_COMMUNICATION_TASK'
 if re.match(r'^(?:邮件回复|邮件接收|邮件处理|招聘手续|招聘流程|招聘管理|招聘渠道|面试安排|面试接待|简历筛选|电话接听)',t) and (role=='R' or NOMINAL.search(t)):return 'R','ADMINISTRATIVE_AUXILIARY_TASK'
 if META.match(t) and not is_task(t):return 'N','RECRUITMENT_CONTACT_OR_METADATA'
 if re.search(r'^(?:可接受|接受|欢迎|面向).{0,10}(?:实习生|应届|毕业生)|https?://|www\.',t) and not is_task(t):return 'N','RECRUITMENT_OR_WEB_ADDRESS'
 if BENEFIT_START.match(t) and not HR.search(t):return 'N','EMPLOYEE_COMPENSATION_OR_BENEFIT'
 if re.match(r'^(?:高薪入职|开启财富|稳定的收入|快速积累财富|广阔的职业发展|实习期\d|实习期[一二三四五六七八九十])',t):return 'N','EMPLOYMENT_PROMOTION_OR_DURATION'
 if re.match(r'^(?:全天班|早班|晚班|夜班|白班|中班|长白班|班次|工时)\s*[:：]?\s*[0-9一二三四五六七八九十]',t):return 'N','EXPLICIT_SHIFT_TIME_OR_PAY'
 if role in {'B','C','A'} and BENEFIT.search(t) and not caption_assignment(t) and not re.match(r'^(?:负责|协助|核算|办理|审核|编制|制定|统计|申报)',t):return 'N','BENEFIT_IN_EMPLOYER_SECTION'
 if re.match(r'^(?:工作简单|生熟手均可|靠岸安排休息|休息期间|一个航期|出差一次|工作轻松|无规则休息|闲时多休|最多不超过\d+公斤|大件有叉车|无重大体力活)',t):return 'N','EMPLOYMENT_SCHEDULE_OR_EASE_CLAIM'
 if role in {'B','C','A'} and re.match(r'^(?:办理离职手续|每日办理入职|只需|即可|欢迎|参加招聘|应聘)',t):return 'N','APPLICANT_ENTRY_EXIT_PROCEDURE'
 if BENEFIT.search(t) and not is_task(t) and not HR.search(t):return 'N','EMPLOYEE_BENEFIT_OR_SCHEDULE'
 if re.match(r'^(?:全部)?新(?:厂区|宿舍)|^(?:机器化程度|两班倒工作|全程智能化生产车间)',t):return 'N','WORKPLACE_DESCRIPTION'
 # Modal operation is a task inside a duties section; elsewhere it is a stated skill.
 if role=='R' and modal_task(t):return 'R','OPERATION_PRESCRIBED_IN_DUTY_SECTION'
 if role=='R' and operational_knowledge(t):return 'R','CURRENT_OPERATIONAL_KNOWLEDGE'
 if qualification(t):return 'N','APPLICANT_CAPABILITY_OR_CONDITION'
 if re.search(r'对.{0,40}(?:较为|有一定|有所)?(?:了解|熟悉)|^(?:高度的工作热情|精力充沛|语言表达|有上进心)',t) and not is_task(t):return 'N','APPLICANT_KNOWLEDGE_OR_TRAIT'
 if role=='Q' and not is_task(t) and not re.match(r'^(?:负责(?!过)|协助|每天|每日|定期|按时|根据|按照|你将|您将)',t) and not (NOMINAL.search(t) and not re.search(r'优先|经验|经历|能力|熟练|熟悉|能够|掌握|精通|知识|要求',t)):return 'N','APPLICANT_SECTION_CONTINUATION'
 if role in {'B','C','A'} and not (caption_assignment(t) or re.match(r'^(?:负责(?!过)|协助|核算|审核|编制|制定|办理员工|办理职工|你将|您将)',t)):return 'N','NON_DUTY_SECTION_CONTENT'
 if is_task(t):return 'R','EXPLICIT_CURRENT_TASK'
 if re.fullmatch(r'.{0,25}(?:上级|领导|经理|店长|主管|管理者).{0,12}(?:交办|安排|交代|交待|布置).{0,18}(?:工作|任务|事项)[。;；]*',t):return 'R','ASSIGNED_AUXILIARY_TASK'
 if role in {'B','A','C'}:return 'N','NON_DUTY_SECTION_CONTENT'
 if re.fullmatch(r'.{1,35}(?:工程师|经理|总监|主管|专员|技术员|顾问|助理|优化师|医师|岗位|职位)(?:\([^)]{0,20}\))?',t):return 'N','POSITION_TITLE_ONLY'
 if NOMINAL.search(t) and len(t)>3:return 'R','NOMINAL_WORK_OR_DELIVERABLE'
 cs=[cleantext(c) for c in re.split('[,，]',t) if cleantext(c)]
 if cs and (NOMINAL.search(cs[0]) or len(cs)>1 and any(is_task(c) for c in cs[1:])) and not any(qualification(c) for c in cs):return 'R','NOMINAL_TASK_WITH_ACTION_CONTINUATION'
 if role is None and re.search(r'客户|项目|产品|设备|图纸|资料|合同|报告|报表|数据|业务|财务|生产|订单|文件|交货|采购|研发|材料|技术|工艺|员工|团队|计划|流程|成本|品牌|教学|课程|指标|资产|库存|税务|账务|编制|盘点',t) and ACT_ANY.search(t) and not re.search(r'招聘|应聘|优先|经验|经历|能力|学历|熟练|熟悉|具备|具有|希望|发展空间|晋升',t):return 'R','LITERAL_WORK_OBJECT_AND_FUNCTION'
 if role=='R':return 'R','LITERAL_CONTENT_OF_EXPLICIT_DUTY_SECTION'
 if previous=='R' and re.match(r'^(?:并|以及|同时|包括|包含|如|例如|其中|以便|从而|保证|确保|以|使|达到)',t):return 'R','DEPENDENT_TASK_CONTINUATION'
 return 'N','NO_EXPLICIT_TASK_STATEMENT'

def operational_knowledge(t):
 return bool(re.match(r'^(?:及时|深入|充分)?(?:了解|掌握|熟悉|理解)',t) and re.search(r'情况|进展|进度|行情|需求|状态|库存|动态|诉求|特点',t) and not re.search(r'学历|学位|经验|能力|者优先|精通|熟练|软件|工具|编程|规则|流程',t))

def modal_task(t):
 if re.match(r'^熟练(?:操作|使用|运用|掌握)',t) and re.search(r'Python|Java|C\+\+|Office|CAD|软件|工具|Word|Excel',t,re.I) and not re.search(r'(?:完成|编写|编制|设计|开发|解决|维修|生产|处理|作业).{2,}',t[4:]):return False
 return bool(re.match(r'^(?:能(?:够|独立|快速|及时|熟练)?|会|熟练)(?:(?:地|的|准确|快速|高效|独立|及时|熟练|全面))*?(?:完成|处理|进行|操作|使用|编写|编制|设计|开发|解决|维修|保养|维护)',t) and not HARDQUAL.search(t))

def caption_assignment(t):
 if ':' in t:
  head,tail=t.split(':',1)
  if len(head)<=32 and not re.search(r'条件|要求|经验|能力|学历|薪酬|薪资|工资|福利|联系方式|地址|招聘|面试',head) and (ACTION.match(tail.lstrip()) or re.match(r'^(?:定期|每日|每天).{0,10}',tail) and ACT_ANY.search(tail)):return True
 return bool(re.match(r'^.{1,20}(?:工|厨师|员|经理|岗位)(?:主要工作是|主要负责|负责|工作是)',t) or re.match(r'^(?:随船|普通|大锅饭|仓库|搬运|叉车|电焊|普工|跟单).{0,30}(?:主要负责|负责日常|主要工作是)',t))

def split_mixed(s,a,b,role):
 # Split only commas that introduce an independent requirement/benefit or a new
 # task after a requirement. Preserve task objects, quantities and outcome tails.
 t=s[a:b];points=[a];depth=0;start=a
 for i,c in enumerate(t):
  if c in '(【《[':depth+=1
  elif c in ')】》]':depth=max(0,depth-1)
  if c not in ',，、' or depth:continue
  pos=a+i+1;left=cleantext(s[start:pos]);right=cleantext(re.split('[,，;；。\n]',s[pos:b],maxsplit=1)[0])
  if not right:continue
  lq=qualification(left);rq=qualification(right)
  if role=='R' and (operational_knowledge(right) or modal_task(right)):rq=False
  rb=(BENEFIT_START.match(right) and not HR.search(right)) or (META.match(right) and not is_task(right) and (':' in right or re.match(r'^(?:请投递|有意者|面试时间|面试地点)',right))) or bool(re.match(r'^(?:每月平均|平均每月|以上岗位|岗位|第一个月|月平均).{0,15}(?:工资|月薪)|^(?:工作简单|生熟手均可|最多不超过|大件有叉车|无重大体力活)',right))
  if c=='、' and not re.match(r'^(?:每月平均|平均每月|以上岗位|第一个月|月平均).{0,15}(?:工资|月薪)|^(?:工作简单|生熟手均可|无重大体力活)',right):continue
  independent=bool(re.match(r'^(?:负责(?!过)|协助|每天|每日|定期|按时|根据|按照|你将|您将)',right)) or bool(role=='R' and is_task(right) and not re.match(r'^(?:完成|操作|使用|开发|设计)',right))
  left_task=is_task(left) or bool((NOMINAL.search(left) or re.search(r'.{2,}(?:操作|作业|销售)$',left)) and not qualification(left))
  switch=((left_task or role=='R') and (rq or rb)) or (lq and independent and not rq) or (is_task(right) and BENEFIT_START.match(left)) or (role in {'A','B','C'} and independent and not rq)
  if switch:points.append(pos);start=pos
 points.append(b)
 return list(zip(points,points[1:]))

def finish_body(body):
 # Cosmetic operations only. Unpaired brackets do not prove absent words.
 stages=[];s=body
 def stage(es,name):
  nonlocal s
  s,es=apply(s,es)
  if es:stages.append(dict(name=name,edits=es))
 pairs={'(':')','[':']','【':'】','《':'》'};stack=[];bad=[]
 for i,c in enumerate(s):
  if c in pairs:stack.append((i,c))
  elif c in pairs.values():
   if stack and pairs[stack[-1][1]]==c:stack.pop()
   else:bad.append(i)
 bad.extend(i for i,c in stack)
 stage([dict(a=i,b=i+1,old=s[i],new='',rule='UNPAIRED_BRACKET_SYNTAX_ONLY') for i in bad],'bracket_syntax')
 es=[]
 for m in re.finditer(r'(?m)^[ \t.,，、;；。:："“”\[\]【】]+|[ \t,，、;；。:："“”\[\]【】]+$|[ \t]{2,}',s):es.append(dict(a=m.start(),b=m.end(),old=m[0],new=' ' if not (m.start()==0 or s[m.start()-1:m.start()]=='\n' or m.end()==len(s) or s[m.end():m.end()+1]=='\n') else '',rule='BOUNDARY_PUNCTUATION_AND_SPACE'))
 stage(es,'edges')
 return s,stages

def process(raw):
 s,norm=normalize(raw);units=[];prev=None;previous_heading=None
 for base in partitions(s):
  if base.get('label')=='S':units.append(base);continue
  for a,b in split_mixed(s,base['a'],base['b'],base['section']):
   role=base['section'];t=cleantext(s[a:b]);effective=role
   if role in {'Q','B','C','A'} and prev=='R' and previous_heading==base['heading'] and is_task(t) and not qualification(t) and not BENEFIT.search(t):effective='R'
   lab,why=decide(s[a:b],effective,prev);units.append(dict(base,a=a,b=b,label=lab,reason=why,effective_section=effective));prev=lab;previous_heading=base['heading']
 assert units and units[0]['a']==0 and units[-1]['b']==len(s) and all(x['b']==y['a'] for x,y in zip(units,units[1:])) if s else not units
 spans=[]
 for u in units:
  if u['label']!='R':continue
  a,b=u['a'],u['b']
  while a<b and s[a].isspace():a+=1
  while a<b and s[b-1].isspace():b-=1
  if a<b:spans.append(dict(a=a,b=b,text=s[a:b]))
 before='\n'.join(x['text'] for x in spans);body,fmt=finish_body(before)
 defects=[u for u in units if u['label']=='X'];r=[u for u in units if u['label']=='R']
 status=('PARTIAL_DUTIES_SOURCE_FRAGMENT_EXCLUDED' if defects else 'DUTIES_RETAINED') if body.strip() else ('NO_USABLE_DUTIES_SOURCE_FRAGMENT' if defects else 'NO_EXPLICIT_DUTIES')
 return dict(normalized_sha256=hashlib.sha256(s.encode()).hexdigest(),normalization=norm,partition=units,render_spans=spans,body_before_format=before,format=fmt,after=body,status=status,excluded_fragment_count=len(defects),retained_unit_count=len(r),undecided_units=0)

# R11: source structure precedes damage classification; qualifications and
# employer offers require positive evidence. Prior R text is protected when no
# positive removal evidence exists. Nothing below consults company/SOC/year.
_normalize10=normalize
_partitions10=partitions
_task10=is_task
_qual10=qualification
_decide10=decide
_finish10=finish_body
ADVERB=re.compile(r'^(?:(?:正确|合理|高效|有效|切实|积极|及时|准确|严格|认真|充分|主动|耐心|妥善|科学|定期|每天|每日|每月|每周|及时准确|认真细致|深入|独立)(?:地)?)+')
PAST=re.compile(r'^(?:在校|曾经|曾|以前|过去|以往|原先)|^(?:有|具备|具有|拥有).{0,70}(?:经验|经历|能力|知识|意识|精神|证书)|^(?:接触|参与|负责|从事|开发|设计|使用|操作|管理|承担|完成|带领|主导|组织|安装|做|带)过')
ATTRIBUTE=re.compile(r'^(?:(?:学习|执行|判断|沟通|抗压|表达|观察|协调|统筹|领导|洞察)(?:力|能力)(?:较强|强|良好|优秀|出色)|积极向上|乐观开朗)(?=[,，;；。]|$)')
KNOWLEDGE_STATE=re.compile(r'^对[^,，;；。]{1,90}(?:有|具有|拥有).{0,12}(?:认知|认识|了解|理解|掌握|兴趣|热情|经验|知识|敏感度)(?=[,，;；。]|$)')
TRAIT_ONLY=re.compile(r'^(?:洞察力|结果导向|分析和目标导向|学习成绩|成绩优秀|职业素养|人际交往能力|沟通表达能力|团队精神|团队协作能力|有机化学基础|专业基础|基础知识|身体健康|诚实正直|敬业精神|逻辑思维|热情自信|耐心细致|品行|服从组织统一安排|服从公司统一调配|服从领导安排|服从管理)')
PAY=re.compile(r'非计件工资|计件工资|(?:底薪|月薪|年薪|综合工资|到手工资)\s*[:：]?\s*[\d一二三四五六七八九十]|\d+\s*(?:元[/／](?:月|天|小时)|[kKwW][/／]月)|年终奖金|每月\d+号发工资')
TASK_EN_NOUN=re.compile(r'^(?:product|project|data|system|customer|service|quality|risk|software|technical|business|team|supply chain|account|sales|marketing)\b.{0,80}(?:management|development|design|analysis|support|maintenance|testing|operations|delivery)(?:\s*[+.&/]\s*.{1,90})?[.。;；]?$',re.I)
DAMAGE=re.compile(r'\ufffd|锟斤拷|烫烫烫|屯屯屯|(?<=[\u3400-\u9fff])\*+(?=[\u3400-\u9fff])|\*{2,}|(?<=[\u3400-\u9fff])\?{2,}(?=[\u3400-\u9fff])|[\ue000-\uf8ff]|\.{3,}|…+')
POSITIVE_ASSIGN=re.compile(r'^(?:(?:主要|具体|日常|全面|独立|及时|积极|主动|并|同时)\s*)*(?:负责(?!过|人|心)|协助|承担|主导|组建|带领|你将|您将)')
LOW_EVIDENCE_N={'NO_EXPLICIT_TASK_STATEMENT','APPLICANT_SECTION_CONTINUATION','SOURCE_DEPENDENT_CONTEXT_NOT_STANDALONE'}
NOMINAL=re.compile(NOMINAL.pattern+r'|.{2,}(?:编程|标注|巡检|稽核|调研|仿真|配送|加工|值守|报关|编码|实验|领用|回收|研发|经营|接收)(?:等|等工作)?[。;；]*$')

def normalize(raw):
 s,stages=_normalize10(raw)
 def stage(es,name):
  nonlocal s
  s,chosen=apply(s,es)
  if chosen:stages.append(dict(name=name,edits=chosen))
 # Repeated same private-font characters at entry beginnings are layout. A
 # private glyph within a word is never decoded into a guessed character.
 es=[]
 for glyph in set(re.findall('[\ue000-\uf8ff]',s)):
  positions=[m.start() for m in re.finditer(re.escape(glyph),s)]
  layout=[i for i in positions if (i==0 or s[i-1].isspace() or s[i-1] in ':：;；。[]【】') and re.match(r'\s*[\u3400-\u9fffA-Za-z0-9]',s[i+1:])]
  if len(layout)>=2 and len(layout)==len(positions):
   es.extend(dict(a=i,b=i+1,old=glyph,new='\n',rule='REPEATED_ENTRY_INITIAL_FONT_MARKER') for i in layout)
 stage(es,'proven_font_layout')
 # A complete explicit heading followed by a star establishes the start of a
 # star list. Require multiple substantial entries; double stars are not bullets.
 es=[];hs=headings(s)
 for j,h in enumerate(hs):
  a=h['b'];b=hs[j+1]['a'] if j+1<len(hs) else len(s);chunk=s[a:b];marks=list(re.finditer(r'(?<!\*)\*(?!\*)',chunk))
  if len(marks)<2 or chunk[:marks[0].start()].strip():continue
  texts=[chunk[m.end():marks[k+1].start() if k+1<len(marks) else len(chunk)].strip() for k,m in enumerate(marks)]
  if not all(len(t)>=6 for t in texts):continue
  for m in marks:es.append(dict(a=a+m.start(),b=a+m.end(),old='*',new='\n',rule='EXPLICIT_HEADING_STAR_LIST'))
 stage(es,'proven_star_layout')
 # Word-internal spaces in qualification terms are formatting, not new words.
 es=[]
 for m in re.finditer(r'经[ \t]+验|学[ \t]+历|能[ \t]+力|任[ \t]+职',s):
  es.append(dict(a=m.start(),b=m.end(),old=m[0],new=re.sub(r'\s+','',m[0]),rule='BROKEN_COMMON_FIELD_WORD_SPACE'))
 stage(es,'split_field_word')
 # Only a literal line-wrapped continuation is joined. Independent next tasks,
 # requirements, headings and numbered entries keep their boundary.
 es=[]
 for m in re.finditer(r'(?<=[\u3400-\u9fffA-Za-z])\r?\n[ \t]*(?=[\u3400-\u9fffA-Za-z])',s):
  left=s[s.rfind('\n',0,m.start())+1:m.start()];right=s[m.end():s.find('\n',m.end()) if '\n' in s[m.end():] else len(s)]
  if left.strip(' :：') in HEADS.get('R',[]) or left.strip(' :：').lower() in HROLE or right.strip(' :：').lower() in HROLE:continue
  if POSITIVE_ASSIGN.match(right) or QUAL.match(right) or re.match(r'^[1-9][.、)]',right):continue
  if re.search(r'各项|质量标准|维护保养|中间|产品检|验证工|工作的|相关的|公司的|其它单位的|其他单位的$',left) and not right.startswith(('职责','要求','任职')):
   es.append(dict(a=m.start(),b=m.end(),old=m[0],new='',rule='LITERAL_SOFT_LINE_WRAP'))
 stage(es,'soft_line_wrap')
 return s,stages

def is_task(t):
 t=cleantext(t);core=ADVERB.sub('',t)
 core=re.sub(r'^(?:并且|并|同时|仅|只)(?=负责|协助|处理|总结|归纳|分享|收集|记录|积累|负责|使用)','',core)
 if PAST.search(t) or TRAIT_ONLY.match(t) or ATTRIBUTE.match(t):return False
 if KNOWLEDGE_STATE.match(t) and not re.search(r'使其|促使|从而|确保|帮助.*形成',t):return False
 if re.match(r'^(?:总结|归纳|分享|传授|积累|沉淀|收集|记录|报告|提炼)(?:工作|实践|相关)?经验',core):return True
 if _task10(t) or core!=t and _task10(core):return True
 if re.match(r'^(?:报告|确定|收派|记录|实现|组建|建设|攻克|孵化|布道|经营|输出|采集|保洁|送达|结算|修订|修理|加工)(?!过|能力|经验|人员)(?=.{2,})',core):return True
 if re.match(r'^(?:与|对|向|通过|根据|按照|依据|利用|结合|在|为)',core) and re.search(r'进行|沟通|互动|解答|报告|完成|处理|管理|设计|开发|使用|提供|制定|执行|安装|维护|经营',core) and not re.search(r'有.{0,20}(?:经验|能力|理解|了解)|者优先',core):return True
 return False

def qualification(t):
 t=cleantext(t)
 if PAST.search(t) or TRAIT_ONLY.match(t) or ATTRIBUTE.match(t):return True
 if KNOWLEDGE_STATE.match(t) and not re.search(r'使其|促使|从而|确保|帮助.*形成',t):return True
 if re.fullmatch(r'.{0,30}(?:基础|理论|知识)(?:扎实|丰富|良好)',t):return True
 if re.search(r'经验者(?:优先|$)|经验(?:丰富|优先|者优先)|曾担任|在校曾|接触过',t) and not re.match(r'^(?:总结|归纳|汇总|分享|传授|积累|沉淀|收集|记录|报告|提炼)',ADVERB.sub('',t)) and not POSITIVE_ASSIGN.match(t):return True
 # A work action ending in “总结经验” is not an experience qualification.
 if is_task(t) and not re.search(r'者优先|学历|学位|从事过|参与过|工作经验|任职条件',t):return False
 return _qual10(t)

def decide(t,role,previous=None):
 t=cleantext(t)
 if not t:return 'S','SEPARATOR'
 if re.match(r'^(?:重点提示|请看清|请看清楚|特别提醒|请注意|请仔细阅读)',t):return 'N','EXPLICIT_RECRUITMENT_NOTICE'
 if re.search(r'均有岗位|不卡地域|面试成绩通用|多个岗位可选',t) and not POSITIVE_ASSIGN.match(t):return 'N','RECRUITMENT_POSITION_CATALOG'
 if re.match(r'^(?:确定后|面试通过后|通过后|录用后).{0,20}(?:入职|报到|录用)',t):return 'N','APPLICANT_ENTRY_PROCEDURE'
 if re.match(r'^(?:描述为完成该岗位|请描述|请填写|请在此填写|此处填写)',t):return 'N','UNFILLED_TEMPLATE_INSTRUCTION'
 if PAST.search(t) or TRAIT_ONLY.match(t):return 'N','EXPLICIT_PERSONAL_HISTORY_OR_ATTRIBUTE'
 if ATTRIBUTE.match(t) or KNOWLEDGE_STATE.match(t) and not re.search(r'使其|促使|从而|确保|帮助.*形成',t):return 'N','EXPLICIT_PERSONAL_KNOWLEDGE_OR_TRAIT'
 if role=='Q' and re.search(r'(?:设计|编程|开发|沟通|分析|理解|判断|学习|管理|阅读|写作|协调|组织)能力(?:强|好|较强)?[。;；]?$|(?:知识|技能|素质|意识|精神)(?:强|好|较强)?[。;；]?$',t) and not POSITIVE_ASSIGN.match(t) and not re.search(r'培养|提高|提升|考核|评价|评估',t):return 'N','EXPLICIT_CAPABILITY_IN_QUALIFICATION_SECTION'
 if re.fullmatch(r'.{0,35}(?:基础|理论|知识)(?:扎实|丰富|良好)',t):return 'N','EXPLICIT_PERSONAL_KNOWLEDGE_ATTRIBUTE'
 if PAY.search(t) and not re.match(r'^(?:负责|协助|核算|计算|统计|制定|审核|编制|发放员工|办理员工)',ADVERB.sub('',t)):return 'N','EXPLICIT_PAY_INFORMATION'
 if role in {'B','A','C','Q'} and re.match(r'^(?:签订|签署)(?:正式)?(?:劳动合同|劳务合同)',t) and re.search(r'五险|保险|社保|待遇',t):return 'N','EMPLOYER_EMPLOYMENT_OFFER'
 if re.search(r'不用担心客户资源|您不用担心|无需大海捞针|公司每天会给您分发|我们所提供的客户案例',t):return 'N','EMPLOYER_RESOURCES_OR_RECRUITMENT_PITCH'
 if re.search(r'(?:累积|累计)?注册用户.{0,12}(?:亿|万)',t) and not POSITIVE_ASSIGN.match(t):return 'N','COMPANY_SCALE_DESCRIPTION'
 if role in {'B','C','A'} and not POSITIVE_ASSIGN.match(t):return 'N','EXPLICIT_NON_DUTY_SECTION'
 if role=='Q' and not is_task(t):return 'N','APPLICANT_SECTION_CONTINUATION'
 if DAMAGE.search(t) and not CODE.search(t):
  # The source has already been separated into layout entries and local
  # clauses. Never let a positive action verb bypass a real local defect.
  dl,dw=_decide10(t,role,previous)
  if dl=='X':return dl,dw
 if TASK_EN_NOUN.match(t) and role in {'R',None}:return 'R','EXPLICIT_ENGLISH_NOMINAL_WORK'
 if is_task(t) and not qualification(t):return 'R','COMPLETE_CURRENT_TASK_STATEMENT'
 if role=='R' and re.match(r'^(?:能(?:够)?|可)(?:独立|及时|准确|快速|有效|熟练)*(?:解答|接待|回复|沟通|处理|销售|安装|收派)',t) and not HARDQUAL.search(t):return 'R','OPERATIONAL_ACTION_IN_DUTY_SECTION'
 return _decide10(t,role,previous)

def _clauses(s,a,b):
 # Enumerated noun objects separated by 、 remain one clause. Full source
 # punctuation and byte-for-byte intervals stay in the audit.
 out=[];last=a
 for m in re.finditer('[,，;；。]',s[a:b]):out.append((last,a+m.end()));last=a+m.end()
 if last<b:out.append((last,b))
 return out

def split_mixed(s,a,b,role):
 t=s[a:b];points={a,b};cs=_clauses(s,a,b)
 # A mask or truncation affects only its local clause, not every work statement
 # before or after it. Classification decides whether intact clauses stand alone.
 if DAMAGE.search(t) and not CODE.search(t):
  for lo,hi in cs:points.update((lo,hi))
  for m in re.finditer(r'并且|并|以及|同时|然后',t):
   pos=a+m.start()
   if _standalone(s[a:pos]) and DAMAGE.search(s[pos:b]):points.add(pos)
 for i in range(1,len(cs)):
  lo,hi=cs[i];left=cleantext(s[cs[i-1][0]:cs[i-1][1]]);right=cleantext(s[lo:hi])
  ql=qualification(left);qr=qualification(right);workl=is_task(left) or bool(NOMINAL.search(left) and not ql)
  if role=='R' and (modal_task(right) or operational_knowledge(right)):qr=False
  benefit=bool(BENEFIT_START.match(right) and not HR.search(right) or PAY.search(right))
  meta=bool(META.match(right) and (':' in right or re.match(r'^(?:请|有意者|面试)',right)))
  if workl and (qr or benefit or meta):points.add(lo)
  if ql and POSITIVE_ASSIGN.match(right):points.add(lo)
  if role in {'A','B','C'} and POSITIVE_ASSIGN.match(right):points.add(lo)
 # Strong assignments embedded in parentheses after a list separator are
 # independent literal clauses; never strip an employer/candidate subject.
 for m in re.finditer(r'(?<=[,，、;；。(])\s*(?=(?:主要|具体)?(?:负责(?!过|人|心)|协助|组建|带领))',t):
  pos=a+m.end();prefix=cleantext(s[a:pos])
  if role in {'B','C','A'} or qualification(prefix):
   points.add(pos)
   close=s.find(')',pos,b)
   if close>=0:points.add(close)
 # Unpunctuated work+requirement joins, e.g. 收派快递对快递有了解的最好.
 for m in re.finditer(r'(?=对[^,，;；。]{1,35}有[^,，;；。]{0,10}(?:了解|理解)|(?:具备|具有|拥有).{0,30}(?:学历|经验|能力)|(?:本科|大专|硕士)以上|原标题\s*[:：])',t):
  pos=a+m.start();prefix=cleantext(s[a:pos])
  if prefix and is_task(prefix):points.add(pos)
 return list(zip(sorted(points),sorted(points)[1:]))

def _standalone(t):
 t=cleantext(t).strip('()')
 if not t or re.search(r'(?:从|到|至|与|和|的|及|其|所|向|对|为|并|中|通过|根据|按照)$',t):return False
 if re.fullmatch(r'(?:主要|具体)?(?:负责|协助|参与)(?:'+AW+r')?',t):return False
 if re.match(r'^(?:结合|按照|根据|依据|通过|在).{0,70}(?:情况|方式|要求|规定|基础上|过程中)$',t) and not re.search(r'负责|完成|开展|进行|实施|提供|管理|处理|执行|制定|确定',t):return False
 return is_task(t) or bool(NOMINAL.search(t)) or bool(TASK_EN_NOUN.match(t))

def _complete_before_ellipsis(t):
 t=cleantext(t)
 if not _standalone(t):return False
 return bool(re.search(r'(?:工作|任务|事项|报告|服务|管理|系统|平台|数据|资料|文件|客户|问题|方案|目标|维护|检查|质量|进度|需求|流程|光纤|设计|开发|编制|编程|安装|施工|保养|操作|经营|推广|销售|采购|分析|等)$',t) or re.fullmatch(r'[A-Za-z].{8,}[.!?]',t))

def finish_body(body):
 # Preserve punctuation inside technical names. Remove only complete source
 # title wrappers and boundary delimiters; then balance residual wrappers.
 s=body;stages=[]
 es=[]
 for m in re.finditer(r'(?m)^\s*【[^】\n]{1,35}】(?=[\u3400-\u9fffA-Za-z])',s):
  es.append(dict(a=m.start(),b=m.end(),old=m[0],new='',rule='COMPLETE_SHORT_TITLE_WRAPPER'))
 s,es=apply(s,es)
 if es:stages.append(dict(name='complete_title_wrappers',edits=es))
 s,old=_finish10(s);stages.extend(old)
 # A boundary strip may expose a closing wrapper; remove that same unmatched
 # syntax in a second pass, never words around it.
 pairs={'(':')','[':']','【':'】','《':'》'};stack=[];bad=[]
 for i,c in enumerate(s):
  if c in pairs:stack.append((i,c))
  elif c in pairs.values():
   if stack and pairs[stack[-1][1]]==c:stack.pop()
   else:bad.append(i)
 bad.extend(i for i,c in stack);es=[dict(a=i,b=i+1,old=s[i],new='',rule='BOUNDARY_EXPOSED_UNPAIRED_WRAPPER') for i in bad];s,es=apply(s,es)
 if es:stages.append(dict(name='final_wrapper_syntax',edits=es))
 es=[dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='EMPTY_LINE_COLLAPSE') for m in re.finditer('\n{2,}',s)];s,es=apply(s,es)
 if es:stages.append(dict(name='empty_lines',edits=es))
 return s,stages

def process(raw):
 s,norm=normalize(raw);units=[];prev=None
 for base in _partitions10(s):
  if base.get('label')=='S':units.append(base);continue
  group_damaged=bool(DAMAGE.search(s[base['a']:base['b']]) and not CODE.search(s[base['a']:base['b']]))
  for a,b in split_mixed(s,base['a'],base['b'],base['section']):
   text=s[a:b];t=cleantext(text);role=base['section'];lab,why=decide(text,role,prev)
   # Known benign “带*星*” notation is not a missing word in job content.
   if lab=='X' and '*星*' in t and not DAMAGE.search(t.replace('*星*','星')):lab,why=decide(t.replace('*星*','星'),role,prev)
   # Keep a complete enumerated task list before an ellipsis. No continuation
   # after the ellipsis is reconstructed, and truncated predicates stay excluded.
   ell=re.search(r'(?:\.{3,}|…+)\s*[。;；)]*\s*$',text)
   if lab=='X' and ell and not DAMAGE.search(text[:ell.start()]) and _complete_before_ellipsis(text[:ell.start()]):
    cut=a+ell.start();prefix=text[:ell.start()];pl,pw=decide(prefix,role,prev)
    if pl=='R':
     units.append(dict(base,a=a,b=cut,label='R',reason='COMPLETE_LITERAL_WORK_BEFORE_SOURCE_ELLIPSIS',source_tail_not_reconstructed=True));units.append(dict(base,a=cut,b=b,label='S',reason='SOURCE_ELLIPSIS_NOT_EXPANDED'));prev='R';continue
   if lab=='R' and group_damaged and not _standalone(t) and why=='LITERAL_CONTENT_OF_EXPLICIT_DUTY_SECTION':lab,why='N','SOURCE_DEPENDENT_CONTEXT_NOT_STANDALONE'
   units.append(dict(base,a=a,b=b,label=lab,reason=why));prev=lab
 assert (not s and not units) or units[0]['a']==0 and units[-1]['b']==len(s) and all(x['b']==y['a'] for x,y in zip(units,units[1:]))
 spans=[]
 for u in units:
  if u['label']!='R':continue
  a,b=u['a'],u['b']
  while a<b and s[a].isspace():a+=1
  while a<b and s[b-1].isspace():b-=1
  if a<b:spans.append(dict(a=a,b=b,text=s[a:b]))
 before='\n'.join(x['text'] for x in spans);after,fmt=finish_body(before);nx=sum(u['label']=='X' for u in units)
 status=('DUTIES_WITH_SOURCE_LIMIT' if nx else 'DUTIES_RETAINED') if after.strip() else ('NO_USABLE_DUTIES_SOURCE_LIMIT' if nx else 'NO_EXPLICIT_DUTIES')
 return dict(normalized_sha256=hashlib.sha256(s.encode()).hexdigest(),normalization=norm,partition=units,render_spans=spans,body_before_format=before,format=fmt,after=after,status=status,excluded_fragment_count=nx,retained_unit_count=sum(u['label']=='R' for u in units),undecided_units=0,_normalized_text=s)
''',
'tools.r11_io': r'''"""Isolated full-corpus correction; published R10 and original files stay frozen."""
import sys,json,hashlib,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
R10=ROOT.parent/'05_后续任务输出/剩余正文终结清洗_R10_20260927'
QA=ROOT.parent/'05_后续任务输出/R10_独立质量抽查_20260927'
OUT=ROOT.parent/'05_后续任务输出/全库职责纠错_R11_20260927'
RAW=ROOT/'3.指标构建/0.招聘数据清洗原始文件/原始数据2.0版本.csv'
LOCK=Path(__file__).resolve().parent/'runtime.lock'
def digest(b):return hashlib.sha256(b).hexdigest()
def compact(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def save(p,x):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+'.tmp');tmp.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8');os.replace(tmp,p)
''',
'tools.r11_engine': r'''"""Source-based corrections with protection for previously retained tasks."""
import sys,re,html,copy,json,functools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
from tools.r11_io import *
from jdclean_unified import responsibility_repair_r11 as rules

def folded(s):
 for _ in range(3):
  q=html.unescape(s)
  if q==s:break
  s=q
 return ''.join(chr(ord(c)-65248) if '\uff01'<=c<='\uff5e' else ' ' if c=='\u3000' else c for c in s)
def flat(s):return ''.join(c for c in folded(s) if c.isalnum() or c in '+#')
def fingerprint(s):return re.sub(r'[\s,，;；。:："“”\[\]【】]+','',folded(s))
def source_old_spans(before,s):
 chars=[];positions=[]
 for i,c in enumerate(s):
  if c.isalnum() or c in '+#':chars.append(c);positions.append(i)
 hay=''.join(chars);cursor=0;spans=[];miss=[]
 for line in before.splitlines():
  needle=flat(line)
  if not needle:continue
  a=hay.find(needle,cursor)
  if a<0:a=hay.find(needle)
  if a<0:miss.append(line);continue
  b=a+len(needle);spans.append(dict(a=positions[a],b=positions[b-1]+1,prior_text=line));cursor=b
 return spans,miss

@functools.lru_cache(None)
def prior_reviews():
 return {x['raw_sha256']:x for x in BUNDLED_RESOURCES['r10_reviews']}

def rebuild(p,s):
 spans=[]
 for u in p['partition']:
  if u['label']!='R':continue
  a,b=u['a'],u['b']
  while a<b and s[a].isspace():a+=1
  while a<b and s[b-1].isspace():b-=1
  if a<b:spans.append(dict(a=a,b=b,text=s[a:b]))
 p['render_spans']=spans;p['body_before_format']='\n'.join(x['text'] for x in spans);p['after'],p['format']=rules.finish_body(p['body_before_format']);nx=sum(x['label']=='X' for x in p['partition']);p['excluded_fragment_count']=nx;p['retained_unit_count']=sum(x['label']=='R' for x in p['partition']);p['status']=('DUTIES_WITH_SOURCE_LIMIT' if nx else 'DUTIES_RETAINED') if p['after'].strip() else ('NO_USABLE_DUTIES_SOURCE_LIMIT' if nx else 'NO_EXPLICIT_DUTIES');return p

def process(raw,row):
 before=row['responsibility_text'];p=rules.process(raw);s=p.pop('_normalized_text');assert digest(s.encode())==p['normalized_sha256'];oldspans,miss=source_old_spans(before,s);protected=[]
 # Only weak absence-of-evidence decisions can inherit a previously retained
 # span. Explicit conditions/benefits/company statements are never rescued.
 for u in p['partition']:
  if u['label']!='N' or u['reason'] not in rules.LOW_EVIDENCE_N or u.get('section') not in {None,'R'}:continue
  for old in oldspans:
   a=max(u['a'],old['a']);b=min(u['b'],old['b'])
   if a<b and s[a:b].strip(rules.PUNCT) and not rules.qualification(rules.cleantext(s[a:b])):
    protected.append(dict(a=a,b=b,label='R',reason='PRIOR_LITERAL_DUTY_PRESERVED_WITHOUT_POSITIVE_REMOVAL_EVIDENCE'))
 corrections=list(protected);exact=prior_reviews().get(digest(raw.encode()));prior_review_applied=False
 if exact:
  assert exact['raw']==raw
  for e in exact['decisions']:
   text=e['text'];locations=[m.start() for m in re.finditer(re.escape(text),s)]
   if len(locations)==1:corrections.append(dict(a=locations[0],b=locations[0]+len(text),label=e['label'],reason=e['reason'],exact_source_review=True))
   elif s[e['a']:e['b']]==text:corrections.append(dict(a=e['a'],b=e['b'],label=e['label'],reason=e['reason'],exact_source_review=True))
   else:raise AssertionError(('old reviewed interval requires explicit remapping',exact['review_id'],text))
  prior_review_applied=True
 if corrections:
  points={0,len(s)}
  for u in p['partition']:points.update((u['a'],u['b']))
  for e in corrections:points.update((e['a'],e['b']))
  us=[];j=0
  for a,b in zip(sorted(points),sorted(points)[1:]):
   while p['partition'][j]['b']<=a:j+=1
   u=dict(p['partition'][j],a=a,b=b);matches=[e for e in corrections if e['a']<=a and b<=e['b']]
   if matches:
    exactmatches=[e for e in matches if e.get('exact_source_review')];e=exactmatches[0] if exactmatches else matches[0];u.update(label=e['label'],reason=e['reason'],prior_preservation=not bool(exactmatches),exact_source_review=bool(exactmatches))
   if u['label']=='R' and not s[a:b].strip(rules.PUNCT):u.update(label='S',reason='FORMAT_BOUNDARY_ONLY')
   us.append(u)
  p['partition']=us;rebuild(p,s)
 # Never discard a previous task merely because a newer mapper cannot locate
 # it. Cases requiring this branch are separately sampled before publication.
 uncovered=[t for t in miss if flat(t) not in flat(p['after'])]
 syntax_bad=bool(re.search(r'<[/]?(?:p|br|div|span)\b|&(?:amp|nbsp|quot);|[\u200b\ufeff\ue000-\uf8ff]',before,re.I) or before.count('【')!=before.count('】') or before.count('[')!=before.count(']'))
 unchanged=fingerprint(before)==fingerprint(p['after']) and not syntax_bad
 adopt=not uncovered and not unchanged
 p.update(record_id=row['record_id'],raw_sha256=digest(raw.encode()),before_sha256=digest(before.encode()),before=before,proposed_after=p['after'],source_alignment_missing=miss,source_alignment_uncovered=uncovered,prior_literal_spans=oldspans,prior_preserved_intervals=protected,exact_prior_review_applied=prior_review_applied,adopted=adopt,text_changed=adopt and p['after']!=before,preserve_parent_reason='UNMAPPED_PRIOR_TEXT_RETAINED' if uncovered else 'SAME_CONTENT_KEEP_PRIOR_PRESENTATION' if unchanged else None,human_gold_standard=False,undecided_units=0)
 if not adopt:p['after']=before;p['status']='PRIOR_DUTIES_RETAINED' if before.strip() else 'NO_EXPLICIT_DUTIES'
 return p
''',
'tools.r11_headings_v4': r'''"""ASCII word boundaries permit directly adjacent Chinese-English captions."""
import re
from jdclean_unified import responsibility_repair_r11 as rules

def headings(s):
 hs=[];stack=[];enclosures=[]
 for i,c in enumerate(s):
  if c in '([【':stack.append((i,c))
  elif c in ')]】' and stack and {'(':')','[':']','【':'】'}[stack[-1][1]]==c:
   lo,op=stack.pop();enclosures.append((lo,i+1,op))
 for m in rules.HEAD.finditer(s):
  a,b=m.span();pre=s[max(0,a-22):a];post=s[b:b+60]
  # Examples and task objects inside parentheses are not section transitions.
  if any(lo<a and b<hi and not (op=='[' and not s[:lo].strip() and not s[hi:].strip()) and s[lo+1:hi-1].strip(' :：')!=m[0] for lo,hi,op in enclosures):continue
  if m[0] in {'内容','技能','要求','待遇','职责'} and a and not (pre[-1:].isspace() or pre[-1:] in '[【。;；:：' or re.search(r'[一二三四五六七八九十][、.)]$',pre)):continue
  if re.search(r'(?:制定|编写|编制|发布|界定|定义|修订|完善|履行|根据|明确|熟悉|了解|执行|满足|符合|确认|梳理|优化|做好|开展|相关)(?:相关|各岗位|公司|员工|的)?$',pre) and not re.match(r'\s*[:：]\s*\(?[1-9][.、)]',post):continue
  if re.search('[A-Za-z]',m[0]) and ((a and bool(re.match('[A-Za-z]',s[a-1]))) or b<len(s) and bool(re.match('[A-Za-z]',s[b]))):continue
  anno=re.match(r'\s*\((?:详细说明|Job Responsibilities|Responsibilities|Requirements|教育|经验|技能)[^()]{0,80}\)\s*',s[b:],re.I)
  if anno:b+=anno.end();post=s[b:b+60]
  narrative=m[0] in {'我们需要怎样的人','我们希望怎样的你'} and re.match(r'\s*[?？]',post) or m[0]=='我们所提供的' and (a==0 or pre[-1:] in '-—\n。;；')
  if not (narrative or re.match(r'\s*(?:[:：;；]|[】\]【])',post) or re.match(r'\s*[1-9][.、)]',post) or m[0] in {'福利待遇','任职资格条件及技能要求','主要工作内容及职责'} or (a==0 or pre[-1:] in '\n\r\t。;；[【、)]') and (not post or post[:1].isspace()) or re.match(r'\s*'+rules.HEAD.pattern,post,re.I)):continue
  if a and s[a-1] in '[【':a-=1
  close=re.match(r'\s*(?:[:：]\s*)?[】\]]?\s*(?:[:：])?',s[b:])
  if close:b+=close.end()
  if narrative and b<len(s) and s[b] in '?？':b+=1
  if narrative and a and s[a-1] in '-—':a-=1
  prefix=re.search(r'[一二三四五六七八九十]+[、.)]\s*$',s[:a])
  if prefix:a=prefix.start()
  if m[0] in {'公司业绩','企业业绩'}:
   prefix=re.search(r'[一二三四五六七八九十]+[、.)][^;；。\n]{0,45}$',s[:a])
   if prefix:a=prefix.start()
  if hs and a<hs[-1]['b']:continue
  hs.append(dict(a=a,b=b,role=rules.HROLE[m[0].lower()],name=m[0]))
 return hs
''',
'tools.r11_policy_v2': r'''"""Explicit actor guard for HR duties and employer promotion; frozen V1 preserved."""
import re
from tools import r11_engine as engine
from tools.r11_io import *
rules=engine.rules
original_decide=rules.decide
HR_OPERATION=re.compile(r'^(?:(?:及时|定期|每月|按时|按规定|按要求|依法|代为|代办)地?)*(?:缴纳|交纳|缴交|申报|代缴|核缴|补缴)(?:公司|企业|本公司|全体|在职)?(?:员工|职工|雇员|人员|同事)(?:的)?(?:社保|社会保险|五险|住房公积金|公积金|保险费)')
EMPLOYER_PROMO=re.compile(r'^(?:我们|公司|本公司|本企业|企业|本集团|集团)(?:一直|始终|非常|十分|高度|格外|更加|都|也)?(?:重视|关注|关心|关爱|尊重|珍惜|鼓励|倡导|崇尚|坚持|坚信)(?!客户投诉处理)')
TRIGGER=re.compile(r'(?:缴纳|交纳|缴交|申报|代缴|核缴|补缴)[^。;；\n]{0,15}(?:员工|职工|雇员|人员|同事)|(?:我们|公司|企业|集团)(?:一直|始终|非常|十分|高度|格外|更加|都|也)?(?:重视|关注|关心|关爱|尊重|珍惜|鼓励|倡导|崇尚|坚持|坚信)')
def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if EMPLOYER_PROMO.match(t):return 'N','EMPLOYER_SUBJECT_VALUES_OR_CARE_STATEMENT'
 if HR_OPERATION.match(t) and role in {None,'R'} and not rules.DAMAGE.search(t) and not rules.qualification(t):return 'R','EXPLICIT_EMPLOYEE_INSURANCE_ADMINISTRATION'
 return original_decide(text,role,previous)
rules.decide=decide
def applicable(raw):return bool(TRIGGER.search(raw))
def process(raw,row):
 p=engine.process(raw,row);p['policy_version']='R11_V2_EXPLICIT_HR_ACTOR';return p

# Decode complete standard entities before sentence partitioning; entity
# semicolons must never become sentence cuts. Unknown names remain untouched.
import html,html.entities
base_normalize=rules.normalize
ENTITY_ALL=re.compile(r'&(?:[A-Za-z][A-Za-z0-9]{1,31}|#\d{1,7}|#x[0-9a-fA-F]{1,6});')
BR_ANCHOR=re.compile(r'(?<![A-Za-z])(?:br)+(?=\s*(?:\d{1,2}(?:[.、)]|(?=[\u3400-\u9fff]))|岗位|职责|工作职责|工作内容|任职|福利|微信|分享|公司提供|家住|[\]}】]|$))')
BR_ALL=re.compile(r'(?<![A-Za-z])(?:br)+(?=\s*(?:\d{1,2}(?:[.、)]|(?=[\u3400-\u9fff]))|岗位|职责|工作职责|工作内容|任职|福利|微信|分享|公司提供|家住|[\]}】]|$|br))')
_context_br=False

def normalize(raw):
 s=raw;stages=[]
 for _ in range(3):
  es=[]
  for m in ENTITY_ALL.finditer(s):
   name=m[0][1:]
   if name.startswith('#') or name in html.entities.html5:
    if not rules.CODE.search(s[max(0,m.start()-25):m.end()+25]):es.append(dict(a=m.start(),b=m.end(),old=m[0],new=html.unescape(m[0]),rule='STANDARD_COMPLETE_HTML_ENTITY'))
  s,es=rules.apply(s,es)
  if es:stages.append(dict(name='all_complete_html_entities',edits=es))
  else:break
 if (_context_br or len(list(BR_ANCHOR.finditer(s)))>=3) and not rules.CODE.search(s):
  es=[dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='COHERENT_REPEATED_BARE_BR_LAYOUT') for m in BR_ALL.finditer(s)];s,es=rules.apply(s,es)
  if es:stages.append(dict(name='complete_bare_br_layout',edits=es))
 s,rest=base_normalize(s);return s,stages+rest
rules.normalize=normalize
base_old_spans=engine.source_old_spans
_parent_norm=[]
def source_old_spans(before,s):
 global _parent_norm
 clean,_parent_norm=normalize(before)
 return base_old_spans(clean,s)
engine.source_old_spans=source_old_spans
base_task=rules.is_task
def is_task(t):
 core=rules.ADVERB.sub('',rules.cleantext(t))
 if re.match(r'^参加(?!过)(?:班组|安全|业务|工作|生产|班前|项目|会议|培训|学习|验收|评审|招聘|定期)',core) and not rules.HARDQUAL.search(t):return True
 return base_task(t)
rules.is_task=is_task
base_decide=rules.decide
def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if re.fullmatch(r'(?:br)+',t):return 'S','ISOLATED_LAYOUT_TOKEN'
 return base_decide(text,role,previous)
rules.decide=decide
original_applicable=applicable
def applicable(raw):
 return original_applicable(raw) or bool(ENTITY_ALL.search(raw) and re.search('&(?!nbsp;|amp;|lt;|gt;|quot;|apos;|#)',raw)) or len(list(BR_ANCHOR.finditer(raw)))>=3 or bool(re.search(r'(?:积极|主动|定期|按时)?参加(?:班组|安全|业务|工作|生产|班前|项目|会议|培训|学习|验收|评审|招聘|定期)',raw))
def process(raw,row):
 global _context_br,_parent_norm
 _context_br=len(list(BR_ANCHOR.finditer(raw)))>=3;_parent_norm=[]
 p=engine.process(raw,row);p['policy_version']='R11_V2_SOURCE_LAYOUT_AND_EXPLICIT_ACTOR';p['parent_alignment_normalization']=_parent_norm
 _context_br=False;return p
# Legacy saved bodies sometimes contain standalone br lines or trailing br.
# The source must already establish a repeated layout convention.
BR_ALL=re.compile(BR_ALL.pattern+r'|(?<![A-Za-z])(?:br)+(?=\s*(?:\n|$))')
BR_ALL=re.compile(BR_ALL.pattern.replace('(?:br)+','(?:br)+(?![A-Za-z])'))
# Add a delimiter only to already proven bare list ordinals, never quantities.
base_normalize_v2=rules.normalize
def normalize(raw):
 s,stages=base_normalize_v2(raw)
 ms=list(re.finditer(r'(?m)^(\d{1,2})(?=组织|生产车间|协调|负责|协助|完成|进行|操作|整理|维护|开发|设计|编制)',s))
 if _context_br and len(ms)>=2 and any(int(b[1])==int(a[1])+1 for a,b in zip(ms,ms[1:])):
  es=[dict(a=m.start(),b=m.end(),old=m[0],new=m[0]+'、',rule='COHERENT_BARE_ORDINAL_DELIMITER') for m in ms];s,es=rules.apply(s,es)
  if es:stages.append(dict(name='bare_ordinal_delimiter',edits=es))
 return s,stages
rules.normalize=normalize
''',
'tools.r11_policy_v3': r'''"""Nested-list, caption-object, and legacy-alignment corrections over frozen V2."""
import re,html
from collections import defaultdict
from tools import r11_policy_v2 as v2
from tools.r11_io import *
engine=v2.engine;rules=v2.rules
base_normalize=rules.normalize;base_headings=rules.headings;base_decide=rules.decide
NESTED=re.compile(r'(?<![A-Za-z0-9.])([1-9]\d?)\.([1-9]\d?)[ \t]*(?=[\u3400-\u9fff])(?![万千百十亿年月天岁米吨元])')
_nested_context=False
_source_entity_names={}
_parent_events=[]

def nested_markers(s):
 ms=list(NESTED.finditer(s));groups=defaultdict(list)
 for m in ms:groups[int(m[1])].append(m)
 valid={k for k,v in groups.items() if len({int(m[2]) for m in v})>=2 and any(0<int(b[2])-int(a[2])<=3 for a,b in zip(v,v[1:]))}
 selected=[m for m in ms if int(m[1]) in valid]
 return selected if len(selected)>=3 else []

def normalize(raw):
 s,st=base_normalize(raw);ms=nested_markers(s)
 if ms:
  es=[dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='COHERENT_MULTI_LEVEL_LIST_MARKER') for m in ms];s,es=rules.apply(s,es);st.append(dict(name='nested_ordinals',edits=es))
 return s,st
rules.normalize=normalize

def headings(s):
 out=[]
 for h in base_headings(s):
  a,b=h['a'],h['b'];name=h['name'];pre=s[:a];post=s[b:]
  if name in {'工作制度','工作时间','团队发展','内容','技能','要求','待遇','职责'} and pre and re.search(r'[\u3400-\u9fffA-Za-z]$',pre) and not re.search(r'[:：]',s[a:b]):continue
  out.append(h)
 return out
rules.headings=headings

# Normalize each prior line separately. Cleaning a whole previous body can join
# adjacent list entries whose intervening source ordinals were already removed.
def source_old_spans(before,s):
 global _parent_events
 es=[];offset=0
 for line in before.splitlines(keepends=True):
  content=line.rstrip('\r\n');transformed=content
  for name,value in _source_entity_names.items():
   transformed=re.sub(re.escape('&'+name)+r'(?:;|(?=$|[,，]))',lambda m:value,transformed)
  transformed,_=base_normalize(transformed)
  if _nested_context:
   transformed=NESTED.sub('\n',transformed)
   transformed=re.sub(r'\d{1,2}\.\s*$','',transformed)
  if content and transformed!=content:es.append(dict(a=offset,b=offset+len(content),old=content,new=transformed,rule='SOURCE_PROVEN_LEGACY_LAYOUT_FOR_ALIGNMENT_ONLY'))
  offset+=len(line)
 clean,events=rules.apply(before,es);_parent_events=[dict(name='prior_line_layout_only',edits=events)] if events else []
 return v2.base_old_spans(clean,s)
engine.source_old_spans=source_old_spans
EMPLOYER_HISTORY=re.compile(r'^(?:自(?:公司)?成立以来|自成立至今|经过.{0,12}发展|经相关监管部门批准|截至\d{4}年|为实现对优秀人才的系统培养)')
EMPLOYER_SENTENCE=re.compile(r'(?:公司|企业|集团|证券|银行).{0,22}(?:建立了良好的声誉|连续.{0,8}被|评为|主要业务范围|各项业务快速发展|核心业务优势|推出.{0,12}培养)')

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if role in {None,'C','B','A'} and (EMPLOYER_HISTORY.match(t) or EMPLOYER_SENTENCE.search(t)) and not re.match(r'^(?:负责|协助|你将|您将)',t):return 'N','EXPLICIT_EMPLOYER_HISTORY_SCALE_OR_TRAINING_PROMOTION'
 if re.match(r'^通过.{0,35}(?:从业资格|执业资格|职业资格).{0,10}考试',t):return 'N','APPLICANT_CERTIFICATION_EXAM'
 if role=='Q' and re.match(r'^(?:从事|担任|任职|工作).{0,70}(?:\d+|[一二三四五六七八九十两]+)年(?:以上|及以上|$|[,，;；。])',t):return 'N','EXPLICIT_PAST_EMPLOYMENT_DURATION'
 if re.fullmatch(r'在提升自我专业能力的同时',t):return 'N','DEPENDENT_EMPLOYER_PROMOTION_PREFIX'
 return base_decide(text,role,previous)
rules.decide=decide

def applicable(raw):
 return v2.applicable(raw) or bool(nested_markers(raw)) or bool(re.search('工作制度|工作时间|自成立以来|主要业务范围|从业资格.{0,10}考试|为实现对优秀人才的系统培养',raw))

def process(raw,row):
 global _nested_context,_source_entity_names,_parent_events
 _nested_context=bool(nested_markers(raw));_source_entity_names={m[0][1:-1]:html.unescape(m[0]) for m in v2.ENTITY_ALL.finditer(raw) if html.unescape(m[0])!=m[0]};_parent_events=[]
 v2._context_br=len(list(v2.BR_ANCHOR.finditer(raw)))>=3
 p=engine.process(raw,row);p['policy_version']='R11_V3_NESTED_LIST_AND_LEGACY_ALIGNMENT';p['parent_alignment_normalization']=_parent_events
 v2._context_br=False;_nested_context=False;return p

# Additional mechanisms exposed by the frozen first fresh risk sample.
_base_norm3=rules.normalize
LETTER_LIST=re.compile(r'(?<![A-Za-z0-9])l(?=[\u3400-\u9fff0-9])')
LETTER_HEADING=re.compile(r'(岗位职责|职责描述|工作职责|任职要求|任职资格)l')
EN_BR=re.compile(r'(?:br)+(?=\s|Responsibilities|Qualifications|Requirements|Key Skills|[;；。\]}]|$)')
BARE_NUMBER=re.compile(r'(?<![A-Za-z0-9.])([1-9]\d?)(?=严格|对疑难|对客户|按照|负责|做好|定期|主动|其他与|组织|协助|完成|参与|指导|检查|维护|开发|设计|编制)')

def _wrapper(s):
 a=len(s)-len(s.lstrip());b=s.rfind(']')
 if a<len(s) and s[a]=='[' and b>a:
  tail=s[b+1:].strip();tail=rules.SOURCE.sub('',tail).strip(rules.PUNCT+'()')
  return (a,b) if not tail and re.search('岗位职责|职责描述|任职要求|任职资格',s[a:b]) else None
 return None

def normalize(raw):
 s=raw;st=[]
 def stage(es,name):
  nonlocal s
  s,es=rules.apply(s,es)
  if es:st.append(dict(name=name,edits=es))
 if LETTER_HEADING.search(s) and len(list(LETTER_LIST.finditer(s)))>=3:
  es=[dict(a=m.start(),b=m.end(),old=m[0],new='\n'+m[1]+':\n',rule='HEADING_WITH_REPEATED_LETTER_LIST_MARKER') for m in LETTER_HEADING.finditer(s)]
  es += [dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='COHERENT_LETTER_LIST_MARKER') for m in LETTER_LIST.finditer(s)];stage(es,'letter_list')
 if len(list(EN_BR.finditer(s)))>=3 and re.search(r'Responsibilities|Qualifications?|Key Skills',s,re.I) and not rules.CODE.search(s):
  stage([dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='REPEATED_ENGLISH_BARE_BR_LAYOUT') for m in EN_BR.finditer(s)],'english_br')
 s,rest=_base_norm3(s);st.extend(rest)
 # A single source wrapper around the entire job ad is layout, not an example.
 wrap=_wrapper(s)
 if wrap:
  stage([dict(a=i,b=i+1,old=s[i],new='',rule='WHOLE_DESCRIPTION_WRAPPER') for i in wrap],'source_outer_wrapper')
 ms=list(BARE_NUMBER.finditer(s))
 if len(ms)>=3 and sum(int(y[1])==int(x[1])+1 for x,y in zip(ms,ms[1:]))>=2:
  stage([dict(a=m.start(),b=m.end(),old=m[0],new='\n'+m[0]+'、',rule='COHERENT_BARE_NUMBER_LIST_DELIMITER') for m in ms],'bare_number_list')
 es=[]
 for m in re.finditer(r'(?<=[A-Za-z])\.(?=\s*(?:[A-Z][a-z]|I\s))',s):
  if re.search(r'(?:\be\.g|\bi\.e|\bMr|\bMrs|\bDr|\bProf|\bvs|\bU\.S)$',s[max(0,m.start()-10):m.start()],re.I):continue
  if not rules.CODE.search(s[max(0,m.start()-35):m.end()+35]):es.append(dict(a=m.start(),b=m.end(),old=m[0],new='.\n',rule='COMPLETE_ENGLISH_SENTENCE_BOUNDARY'))
 stage(es,'english_sentences')
 stage([dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='LITERAL_CONCATENATED_ENGLISH_ROLE_CAPTION') for m in re.finditer(r'Your\s+Role(?=You\s+will)',s)],'english_role_caption')
 return s,st
rules.normalize=normalize

_heading3=rules.headings
HARD_FIELDS={'专业要求','学历要求','教育背景','年龄要求','性别要求','英语能力','经历要求','经验要求','工作经验'}
def headings(s):
 out=_heading3(s)
 for h in out:
  if h['name'] in HARD_FIELDS:h['role']='Q_FIELD'
 return out
rules.headings=headings

ATTR=re.compile(r'^(?:工作主动|积极主动|纪律性强|责任心强|适应能力强)(?=[、,，;；。]|$)|^[^,，;；。]{1,45}(?:能力|动手能力)(?:较强|很强|强|良好|优秀)(?=[,，;；。]|$)')
PAST_Q=re.compile(r'^(?:在|于|曾|此前).{0,80}(?:提交|参与|完成|开发|设计|主导|负责|任职|从事|工作)过')
CREDENTIAL=re.compile(r'^(?:主治|副主任|主任|执业)(?:医师|医生)?(?:及)?以上职称')
CAPABILITY_ACTION=re.compile(r'^(?:负责|协助|通过.{0,30})?.{0,12}(?:提升|提高|培养|培训|考核|评价|评估|增强|开发)')
_qualification3=rules.qualification

def qualification(t):
 t=rules.cleantext(t)
 if (ATTR.search(t) and not CAPABILITY_ACTION.search(t)) or CREDENTIAL.match(t):return True
 return _qualification3(t)
rules.qualification=qualification

MODAL_WORK=re.compile(r'^(?:能(?:够)?|可)(?:独立|高效|准确|及时|有效|熟练|完全)*(?:地|的)?(?:对.{1,25}(?:提出|提供)|编制|编写|拓展|优化|支持|指导|完成|处理|解答|制作|设计|开发|维护).{3,}')
DELIVERABLE=re.compile(r'(?:制作|评审|验证|检讨改善|推进实施|试模|交付|验收|核对|审核|检查|编制|编写|归档|维护|开发|设计|定义改善)[。;；:：]*$')
_decide3=rules.decide

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if role=='Q_FIELD' and not rules.POSITIVE_ASSIGN.match(t):return 'N','EXPLICIT_APPLICANT_EDUCATION_OR_FIELD'
 if qualification(t) and (ATTR.search(t) and not CAPABILITY_ACTION.search(t) or CREDENTIAL.match(t)):return 'N','EXPLICIT_PERSONAL_CAPABILITY_OR_CREDENTIAL'
 if role=='Q' and PAST_Q.match(t):return 'N','EXPLICIT_PAST_SUBMISSION_OR_PROJECT_EXPERIENCE'
 if re.match(r'^(?:Clear mind|Good understanding|hands on experience)\b',t,re.I):return 'N','EXPLICIT_ENGLISH_CAPABILITY_OR_EXPERIENCE'
 if role in {None,'B','C','A'} and re.match(r'^(?:培养期结束后|并将培养期间考核|经校园招聘录用的|将由各单位负责培养)',t):return 'N','APPLICANT_TRAINING_PLAN_OR_PROMOTION'
 if role=='Q' and DELIVERABLE.search(t) and not qualification(t) and not re.search('能力|经验|熟悉|熟练|掌握|精通|知识|优先|能够|会使用|能独立',t):return 'R','CONCRETE_NOMINAL_DELIVERABLE_DESPITE_QUALIFICATION_CAPTION'
 if role=='R' and MODAL_WORK.match(t) and not rules.HARDQUAL.search(t):return 'R','CURRENT_MODAL_OPERATION_IN_DUTY_SECTION'
 if role in {None,'R'} and re.match(r'^(?:You|The employee|The candidate)\s+(?:will|shall)\s+be\s+(?:working|responsible|managing|providing|performing)\b',t,re.I) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_ENGLISH_ASSIGNED_OPERATION'
 return _decide3(text,role,previous)
rules.decide=decide

_split3=rules.split_mixed
def split_mixed(s,a,b,role):
 intervals=_split3(s,a,b,role);points={a,b}
 for x,y in intervals:points.update((x,y))
 cs=rules._clauses(s,a,b)
 if role=='R':
  for i in range(1,len(cs)):
   lo,hi=cs[i];left=rules.cleantext(s[cs[i-1][0]:cs[i-1][1]]);right=rules.cleantext(s[lo:hi])
   if qualification(left) and (rules.is_task(right) and not qualification(right) or MODAL_WORK.match(right)):points.add(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

# A deliberately broad lexical screen is evaluated on every raw record.
# Every record with a possible new mechanism is recomputed from R10 + source.
def applicable(raw):
 return bool(nested_markers(raw) or LETTER_HEADING.search(raw) or re.search(r'Responsibilities|Your(?:\s|&nbsp;)+Role|工作制度|工作时间|自成立以来|主要业务范围|从业资格.{0,10}考试|为实现对优秀人才的系统培养|培养期结束后|校园招聘录用|工作主动|动手能力|纪律性强|主治.*职称|提交过|\bClear mind\b',raw,re.I) or (re.search('任职要求|任职资格',raw) and DELIVERABLE.search(raw)) or re.search(r'任职(?:要求|资格)[\s\S]*(?:制作|评审|验证|检讨改善|推进实施|试模|交付|验收|核对|审核|检查|编制|编写|归档|维护|开发|设计|定义改善)',raw) or (raw.lstrip().startswith('[') and ('职责' in raw or '任职' in raw)) or len(list(BARE_NUMBER.finditer(raw)))>=3 or re.search(r'熟悉|精通|掌握|能力(?:较强|很强|强|良好|优秀)',raw))

# Parent alignment needs only source-proven layout changes, not the full source
# normalizer (which could join separate already-cleaned lines).
_source_has_br=False
_source_has_letter=False

def source_old_spans(before,s):
 global _parent_events
 clean=before;st=[]
 def stage(es,name):
  nonlocal clean
  clean,es=rules.apply(clean,es)
  if es:st.append(dict(name=name,edits=es))
 es=[]
 for name,value in _source_entity_names.items():
  for m in re.finditer(re.escape('&'+name)+r'(?:;|(?=$|[,，\n]))',clean):es.append(dict(a=m.start(),b=m.end(),old=m[0],new=value,rule='SOURCE_PROVEN_LEGACY_ENTITY_FOR_ALIGNMENT_ONLY'))
 stage(es,'legacy_entities_for_alignment')
 if _source_has_br:
  rx=re.compile(v2.BR_ALL.pattern+'|'+EN_BR.pattern)
  stage([dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='SOURCE_PROVEN_LEGACY_BR_FOR_ALIGNMENT_ONLY') for m in rx.finditer(clean)],'legacy_br_for_alignment')
 if _source_has_letter:
  stage([dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='SOURCE_PROVEN_LEGACY_LETTER_FOR_ALIGNMENT_ONLY') for m in LETTER_LIST.finditer(clean)],'legacy_letter_for_alignment')
 if _nested_context:
  stage([dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='SOURCE_PROVEN_NESTED_ORDINAL_FOR_ALIGNMENT_ONLY') for m in NESTED.finditer(clean)],'legacy_nested_ordinals')
  stage([dict(a=m.start(),b=m.end(),old=m[0],new='',rule='SOURCE_PROVEN_DANGLING_ORDINAL_FOR_ALIGNMENT_ONLY') for m in re.finditer(r'(?m)\d{1,2}\.\s*$',clean)],'legacy_ordinal_remnants')
 _parent_events=st;return v2.base_old_spans(clean,s)
engine.source_old_spans=source_old_spans

def process(raw,row):
 global _nested_context,_source_entity_names,_parent_events,_source_has_br,_source_has_letter
 _nested_context=bool(nested_markers(raw));_source_entity_names={m[0][1:-1]:html.unescape(m[0]) for m in v2.ENTITY_ALL.finditer(raw) if html.unescape(m[0])!=m[0]};_parent_events=[]
 v2._context_br=len(list(v2.BR_ANCHOR.finditer(raw)))>=3
 _source_has_br=v2._context_br or (len(list(EN_BR.finditer(raw)))>=3 and bool(re.search(r'Responsibilities|Qualifications?|Key Skills',raw,re.I)))
 _source_has_letter=bool(LETTER_HEADING.search(raw) and len(list(LETTER_LIST.finditer(raw)))>=3)
 p=engine.process(raw,row);p['policy_version']='R11_V3_SOURCE_STRUCTURES_AND_EXPLICIT_TASKS';p['parent_alignment_normalization']=_parent_events
 v2._context_br=False;_nested_context=False;_source_has_br=False;_source_has_letter=False;return p

# Prevent a qualification's leading object from becoming a new task merely
# because a following comma carries the experience predicate.
OBJECT_EXPERIENCE=re.compile(r'^对[^。;；]{1,150}[,，]\s*(?:有|具有|具备).{0,40}(?:经验|经历|能力)')
BELIEF=re.compile(r'^对[^,，;；。]{1,80}(?:有|具有).{0,10}(?:信念|热诚|热情|兴趣)')
_decide4=rules.decide

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if role in {None,'Q','Q_FIELD'} and (OBJECT_EXPERIENCE.search(t) or BELIEF.search(t)):return 'N','EXPLICIT_KNOWLEDGE_EXPERIENCE_OR_INTEREST_PREDICATE'
 if role is None and re.fullmatch(r'(?:院长|病理医生|口腔医生|医生|护士|诊所主任)(?:职位描述[:：]?)?',t):return 'N','EXPLICIT_STANDALONE_POSITION_TITLE'
 return _decide4(text,role,previous)
rules.decide=decide

_split4=rules.split_mixed

def split_mixed(s,a,b,role):
 text=s[a:b];t=rules.cleantext(text)
 if role in {None,'Q','Q_FIELD'} and OBJECT_EXPERIENCE.search(t) and not rules.POSITIVE_ASSIGN.match(t):return [(a,b)]
 # A degree/tenure requirement in the same item makes weak "can do" phrases
 # part of that requirement; explicit independent assignments still split.
 if role=='R' and rules.HARDQUAL.search(t):return _split3(s,a,b,role)
 return _split4(s,a,b,role)
rules.split_mixed=split_mixed
BARE_NUMBER=re.compile(r'(?<![A-Za-z0-9.])([1-9]\d{0,2})(?=严格|对疑难|对客户|按照|负责|做好|定期|主动|其他与|组织|协助|完成|参与|指导|检查|维护|开发|设计|编制|制定|依照|统筹|完善|领导|参加|审查|监督|授权|控制|推动|支持|督导|辅导|建立|配合|离开|适时|教导|规划|制订|在上级)')
_prev_applicable=applicable

def applicable(raw):return _prev_applicable(raw) or bool(OBJECT_EXPERIENCE.search(raw) or BELIEF.search(raw) or re.search(r'(?:院长|医生|护士)职位描述',raw))

_norm4=rules.normalize
SPACED_NUMBER=re.compile(r'(?<![A-Za-z0-9.])([1-9]\d?)[ \t]+(?=[\u3400-\u9fffA-Za-z])(?![年月天岁米吨元万千百亿])')
def normalize(raw):
 s,st=_norm4(raw);es=[]
 for m in re.finditer(r'(?:工作内容|岗位职责|工作职责|职责描述|任职要求|任职资格)(?=\s{2,})',s):
  if re.search(r'(?:根据|按照|制定|编制|编写|明确|相关|履行|的)$',s[max(0,m.start()-12):m.start()]):continue
  es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n'+m[0]+':\n',rule='MULTISPACE_SECTION_CAPTION'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='caption_whitespace_boundaries',edits=es))
 ms=list(SPACED_NUMBER.finditer(s))
 if len(ms)>=3 and sum(int(y[1])==int(x[1])+1 for x,y in zip(ms,ms[1:]))>=2:
  es=[dict(a=m.start(),b=m.end(),old=m[0],new='\n'+m[1]+'、',rule='COHERENT_SPACED_LIST_ORDINAL') for m in ms];s,es=rules.apply(s,es)
  if es:st.append(dict(name='spaced_list_ordinals',edits=es))
 return s,st
rules.normalize=normalize
_task3=rules.is_task

def is_task(t):
 t=rules.cleantext(t)
 if re.match(r'^(?:承接|支撑|主攻|解读|抓好|预估)(?!过|能力|经验).{2,}',t):return True
 return _task3(t)
rules.is_task=is_task
_decide5=rules.decide

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if re.fullmatch(r'.{1,25}管理员(?:\([^)]{1,25}\))?',t) and not re.match(r'^(?:负责|协助|指导|培养|培训|担任|配合|招聘|管理)',t):return 'N','EXPLICIT_STANDALONE_POSITION_TITLE'
 return _decide5(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 text=s[a:b];t=rules.cleantext(text)
 if role in {None,'Q','Q_FIELD'} and OBJECT_EXPERIENCE.search(t) and not rules.POSITIVE_ASSIGN.match(t):return [(a,b)]
 intervals=_split3(s,a,b,role);points={a,b}
 for x,y in intervals:points.update((x,y))
 cs=rules._clauses(s,a,b)
 if role=='R':
  hard=bool(rules.HARDQUAL.search(t))
  for i in range(1,len(cs)):
   lo,hi=cs[i];left=rules.cleantext(s[cs[i-1][0]:cs[i-1][1]]);right=rules.cleantext(s[lo:hi]);prefix=rules.cleantext(s[a:lo])
   if qualification(left) or qualification(prefix):
    if rules.is_task(right) and not qualification(right) or (not hard and MODAL_WORK.match(right)):points.add(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed
_applicable4=applicable

def applicable(raw):return _applicable4(raw) or len(list(SPACED_NUMBER.finditer(raw)))>=3 or bool(re.search('工作内容|管理员|承接|支撑|主攻|解读|预估',raw))
_finish3=rules.finish_body

def finish_body(body):
 s,st=_finish3(body);es=[dict(a=m.start(),b=m.end(),old=m[0],new='',rule='EXPLICIT_THREE_DIGIT_LIST_MARKER') for m in re.finditer(r'(?m)^\s*\d{3}、\s*',s)];s,es=rules.apply(s,es)
 if es:st.append(dict(name='three_digit_list_syntax',edits=es))
 return s,st
rules.finish_body=finish_body
_headings4=rules.headings

def headings(s):
 out=[]
 for h in _headings4(s):
  if h['name']=='工作经验' and re.search(r'(?:总结|积累|分享|提炼|收集|报告|交流)(?:相关|已有)?$',s[max(0,h['a']-12):h['a']]):continue
  out.append(h)
 return out
rules.headings=headings

# The completed V2 scan already evaluates all source records. This final pass
# re-evaluates every potentially affected record, including empty and inherited
# results, and leaves verified unaffected bodies byte-identical.
QCAP=re.compile(r'任职要求|任职资格|岗位要求|职位要求|资格条件|招聘要求|应聘要求')
RCAP=re.compile(r'岗位职责|工作职责|职责描述|工作内容|主要职责')
PAIR_QUAL_TASK=re.compile(r'(?:熟悉|精通|掌握|具备|具有|经验|学历)[^。;；\n]{0,140}[,，]\s*(?:能|可|根据|通过|对|为|按照|提供|处理|维护|开展|负责|协助|关注)')
BODY_RISK=re.compile(r'能力(?:较强|很强|强|良好|优秀)|工作主动|纪律性强|信念|热诚|提交过|主治.*职称|培养期结束后|培养期间考核|校园招聘录用|管理类|经济类|思想政治|从事.{0,60}年|担任.{0,60}年|自成立以来|主要业务范围|建立了良好的声誉|公司.*(?:重视|关爱)|(?:院长|管理员)(?:\(|$)|任职要求|(?:^|\n)(?:br)+|&[A-Za-z]+',re.M)
OBJECT_EXPERIENCE_ANY=re.compile(OBJECT_EXPERIENCE.pattern[1:])

def applicable_row(raw,row):
 body=row['responsibility_text']
 if not body.strip() or row['r11_group']=='PRIOR_ALIGNMENT_PRESERVED':return True
 if BODY_RISK.search(body):return True
 if LETTER_HEADING.search(raw) or re.search(r'Responsibilities|Your(?:\s|&nbsp;)+Role|\bClear mind\b',raw,re.I):return True
 if raw.lstrip().startswith('[') and re.search('职责|任职',raw):return True
 if nested_markers(raw) or len(list(BARE_NUMBER.finditer(raw)))>=3 or len(list(SPACED_NUMBER.finditer(raw)))>=3:return True
 if re.search(r'(?:工作内容|岗位职责|工作职责|职责描述|任职要求|任职资格)\s{2,}',raw):return True
 if re.search(r'(?:编制|制定|修订|更改|安排|调整|优化|控制|减少)[^。;；\n]{0,35}(?:工作制度|工作时间)',raw):return True
 if re.search(r'从业资格.{0,10}考试|为实现对优秀人才的系统培养|培养期结束后|校园招聘录用|承接|主攻|解读|预估|信念|热诚|提交过|主治.*职称',raw):return True
 if OBJECT_EXPERIENCE_ANY.search(raw) or PAIR_QUAL_TASK.search(raw):return True
 # Nominal concrete outputs can appear under a mistakenly named Q caption.
 # This cheap structural screen deliberately over-selects; the full policy
 # still excludes knowledge, experience, and ability statements.
 if QCAP.search(raw):
  t=html.unescape(raw) if '&' in raw else raw
  if '<' in t:t=re.sub(r'<[^<>]{0,300}>','\n',t)
  t=t.replace('\\n','\n').replace('\\r','\n')
  for m in QCAP.finditer(t):
   nxt=RCAP.search(t,m.end());block=t[m.end():nxt.start() if nxt else len(t)]
   for line in re.split(r'[。;；\n]|\d+[.、)]',block):
    line=line.strip()
    if DELIVERABLE.search(line) and not re.search('能力|经验|熟悉|熟练|掌握|精通|知识|优先|能够|会使用|能独立',line):return True
 return False
_decide6=rules.decide

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if role=='Q' and previous=='R' and re.match(r'^(?:包括|包含|涵盖|例如|其中|以及)',t) and not qualification(t):return 'R','LITERAL_OBJECT_CONTINUATION_OF_EXPLICIT_TASK'
 return _decide6(text,role,previous)
rules.decide=decide
_finish4=rules.finish_body

def finish_body(body):
 s,st=_finish4(body);es=[]
 for m in re.finditer(r'\s+微信分享\s*$',s):
  if re.search(r'(?:工作|任务|架构|系统|资料|文档|计划|方案|流程|业务|服务|能力|经验)$',s[:m.start()]):es.append(dict(a=m.start(),b=m.end(),old=m[0],new='',rule='TRAILING_SHARE_WIDGET_AFTER_COMPLETE_STATEMENT'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='trailing_share_widget',edits=es))
 return s,st
rules.finish_body=finish_body
_applicable_row4=applicable_row

def applicable_row(raw,row):return _applicable_row4(raw,row) or '微信分享' in row['responsibility_text'] or bool(re.search(r'任职(?:要求|资格)[\s\S]*[;；]\s*(?:包括|包含|涵盖|例如|其中|以及)',raw))
''',
'tools.r11_policy_v4': r'''"""Remaining literal layout, nominal-office tasks, and benefit-caption fixes."""
import re
from tools import r11_policy_v3 as v3
from tools.r11_io import *
rules=v3.rules;engine=v3.engine
BASE_NORMALIZE=rules.normalize;BASE_OLD_SPANS=engine.source_old_spans;BASE_HEADINGS=rules.headings;BASE_DECIDE=rules.decide;BASE_QUAL=rules.qualification;BASE_TASK=rules.is_task
BR=re.compile(r'(?<!<)(?:br)+(?=\s|[1-9]\d{0,2}[.、)]|[\u3400-\u9fff]|Responsibilities|Requirements|Qualifications|Key Skills|[;；。\]}]|$)')
BR_HEAD=re.compile(r'(?:Responsibilities|Requirements|Qualifications?|岗位职责|任职要求|任职资格|工作职责|工作内容|职责描述)\s*[:：]?\s*br',re.I)
_br_active=False

def br_layout(raw):return bool(len(list(BR.finditer(raw)))>=3 and (BR_HEAD.search(raw) or len(re.findall(r'br[1-9]\d?[.、)]',raw))>=3))
def br_edits(s):
 out=[]
 for m in BR.finditer(s):
  if re.match('标签|元素|节点|指令',s[m.end():]):continue
  out.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='COHERENT_BARE_BR_WITH_ALPHABETIC_NEIGHBOUR_OR_FREE_TEXT'))
 return out

def normalize(raw):
 global _br_active
 _br_active=br_layout(raw);s=raw;st=[]
 if _br_active:
  s,es=rules.apply(s,br_edits(s))
  if es:st.append(dict(name='complete_bare_br_boundaries_v4',edits=es))
 s,rest=BASE_NORMALIZE(s);st.extend(rest)
 if any(stage['name']=='nested_ordinals' for stage in st):v3._nested_context=True
 if _br_active:v3._source_has_br=True
 return s,st
rules.normalize=normalize

def source_old_spans(before,s):
 prefix=[];clean=before
 if _br_active:
  clean,es=rules.apply(clean,br_edits(clean))
  if es:prefix.append(dict(name='source_proven_legacy_br_alignment_v4',edits=es))
 spans,miss=BASE_OLD_SPANS(clean,s);v3._parent_events=prefix+v3._parent_events;return spans,miss
engine.source_old_spans=source_old_spans

rules.HROLE['员工待遇']='B'
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)
def headings(s):
 hs=[]
 for h in BASE_HEADINGS(s):
  if h['name']=='员工待遇' and re.search(r'(?:负责|协助|办理|管理|核算|处理|落实|完善|制定|统筹)$',s[max(0,h['a']-12):h['a']]):continue
  hs.append(h)
 return hs
rules.headings=headings
KNOW=re.compile(r'^(?:深入|全面|充分|熟练)?(?:通晓|熟谙|谙熟|熟识)')
AUX=re.compile(r'^当好.{0,30}(?:参谋|助手|把关人|工作窗口|业务窗口)[。;；]?$')
OBJ=re.compile('办公室|办公设施|办公位|厂商|用车|车辆|通讯补贴|行政公告|前台|物资|库存|订单|合同|票据|仓库|设备|客户|供应商|工程|生产|现场|材料|产品|图纸|档案|会议|员工|薪酬|餐饮|经费|资产|报销|考勤|文印')
SOFT_END=re.compile(r'(?:管理|事务|安排|发布|采购|收发|对接|接待|保养|巡查|盘点|调度|核算|制作发布|报销|维护)[。;；:：]*$')
FIELD_ONLY=re.compile(r'^(?:行政管理|人力资源管理|财务管理|公共管理|工商管理|企业管理|旅游管理|酒店管理|工程管理|信息管理|经济管理|管理科学)$')

def qualification(t):return bool(KNOW.match(rules.cleantext(t))) or BASE_QUAL(t)
rules.qualification=qualification

def is_task(t):return bool(AUX.match(rules.cleantext(t))) or BASE_TASK(t)
rules.is_task=is_task

def office_nominal(t):
 return bool(OBJ.search(t) and SOFT_END.search(t.rstrip(')）')) and not FIELD_ONLY.fullmatch(t) and not rules.DAMAGE.search(t) and not qualification(t) and not re.search('经验|能力|知识|熟悉|熟练|掌握|精通|优先|学历|学位|相关专业|公司提供|我们提供|享受',t))
def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if t in {'其他','其它'}:return 'S','BARE_OTHER_SECTION_TOKEN'
 if KNOW.match(t):return 'N','EXPLICIT_KNOWLEDGE_PROFICIENCY'
 if role=='Q' and office_nominal(t):return 'R','CONCRETE_WORK_OBJECT_AND_ADMINISTRATIVE_FUNCTION'
 if AUX.match(t) and not rules.DAMAGE.search(t) and role in {None,'R','Q'}:return 'R','EXPLICIT_ASSIGNED_ADVISORY_AUXILIARY_TASK'
 return BASE_DECIDE(text,role,previous)
rules.decide=decide

def applicable_row(raw,row):
 if not row['responsibility_text'].strip() or row['r11_group']=='PRIOR_ALIGNMENT_PRESERVED' or re.search(r'(?m)^\s*(?:其他|其它)\s*$',row['responsibility_text']):return True
 if br_layout(raw) or re.search(r'员工待遇|通晓|熟谙|谙熟|熟识|当好.{0,30}(?:参谋|助手|把关人|工作窗口|业务窗口)',raw):return True
 if v3.QCAP.search(raw) and OBJ.search(raw):
  for m in v3.QCAP.finditer(raw):
   nxt=v3.RCAP.search(raw,m.end());block=raw[m.end():nxt.start() if nxt else len(raw)]
   if re.search('管理|事务|安排|发布|采购|收发|对接|接待|保养|巡查|盘点|调度|核算|报销|维护',block):return True
 return False

def process(raw,row):
 p=v3.process(raw,row);p['policy_version']='R11_V4_LITERAL_LAYOUT_NOMINAL_WORK_AND_CAPTIONS';return p

# Protect literal quantities and referenced document identifiers. A decimal is
# a task-list marker only when a list boundary or matching parent proves it.
_NESTED_BASE=v3.nested_markers
v3.NESTED=re.compile(r'(?<![A-Za-z0-9.])([1-9]\d?)\.([1-9]\d?)[ \t]*(?=[\u3400-\u9fff])(?!(?:万|千|百|十|亿|年|月|天|岁|米|吨|元|寸|英寸|秒|小时|分钟|毫|伏|瓦|安培|赫兹|度|升|克|公斤|倍|条|章|节|款|号|版))')
REF_CUE=re.compile(r'(?:依据|根据|参照|按照|遵循|符合|满足|阅读|查阅|学习|执行|标准|版本|编号)\s*$')
def nested_markers(s):
 ms=_NESTED_BASE(s);allowed=[]
 for m in ms:
  if REF_CUE.search(s[max(0,m.start()-15):m.start()]):continue
  major=m[1];chinese='一二三四五六七八九'[int(major)-1] if 1<=int(major)<=9 else None
  parent=bool(re.search(r'(?<![A-Za-z0-9.])'+re.escape(major)+r'[、.)](?!\d)',s)) or bool(chinese and re.search(re.escape(chinese)+r'[、.)]',s))
  group_anchor=any(x[1]==major and (not s[:x.start()].strip() or re.search(r'[\n;；。:：]\s*$',s[:x.start()])) for x in ms)
  if parent or group_anchor:allowed.append(m)
 return allowed
v3.nested_markers=nested_markers
_norm4=rules.normalize

def normalize(raw):
 s,st=_norm4(raw)
 if any(stage['name']=='nested_ordinals' for stage in st):
  es=[]
  for m in v3.NESTED.finditer(s):
   if not s[:m.start()].strip() or re.search(r'\n\s*$',s[:m.start()]):es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='SINGLE_CHILD_WITHIN_PROVEN_NESTED_LIST'))
  s,es=rules.apply(s,es)
  if es:st.append(dict(name='singleton_child_list_marker',edits=es))
 return s,st
rules.normalize=normalize

rules.HROLE['工作内容与要求']='R';rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)
INTEREST=re.compile(r'^(?:对|对于)[^,，;；。]{1,80}(?:热爱|热情|兴趣)(?:浓厚|极大|很高|十足)?(?=[,，;；。]|$)')
MODAL_CORRECT=re.compile(r'^(?:能(?:够)?|可)(?:正确|准确|安全|规范|独立|熟练)(?:地|的)?(?:操作|使用|处理|维修|检修|执行|完成|判断).{2,}')
_qu4=rules.qualification;_ta4=rules.is_task;_de4=rules.decide;_sp4=rules.split_mixed

def qualification(t):return bool(INTEREST.match(rules.cleantext(t))) or _qu4(t)
rules.qualification=qualification

def is_task(t):
 t=rules.cleantext(t)
 if re.match(r'^(?:准确|正确|及时)?判断(?:各种|设备|系统|产品|异常|故障|运行|生产|客户|业务|问题)',t):return True
 return _ta4(t)
rules.is_task=is_task

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if INTEREST.match(t):return 'N','EXPLICIT_PERSONAL_INTEREST_OR_ENTHUSIASM'
 question=re.search(r'是否(?:做|参与|负责|开发|完成)过',t)
 if question and re.match(r'^(?:在|对|是否|你|您)',t) and not re.search(r'检查|审核|核查|核对|评估|调查|确认|统计|记录|询问',t[:question.start()]):return 'N','APPLICANT_PAST_EXPERIENCE_QUESTION'
 if re.search('从基层做起|从基层岗位做起|方可成为管理干部',t) and not re.match(r'^(?:负责|协助|制定|组织|实施|开展|建立|安排)',t):return 'N','APPLICANT_DEVELOPMENT_PATH'
 if role=='R' and MODAL_CORRECT.match(t) and not rules.HARDQUAL.search(t) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_CORRECT_OPERATION_IN_DUTY_SECTION'
 return _de4(text,role,previous)
rules.decide=decide
CAUSE=re.compile(r'确保|保证|使其|让|使|帮助|促使|培训|指导|推动|促进|培养|提升|提高|协助|支持|组织')

def split_mixed(s,a,b,role):
 intervals=_sp4(s,a,b,role);points={a,b}
 for lo,hi in intervals:points.update((lo,hi))
 for point in list(points-{a,b}):
  if s[point-1] in ',，;；。\n':continue
  right=rules.cleantext(s[point:b]);last_clause=re.split('[,，;；。\n]',s[a:point])[-1]
  if re.match('对|具备|具有|拥有',right) and CAUSE.search(last_clause) and not re.search('者优先|最好|为佳|学历|学位|本科|大专',right):points.discard(point)
 if role=='R':
  cs=rules._clauses(s,a,b)
  for i in range(1,len(cs)):
   lo,hi=cs[i];left=rules.cleantext(s[cs[i-1][0]:cs[i-1][1]]);right=rules.cleantext(s[lo:hi])
   if (MODAL_CORRECT.match(left) or rules.is_task(left)) and qualification(right):points.add(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed
_app4=applicable_row

def applicable_row(raw,row):
 return _app4(raw,row) or bool(re.search(r'工作内容与要求|是否(?:做|参与|负责|开发|完成)过|对[^。;；\n]{1,80}(?:热爱|热情|兴趣)|从基层做起|从基层岗位做起|方可成为管理干部|(?:能(?:够)?|可)(?:正确|准确|安全|规范)(?:操作|使用|处理|维修|检修|执行|完成|判断)',raw)) or bool(re.search(r'(?:确保|保证|使其|让|帮助|促使|培训|指导|推动|促进|培养|提升|提高|协助|支持|组织)[^。;；\n]{0,80}(?:对[^,，;；]{1,35}有|具备|具有|拥有)',raw)) or bool(re.search(r'\d+[.．]\d+\s*[\u3400-\u9fff]',raw))

_wrapper_base=v3._wrapper
CAPTION_EVIDENCE=re.compile(r'(?:岗位职责|工作职责|职责描述|工作内容|岗位要求|任职要求|任职资格|技能要求)\s*[:：]')
def wrapper(s):
 a=len(s)-len(s.lstrip());b=s.rfind(']')
 if a<len(s) and s[a]=='[' and b>a and b-a>40 and len(list(CAPTION_EVIDENCE.finditer(s[a:b])))>=2:return (a,b)
 return _wrapper_base(s)
v3._wrapper=wrapper
_de5=rules.decide

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if re.match(r'^(?:详见官网|详情见官网|更多职位上|更多职位请|更多招聘信息)',t):return 'N','SOURCE_OR_JOB_BOARD_FOOTER'
 return _de5(text,role,previous)
rules.decide=decide
_app5=applicable_row

def applicable_row(raw,row):return _app5(raw,row) or (raw.lstrip().startswith(('[','［')) and len(list(CAPTION_EVIDENCE.finditer(raw)))>=2)

# Past-tense suffixes must not match the first character of 过程 or related
# work objects (负责过程管理 / 负责过账 / 管理过期物料).
COMPOUND_AFTER_GUO='程|账|户|磅|站|检|期|渡|氧'
rules.HARDQUAL=re.compile(rules.HARDQUAL.pattern.replace('从事过','从事过(?!'+COMPOUND_AFTER_GUO+')').replace('负责过','负责过(?!'+COMPOUND_AFTER_GUO+')').replace('参与过','参与过(?!'+COMPOUND_AFTER_GUO+')').replace('做过','做过(?!'+COMPOUND_AFTER_GUO+')'))
rules.PAST=re.compile(rules.PAST.pattern.replace(')过',')过(?!'+COMPOUND_AFTER_GUO+')'))
rules.ACTION=re.compile(rules.ACTION.pattern.replace('(?!过|','(?!过(?!'+COMPOUND_AFTER_GUO+')|'))
_task5=rules.is_task;_qual5=rules.qualification;_decide7=rules.decide;_operational=rules.operational_knowledge
PROCESS_WORK=re.compile(r'^(?:负责|参与|主导|从事|设计|开发|操作|完成|组织|使用|处理|管理|做好)(?:过程|过账|过户|过磅|过站|过检|过期|过渡|过氧)')
HAVE_ATTRIBUTE=re.compile(r'^(?:在|于)[^,，;；。]{0,45}(?:有|具有|具备|拥有)[^,，;；。]{0,35}(?:人脉|关系|资源|经验|经历|能力)')
DEGREE_FIELD=re.compile(r'^[^。;；:：]{1,90}(?:相关)?专业[。;；]*$')

OBJ=re.compile(OBJ.pattern+'|厂区|绿化|卫生|环境|运输|油卡|厂务')
SOFT_END=re.compile(r'(?:管理|事务|安排|发布|采购|收发|对接|接待|保养|巡查|盘点|调度|核算|制作发布|报销|维护|监督|改善|跟进|充值|提交)(?:等|工作|等工作)?[。;；:：]*$')

def is_task(t):
 t=rules.cleantext(t);core=rules.ADVERB.sub('',t)
 if PROCESS_WORK.match(core):return True
 if re.match(r'^交流(?:工作|项目|管理|先进|实践|技术|相关)?经验',core):return True
 if re.match(r'^(?:严格)?(?:按照|根据|按)',core) and re.search(r'摆放|放置|挂在|挂放|归位|理货|查找',core) and not re.search('能力|经验|知识|技能|者优先',core):return True
 if re.match(r'^保持',core) and re.search('设备|工具|机器|机台|场地|厂区|现场|车内|车外|卫生|清洁|库房|货架',core):return True
 return _task5(t)
rules.is_task=is_task

def qualification(t):
 t=rules.cleantext(t)
 if HAVE_ATTRIBUTE.match(t):return True
 if DEGREE_FIELD.match(t) and not re.match(r'^(?:负责|协助|培养|培训|讲授|教学|授课|招聘|指导|学习|教授|从事|开展)',t):return True
 if PROCESS_WORK.match(rules.ADVERB.sub('',t)) and not re.search('学历|学位|能力|经验|经历|技能|知识|优先',t):return False
 return _qual5(t)
rules.qualification=qualification

def operational_knowledge(t):
 return _operational(t) or bool(re.match(r'^(?:及时|深入|充分|全面)?(?:了解|掌握|熟悉|理解)',t) and re.search('运行状况|设备状况|生产状况|工况',t) and not re.search('学历|学位|经验|能力|者优先|精通|熟练|软件|工具|编程',t))
rules.operational_knowledge=operational_knowledge

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if HAVE_ATTRIBUTE.match(t):return 'N','EXPLICIT_PERSONAL_RELATIONSHIP_RESOURCE_OR_CAPABILITY'
 if DEGREE_FIELD.match(t) and not re.match(r'^(?:负责|协助|培养|培训|讲授|教学|授课|招聘|指导|学习|教授|从事|开展)',t):return 'N','EXPLICIT_APPLICANT_DISCIPLINE_LIST'
 if re.match(r'^(?:以上|上述|所有|本次)(?:招聘)?(?:岗位|职位).{0,70}(?:签订|签署).{0,30}(?:劳动合同|劳务合同)',t):return 'N','RECRUITMENT_EMPLOYMENT_CONTRACT_NOTICE'
 if role in {None,'R','Q'} and office_nominal(t):return 'R','LITERAL_WORK_OBJECT_AND_NOMINAL_OPERATION'
 if role=='R' and re.match(r'^(?:了解|熟悉|掌握)(?:并|和|及)(?:发掘|挖掘|开拓|开发|维护|操作|处理|解决)',t) and not rules.DAMAGE.search(t):return 'R','KNOWLEDGE_JOINED_TO_CURRENT_OPERATION'
 if role=='R' and re.match(r'^(?:学习|练习)(?!能力|意愿|成绩|兴趣|效率|素质).{2,}',t) and not rules.HARDQUAL.search(t) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_ASSIGNED_LEARNING_OR_PRACTICE'
 return _decide7(text,role,previous)
rules.decide=decide

# Explicit field captions. Working objects preceded by an assignment verb are
# not interpreted as a new metadata section.
NEW_HEADS={'角色和责任':'R','角色和职责':'R','职位概要':'R','Post summary':'R','Work contents':'R','Work content':'R','Work experience':'Q_FIELD','语言要求':'Q_FIELD','Language requirement':'Q_FIELD','职业生涯规划':'B','Career planning':'B','培训需求':'Q_FIELD','Training requirements':'Q_FIELD','工作条件':'A','Work conditions':'A'}
for name,role in NEW_HEADS.items():rules.HROLE[name.lower()]=role
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)
_heads4=rules.headings

def headings(s):
 result=[]
 for h in _heads4(s):
  if h['name'].lower() in {x.lower() for x in NEW_HEADS} and re.search(r'(?:负责|协助|办理|管理|核算|处理|落实|完善|制定|统筹|改善|优化|编制)$',s[max(0,h['a']-12):h['a']]):continue
  result.append(h)
 return result
rules.headings=headings

# A trailing dot is a conventional list-marker delimiter, not a third level.
v3.NESTED=re.compile(v3.NESTED.pattern.replace(r'\.([1-9]\d?)[ \t]*',r'\.([1-9]\d?)\.?[ \t]*'))
_removed_markers=set();_normal5=rules.normalize;_oldspans4=engine.source_old_spans

def normalize(raw):
 global _removed_markers
 s,st=_normal5(raw);_removed_markers=set()
 for stage in st:
  if stage['name'] in {'nested_ordinals','singleton_child_list_marker'}:
   for e in stage['edits']:
    m=re.match(r'\s*(\d+(?:\.\d+)+)',e['old'])
    if m:_removed_markers.add(m[1])
 return s,st
rules.normalize=normalize

def source_old_spans(before,s):
 es=[];offset=0;hay=engine.flat(s)
 if _removed_markers:
  for line in before.splitlines(keepends=True):
   content=line.rstrip('\r\n');m=re.search(r'(?<![\d.])(\d+(?:\.\d+)+)\.?\s*$',content)
   if m and m[1] in _removed_markers and engine.flat(content) not in hay:es.append(dict(a=offset+m.start(),b=offset+m.end(),old=m[0],new='',rule='SOURCE_PROVEN_PRIOR_TRAILING_LIST_NUMBER_FOR_ALIGNMENT_ONLY'))
   offset+=len(line)
 clean,es=rules.apply(before,es);prefix=[dict(name='prior_trailing_list_number_alignment',edits=es)] if es else []
 spans,miss=_oldspans4(clean,s);v3._parent_events=prefix+v3._parent_events;return spans,miss
engine.source_old_spans=source_old_spans
_app6=applicable_row

def applicable_row(raw,row):
 return _app6(raw,row) or bool(re.search(r'(?:负责|参与|主导|从事|设计|开发|操作|完成|组织|使用|做|处理|管理)(?:过程|过账|过户|过磅|过站|过检|过期|过渡|过氧)|交流.{0,6}经验|人脉|角色和责任|角色和职责|职位概要|Work experience|Work contents|培训需求|工作条件|职业生涯规划|(?:保持).{0,35}(?:机台|设备|现场|卫生|清洁)|(?:按照|按|根据).{0,55}(?:摆放|放置|挂在|查找)|油卡|厂区卫生|绿化|工作环境.{0,15}改善|运行状况|(?:以上|上述)招聘岗位|了解和发掘|学习幻灯片|练习幻灯片|类专业',raw,re.I))

# A caption may introduce a numbered duty without a colon or dot.
_normal6=rules.normalize
BARE_CAPTION=re.compile(r'(职位描述|岗位职责|职责描述|工作职责|工作内容|任职要求|任职资格)\s*(?=[1-9]\d?(?:能|可|需|负责|协助|在|按|完成))')
MODAL_ENUM=re.compile(r'(?<![A-Za-z0-9.])([1-9]\d?)\s*(?=(?:能够|能|可|需)(?:保持|协助|完成|正确|准确|独立|熟练|操作|使用))')

def normalize(raw):
 s,st=_normal6(raw);es=[]
 for m in BARE_CAPTION.finditer(s):
  if re.search('编写|制定|编制|撰写|根据|修改|界定|定义',s[max(0,m.start()-12):m.start()]):continue
  es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n'+m[1]+':\n',rule='CAPTION_BEFORE_BARE_TASK_ORDINAL'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='bare_caption_boundary',edits=es))
 ms=list(MODAL_ENUM.finditer(s))
 if len(ms)>=2 and any(int(y[1])==int(x[1])+1 for x,y in zip(ms,ms[1:])):
  es=[dict(a=m.start(),b=m.end(),old=m[0],new='\n'+m[1]+'、',rule='COHERENT_MODAL_TASK_ORDINAL') for m in ms];s,es=rules.apply(s,es)
  if es:st.append(dict(name='modal_task_ordinals',edits=es))
 return s,st
rules.normalize=normalize
_decide8=rules.decide

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if role=='R' and re.match(r'^(?:能(?:够)?|可)(?:独立|高效|及时|正确|准确|有效|熟练)*(?:协助|保持|完成)',t) and re.search('工作|任务|客户|沟通|对接|设备|设计|勘察|操作',t) and not rules.HARDQUAL.search(t) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_MODAL_COLLABORATION_OR_OPERATION'
 return _decide8(text,role,previous)
rules.decide=decide
_app7=applicable_row

def applicable_row(raw,row):
 return _app7(raw,row) or bool(BARE_CAPTION.search(raw) or re.search(r'学习(?!能力|意愿|成绩|兴趣|效率|素质)|练习|(?:能(?:够)?|可)(?:独立|高效|及时|正确|准确|有效|熟练)*(?:协助|保持|完成)',raw))

# Attribute adjectives are not assignments; explicit modal work under a duty
# caption is retained, but a degree/tenure/preference clause remains excluded.
rules.POSITIVE_ASSIGN=re.compile(rules.POSITIVE_ASSIGN.pattern.replace('(?!过|人|心)',r'(?!过|人|心|的(?:职业态度|工作态度|态度|精神)|态度|精神)'))
DEGREE_CONDITION=re.compile(r'^[^。;；:：]{1,100}(?:相关|类)?专业(?:者|人员|毕业)?(?:优先考虑|优先录用|优先)?[。;；!！]*$')
MODAL_JOB=re.compile(r'^(?:能(?:够)?|可)(?:(?:正确|准确|安全|规范|独立|熟练|高效|及时|快速|有效)(?:地|的)?)*(?:协调|响应|支撑|应对|组织|维护|执行|操作|使用|协助|完成|提供|处理|开发|设计|分析|判断).{2,}')
_task6=rules.is_task;_qual6=rules.qualification;_decide9=rules.decide;_split6=rules.split_mixed

OBJ=re.compile(OBJ.pattern+'|工作时间|工时|数据库|系统')
SOFT_END=re.compile(SOFT_END.pattern.replace('|提交)', '|提交|录入|运维|支撑)'))

def is_task(t):
 core=rules.ADVERB.sub('',rules.cleantext(t))
 if re.match(r'^(?:配置|调配|部署|分发)(?!过|能力|经验|要求|参数).{2,}',core):return True
 return _task6(t)
rules.is_task=is_task

def qualification(t):
 t=rules.cleantext(t)
 if re.match(r'^负责(?:的)?(?:职业态度|工作态度|态度|精神|意识|心)',t):return True
 if DEGREE_CONDITION.match(t) and not re.match(r'^(?:负责|协助|培养|培训|讲授|教学|授课|招聘|指导|学习|教授|从事|开展)',t):return True
 return _qual6(t)
rules.qualification=qualification

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if re.match(r'^负责(?:的)?(?:职业态度|工作态度|态度|精神|意识|心)',t):return 'N','RESPONSIBLE_AS_PERSONAL_ATTITUDE_ADJECTIVE'
 if DEGREE_CONDITION.match(t) and not re.match(r'^(?:负责|协助|培养|培训|讲授|教学|授课|招聘|指导|学习|教授|从事|开展)',t):return 'N','EXPLICIT_APPLICANT_DISCIPLINE_OR_PREFERENCE'
 if re.match(r'^(?:有想学|想学.{1,30}(?:人员|人才)|有意学习)',t):return 'N','APPLICANT_LEARNING_INTEREST'
 if role=='R' and MODAL_JOB.match(t) and not rules.HARDQUAL.search(t) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_ASSIGNED_MODAL_WORK'
 if role=='Q' and not qualification(t) and not re.search('经验|经历|能力|知识|熟悉|熟练|精通|掌握|优先|学历|学位',t):
  cs=[rules.cleantext(x) for x in re.split('[,，]',t)]
  if len(cs)>1 and OBJ.search(cs[0]) and re.search('工作|运维|维护|支撑|开发|设计|管理|服务',cs[0]) and any(rules.is_task(x) for x in cs[1:]):return 'R','CONCRETE_NOMINAL_WORK_WITH_ASSIGNED_CONTINUATION'
 return _decide9(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 intervals=_split6(s,a,b,role);points={a,b}
 for lo,hi in intervals:points.update((lo,hi))
 if role=='R':
  cs=rules._clauses(s,a,b)
  for i in range(1,len(cs)):
   lo,hi=cs[i];left=rules.cleantext(s[cs[i-1][0]:cs[i-1][1]]);right=rules.cleantext(s[lo:hi])
   if MODAL_JOB.match(left) and qualification(right):points.add(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed
rules.HROLE['全方位保障']='B';rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)

# Final policy is evaluated on all 4,073,781 rows. No lexical applicability
# screen can omit a case affected by any of the accumulated corrections.
def applicable_row(raw,row):return True

# Personal opportunities/advantages are not a source of additional assigned
# work. The next actual duty caption resets this role in the usual way.
for h in ['你将获得','您将获得','职位优势','培训成长']:
 rules.HROLE[h.lower()]='OFFER'
for h in ['销售指标达成','数据报表管理','主要职责Essential responsibilities and duties','Essential responsibilities and duties','主要任务The main missions of the role are','The main missions of the role are','通用职责General responsibilities','通用职责','General responsibilities']:
 rules.HROLE[h.lower()]='R'
for h in ['技术和能力/ Skills and competencies','Skills and competencies','领导力模型LCM','领导力模型','公司期望的行为 Company’s Expected Behaviors','Company’s Expected Behaviors','公司期望的行为','资格要求Qualifications']:
 rules.HROLE[h.lower()]='Q_FIELD'
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)
_head7=rules.headings

GENERIC_JD={'职位描述','岗位描述','职位说明','岗位说明','job description'}

def headings(s):
 hs=_head7(s);out=[]
 for h in hs:
  before=s[:h['a']];pre=before.rstrip()
  if h['name']=='工作经验':
   boundary=not pre or bool(re.search(r'\n\s*$',before)) or pre[-1:] in '。;；:：[(【' or bool(re.search(r'(?:\d+[、.)]|[一二三四五六七八九十][、.)])\s*$',before))
   explicit_colon=bool(re.search('[:：]',s[h['a']:h['b']]))
   if not boundary and not explicit_colon:continue
  if h['name'].lower() in GENERIC_JD:
   lead=s[h['b']:].lstrip();lead=re.sub(r'^\d+[.、)]\s*','',lead);first=re.split('[,，。;；\n]',lead,1)[0].strip()
   academic=bool(DEGREE_FIELD.fullmatch(first) or re.fullmatch(r'(?:全日制|统招)?(?:本科|大专|专科|硕士|博士)(?:及以上|以上)?(?:学历|毕业)?',first))
   if academic and not re.match(r'^(?:负责|协助|培养|培训|讲授|教学|授课|招聘|指导|学习|教授|从事|开展)',first):h=dict(h,role=None,neutral_container=True)
  out.append(h)
 return out
rules.headings=headings
_task7=rules.is_task;_decide10=rules.decide;_split7=rules.split_mixed;_operational2=rules.operational_knowledge
ANIMAL_OPERATION=re.compile(r'^.{1,45}(?:隔离驯化|饲养管理|饲喂|育种|驯化)(?:\([^)]{0,45}\))?[。;；]?$')

def is_task(t):
 t=rules.cleantext(t)
 if re.match(r'^(?:专业)?(?:处理|接待|解答|维护|分析)(?!能力|经验|知识|技能).{0,}',t) and t.startswith('专业') and not re.search('能力|经验|知识|技能|优先',t):return True
 if re.match(r'^(?:了解收集|了解并收集|了解并发掘|熟悉并操作).{2,}',t):return True
 if re.fullmatch(r'[^,，;；。]{1,65}跑市场[。;；]?',t) and not re.search('经验|能力|能适应|可接受|愿意|喜欢|希望|热爱|兴趣|具备|具有',t):return True
 if ANIMAL_OPERATION.match(t) and not re.search('熟悉|掌握|了解|经验|能力|学历|专业',t):return True
 return _task7(t)
rules.is_task=is_task

def operational_knowledge(t):
 return _operational2(t) or bool(re.match(r'^(?:及时|充分)?(?:了解|掌握|熟悉)',t) and re.search('售点|市场动态|市场变化',t) and not re.search('经验|能力|知识|技巧|课程|软件|工具|规则|流程|学历|学位',t))
rules.operational_knowledge=operational_knowledge

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if role=='OFFER':return 'N','EXPLICIT_PERSONAL_BENEFIT_OR_CAREER_OPPORTUNITY_SECTION'
 if re.fullmatch(r'本岗位为.{1,45}(?:岗|职位|岗位)[。;；]?',t):return 'N','EXPLICIT_POSITION_IDENTITY_ONLY'
 if role=='R' and re.match(r'^(?:能(?:够)?|可)(?:高效|有效|正确|准确|及时|快速|独立|熟练)*(?:制定|识别|遵守).{2,}',t) and not rules.HARDQUAL.search(t) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_ASSIGNED_PROCEDURE_OR_COMPLIANCE'
 if role in {None,'R'} and ANIMAL_OPERATION.match(t) and not qualification(t):return 'R','LITERAL_ANIMAL_OPERATION_WITH_OBJECT_AGE_ANNOTATION'
 return _decide10(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 ints=_split7(s,a,b,role);points={a,b}
 for lo,hi in ints:points.update((lo,hi))
 if role is None:
  first=rules.cleantext(s[a:b]);cs=rules._clauses(s,a,b)
  if re.match(r'^(?:熟悉|精通|掌握|了解)',first):
   for lo,hi in cs[1:]:
    prefix=s[a:lo];right=rules.cleantext(s[lo:hi])
    if not re.search('经验|能力|学历|学位|具备|具有|拥有',prefix) and rules.is_task(right) and not qualification(right):points.add(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

# The original bilingual matcher treated Chinese characters as adjacent
# English letters. Correct its word boundary without altering any source text.
from tools.r11_headings_v4 import headings as ascii_word_headings
v3.base_headings=ascii_word_headings
_qual7=rules.qualification;_decide11=rules.decide;_split8=rules.split_mixed
LOCATION_CONDITION=re.compile(r'^服从.{0,35}(?:工作地|工作地点|驻地|就近工作地)安排[。;；]?$')
def _without_connector(t):return re.sub(r'^(?:另|另外|此外)\s*[,，:：]\s*','',rules.cleantext(t))
def qualification(t):return bool(LOCATION_CONDITION.match(_without_connector(t))) or _qual7(t)
rules.qualification=qualification

def decide(text,role,previous=None):
 if LOCATION_CONDITION.match(_without_connector(text)):return 'N','APPLICANT_WORK_LOCATION_ALLOCATION_CONDITION'
 return _decide11(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 ints=_split8(s,a,b,role);points={a,b}
 for lo,hi in ints:points.update((lo,hi))
 cs=rules._clauses(s,a,b)
 for i in range(1,len(cs)):
  lo,hi=cs[i];left=rules.cleantext(s[cs[i-1][0]:cs[i-1][1]]);right=_without_connector(s[lo:b])
  if rules.is_task(left) and LOCATION_CONDITION.match(right):points.add(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

_finish5=rules.finish_body

def finish_body(body):
 s,st=_finish5(body);majors={x.split('.')[0] for x in _removed_markers};es=[]
 for m in re.finditer(r'(?m)^([1-9]\d?)[ \t]*(?=[\u3400-\u9fff])(?![万千百十亿元年月日周时分秒天岁米吨寸型号级类代维相核轴系国家个件次批种套台人位户条头只辆间层期段项所座份张株升毫克斤页])',s):
  if m[1] in majors:es.append(dict(a=m.start(),b=m.end(),old=m[0],new='',rule='MAJOR_ORDINAL_WITH_PROVEN_CHILD_LIST'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='proven_parent_list_marker',edits=es))
 return s,st
rules.finish_body=finish_body

# Recover a last single-child 'other' section only inside an already proven
# hierarchy. Do not change an unproven decimal or a referenced document ID.
_norm7=rules.normalize

def normalize(raw):
 s,st=_norm7(raw)
 if len({x.split('.')[0] for x in _removed_markers})>=2:
  es=[]
  for m in re.finditer(r'(?<![\d.])([1-9]\d?)(?:其他|其它)\s*\1\.1\s*(?=完成|负责|协助|承担)',s):
   if REF_CUE.search(s[max(0,m.start()-20):m.start()]):continue
   es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='PROVEN_LAST_OTHER_SECTION_WITH_SINGLE_CHILD'))
  s,es=rules.apply(s,es)
  if es:st.append(dict(name='last_other_child_structure',edits=es))
 return s,st
rules.normalize=normalize
_decide12=rules.decide

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if t=='执行机构':return 'N','BARE_TECHNICAL_COMPONENT_IS_NOT_A_TASK'
 if t=='自我管理':return 'N','GENERIC_SELF_MANAGEMENT_ATTRIBUTE'
 return _decide12(text,role,previous)
rules.decide=decide
_finish6=rules.finish_body

def finish_body(body):
 s=body;st=[];majors={x.split('.')[0] for x in _removed_markers};es=[]
 for m in re.finditer(r'(?m)^([1-9]\d?)\s*(?:管理|其他|其它)\s*(?=\n|$)',s):
  if m[1] in majors:es.append(dict(a=m.start(),b=m.end(),old=m[0],new='',rule='BARE_PARENT_CATEGORY_WITH_PROVEN_CHILD_TASKS'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='bare_parent_category_syntax',edits=es))
 s,rest=_finish6(s);st.extend(rest);return s,st
rules.finish_body=finish_body
''',
'tools.r11_policy_v5': r'''"""Final eligibility-boundary fixes and original-source reconstruction."""
import re
from tools import r11_policy_v4 as v4
from tools.r11_io import *
engine=v4.engine;rules=v4.rules;v3=v4.v3
BASE_SPANS=engine.source_old_spans;BASE_QUAL=rules.qualification;BASE_DECIDE=rules.decide;BASE_SPLIT=rules.split_mixed
ADAPT=re.compile(r'^(?:能(?:够)?|可)?适应.{0,20}(?:出差|倒班|加班|工作时间|工作节奏|工作压力|工作强度)[。;；]?$')
FLUENT_REVERSED=re.compile(r'^[^,，;；。]{1,65}(?:操作|使用|应用|运用)(?:比较|较为)?熟练(?=[,，;；。]|$)')
PERSON_SKILL=re.compile(r'培养|培训|指导|帮助|使其|让|提高|提升|确保|保证|考核|评估')
TITLE=re.compile(r'^.{1,40}负责人[。;；]?$')

def source_old_spans(before,s):
 clean=engine.folded(before).replace('\xa0',' ');prefix=[]
 if before and clean!=before:prefix=[dict(name='parent_representation_whitespace_and_width',edits=[dict(a=0,b=len(before),old=before,new=clean,rule='PARENT_ALIGNMENT_ONLY_EQUIVALENT_ENTITY_WIDTH_WHITESPACE')])]
 spans,missing=BASE_SPANS(clean,s);v3._parent_events=prefix+v3._parent_events;return spans,missing
engine.source_old_spans=source_old_spans

def qualification(t):
 t=rules.cleantext(t)
 if ADAPT.match(t) or (FLUENT_REVERSED.match(t) and not PERSON_SKILL.search(re.split('[,，;；。]',t,1)[0])):return True
 return BASE_QUAL(t)
rules.qualification=qualification

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if ADAPT.match(t):return 'N','APPLICANT_TRAVEL_SHIFT_OR_WORKLOAD_ADAPTABILITY'
 if FLUENT_REVERSED.match(t) and not PERSON_SKILL.search(re.split('[,，;；。]',t,1)[0]):return 'N','REVERSED_PERSONAL_PROFICIENCY_STATEMENT'
 if TITLE.match(t) and not re.match(r'^(?:负责|协助|培养|培训|指导|招聘|支持|帮助|担任|配合|作为)',t):return 'N','STANDALONE_JOB_HOLDER_TITLE'
 return BASE_DECIDE(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 ints=BASE_SPLIT(s,a,b,role);points={a,b}
 for lo,hi in ints:points.update((lo,hi))
 for lo in list(points-{a,b}):
  prefix=rules.cleantext(s[a:lo]);right=rules.cleantext(s[lo:b])
  if rules.HARDQUAL.search(prefix) and qualification(prefix) and re.match(r'^(?:能(?:够)?|可)(?:独立|高效|熟练|有效|正确|快速|及时|准确)*(?:完成|开发|设计|操作|使用|处理|分析|判断|维护|协助|协调|制定|识别)',right):points.discard(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

def process(raw,row):
 p=v4.process(raw,row);p['policy_version']='R11_V5_ORIGINAL_SOURCE_FINALIZATION'
 if p['source_alignment_uncovered']:
  # An unlocatable prior output is retained as historical evidence, not allowed
  # to veto a fully source-traced reconstruction of this record's original.
  p['historical_parent_alignment_gaps']=p['source_alignment_uncovered'];p['source_alignment_uncovered']=[];p['parent_alignment_resolution']='REBUILT_FROM_COMPLETE_ORIGINAL';p['after']=p['proposed_after'];p['adopted']=True;p['text_changed']=p['after']!=p['before'];p['preserve_parent_reason']=None
  nx=p['excluded_fragment_count'];p['status']=('DUTIES_WITH_SOURCE_LIMIT' if nx else 'DUTIES_RETAINED') if p['after'].strip() else ('NO_USABLE_DUTIES_SOURCE_LIMIT' if nx else 'NO_EXPLICIT_DUTIES')
 return p

def applicable_row(raw,row):
 # These new negative rules can only change a currently retained matching
 # literal term; every old-alignment exception is included without exception.
 t=engine.flat(row['responsibility_text'])
 return row['r11_group']=='PRIOR_ALIGNMENT_PRESERVED' or any(x in t for x in ['适应','熟练','能','可','负责人'])

# A common caption word embedded in a sentence is an object, not a new field.
BASE_HEADS=rules.headings
GENERIC_CAPTIONS={'工作任务','工作内容','技术要求','工作制度','工作时间','职责','内容','要求','技能','待遇','福利'}
OBJECT_END=re.compile(r'(?:其他|其它|相关|这些|各项|相应|上述|本岗|本岗位|日常|所需|明确|具体|该|此|其)\s*$')
OBJECT_VERB=re.compile(r'(?:完成|承担|处理|执行|履行|做好|负责|根据|按照|明确|界定|编制|制定|符合|满足|遵守|了解|熟悉|掌握|修改|优化|改善|培训|组织)(?:相关|这些|各项|相应|具体|明确|的)?\s*$')
for h,r in {'基本职责':'R','业务技能要求':'Q_FIELD','专业知识要求':'Q_FIELD','专业知识及技能':'Q_FIELD','专业知识及技能要求':'Q_FIELD','我们为员工提供':'OFFER','你将受益匪浅':'OFFER','职位福利':'OFFER','职位亮点':'OFFER','负责产品':'A','职位':'A','隶属':'A','服务区域':'A'}.items():rules.HROLE[h.lower()]=r
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)

DETACHED_HEAD=re.compile(r'(?<!\S)('+'|'.join(sorted([re.escape(k) for k in rules.HROLE if len(k)>=4 and re.fullmatch('[\u3400-\u9fff]+',k)],key=len,reverse=True))+r')(?=\s+\S)')
def headings(s):
 out=[]
 for h in BASE_HEADS(s):
  pre=s[:h['a']]
  if h['name'] in GENERIC_CAPTIONS and ((pre and re.search('[\u3400-\u9fffA-Za-z]$',pre)) or OBJECT_END.search(pre) or OBJECT_VERB.search(pre)):continue
  out.append(h)
 for m in DETACHED_HEAD.finditer(s):
  if any(h['a']<=m.start()<h['b'] for h in out):continue
  pre=s[max(0,m.start()-30):m.start()]
  if OBJECT_END.search(pre) or OBJECT_VERB.search(pre):continue
  out.append(dict(a=m.start(),b=m.end(),role=rules.HROLE[m[1].lower()],name=m[1]))
 return sorted(out,key=lambda h:(h['a'],h['b']))
rules.headings=headings

# Generic labels followed by alternate colon typography are still labels;
# mathematical ratios elsewhere are not touched.
BASE_NORMAL=rules.normalize

def normalize(raw):
 s,st=BASE_NORMAL(raw);es=[]
 for m in re.finditer(r'(?:岗位职责|工作职责|职责描述|任职要求|任职资格|岗位要求|职位要求)\s*∶',s):es.append(dict(a=m.end()-1,b=m.end(),old='∶',new=':',rule='CAPTION_ONLY_ALTERNATE_COLON'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='caption_colon_typography',edits=es))
 # Circled ordinal glyphs are layout; their values are preserved in the log.
 es=[dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='CIRCLED_LIST_MARKER') for m in re.finditer('[①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳]',s)]
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='circled_list_layout',edits=es))
 return s,st
rules.normalize=normalize
D5=rules.decide;Q5=rules.qualification;TASK5=rules.is_task;OP5=rules.operational_knowledge

def is_task(t):
 t=rules.cleantext(t)
 if re.match(r'^(?:以及|并且|并|同时)',t):
  rest=re.sub(r'^(?:以及|并且|并|同时)\s*','',t)
  if TASK5(rest):return True
 if re.match(r'^独立自主(?:地)?进行.{2,}',t):return True
 return TASK5(t)
rules.is_task=is_task

def operational_knowledge(t):return OP5(t) or bool(re.match(r'^(?:及时|充分|全面)?(?:掌握|了解|熟悉)',t) and re.search('市场信息|业务进展|客户动态',t) and not re.search('能力|经验|知识|技巧|软件|工具|规则|流程',t))
rules.operational_knowledge=operational_knowledge

def qualification(t):
 t=rules.cleantext(t)
 if re.match(r'^(?:能|可)(?:接受|适应).{0,20}(?:出差|倒班|加班|工作压力|工作强度)',t):return True
 if re.match(r'^[^,，;；。]{0,18}(?:岗位|职位)要求[^,，;；。]{0,35}(?:学历|中专|大专|本科|硕士|博士)',t):return True
 if re.match(r'^有[^。;；]{0,120}(?:经验|经历)',t):return True
 return Q5(t)
rules.qualification=qualification

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if re.match(r'^(?:能|可)(?:接受|适应).{0,20}(?:出差|倒班|加班|工作压力|工作强度)',t):return 'N','APPLICANT_TRAVEL_OR_SCHEDULE_ACCEPTANCE'
 if re.match(r'^[^,，;；。]{0,18}(?:岗位|职位)要求[^,，;；。]{0,35}(?:学历|中专|大专|本科|硕士|博士)',t) and not re.match('负责|协助|制定|编制|设计',t):return 'N','EXPLICIT_POSITION_ELIGIBILITY_STATEMENT'
 if re.match(r'^有[^。;；]{0,120}(?:经验|经历)',t):return 'N','PERSONAL_EXPERIENCE_WITH_MULTIPLE_OBJECTS'
 if role in {'Q','Q_FIELD',None} and re.match(r'^能(?:建立|使用|全力配合)',t):return 'N','PERSONAL_CAPABILITY_WITHOUT_CURRENT_ASSIGNMENT'
 if role in {'Q','Q_FIELD'} and re.search(r'(?:领导|负责|参与|开发|管理)过(?!程|账|户|期|渡)',t[:70]) and not re.match('检查|核查|审核|统计|确认',t):return 'N','EXPLICIT_PAST_PROJECT_OR_LEADERSHIP_EXPERIENCE'
 if re.match(r'^(?:中国|亚洲|全球|世界|国内).{0,90}(?:企业|公司|供应商|品牌)(?:之一)?[。;；]?$',t) and re.search('规模|最强|领先|盈利|最大|知名',t):return 'N','EMPLOYER_SCALE_OR_MARKET_POSITION'
 if re.match(r'^(?:新入职人员福利|入职人员福利)',t):return 'N','NEW_EMPLOYEE_BENEFIT_DESCRIPTION'
 if re.match(r'^(?:怎么做\?|工作模式\?).*我们的客户',t) or re.match(r'^我们的客户.{0,25}(?:百分之|主动申请)',t):return 'N','RECRUITMENT_CUSTOMER_RESOURCE_EXPLANATION'
 if re.match(r'^是正编还是借聘',t):return 'N','RECRUITMENT_EMPLOYMENT_RELATIONSHIP_EXPLANATION'
 if t=='为提高沟通效率':return 'N','INCOMPLETE_RECRUITER_INTRODUCTION_PURPOSE'
 return D5(text,role,previous)
rules.decide=decide

# Only these exact source phrases alter the supplemental logic; final runner
# may use full evaluation if a conservative narrow screen is not provable.
def applicable_row(raw,row):return True

H5=rules.headings
ASSIGN_SUBJECT=re.compile(r'^(?:本岗位|该岗位|此岗位|本职位|该职位|员工|你|您)(?:主要|全面|具体|日常|需|需要)*负责')
FULL_SUBJECT=re.compile(r'(?:本岗位|该岗位|此岗位|本职位|该职位|员工)(?:主要|全面|具体|日常|需|需要)*负责')

def headings(s):
 out=H5(s);clean=[]
 for h in out:
  pre=s[:h['a']]
  # Strict end-of-string, not Python $ (which also matches before a newline).
  if h['name'] in GENERIC_CAPTIONS and pre and re.search('[\u3400-\u9fffA-Za-z]\\Z',pre):continue
  if OBJECT_VERB.search(pre) and not re.search(r'\n\s*$',pre):continue
  clean.append(h)
 # A short literal title immediately before 岗位要求 is not a duty statement.
 for h in list(clean):
  if h['name']=='岗位要求':
   prefix=s[:h['a']].strip()
   if 1<len(prefix)<35 and not re.search('[,，;；。\n]',prefix) and not re.match(rules.AW,prefix) and not rules.HEAD.search(prefix):clean.append(dict(a=0,b=h['a'],role='A',name='LITERAL_POSITION_TITLE_PREFIX'))
 return sorted(clean,key=lambda x:(x['a'],x['b']))
rules.headings=headings
# Repair the earlier generic-caption filter's newline handling in place by
# supplying an equivalent wrapper that restores explicit line-start captions.
H6=rules.headings

def headings(s):
 hs=H6(s)
 for m in rules.HEAD.finditer(s):
  if m[0] not in GENERIC_CAPTIONS:continue
  if not (m.start()==0 or re.search(r'\n\s*$',s[:m.start()])):continue
  if not re.match(r'\s*[:：]',s[m.end():]):continue
  if any(h['a']<=m.start()<h['b'] for h in hs):continue
  end=m.end()+re.match(r'\s*[:：]\s*',s[m.end():]).end();hs.append(dict(a=m.start(),b=end,role=rules.HROLE[m[0].lower()],name=m[0]))
 return sorted(hs,key=lambda x:(x['a'],x['b']))
rules.headings=headings
T6=rules.is_task;D6=rules.decide;S6=rules.split_mixed

def is_task(t):
 t=rules.cleantext(t)
 if ASSIGN_SUBJECT.match(t):return True
 if re.match(r'^对现有(?:设备|产品|系统|项目|工艺|流程|程序)',t) and re.search('优化|改进|改造|维护|调整|降成本',t) and not re.search('丰富经验|经验丰富|者优先',t):return True
 return T6(t)
rules.is_task=is_task

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if ASSIGN_SUBJECT.match(t) and not qualification(t) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_CURRENT_EMPLOYEE_OR_POSITION_ASSIGNMENT'
 if role=='R' and re.match(r'^能(?:够)?(?:为.{1,25}提供|(?:独立|及时|有效)*举办).{2,}',t) and not rules.HARDQUAL.search(t) and not rules.DAMAGE.search(t):return 'R','EXPLICIT_CURRENT_SERVICE_OR_EVENT_DUTY'
 if re.match(r'^(?:上班可带手机|工作轻松|更多普工招聘)',t):return 'N','RECRUITMENT_CONDITION_OR_ADVERTISEMENT'
 return D6(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 ints=S6(s,a,b,role);points={a,b}
 for lo,hi in ints:points.update((lo,hi))
 t=s[a:b]
 for m in re.finditer(r'负责(?!过|人|心)|协助',t):
  pos=a+m.start();pre=rules.cleantext(s[a:pos]);tail=rules.cleantext(s[pos:b])
  if pre and re.search(r'(?:专业|学历|经验|专业背景)$',pre) and qualification(pre) and not re.search(r'(?:经验|能力|知识|技能)[。;；]?$',tail):points.add(pos)
 for m in FULL_SUBJECT.finditer(t):
  points.add(a+m.start())
  end=re.search(r'上班可带手机|工作轻松|更多普工招聘',s[a+m.end():b])
  if end:points.add(a+m.end()+end.start())
 cs=rules._clauses(s,a,b)
 for i in range(1,len(cs)):
  lo,hi=cs[i];left=rules.cleantext(s[cs[i-1][0]:cs[i-1][1]]);right=rules.cleantext(s[lo:hi])
  if re.fullmatch(r'.{1,35}(?:工程师|技术员|专员|主管|经理)岗位',left) and rules.is_task(right):points.add(lo)
  if role=='R' and re.match(r'^(?:专业)?知识(?:过关|扎实|丰富)',left) and re.match(r'^能(?:够)?(?:为.{1,25}提供|(?:独立|及时|有效)*举办)',right):points.add(lo)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

BASE_PROCESS5=process

def process(raw,row):
 p=BASE_PROCESS5(raw,row)
 # A complete task's intact conditional clause stays attached after a damaged
 # neighbour; the condition is never kept by itself without a following task.
 from tools.r11_verify_release import replay
 s,_=replay(raw,p['normalization']);us=p['partition'];changed=False
 for i,u in enumerate(us[:-1]):
  text=s[u['a']:u['b']];nxt=us[i+1]
  if u['label']=='N' and u['reason']=='SOURCE_DEPENDENT_CONTEXT_NOT_STANDALONE' and text.rstrip().endswith((',', '，')) and re.match(r'^(?:对|对于|针对|在|当|为|根据|按照|如果|若|如遇)',rules.cleantext(text)) and not rules.DAMAGE.search(text) and nxt['label']=='R' and nxt.get('heading')==u.get('heading'):
   u.update(label='R',reason='INTACT_CONDITION_ATTACHED_TO_FOLLOWING_LITERAL_TASK');changed=True
 if changed:
  engine.rebuild(p,s);p['proposed_after']=p['after'];p['adopted']=True;p['text_changed']=p['after']!=p['before'];p['preserve_parent_reason']=None
 return p

# Preserve original heading line boundaries before the inherited soft-wrap
# cleaner runs. Only known heading captions followed by a colon are protected.
N6=rules.normalize

def normalize(raw):
 names=[k for k in rules.HROLE if (re.search('[A-Za-z]',k) and re.search('[\u3400-\u9fff]',k)) or k=='通用职责']
 pattern=re.compile(r'(?:\r\n|\n|\\r\\n|\\n)(?=\s*(?:'+'|'.join(sorted(map(re.escape,names),key=len,reverse=True))+r')\s*[:：])',re.I)
 es=[dict(a=m.start(),b=m.end(),old=m[0],new=m[0]+m[0],rule='PRESERVE_EXPLICIT_BILINGUAL_HEADING_LINE_BOUNDARY') for m in pattern.finditer(raw)]
 s,es=rules.apply(raw,es);prefix=[dict(name='heading_boundary_protection',edits=es)] if es else [];s,st=N6(s);return s,prefix+st
rules.normalize=normalize

T7=rules.is_task;D7=rules.decide;S7=rules.split_mixed
BUSINESS_INFO=re.compile(r'^(?:准确|及时|充分|全面|深入)?(?:了解|掌握|熟悉)(?:客户需求|客户商务运作周期|市场信息|客户动态)')

def is_task(t):
 t=rules.cleantext(t)
 if BUSINESS_INFO.match(t) and not re.search('能力|经验|知识|优先',t):return True
 if re.match(r'^控制.{0,25}(?:费用|成本|预算|风险|参数|质量)',t) and not re.search('能力|经验|知识|优先',t):return True
 return T7(t)
rules.is_task=is_task

def decide(text,role,previous=None):
 t=rules.cleantext(text)
 if BUSINESS_INFO.match(t) and role in {None,'R'} and not re.search('能力|经验|知识|优先',t):return 'R','EXPLICIT_CURRENT_BUSINESS_INFORMATION_ACQUISITION'
 return D7(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 ints=S7(s,a,b,role);points={a,b};t=s[a:b]
 for lo,hi in ints:points.update((lo,hi))
 # Complete first object remains usable when the coordinated second object
 # contains a literal mask; no missing object is reconstructed.
 for m in re.finditer(r'(?:和|及|与)(?=\*{2,}|\ufffd)',t):
  pos=a+m.start();left=rules.cleantext(s[a:pos])
  if rules._standalone(left) and not qualification(left):points.add(pos)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

# This explicit source text is a confirmed character-loss fragment. A generic
# question mark elsewhere is not automatically considered a missing word.
SOURCE_LOSS_LITERAL='结合公司自身资源寻找项?合作机会'
DIRECT_DUTY_LITERAL='电梯保养工作'
P7=process

def process(raw,row):
 p=P7(raw,row)
 from tools.r11_verify_release import replay
 s,_=replay(raw,p['normalization']);patches=[]
 for text,label,why in [(SOURCE_LOSS_LITERAL,'X','REVIEW_CONFIRMED_LITERAL_CHARACTER_LOSS_NOT_GUESSED')]:
  for m in re.finditer(re.escape(text),s):patches.append(dict(a=m.start(),b=m.end(),label=label,reason=why))
 # A no-experience condition ends before a literally named activity; the
 # following recruiting-area text is not part of that duty.
 for m in re.finditer(r'(?<=经验不限)电梯保养工作(?=现在招聘区域)',s):patches.append(dict(a=m.start(),b=m.end(),label='R',reason='EXPLICIT_NOMINAL_DUTY_AFTER_CLOSED_ELIGIBILITY_PHRASE'))
 if patches:
  points={0,len(s)}
  for u in p['partition']:points.update((u['a'],u['b']))
  for e in patches:points.update((e['a'],e['b']))
  new=[];j=0
  for a,b in zip(sorted(points),sorted(points)[1:]):
   while p['partition'][j]['b']<=a:j+=1
   u=dict(p['partition'][j],a=a,b=b)
   for e in patches:
    if e['a']<=a and b<=e['b']:u.update(label=e['label'],reason=e['reason'])
   new.append(u)
  p['partition']=new;engine.rebuild(p,s);p['proposed_after']=p['after'];p['adopted']=True;p['text_changed']=p['after']!=p['before'];p['preserve_parent_reason']=None;p['source_specific_literal_repairs']=patches
 return p
''',
'tools.r11_verify_release': r'''def replay(s,stages):
 count=0
 for stage in stages:
  out=[];last=0
  for e in stage['edits']:
   a,b=e['a'],e['b'];assert 0<=last<=a<b<=len(s) and s[a:b]==e['old'];out.extend([s[last:a],e['new']]);last=b;count+=1
  out.append(s[last:]);s=''.join(out)
 return s,count
''',
'tools.r12_policy': r'''"""R12: complete qualification scope, assigned work, and nominal work lists.

Additive policy in a new module. All retained text remains a source interval.
Frozen R11 modules and data are never edited. No record-ID-specific decisions.
"""
import re
from tools import r11_policy_v5 as parent
from tools.r11_verify_release import replay

rules=parent.rules
engine=parent.engine
BASE_DECIDE=rules.decide
BASE_QUAL=rules.qualification
BASE_TASK=rules.is_task
BASE_SPLIT=rules.split_mixed
BASE_HEADINGS=rules.headings
BASE_FINISH=rules.finish_body

ADV=r'(?:(?:并且|并|同时|主要|具体|日常|及时|准确|充分|深入|全面|有效|独立|快速|严格|认真|积极|持续|不断|进一步)(?:地)?)*'
DYNAMIC=re.compile(r'^'+ADV+r'(?:了解|掌握|理解|熟悉)(?:客户.{0,8}(?:需求|诉求|动态|状况|状态|进展|业务)|市场.{0,8}(?:动态|行情|变化|信息|需求)|行业.{0,8}(?:动态|态势|趋势)|(?:业务|项目|生产|设备|库存|销售).{0,8}(?:进展|进度|状态|状况|动态|情况))')
MODAL=re.compile(r'^(?:能(?:够)?|可|会)(?:(?:独立|高效|准确|及时|有效|熟练|完全|快速|安全|规范)(?:地|的|、|,)?)*(?:开展|进行|完成|处理|解决|控制|分析|判断|识别|制定|编制|编写|开发|设计|维护|安装|检修|沟通|协调|提供|支持|出具|承担|带领|组织|实施|操作|使用|维修|接待|回复|销售|举办).{2,}')
EXPERIENCE=re.compile(r'(?:经验|经历|年限|履历)(?:丰富|扎实|优先|者优先|为佳|尤佳)?[。;；,，\s]*$|(?:\d+|[一二两三四五六七八九十]+)\s*年(?:以上|及以上|左右)?(?:的)?(?:相关)?(?:经验|工作|经历)?[。;；,，\s]*$')
KNOW=re.compile(r'^(?:一定程度上|一定程度|基本|比较|较为|全面|深入|充分|并|同时)*(?:熟悉|熟知|通晓|精通|了解|掌握|理解|善于|擅长)')
PERSONAL=re.compile(r'^(?:对[^,，;；。]{1,45}(?:敏感|领悟深|有[^,，;；。]{0,25}(?:认识|认知|见解|想法|理解|意识))|逻辑性强|思维敏捷|学习(?:力|成绩|能力|和适应能力)|执行力|开发基础(?:良好|扎实)|负责的职业态度|(?:优秀|良好|较强)的.{0,40}(?:能力|精神|意识)|对[^,，;；。]{1,35}有(?:强烈|较强|良好)的意识)')
CREDENTIAL=re.compile(r'^(?:需|须|必须|要求)?(?:持有|持|具备|取得).{1,35}(?:资格证(?:书)?|操作证|上岗证|电工证|会计师证|驾驶证|消防操作证|职称)[。;；,，\s]*$')
OBJECT=re.compile(r'订单|工单|料单|排期|齐套|备损|试产|物料|存货|呆料|库存|交货|备料|供应商|客户|品质|质量|产品|项目|设备|模型|数据|系统|档案|文件|资料|合同|报表|报告|票据|费用|成本|风险|生产|技术|工艺|异常|需求|OB|OTD|效率|流程|人员|员工|车辆|仓库',re.I)
NOM_END=re.compile(r'(?:搭建|建设|建立|结清|清理|清点|上报|填报|预测|评审|改善|改进|推动|跟进|减少|降低|提升|提高|准确性|准确率|齐套率|及时性|模型|维护|保养|盘点|检查|管理|核算|分析|检测|调研|汇总|整理|审核|收集|记录|处理|跟踪|培训|编制|编写|规划|排程|安排|优化|支持|开发|设计|制作|交付|落实)(?:等|工作|等工作)?[。;；,，\s]*$')
HARD_PERSON=re.compile(r'学历|学位|者优先|优先考虑|优先录用|毕业|本科|硕士|研究生|大专|高中|中专|从业经验|工作经验|工作履历|相关经验|(?:具备|具有|拥有).{0,30}(?:经验|能力|知识)|有.{0,10}(?:年|经验)|适应.{0,8}(?:出差|倒班|加班)')
CURRENT=re.compile(r'^'+ADV+r'(?:负责(?!过)|协助|承担|主导|推动|推进|跟进|形成|建立|搭建|培养|提高|提升|增强|整合|识别|监控|监测|执行|开展|进行|制定|编制|编写|组织|指导|协调|处理|解决|维护|开发|设计|管理|支持|提供|实施|总结|学习|阅读|研究|关注)(?=.{2,})')
BENEFIT_ROLES={'B','OFFER','C','A'}

def strip_clause(t):
    t=rules.cleantext(t)
    return t[1:-1].strip() if t.startswith('(') and t.endswith(')') else t

def operational(t):
    if DYNAMIC.match(t) or parent.BUSINESS_INFO.match(t) or re.match(r'^'+ADV+r'(?:了解(?:和|并|及)?(?:发掘|收集)|掌握售点|(?:善于)?(?:捕捉|把握)(?:客户需求|市场.{0,10}(?:动态|信息)|行业.{0,12}趋势))',t):return True
    first=re.split('[,，;；。]',t,1)[0]
    if re.search('法规|法律|政策|标准|规范|原则|原理|规律|编程|软件|工具|流程|技巧|技术|专业知识',first):return False
    return bool(rules.operational_knowledge(t))

def nominal(t):
    t=strip_clause(t)
    t=re.sub(r'\([^()]*\)\s*$', '',t).rstrip()
    return bool(len(t)>3 and OBJECT.search(t) and NOM_END.search(t)
        and not re.search('学历|学位|经验|经历|能力|知识|熟悉|熟练|精通|掌握|优先|要求|职业发展|培养方向|公司提供|招聘|应聘|福利|补贴|奖金',t)
        and not re.match(r'^(?:能|可|会|至少|如|例如|研究生|本科|硕士|博士|\d+年)',t)
        and not rules.DAMAGE.search(t))

def current(t):
    t=strip_clause(t)
    if HARD_PERSON.search(t) or PERSONAL.match(t) or re.search('从基层做起|职业态度|培养方向|培养计划',t):return False
    if EXPERIENCE.search(t) and not (CURRENT.match(t) or re.match(r'^对现有',t)):return False
    return bool(CURRENT.match(t) or operational(t) or nominal(t))

def personal(t):
    t=strip_clause(t)
    if CREDENTIAL.match(t) or PERSONAL.match(t):return True
    if KNOW.match(t) and not operational(t):return True
    if re.match(r'^(?:对于|对|在).{0,160}(?:需要|要求)(?:有|具备|具有).{0,65}(?:知识|经验|能力)',t):return True
    if (t.startswith(('有','具备','具有','拥有','对','在','对于')) or re.search('岗位工作|职位工作',t)) and EXPERIENCE.search(t):
        if not re.match(ADV+r'(?:总结|归纳|分享|积累|沉淀|交流|传授|收集|记录|提炼|整合|组织)|^对现有',t):return True
    return False

def is_task(t):
    t=strip_clause(t)
    if personal(t):return False
    if operational(t):return True
    core=rules.ADVERB.sub('',t)
    if core!=t and BASE_TASK(core) and not HARD_PERSON.search(t):return True
    return BASE_TASK(t)
rules.is_task=is_task

def qualification(t):
    t=strip_clause(t)
    if personal(t):return True
    # Do not read 有效整合...能力 as 有...能力 (possession).
    core=rules.ADVERB.sub('',t)
    if operational(t) or core!=t and BASE_TASK(core) and not HARD_PERSON.search(t):return False
    return BASE_QUAL(t)
rules.qualification=qualification

def decide(text,role,previous=None):
    t=strip_clause(text)
    if not t:return 'S','R12_EMPTY_SEPARATOR'
    if role in {'NOTICE','COMPETENCY'}:return 'N','R12_EXPLICIT_NON_TASK_NOTICE_OR_COMPETENCY_BLOCK'
    if re.fullmatch(r'\*{2,}(?:大|高|低)?(?:限度|程度)地?',t):return 'X','R12_UNRECOVERABLE_MASKED_DEGREE_MODIFIER'
    if t in {'权责范围','权利','责任','一','二','三','四','五','全面负责','机修机电'}:return 'S','R12_ORPHAN_STRUCTURE_OR_RESPONSIBILITY_LEVEL'
    if re.match(r'^(?:我司|本司|本公司|公司|本企业|企业|集团)(?:目前|现|主要|长期|一直)?(?:为|是一家|从事|经营|主营|的.{0,18}(?:规模|业务|产品)(?:主要)?(?:有|为|是))',t):return 'N','R12_EMPLOYER_SUBJECT_PROFILE'
    if re.match(r'^(?:储备干部|管理培训生|管培生)?.{0,12}培养方向(?:为|是|:)',t):return 'N','R12_TRAINING_DIRECTION_NOT_ASSIGNED_TASK'
    if re.search(r'诚聘|工厂直聘|不收取任何介绍费',t[:60]) and not re.match(ADV+r'(?:负责|协助|组织|开展|管理)',t):return 'N','R12_RECRUITMENT_ADVERTISEMENT'
    if re.match(r'^岗位\*?【[^】]+】.{0,40}详情',t):return 'N','R12_RECRUITMENT_TITLE'
    if re.match(r'^(?:不穿无尘服|不看显微镜|中央空调车间|空调车间)',t):return 'N','R12_WORKPLACE_ENVIRONMENT'
    if re.match(r'^.{0,65}派遣制员工',t) or re.match(r'^(?:需|须|需要)与.{0,50}(?:签字|签订|签署)劳动合同',t):return 'N','R12_EMPLOYMENT_RELATIONSHIP'
    if role in BENEFIT_ROLES and not rules.POSITIVE_ASSIGN.match(t) and not parent.ASSIGN_SUBJECT.match(t) and not re.match(r'^'+ADV+r'(?:核算|审核|统计|编制|办理员工|办理职工|申报员工)',t):return 'N','R12_NON_DUTY_SECTION_SCOPE'
    if re.match(r'^(?:新员工|员工|职工).{0,25}(?:费用|补贴|补助).{0,12}(?:公司报销|公司承担|企业承担)',t):return 'N','R12_EMPLOYEE_BENEFIT'
    if re.match(r'^.{1,12}奖\s*[:：(].{0,30}(?:元|\d)',t) and not re.match(r'负责|制定|核算|审核|统计',t):return 'N','R12_BENEFIT_AWARD_AMOUNT'
    if personal(t):return 'N','R12_COMPLETE_PERSONAL_CONDITION'
    if role in {'Q','Q_FIELD'} and KNOW.match(t):return 'N','R12_KNOWLEDGE_IN_APPLICANT_SECTION'
    if role in {None,'Q','Q_FIELD'} and re.match(r'^至少.{0,100}全程参与.{0,30}完整.{0,15}项目',t):return 'N','R12_MINIMUM_COMPLETE_PROJECT_EXPERIENCE'
    if role in {'Q','Q_FIELD'} and HARD_PERSON.search(t) and not rules.POSITIVE_ASSIGN.match(t) and not parent.ASSIGN_SUBJECT.match(t):return 'N','R12_EXPLICIT_APPLICANT_ELIGIBILITY_SCOPE'
    if role in {'Q','Q_FIELD'} and (MODAL.match(t) or re.match(r'^(?:对|针对|根据|按照|在).{0,70}[,，].{0,5}(?:能|可)',t)):
        return 'N','R12_MODAL_APPLICANT_CAPABILITY'
    if role in {None,'R'} and operational(t) and not HARD_PERSON.search(t):return 'R','R12_CURRENT_INFORMATION_ACQUISITION'
    if role=='R' and MODAL.match(t) and not HARD_PERSON.search(t) and not rules.DAMAGE.search(t):return 'R','R12_ASSIGNED_MODAL_WORK'
    if current(t) and not rules.DAMAGE.search(t) and role in {None,'R'}:
        return 'R','R12_LITERAL_ACTION_OR_NOMINAL_DELIVERABLE'
    return BASE_DECIDE(text,role,previous)
rules.decide=decide

def clauses(s,a,b):
    out=[];start=a;depth=0
    for i in range(a,b):
        c=s[i]
        if c in '([【《':depth+=1
        elif c in ')]】》':depth=max(0,depth-1)
        if depth==0 and c in ',，':out.append((start,i+1));start=i+1
    if start<b:out.append((start,b))
    return out

def split_mixed(s,a,b,role):
    t=s[a:b];cs=clauses(s,a,b);points={a,b}
    for lo,hi in BASE_SPLIT(s,a,b,role):points.update((lo,hi))
    if role=='R' and cs and rules.HARDQUAL.search(s[cs[0][0]:cs[0][1]]) and qualification(s[cs[0][0]:cs[0][1]]) and not CURRENT.match(strip_clause(t)) and not rules.DAMAGE.search(t):
        # A mislabeled degree/tenure item still governs following skill clauses;
        # only explicit responsible-for assignments can escape that scope.
        safe=[lo for lo,hi in cs[1:] if re.match(ADV+r'(?:负责|协助|关注|处理|识别出|严格按照)',strip_clause(s[lo:hi])) and not qualification(s[lo:hi])]
        ps=sorted({a,b,*safe,*[x for x in points if safe and x>=min(safe)]});return list(zip(ps,ps[1:]))
    if cs and role in {'Q','Q_FIELD',None} and qualification(s[cs[0][0]:cs[0][1]]) and not rules.DAMAGE.search(t):
        verbs=r'(?:负责|协助|主导|承担)' if MODAL.match(strip_clause(s[cs[0][0]:cs[0][1]])) else r'(?:负责|协助|主导|承担|关注|识别出|严格按照|处理)'
        safe=[lo for lo,hi in cs[1:] if re.match(ADV+verbs,strip_clause(s[lo:hi])) and not qualification(s[lo:hi])]
        safe.extend(lo for lo in points-{a,b} if rules.POSITIVE_ASSIGN.match(strip_clause(s[lo:b])) and not qualification(s[lo:b]))
        ps=sorted({a,b,*safe,*[x for x in points if safe and x>=min(safe)]});return list(zip(ps,ps[1:]))
    # A complete reversed experience predicate governs the entire leading
    # object list. Explicit subsequent work clauses may still start a new item.
    if role in {None,'Q','Q_FIELD'} and EXPERIENCE.search(strip_clause(t)) and not CURRENT.match(strip_clause(t)) and not re.match(r'^对现有',strip_clause(t)):
        return [(a,b)]
    if role in {'Q','Q_FIELD'} and (PERSONAL.match(strip_clause(t)) or re.match(r'^(?:对|针对).{0,70}[,，]\s*(?:能|可)',strip_clause(t)) or re.match(r'^(?:对于|对|在).{0,160}(?:需要|要求)(?:有|具备|具有).{0,65}(?:知识|经验|能力)',strip_clause(t))):return [(a,b)]
    for i,(lo,hi) in enumerate(cs):
        c=strip_clause(s[lo:hi]);left=strip_clause(s[cs[i-1][0]:cs[i-1][1]]) if i else ''
        # Split genuine skills/environment fragments from neighboring tasks.
        if personal(c) or re.match(r'^(?:不穿无尘服|不看显微镜|中央空调车间|空调车间)',c):
            points.update((lo,hi))
        if i and personal(left) and (current(c) or role=='R' and MODAL.match(c)):
            points.add(lo)
        if role in {'Q','Q_FIELD'} and i and (qualification(left) or HARD_PERSON.search(s[a:lo])):
            if re.match(ADV+r'(?:负责|协助|主导|承担|识别出|严格按照|按照|组织|编制|审核|开展|进行)',c) and current(c):points.add(lo)
        # A work result and a prescribed learning goal belong to the action.
        if i and re.match(r'^(?:形成|提升|提高|增强).{1,65}能力',c) and current(left):points.discard(lo)
        if i and re.search(r'学习|阅读|培训|研习',left) and KNOW.match(c) and not HARD_PERSON.search(c):points.discard(lo)
        if i and role in {None,'R'} and operational(left) and re.match(r'^掌握(?:行业|业务|项目|客户).{0,15}案例',c):points.discard(lo)
        # A named task topic can precede a personal condition on the same line.
        inner=re.match(r'^.{1,22}:\s*',s[lo:hi])
        if inner:
            at=lo+inner.end()
            if personal(s[at:hi]):points.update((at,hi))
    # Parenthetical applicant credentials are local conditions, not task text.
    for m in re.finditer(r'\([^()]{1,55}\)',t):
        if CREDENTIAL.match(strip_clause(m[0])):points.update((a+m.start(),a+m.end()))
    mask=re.match(r'\s*\*{2,}(?:大|高|低)?(?:限度|程度)地?',t)
    if mask:points.add(a+mask.end())
    for m in re.finditer(r'(?<=[)）])\s+(?=(?:总经理|上级|领导|经理|主管).{0,8}(?:交待|交办|交代|安排))',t):points.add(a+m.end())
    # Do not preserve prefix fragments such as 在...至少 after splitting 具备.
    for lo in list(points-{a,b}):
        prefix=strip_clause(s[a:lo]);suffix=strip_clause(s[lo:b])
        if role in {None,'Q','Q_FIELD'} and prefix.startswith(('对','对于','在','针对')) and re.match(r'^(?:有|具有|具备|拥有)',suffix) and re.search('经验|经历|知识|能力',suffix):points.discard(lo)
        if rules.HARDQUAL.search(prefix) and qualification(prefix) and MODAL.match(suffix):points.discard(lo)
    return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

for name,role in {'岗位概述':'R','权责范围':'R','权利':'B','责任':'R','相关福利':'B','招聘要求描述':'Q','任职能力要求':'Q_FIELD','求职者隐私声明':'NOTICE','求职者隐私申明':'NOTICE','申请人隐私声明':'NOTICE','Job Applicant Privacy Policy':'NOTICE','全球胜任力':'COMPETENCY','Global Competencies':'COMPETENCY','技能这些必须有':'Q','这些可以有':'Q'}.items():rules.HROLE[name.lower()]=role
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)

def headings(s):
    out=[h for h in BASE_HEADINGS(s) if h['name'] not in {'责任','权利'} or ':' in s[h['a']:h['b']]]
    for m in rules.HEAD.finditer(s):
        name=m[0].lower();role=rules.HROLE[name]
        if any(h['a']<=m.start()<h['b'] for h in out):continue
        pre=s[max(0,m.start()-35):m.start()];post=s[m.end():]
        boundary=not s[:m.start()].strip() or bool(re.search(r'[\n,，;；。:]\s*$',pre))
        is_caption=(name in {'员工福利待遇','员工福利','福利待遇','薪资福利','薪资待遇'} and boundary and re.match(r'\s*[,，:：\n]',post))
        is_block=name in {'全球胜任力','global competencies'} and re.match(r'\s+',post) and not re.search(r'负责|制定|建立|设计|开发|评估|编制',pre)
        if is_caption or is_block:
            out.append(dict(a=m.start(),b=m.end(),role=role,name=m[0]))
    # Preserve ordinal scope but suppress isolated Chinese chapter numbers.
    for h in out:
        m=re.search(r'[一二三四五六七八九十]+:\s*$',s[:h['a']])
        if m:h['a']=m.start()
    return sorted(out,key=lambda x:(x['a'],x['b']))
rules.headings=headings

def finish_body(body):
    s,st=BASE_FINISH(body)
    # Balance only orphan quote syntax; no task words or technical numbers.
    es=[]
    for op,cl in [('“','”'),('‘','’')]:
        stack=[]
        for i,c in enumerate(s):
            if c==op:stack.append(i)
            elif c==cl:
                if stack:stack.pop()
                else:es.append(dict(a=i,b=i+1,old=c,new='',rule='R12_ORPHAN_QUOTE'))
        es.extend(dict(a=i,b=i+1,old=s[i],new='',rule='R12_ORPHAN_QUOTE') for i in stack)
    s,es=rules.apply(s,es)
    if es:st.append(dict(name='r12_orphan_quotes',edits=es))
    return s,st
rules.finish_body=finish_body

def process(raw,row):
    p=parent.process(raw,row);s,_=replay(raw,p['normalization'])
    # Inheritance may protect only weak evidence. Explicit new exclusions
    # override old literal retention, including old exact development cases.
    changed=False
    for u in p['partition']:
        if u['label']=='S':continue
        lab,why=decide(s[u['a']:u['b']],u.get('section'))
        if why.startswith('R12_') and (lab in {'N','S','X'} or lab=='R' and u['label']!='X'):
            if u['label']!=lab:changed=True
            u.update(label=lab,reason=why)
    if changed:
        engine.rebuild(p,s)
        p['proposed_after']=p['after'];p['adopted']=True;p['text_changed']=p['after']!=p['before'];p['preserve_parent_reason']=None
    elif any(p['before'].count(op)!=p['before'].count(cl) for op,cl in [('“','”'),('‘','’')]) and p['proposed_after']!=p['after']:
        p['after']=p['proposed_after'];p['adopted']=True;p['text_changed']=p['after']!=p['before'];p['preserve_parent_reason']=None
    p['policy_version']='R12_COMPLETE_CLAUSE_TASK_AND_NOMINAL_REPAIR'
    return p
''',
'tools.r12_policy_v2': r'''"""Second R12 policy: source-list context and predicate scope, frozen V1 intact."""
import re
from tools import r12_policy as v1
from tools.r11_verify_release import replay
rules=v1.rules;engine=v1.engine
BASE_NORMAL=rules.normalize;BASE_HEADS=rules.headings;BASE_PARTS=rules._partitions10
BASE_DECIDE=rules.decide;BASE_SPLIT=rules.split_mixed;BASE_TASK=rules.is_task
BASE_OP=v1.operational
COMPOUND=re.compile(r'^(?:及时|深入|全面|充分|快速|准确)*(?:熟悉|了解|掌握|理解)(?:并且|并|及|和|、)(?:严格|及时|深入|全面|认真)*(?:执行|梳理|分析|收集|反馈|挖掘|发掘|跟踪|研究|判断|制定|优化|实施)')
CURRENT_ADV=re.compile(r'^(?:(?:积极|主动|认真|努力|持续|不断|定期|及时|准确|快速|高效|独立|全面|充分|深入|严格|合理|有效)(?:地)?)+')
WORK_START=re.compile(r'^(?:负责(?!的?职业态度|心|人|[、,，])|协助|承担|主导|推动|推进|跟进|形成|建立|搭建|培养|提高|提升|增强|整合|识别|监控|监测|执行|开展|进行|制定|编制|编写|组织|指导|协调|处理|解决|维护|开发|设计|管理|支持|提供|实施|总结|学习|阅读|研究|关注|参加|参与|完成|丰富产品线|据.{0,40}进行)(?=.{2,})')
CAPABILITY_NOUN=re.compile(r'^(?:开发|运维|设计|编程|沟通|组织|协调|学习|分析|执行|逻辑|亲和|抗压|适应|创新|判断|写作|专业|业务)(?:能力|力)(?:[、,，。;；]|方面|良好|强|优秀|$)')
GENERIC_COMPLIANCE=re.compile(r'^(?:服从|听从).{0,25}(?:管理|指挥|安排|调配)[。;；,，]*$')
KNOWLEDGE_TOPIC=re.compile(r'^(?:常见|相关|基本|基础|各种|各类|主要|专业).{0,35}(?:原理|基础概念|技术知识|理论知识)(?:和|及|、|[,，]|$)')
MODAL_CONDITION=re.compile(r'^(?:能(?:够)?|可以?|会)(?:结合|根据|通过|围绕|按照|依据|针对|对).{2,}')
LEARNING_ACT=re.compile(r'(?:努力|积极|不断|持续)?学习(?!能力|成绩|意识|意愿|力)|(?:参加|参与|开展|进行).{0,25}(?:培训|学习)|提高自身业务水平|进行.{0,5}(?:了解|研究|调查|调研|学习|分析)|直播前')
NOMINAL_EVENT=re.compile(r'^(?:公司|部门|项目|团队)(?:的)?(?:团建|培训|会议|活动).{0,25}(?:策划|组织|执行|安排|管理|协调|落实|开展)')
ASSIGN=re.compile(r'^(?:(?:主要|具体|全面|日常|及时|独立|严格)\s*)*(?:负责(?!的?职业态度|心|人|[、,，])|协助|承担|主导)')
BARE=re.compile(r'(?<![A-Za-z0-9.])([1-9]\d?)(?=[\u3400-\u9fff])')
QUANTITY=re.compile(r'^(?:年|月|天|时|分钟|岁|个|人|名|位|届|元|万|千|百|亿|米|吨|兆|号|级|倍|层|种|次|条|家|日|以内|以上|以下|及以上|年限)')
BLOCK_ROLES={'A','B','C','OFFER','NOTICE','COMPETENCY','Q_FIELD'}

def txt(s):return v1.strip_clause(s)
def actual(t):
    t=txt(t)
    if CAPABILITY_NOUN.match(t) or v1.PERSONAL.match(t) or re.match(r'^研究生|^认真负责[、,，]',t):return False
    core=CURRENT_ADV.sub('',t)
    return bool(COMPOUND.match(t) or NOMINAL_EVENT.match(t) or WORK_START.match(core) or ASSIGN.match(t) or BASE_TASK(t))

def coherent_bare(s):
    ms=[m for m in BARE.finditer(s) if not QUANTITY.match(s[m.end():])]
    if not ms:return []
    anchors=list(re.finditer(r'(?<![A-Za-z0-9.])([1-9]\d?)[.、)]\s*(?=[^\d\s])',s))
    seq=sorted(ms+anchors,key=lambda m:m.start())
    if len(seq)<3:return []
    supported=set()
    for i,m in enumerate(seq):
        near=[j for j in range(max(0,i-2),min(len(seq),i+3)) if j!=i and int(seq[j][1])-int(m[1])==j-i]
        if near:supported.add(m.start())
    return [m for m in ms if m.start() in supported] if len(supported)>=3 else []

def normalize(raw):
    s,st=BASE_NORMAL(raw);es=[]
    for m in coherent_bare(s):es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='R12V2_COHERENT_BARE_ORDINAL'))
    marks=list(re.finditer(r'\d{1,2}[.、)]\s*(\?)(?=[\u3400-\u9fff])',s))
    if len(marks)>=2:
        for m in marks:es.append(dict(a=m.start(1),b=m.end(1),old='?',new='',rule='R12V2_REPEATED_ENTRY_INITIAL_QUESTION_LAYOUT'))
    for m in re.finditer(r'(?<=[\u3400-\u9fff])\.(?=\d{1,2}\.)',s):es.append(dict(a=m.start(),b=m.end(),old='.',new='.\n',rule='R12V2_SENTENCE_BEFORE_LIST_NUMBER'))
    for m in re.finditer(r'(?<=[A-Za-z])Responsibilities\s*:',s):
        es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n'+m[0],rule='R12V2_CONCATENATED_EXPLICIT_ENGLISH_CAPTION'))
    s,es=rules.apply(s,es)
    if es:st.append(dict(name='r12v2_proven_list_and_caption_boundaries',edits=es))
    return s,st
rules.normalize=normalize

for name,role in {
    '工作情况':'R','录用条件':'Q','招募要求':'Q','岗位福利':'B','品牌优势':'B',
    '硬福利':'B','软福利':'B','培训福利':'B','岗位':'A','Objectives of the Position':'R',
    'Technical Professional Knowledge':'Q_FIELD'
}.items():rules.HROLE[name.lower()]=role
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)

def headings(s):
    hs=[]
    for h in BASE_HEADS(s):
        a,b=h['a'],h['b'];name=h['name'];post=s[b:b+30]
        # Benefit/qualification labels inside an assigned work object are not
        # section boundaries. An actual caption colon/list still establishes one.
        line=max(s.rfind('\n',0,a),s.rfind(';',0,a),s.rfind('。',0,a),s.rfind(',',0,a))+1
        pre=s[line:a]
        if h['role'] in {'A','B','C','OFFER','Q','Q_FIELD'} and re.search(r'负责|核算|审核|编制|制定|统计|办理|管理|统筹|完善|计算|跟进',pre) and not ':' in s[a:b]:
            if pre and re.search(r'[\u3400-\u9fffA-Za-z]$',pre) and not re.match(r'\s*[1-9][.、)]',post):continue
        if name=='岗位' and (':' not in s[a:b] or a and re.search(r'[\u3400-\u9fffA-Za-z]',s[a-1])):continue
        hs.append(h)
    for m in re.finditer(r'加入[^。;；\n:]{1,30}(?:您|你)?将享有(?:以下)?福利\s*:',s):
        hs=[h for h in hs if not (m.start()<=h['a']<m.end())]
        hs.append(dict(a=m.start(),b=m.end(),role='B',name='EXPLICIT_EMPLOYMENT_BENEFIT_INTRODUCTION'))
    return sorted(hs,key=lambda h:(h['a'],h['b']))
rules.headings=headings

def operational(t):
    return bool(COMPOUND.match(txt(t)) or BASE_OP(t))
v1.operational=operational

def is_task(t):
    t=txt(t)
    if CAPABILITY_NOUN.match(t) or re.match(r'^热衷|^研究生|^认真负责[、,，]',t):return False
    if COMPOUND.match(t) or NOMINAL_EVENT.match(t):return True
    core=CURRENT_ADV.sub('',t)
    if core!=t and WORK_START.match(core) and not re.match(r'^负责[、,，]|^负责的?职业态度',core):return True
    if re.match(r'^据.{0,65}(?:进行|开展|制定|执行)',t):return True
    return BASE_TASK(t)
rules.is_task=is_task

def contextual_partitions(s):
    parts=BASE_PARTS(s);out=[];heading_key=None;inferred=None;clear_count=0;benefit_count=0;had_work=False;qual_cont=False
    for base in parts:
        u=dict(base);role=u.get('section');key=(role,u.get('heading'))
        if key!=heading_key:
            heading_key=key;inferred=None;clear_count=benefit_count=0;had_work=False;qual_cont=False
        if u.get('label')=='S':
            if u.get('reason') in {'EXPLICIT_LIST_MARKER','COHERENT_INLINE_CHINESE_ORDINAL','COHERENT_BARE_ORDINAL','COHERENT_SPACED_ORDINAL','DECORATIVE_LIST_MARKER'}:qual_cont=False
            out.append(u);continue
        t=txt(s[u['a']:u['b']]);lab,why=BASE_DECIDE(t,role)
        clear=lab=='R' and actual(t) and not v1.personal(t) and not CAPABILITY_NOUN.match(t)
        if role in {None,'A'} and inferred=='R' and v1.MODAL.match(t) and not v1.HARD_PERSON.search(t):clear=True
        condition=(v1.qualification(t) or CAPABILITY_NOUN.match(t) or KNOWLEDGE_TOPIC.match(t)) and not clear
        benefit=lab=='N' and any(k in why for k in ['BENEFIT','PAY_INFORMATION','EMPLOYMENT_OFFER','COMPENSATION']) and not ASSIGN.match(t)
        if role=='R' and not had_work and benefit:
            benefit_count+=1
            if benefit_count>=2:inferred='B'
        if role in {None,'A'}:
            if clear:
                inferred='R';had_work=True;clear_count+=1
            elif condition:inferred='Q'
            if inferred:
                u['original_section']=role;u['section']=inferred;u['context_basis']='LITERAL_ASSIGNMENTS_AND_QUALIFICATIONS_IN_SAME_SOURCE_BLOCK'
        elif role=='Q' and u.get('heading')=='岗位要求':
            if clear:
                clear_count+=1
                if clear_count>=2:inferred='R'
            elif condition:inferred='Q';clear_count=0
            if inferred=='R':u['original_section']=role;u['section']='R';u['context_basis']='CONSECUTIVE_EXPLICIT_TASKS_UNDER_WEAK_REQUIREMENTS_CAPTION'
        elif role=='R' and inferred=='B' and not ASSIGN.match(t):
            u['original_section']=role;u['section']='B';u['context_basis']='CONSECUTIVE_EMPLOYER_BENEFITS_BEFORE_ANY_ASSIGNED_WORK'
        if role=='R' and clear:had_work=True
        # Semicolon-separated knowledge examples stay attached to the original
        # skill item; a new numbered item or actual action resets this scope.
        if qual_cont and not clear and u['section'] not in {'B','C','A','OFFER','NOTICE','COMPETENCY'}:
            u['original_section']=role;u['section']='Q_FIELD';u['context_basis']='CONTINUATION_OF_EXPLICIT_KNOWLEDGE_ITEM'
        if condition and (v1.KNOW.match(t) or KNOWLEDGE_TOPIC.match(t)):qual_cont=True
        elif clear:qual_cont=False
        out.append(u)
    return out
rules._partitions10=contextual_partitions

def decide(text,role,previous=None):
    t=txt(text)
    if not t:return 'S','R12V2_EMPTY'
    if re.fullmatch(r'(?:各|不同|多个|相关)(?:学科|专业|岗位|职位)(?:分别|均|单独)?招聘[。;；]*',t):return 'N','R12V2_RECRUITMENT_DISTRIBUTION_NOTICE'
    if re.match(r'^上市公司直聘|^.{1,30}公司直聘[!！。;；]*$',t):return 'N','R12V2_EMPLOYER_DIRECT_RECRUITMENT'
    if re.match(r'^这里有一份.{0,35}(?:工作|职位)',t):return 'N','R12V2_EMPLOYER_RECRUITMENT_PITCH'
    if CAPABILITY_NOUN.match(t) or KNOWLEDGE_TOPIC.match(t) or re.match(r'^热衷',t):return 'N','R12V2_PERSONAL_CAPABILITY_KNOWLEDGE_OR_INTEREST'
    if re.match(r'^[^,，;；。]{1,25}(?:技巧|能力|技能)(?:娴熟|熟练|扎实|优秀|较强|强)[。;；,，]*$',t) and not re.match(r'^(?:提高|提升|增强|训练|培训|培养|指导|考核|评估)',t):return 'N','R12V2_REVERSED_PERSONAL_PROFICIENCY'
    if re.match(r'^(?:担任|从事|任职).{1,60}(?:岗位|工作|职位)\s*\d+(?:\.\d+)?年(?:以上|及以上)',t):return 'N','R12V2_PRIOR_EMPLOYMENT_DURATION'
    if role in {'Q','Q_FIELD',None} and GENERIC_COMPLIANCE.fullmatch(t):return 'N','R12V2_APPLICANT_COMPLIANCE_CONDITION'
    if re.match(r'^实现个人.{0,70}职业(?:转型|发展)',t):return 'N','R12V2_PERSONAL_CAREER_PROMOTION'
    if re.search(r'\bexperience\b.*\bis a plus\b',t,re.I):return 'N','R12V2_ENGLISH_EXPERIENCE_PREFERENCE'
    if re.search(r'(?:工作的|文件的|报告的)编[。;；]*$',t):return 'X','R12V2_TRUNCATED_DOCUMENT_PREDICATE'
    if re.fullmatch(r'\*{2,}(?:大|高|低)?(?:限度|程度)地?',t):return 'X','R12V2_UNRECOVERABLE_DEGREE_MODIFIER'
    if role in {'R',None} and not v1.HARD_PERSON.search(t) and not rules.DAMAGE.search(t):
        if COMPOUND.match(t) or NOMINAL_EVENT.match(t):return 'R','R12V2_COMPOUND_ACTION_OR_ADMINISTRATIVE_WORK'
        core=CURRENT_ADV.sub('',t)
        if core!=t and WORK_START.match(core) and not v1.personal(t) and not re.match(r'^负责[、,，]|^负责的?职业态度',core):return 'R','R12V2_ACTION_AFTER_MANNER_ADVERBS'
        if re.match(r'^丰富(?:公司|业务)?(?:产品线|产品矩阵|产品类型|产品种类|品类|内容)',t):return 'R','R12V2_TRANSITIVE_PRODUCT_OR_CONTENT_EXPANSION'
        if re.match(r'^据.{0,65}(?:进行|开展|制定|执行)',t):return 'R','R12V2_LITERAL_TASK_BASIS_AND_ACTION'
        if MODAL_CONDITION.match(t) and re.search(r'完成|分析|处理|提供|解决|制定|设计|开发|编制|开展',t):return 'R','R12V2_ASSIGNED_ACTION_WITH_ITS_BASIS'
        if re.match(r'^(?:直播|工作|作业|销售)前对.{0,90}进行.{0,5}了解',t):return 'R','R12V2_EXPLICIT_WORK_PREPARATION_AND_INFORMATION_ACQUISITION'
    return BASE_DECIDE(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
    t=s[a:b];points={a,b}
    for lo,hi in BASE_SPLIT(s,a,b,role):points.update((lo,hi))
    cs=v1.clauses(s,a,b)
    if role in {'R',None}:
        for i,(lo,hi) in enumerate(cs):
            c=txt(s[lo:hi])
            if i and role=='R' and MODAL_CONDITION.match(c) and re.search(r'完成|分析|处理|提供|解决|制定|设计|开发|编制|开展',c):points.add(lo)
            if i and role=='R' and (GENERIC_COMPLIANCE.fullmatch(txt(s[cs[i-1][0]:cs[i-1][1]])) or v1.qualification(s[cs[i-1][0]:cs[i-1][1]])) and re.match(r'^(?:按照|根据).{0,50}(?:完成|执行|开展|进行)',c):points.add(lo)
        for lo in list(points-{a,b}):
            prefix=txt(s[a:lo]);tail=txt(s[lo:b])
            if LEARNING_ACT.search(prefix) and v1.KNOW.match(tail) and not v1.HARD_PERSON.search(prefix+tail):points.discard(lo)
            if re.search('系统|平台|设备|产品',prefix) and re.match(r'^(?:设计|开发|建立|搭建|负责.{0,15}(?:设计|开发))',prefix) and re.match(r'^能(?:够)?(?:支持|满足|实现|处理|承载)',tail):points.discard(lo)
            if MODAL_CONDITION.match(prefix) and actual(tail) and not v1.HARD_PERSON.search(prefix):points.discard(lo)
        for i,(lo,hi) in enumerate(cs):
            if i and txt(s[lo:hi]).startswith('实现个人') and '职业' in s[lo:hi]:points.add(lo)
        # Preserve explicit post-production work examples after a proficiency
        # modifier in a current task; these are operations, not tool names.
        if re.match(r'^(?:负责|参与|完成).{0,35}(?:拍摄|制作|剪辑)',txt(t)) and re.search(r'包括.{0,80}(?:剪辑|调色|字幕|特效)',t):
            for lo in list(points-{a,b}):
                if re.match(r'^(?:熟练运用镜头语言|包括剪辑|字幕处理|特效合成)',txt(s[lo:b])):points.discard(lo)
    if role=='Q':
        for i,(lo,hi) in enumerate(cs):
            if i and re.match(r'^(?:按照要求完成.{0,20}(?:交办|安排)|进行风险识别|独立完成)',txt(s[lo:hi])):points.add(lo)
    for m in re.finditer(r'\*{2,}(?:大|高|低)?(?:限度|程度)地?',t):points.update((a+m.start(),a+m.end()))
    return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

TRIGGER=re.compile(r'工作情况|录用条件|招募要求|岗位福利|品牌优势|Objectives of the Position|[A-Za-z]Responsibilities\s*:|分别招聘|加入[^。;；\n]{0,30}将享有|熟悉[、和并及]|了解[、和并及]|掌握[、和并及]|能够结合|能对.{0,45}(?:分析|提供|解决)|能够支持|能(?:够)?独立完成(?:公司|部门|日常)|(?:学习|培训|提高自身业务水平)[^。;；]{0,90}掌握|(?:积极|主动|认真|努力)+地?(?:完成|参加)|丰富(?:公司|业务)?产品|公司团建活动|据市场信息|岗位\s*[:：]|实现个人.{0,70}职业|(?:负责|核算|审核|编制|制定|统计|办理|管理|统筹)[^。;；\n]{0,70}(?:薪资福利|薪酬福利|工资|薪资|福利待遇)|按照要求完成.{0,20}(?:交办|安排)|进行风险识别|(?:^|[。;；\n])工作地点|(?:服从|听从)[^。;；]{0,50}(?:按照|根据|完成)|熟练运用镜头语言',re.I)
BODY_TRIGGER=re.compile(r'原理和主要应用|开发能力|运维方面|热衷|无不良从业|连续任职满|工作的编|\*{2,}限度地|experience.{0,80}is a plus|服从公司和部门管理|担任.{0,50}岗位\d+年',re.I)
def applicable(raw,body):
    return bool(TRIGGER.search(raw) or '培训福利' in raw or BODY_TRIGGER.search(body) or coherent_bare(raw)
        or re.search(r'(?<=[\u3400-\u9fff])\.\d{1,2}\.',raw)
        or len(re.findall(r'\d{1,2}[.、)]\s*\?(?=[\u3400-\u9fff])',raw))>=2
        or ('工作地点' in raw[:180] and re.search(r'维护.{0,40}财务',raw))
        or (re.search(r'针对优秀员工.{0,25}培训',body) and re.search('底薪|工资|薪资|待遇',raw)))

def process(raw,row):
    p=v1.process(raw,row);s,_=replay(raw,p['normalization']);changed=False
    previous_work=None
    for u in p['partition']:
        if u['label']=='S':
            if u['reason']=='EXPLICIT_SECTION_HEADING':previous_work=None
            continue
        lab,why=decide(s[u['a']:u['b']],u.get('section'))
        if why.startswith('R12V2_') and (lab in {'N','S','X'} or lab=='R' and u['label']!='X'):
            if u['label']!=lab:changed=True
            u.update(label=lab,reason=why)
        t=rules.cleantext(s[u['a']:u['b']])
        if u['label']=='N' and t.startswith('(') and t.rstrip('。;；').endswith(')') and previous_work and previous_work.get('heading')==u.get('heading') and not v1.qualification(t) and not rules.DAMAGE.search(t):
            u.update(label='R',reason='R12V2_PARENTHESES_DETAIL_OF_PRECEDING_TASK');changed=True
        previous_work=u if u['label']=='R' else None
    if changed:
        engine.rebuild(p,s);p['proposed_after']=p['after'];p['adopted']=True;p['text_changed']=p['after']!=p['before'];p['preserve_parent_reason']=None
    p['policy_version']='R12_V2_SOURCE_ITEM_CONTEXT_AND_COMPOUND_PREDICATES'
    return p
''',
'tools.r12_policy_v3': r'''"""Unified full-corpus policy: no keyword eligibility gate, literal-source only."""
import re,functools
from tools import r12_policy_v2 as v2
from tools.r11_verify_release import replay
v1=v2.v1;rules=v2.rules;engine=v2.engine
BASE_HEADS=rules.headings;RAW_PARTS=v2.BASE_PARTS
BASE_DECIDE=rules.decide;BASE_TASK=rules.is_task;BASE_SPLIT=rules.split_mixed
OLD_OPERATIONAL=v1.operational;BASE_NORMAL=rules.normalize
NON_DUTY={'A','B','C','OFFER','NOTICE','COMPETENCY'}
DEGREE_START=re.compile(r'^(?:全日制|统招|大学)?(?:本科|专科|大专|中专|硕士|博士|研究生|高中)|^(?:年龄|学历|学位|性别|身高|工作年限)')
TRAIT=re.compile(r'^(?:对)?(?:工作|本职工作|做事|为人|工作态度)?(?:负责认真|认真负责|认真|细致负责|细致|细心|严谨|踏实|诚实|正直|勤奋|阳光|乐观|开朗|有责任心|责任心|有上进心|积极主动|主动积极|热爱|热衷|认同|认可|敢想敢干)(?=[、,，;；。]|负责|细心|踏实|严谨|吃苦|工作|公司|企业|销售|本职|游戏|$)')
REVERSED_STATE=re.compile(r'^(?:对|对于)[^。;；]{1,90}(?:熟悉|精通|娴熟|了解深入|认识深刻|理解深入|高度认同|非常认同|有[^,，;；]{0,15}(?:兴趣|逻辑概念|表现力))(?=[、,，;；。]|者|优先|$)')
STATE_LEAD=re.compile(r'^(?:具备|具有|拥有|有着|有良好|有较强|有丰富)')
GENERIC_REQUIREMENT=re.compile(r'^(?:服从|听从|遵守|遵循)(?:公司|部门|工作|国家|法律|法令|各项|相关|上级|领导|的|和|与|及|安排|管理|指挥|制度|规定|规章|法规|要求|纪律|劳动|生产|安全|职业|道德|[、,，]){1,45}[。;；]*$')
EMPLOYER=re.compile(r'^(?!负责|协助|参与|审核|管理|维护|联系|对接|代表|帮助|支持|为|与|向|对|根据|按照)(?:[^。;；:]{1,85}(?:有限责任公司|股份有限公司|有限公司|集团|公司)(?:\([^)]{0,60}\))?\s*[,，]?\s*(?:成立|是|主要从事|主营|位于|专注|致力|总部|拥有)|(?:我司|本司|本公司)(?:为|是|主要)|[^。;；]{1,50}(?:工厂|新厂|公司|企业|中心)[,，]?\s*(?:大量招聘|诚聘|招聘普工))')
RECRUIT_NOTICE=re.compile(r'^(?!负责|协助|组织|策划|实施|开展|安排|发布|编写|制作|管理|参与).{0,50}(?:欢迎(?:您|你|大家|各位)(?:的)?加入|期待(?:您|你)(?:的)?加入|简历的小伙伴.{0,18}面试机会|投递简历|求职者请|报名咨询)')
ENVIRONMENT=re.compile(r'^(?:简单易懂|无需任何技术|无需技术|无需学历|工作简单|生熟手均可|不重|有活就干|没活休息|中途休息|休息时间长|车间内设|舒适优越工作环境|有人带教|可培训)[。;；!！,，]*')
LOCATION=re.compile(r'^(?:长期驻场|驻场地点|办公地址|办公地点|工作地点|上班地点|工作地址|负责区域|工作区域|服务区域|驻点地点)\s*[:：]?\s*[^。;；]*$')
PAYROLL_OP=re.compile(r'^(?:员工|职工|公司员工|公司|企业|人事)?(?:的)?(?:社保|社会保险|公积金|薪资|薪酬|工资|奖金|津贴|补贴|费用|报销)[^。;；]{0,55}(?:核算|计算|审核|登记|申报|办理|审批|增减员|停缴|续缴|补缴|转移|对账)')
MACHINE=re.compile(r'^(?:开|开启|操作|操纵|启动|运行|驾驶|驾驭)(?:CNC|数控|冲压|冲床|机床|车床|磨床|铣床|设备|机器|叉车|行车|吊车|货车|挖掘机|压铸|注塑|缝纫|自动机)',re.I)
BUSINESS_OBJECT=re.compile(r'客户|顾客|用户|市场|行业|项目|产品|商品|收费|校区|设备|设施|生产|工艺|订单|业务|运行|政策|技术|专业沟通|机床|车辆|材料|数据|需求|投诉|反馈|信息')
STATIC_KNOWLEDGE=re.compile(r'规则|规律|法规|法律|政策|原理|理论|软件|工具|协议|编程|语言|基础知识|技术知识|规范|标准|方法')
SOFTWARE_KNOWLEDGE=re.compile(r'数据库|框架|组件|类库|开发环境|软件|工具|脚本|语言|springcloud|mysql|oracle|springboot',re.I)
DYNAMIC_CONTEXT=re.compile(r'变化|变动|动态|进展|进度|状况|现状|现有|目前|及时|实时|随时|最新|痛点|诉求|配置|重点部位|隐蔽工程|发展要求|收费项目')
MODAL_PREFIX=re.compile(r'^(?:能(?:够)?|可以?|会)(?:独立|自主|高效|准确|及时|有效|熟练|完全|快速|安全|规范|主动|较好|很好的|很好|高质量|地|的|、|,)*')
MODAL_ACTION=re.compile(r'^(?:负责|协助|开展|进行|完成|处理|解决|控制|分析|判断|识别|制定|编制|编写|开发|设计|维护|安装|检修|沟通|协调|提供|支持|出具|承担|带领|组织|实施|操作|使用|维修|接待|回复|销售|举办|挖掘|抓住|运用|为.{1,45}(?:提供|解决)|(?:对|与|和|结合|根据|按照|通过|针对).{1,65}(?:负责|协助|完成|分析|解决|沟通|协调|提供|开发|设计|处理|制作|吸引))')
MODAL_ACTION=re.compile(MODAL_ACTION.pattern.replace('|运用|','|运用|还原|').replace('|制作|吸引','|制作|还原|吸引'))
OFFER_CLAUSE=re.compile(r'^(?!负责|协助|制定|规划|拓展|培养|促进|推动|管理)(?:公司|企业|工厂|新厂|本厂|平台|岗位)?.{0,8}(?:晋升空间|发展空间|晋升机会|发展机会).{0,15}$')
PLAIN_JOB_TITLE=re.compile(r'^(?:(?:电子|手工)?装配工|普工|操作员|物料员|质检员|检验员|测试员|搬运工|焊工|铆工|叉车工|保洁员)[。;；]*$')
WEAK_DUTY_HEADINGS={'职位描述','岗位描述','职位说明','岗位详情','职位详情'}
PURE_BENEFIT=re.compile(r'^(?:享有|享受|提供(?:住宿|食宿|工作餐|餐补|午餐|免费)|员工旅游|生日礼物|节日物资|到公司面试者报销|(?:[一二三四五六七八九十]+[:：])?完善的福利保障)')
BENEFIT_ADMIN=re.compile(r'负责|协助|核算|审核|审批|采购|策划|组织|制定|统计|登记|办理|管理')
COMMON_FIELD_WORDS={'学历','专业','经验','要求','技能','职责','内容','待遇','福利','岗位','职位'}
v2.QUANTITY=re.compile(v2.QUANTITY.pattern.replace('年|月|','款|项|台|套|份|门|张|批|辆|组|类|年|月|'))

for name,role in {
 '工作目标':'R','岗位目标':'R','主要工作目标':'R','职位详情':'R','岗位详情':'R',
 '岗位内容':'R','职责范围':'R','工作范围':'R','岗位基本需求':'Q',
 '基本技能和素质':'Q_FIELD','RequiredSkills&Knowledge':'Q_FIELD',
 '核心能力':'COMPETENCY','完善的福利保障':'B','相关待遇':'B',
 '学历背景及工作经验':'Q_FIELD','Education&Experience':'Q_FIELD',
 '办公地址':'A','办公地点':'A','驻场地点':'A','负责区域':'A','工作区域':'A'
}.items():rules.HROLE[name.lower()]=role
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)
GENERIC_FIELDS=re.compile(r'(?P<q>(?:岗位|职位|任职|招聘|应聘|录用|招募)(?:基本|任职|资格|专业|技能|人员|素质)?(?:需求|要求|条件|资格))|(?P<r>(?:主要|核心|日常)?(?:工作|岗位|职位)(?:主要|基本|核心)?(?:目标|内容|任务|职责|范围|详情))|(?P<a>(?:办公|工作|上班|联系|驻场|驻点|面试)(?:地址|地点|区域))')

def headings(s):
 out=[]
 for h in BASE_HEADS(s):
  a,b=h['a'],h['b'];pre=s[:a];post=s[b:]
  inside=bool(a and re.search(r'[\u3400-\u9fffA-Za-z]$',pre))
  caption=(h['role'] in {'COMPETENCY','NOTICE'} or ':' in s[a:b] or s[a:a+1] in '-—[【(' or re.match(r'\s*[1-9]\d?[.、)]',post) or re.match(r'[ \t]*\n',post))
  if h['name'] in {'福利待遇','薪酬福利','薪资福利','员工福利'} and re.match(r'[ \t]*(?:技能培训|五险|六险|年底|年终|带薪|双休|绩效|岗位晋升|免费|节日)',post):caption=True
  if inside and h['name'] in COMMON_FIELD_WORDS and ':' not in s[a:b]:continue
  if inside and not caption:continue
  out.append(h)
 for m in GENERIC_FIELDS.finditer(s):
  a,b=m.span()
  if any(h['a']<=a<h['b'] for h in out):continue
  if a and not (s[a-1].isspace() or s[a-1] in '[【:：;；。,，)'):continue
  tail=re.match(r'[ \t]*(?:[:：][ \t]*|\r?\n)',s[b:])
  if not tail:continue
  role='Q' if m['q'] else 'R' if m['r'] else 'A'
  out.append(dict(a=a,b=b+tail.end(),role=role,name=m[0]))
 for m in re.finditer(r'(?m)^[ \t]*(核心能力)[ \t]*(?:\r?\n|[:：])',s):
  if not any(h['a']<=m.start(1)<h['b'] for h in out):out.append(dict(a=m.start(1),b=m.end(),role='COMPETENCY',name='核心能力'))
 return sorted(out,key=lambda h:(h['a'],h['b']))
rules.headings=headings

def normalize(raw):
 s,st=BASE_NORMAL(raw);es=[]
 # Exclamation marks delimit advertising sentences, except in programming code.
 if not rules.CODE.search(s):
  for m in re.finditer(r'[!！]+(?=\s*[\u3400-\u9fff(])',s):
   es.append(dict(a=m.start(),b=m.end(),old=m[0],new='。\n',rule='R12V3_AD_SENTENCE_BOUNDARY'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='r12v3_sentence_layout',edits=es))
 return s,st
rules.normalize=normalize

def personal(t):
 t=v1.strip_clause(t)
 if TRAIT.match(t) or REVERSED_STATE.match(t):return True
 if STATE_LEAD.match(t) and not re.search(r'(?:系统|平台|产品|设备).{0,15}(?:开发|设计|建设|测试|改进)$',t):return True
 return False

def operational(t):
 t=v1.strip_clause(t)
 if re.search(r'(?:经验|经历|能力|者优先)[。;；,，]*$',t):return False
 if re.match(r'^(?:及时|定期|持续|深入|全面|充分|实时|随时)?(?:获悉|获知)',t) and BUSINESS_OBJECT.search(t):return True
 if re.match(r'^(?:及时|定期|持续|深入|全面|充分|实时|随时)?(?:了解|掌握|熟悉|理解)',t):
  first=re.split('[,，;；。]',t,1)[0]
  if BUSINESS_OBJECT.search(first) and (DYNAMIC_CONTEXT.search(first) or not (STATIC_KNOWLEDGE.search(first) or SOFTWARE_KNOWLEDGE.search(first))):
   return True
 return OLD_OPERATIONAL(t)
v1.operational=operational

def modal(t):
 t=re.sub(r'^(?:并且|并|同时)\s*','',v1.strip_clause(t));m=MODAL_PREFIX.match(t)
 return bool(m and MODAL_ACTION.match(t[m.end():]) and not v1.HARD_PERSON.search(t))

def is_task(t):
 t=v1.strip_clause(t)
 if personal(t):return False
 if MACHINE.match(t) or operational(t) or PAYROLL_OP.match(t):return True
 core=v2.CURRENT_ADV.sub('',t)
 if core!=t and BUSINESS_OBJECT.search(core) and not re.match(r'^(?:认可|认同|喜欢|热爱|向上|有责任|具备|具有|拥有|承担压力|吃苦)',core):return True
 return BASE_TASK(t)
rules.is_task=is_task

def decide(text,role,previous=None):
 t=v1.strip_clause(text)
 if not t:return 'S','R12V3_EMPTY'
 if EMPLOYER.match(t):return 'N','R12V3_NAMED_EMPLOYER_DESCRIPTION'
 if RECRUIT_NOTICE.match(t):return 'N','R12V3_RECRUITMENT_INVITATION_OR_APPLICATION_NOTICE'
 if re.match(r'^(?:接受|接收|可接受)(?:学徒工|学徒|应届生|应届毕业生)',t):return 'N','R12V3_APPLICANT_CATEGORY'
 if PURE_BENEFIT.match(t) and not BENEFIT_ADMIN.search(t):return 'N','R12V3_EXPLICIT_BENEFIT_OR_RECRUITMENT_PAYMENT'
 if OFFER_CLAUSE.match(t):return 'N','R12V3_EMPLOYER_DEVELOPMENT_OFFER'
 if PLAIN_JOB_TITLE.fullmatch(t):return 'N','R12V3_STANDALONE_WORKER_TITLE'
 if ENVIRONMENT.match(t) and not re.search(r'负责|核算|审核|办理|制定|安排',t[:12]):return 'N','R12V3_EMPLOYMENT_EASE_OR_ENVIRONMENT'
 if LOCATION.fullmatch(t) and not re.search(r'区域内|市场|客户|开拓|开发|销售|维护|管理|巡查|安装|检查|测试|实施|支持',t):return 'N','R12V3_STANDALONE_LOCATION_OR_DEPLOYMENT'
 if personal(t):return 'N','R12V3_EXPLICIT_PERSONAL_STATE_OR_TRAIT'
 if re.fullmatch(r'.{1,35}(?:业务岗|业务岗位|技术岗|技术岗位)[。;；]*',t) and not v2.ASSIGN.match(t):return 'N','R12V3_POSITION_TITLE'
 if re.match(r'^(?:需|需要)(?:在|到)?客户现场.{0,20}(?:共同)?(?:开发|调试|安装|实施)',t):return 'R','R12V3_EXPLICIT_CUSTOMER_SITE_ASSIGNMENT'
 if role is None and v1.KNOW.match(t) and not DYNAMIC_CONTEXT.search(t):return 'N','R12V3_UNHEADED_STATIC_KNOWLEDGE_CONDITION'
 if role in {'Q','Q_FIELD'}:
  if re.match(r'^(?:或|或者|且|以及|并|同时)\s*(?:从事过|参与过|负责过(?!程|账|户|期)|曾经|有过)',t):return 'N','R12V3_COORDINATED_PAST_EXPERIENCE'
  if MODAL_PREFIX.match(t) or GENERIC_REQUIREMENT.fullmatch(t) or v1.KNOW.match(t):return 'N','R12V3_APPLICANT_MODAL_KNOWLEDGE_OR_COMPLIANCE'
  if re.match(r'^(?:员工全国跟随项目出差|员工入职后|培训完成后|对于交通不便者)',t) or re.search(r'(?:周|入职|园区).{0,30}(?:培训|住宿)',t):return 'N','R12V3_ENTRY_TRAINING_OR_DEPLOYMENT_CONDITION'
 if role=='Q' and v1.nominal(t) and not v1.parent.v4.FIELD_ONLY.fullmatch(t):return 'R','R12V3_CONCRETE_NOMINAL_WORK_IN_MIXED_LIST'
 if re.match(r'^熟练(?:使用|运用|掌握)',t) and SOFTWARE_KNOWLEDGE.search(t) and not re.search(r'(?:完成|编写|编制|开发|设计|制作|处理).{2,}',t[4:]):return 'N','R12V3_SOFTWARE_PROFICIENCY_WITHOUT_TASK'
 if role in {'R',None}:
  if MACHINE.match(t) and not v1.HARD_PERSON.search(t):return 'R','R12V3_EXPLICIT_MACHINE_OPERATION'
  if operational(t) and not v1.HARD_PERSON.search(t):return 'R','R12V3_CURRENT_BUSINESS_INFORMATION_ACQUISITION'
  if PAYROLL_OP.match(t) and not re.search(r'\d+\s*(?:元|号|月)|公司为|我们为',t):return 'R','R12V3_EXPLICIT_HR_PAYROLL_ADMINISTRATION'
  if role=='R' and (modal(t) or re.match(r'^能(?:够)?保持良好沟通',t)) and not rules.DAMAGE.search(t):return 'R','R12V3_CURRENT_MODAL_ACTION'
  core=v2.CURRENT_ADV.sub('',t)
  if core!=t and BUSINESS_OBJECT.search(core) and is_task(t) and not rules.DAMAGE.search(t) and not v1.HARD_PERSON.search(t):return 'R','R12V3_BUSINESS_ACTION_WITH_MANNER_ADVERB'
 return BASE_DECIDE(text,role,previous)
rules.decide=decide

def partitions(s):
 out=[];key=None;inferred=None;company=False;tasks=benefits=0;had_work=False;qcontinuation=False
 for base in RAW_PARTS(s):
  u=dict(base);original=u.get('section');newkey=(original,u.get('heading'))
  if newkey!=key:
   key=newkey;inferred=None;tasks=benefits=0;had_work=False;qcontinuation=False;company=original=='C'
  if u.get('label')=='S':
   if u['reason']=='EXPLICIT_SECTION_HEADING':company=original=='C'
   if 'LIST_MARKER' in u['reason'] or 'ORDINAL' in u['reason']:qcontinuation=False
   out.append(u);continue
  t=v1.strip_clause(s[u['a']:u['b']])
  if EMPLOYER.match(t):company=True
  if company and not v1.parent.ASSIGN_SUBJECT.match(t):
   u.update(original_section=original,section='C',context_basis='COMPLETE_EMPLOYER_PREFACE_UNTIL_NEW_SECTION');out.append(u);continue
  weak=original=='R' and u.get('heading') in WEAK_DUTY_HEADINGS
  first=v1.strip_clause(re.split('[,，;；。]',t,1)[0])
  if weak and not had_work and (v1.KNOW.match(first) or DEGREE_START.match(first) or personal(first)):inferred='Q'
  effective=inferred if (original in {None,'A'} or weak) and inferred else original
  lab,why=decide(t,effective)
  firstlab,firstwhy=decide(first,effective)
  weak_reasons={'LITERAL_CONTENT_OF_EXPLICIT_DUTY_SECTION','DEPENDENT_TASK_CONTINUATION','PRIOR_LITERAL_DUTY_PRESERVED_WITHOUT_POSITIVE_REMOVAL_EVIDENCE'}
  clear=lab=='R' and why not in weak_reasons and not personal(t)
  firstclear=firstlab=='R' and firstwhy not in weak_reasons and not personal(first)
  if firstclear:clear=True
  if effective=='R' and modal(first):clear=True
  q=(DEGREE_START.match(first) or personal(first) or v1.qualification(first)) and not clear
  offer=lab=='N' and any(w in why for w in ['BENEFIT','PAY_INFORMATION','EMPLOYMENT_OFFER','COMPENSATION','EMPLOYEE_BENEFIT']) and not v2.ASSIGN.match(t)
  if original=='R' and not had_work and offer:
   benefits+=1
   if benefits>=2:inferred='B'
  if original in {None,'A'} or weak:
   if clear:inferred='R';had_work=True;tasks+=1
   elif q and not (weak and (had_work or MODAL_PREFIX.match(first) and inferred is None)):inferred='Q'
   if inferred:u.update(original_section=original,section=inferred,context_basis='FULL_SOURCE_TASK_AND_QUALIFICATION_SEQUENCE')
  elif original=='Q' and u.get('heading') in {'岗位要求','岗位需求'}:
   if clear:tasks+=1
   elif q:tasks=0;inferred='Q'
   if tasks>=2:inferred='R'
   if inferred=='R':u.update(original_section=original,section='R',context_basis='CONSECUTIVE_EXPLICIT_ASSIGNMENTS')
  elif original=='R' and inferred=='B' and not v2.ASSIGN.match(t):
   u.update(original_section=original,section='B',context_basis='EXPLICIT_BENEFIT_SEQUENCE_WITHOUT_ASSIGNED_WORK')
  if original=='R' and clear:had_work=True
  if qcontinuation and not clear and not MODAL_PREFIX.match(t) and u['section'] not in NON_DUTY:
   u.update(original_section=original,section='Q_FIELD',context_basis='KNOWLEDGE_ITEM_CONTINUATION')
  if q and (v1.KNOW.match(t) or v2.KNOWLEDGE_TOPIC.match(t)):qcontinuation=True
  elif clear:qcontinuation=False
  out.append(u)
 return out
rules._partitions10=partitions

def split_mixed(s,a,b,role):
 points={a,b}
 for lo,hi in BASE_SPLIT(s,a,b,role):points.update((lo,hi))
 cs=v1.clauses(s,a,b)
 for i,(lo,hi) in enumerate(cs):
  t=v1.strip_clause(s[lo:hi]);left=v1.strip_clause(s[a:lo])
  if ENVIRONMENT.match(t) or LOCATION.fullmatch(t) or RECRUIT_NOTICE.match(t) or OFFER_CLAUSE.match(t) or PLAIN_JOB_TITLE.fullmatch(t):points.update((lo,hi))
  if role=='R' and i:
   if personal(t) or DEGREE_START.match(t):points.add(lo)
   if modal(left) and (personal(t) or v1.HARD_PERSON.search(t)):points.add(lo)
   if v1.qualification(left) and (modal(t) or operational(t)):points.add(lo)
   if PAYROLL_OP.match(t) and re.search('员工|人事|入职|离职|劳动合同|考勤',left):points.add(lo)
  if role in {'Q','Q_FIELD'} and MODAL_PREFIX.match(v1.strip_clause(s[a:b])):
   # The ability modal governs coordinated predicates throughout this item.
   return [(a,b)]
 first=v1.strip_clause(s[cs[0][0]:cs[0][1]]) if cs else ''
 hard_governor=bool(rules.HARDQUAL.search(first) and v1.qualification(first) and not v2.ASSIGN.match(first))
 if role=='R' and not hard_governor:
  for m in re.finditer(r'并(?:且)?能(?:够)?',s[a:b]):
   pos=a+m.start()
   if modal(s[pos:b]) and v1.qualification(s[a:pos]):points.add(pos)
 if hard_governor and not (role=='R' and modal(first)):
  for pos in list(points-{a,b}):
   if modal(s[pos:b]):points.discard(pos)
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

def _process(raw,row):
 p=v2.process(raw,row);s,_=replay(raw,p['normalization']);changed=False
 for u in p['partition']:
  if u['label']=='S':continue
  lab,why=decide(s[u['a']:u['b']],u.get('section'))
  if why.startswith('R12V3_') and (lab in {'N','S','X'} or lab=='R' and u['label']!='X'):
   if u['label']!=lab:changed=True
   u.update(label=lab,reason=why)
 if changed:
  engine.rebuild(p,s);p['proposed_after']=p['after'];p['adopted']=True;p['text_changed']=p['after']!=p['before'];p['preserve_parent_reason']=None
 p['policy_version']='R12_V3_UNIFIED_FULL_SOURCE_RULES'
 return p

@functools.lru_cache(maxsize=4096)
def _cached(raw,before):
 return _process(raw,dict(record_id='LITERAL_SOURCE_CACHE',responsibility_text=before))

def process(raw,row):
 # No metadata, record identity, employer or year enters the classification.
 p=dict(_cached(raw,row['responsibility_text']));p['record_id']=row['record_id'];return p
''',
'tools.r12_policy_v4': r'''"""Fourth candidate: explicit section boundaries and clause-level duty scope.

Source-only decisions; historical body is comparison evidence, never a label.
No identifier, company, occupation or year is used for classification.
"""
import re, functools
from tools import r12_policy_v3 as v3
from tools.r11_verify_release import replay
v2=v3.v2;v1=v3.v1;rules=v3.rules;engine=v3.engine
BASE_HEAD=rules.headings;BASE_NORMAL=rules.normalize;BASE_DECIDE=rules.decide
BASE_SPLIT=rules.split_mixed;BASE_TASK=rules.is_task;BASE_OP=v1.operational
for name,role in {'理想中的你':'Q','我们期待的你':'Q','我们希望你':'Q','你需要具备':'Q','应具备条件':'Q','企业福利':'B','报酬福利':'B','其他福利':'B','培训体系':'B','平台优势':'B','位职责':'R'}.items():rules.HROLE[name.lower()]=role
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)
STRONG_CAPTIONS=re.compile(r'(?P<bracket>[【\[](?P<name>[^】\]\n]{2,25})[】\]])|(?P<plain>岗位职责|岗位要求|工作内容|任职要求|任职资格|职位要求|职责描述|福利待遇|薪资福利|薪酬福利|员工福利)(?P<end>\s*[:：]|(?=[1-9][.、)]))')
BENEFIT_HEAD=re.compile(r'(?:福利待遇|员工福利|薪酬福利)(?=\s*(?:技能培训|五险|六险|带薪|年终|年底|绩效|免费|节日|双休))')

def headings(s):
 hs=BASE_HEAD(s);extra=[]
 for m in STRONG_CAPTIONS.finditer(s):
  name=m['name'] or m['plain'];role=rules.HROLE.get(name.lower())
  if not role:continue
  # Brackets/colon are explicit field syntax, even after a task predicate.
  a,b=m.span();tail=re.match(r'\s*[:：]?\s*',s[b:]);b+=tail.end()
  extra.append(dict(a=a,b=b,role=role,name=name))
 for m in BENEFIT_HEAD.finditer(s):extra.append(dict(a=m.start(),b=m.end(),role='B',name=m[0]))
 for e in extra:
  covering=[h for h in hs if h['role']==e['role'] and h['a']<=e['a'] and e['a']<h['b']<=e['b']]
  if covering:e['a']=min(e['a'],*(h['a'] for h in covering))
  hs=[h for h in hs if not (h['a']<e['b'] and e['a']<h['b'])];hs.append(e)
 return sorted(hs,key=lambda h:(h['a'],h['b']))
rules.headings=headings

def normalize(raw):
 s,st=BASE_NORMAL(raw);ms=list(re.finditer(r'(?<![\d.])([1-9]\d?)\.02(?=[\u3400-\u9fff])',s))
 # Repeated ordinal+02 artifacts only; decimals and single occurrences stay.
 if len(ms)>=3 and any(int(y[1])==int(x[1])+1 for x,y in zip(ms,ms[1:])):
  es=[dict(a=m.start(),b=m.end(),old=m[0],new=m[1]+'、',rule='R12V4_REPEATED_ORDINAL_ENCODING_ARTIFACT') for m in ms]
  s,es=rules.apply(s,es);st.append(dict(name='r12v4_proven_ordinal_layout',edits=es))
 return s,st
rules.normalize=normalize

TRAIT=re.compile(r'^(?:(?:沟通|表达|沟通表达|沟通协调|语言表达|逻辑思维|学习|执行|抗压)(?:能力)?(?:良好|优秀|较好|出色|强)|关注细节(?=[。;；,，]|$))')
Q_RESEARCH=re.compile(r'^(?:对|对于).{1,55}有(?:一定|较深|深入|较多|深刻)?(?:的)?(?:研究|认识|理解|了解|认知)(?=[,，;；。]|$)')
CREDENTIAL=re.compile(r'^(?:通过|取得|持有|具备|具有|拥有).{0,45}(?:从业考试|从业资格|执业资格|资格考试|资格证书)(?=[,，;；。]|$)')
APPLICATION=re.compile(r'^(?:需|须|需要|要求|请|必须)(?:提供|提交|携带|附上)(?:个人|本人|相关|设计|原创|代表)?(?:作品|简历|证件|证书|照片|材料)(?=[,，;；。]|集|$)')
RECRUIT=re.compile(r'^(?!负责|协助|管理|组织|制定|实施|开展|发布|编写|维护|更新|优化|统筹).{0,65}(?:欢迎投递|同步招聘|现正招聘|现招聘|现招|诚招|诚聘|针对.{0,15}招聘.{0,25}\d+名)')
EMPLOYMENT=re.compile(r'^(?:可以?|能(?:够)?|愿意)?(?:接受|适应|服从)(?:公司|集团|单位|部门|上级|领导|的|安排|调配|管理|短期|长期|异地|全国|外派|出差|倒班|加班|[()、,，\u3400-\u9fff]){0,60}$')
HR_WORK=re.compile(r'^(?:(?:应聘|求职|候选)(?:人员|者|人)(?:的)?(?:预约|接待|初面|面试|筛选)|招聘[、,，].{0,35}(?:培训|管理|考核)|(?:每周|每月|每日|定期|月度|周度).{0,45}(?:核对考勤|处理考勤|考勤异常|工资异常)|(?:对|根据|依据).{0,45}(?:员工|人员|人才).{0,15}招聘.{0,40}(?:协调|共享|计划|管理))')
NOMINAL_INFO=re.compile(r'^.{2,85}(?:信息|通知|文件|决议|政策)(?:的)?(?:上传下达|传达|传递)[。;；,，]*$')
DRAWING=re.compile(r'^(?:绘制.{2,90}(?:图|图纸)|.{2,40}图纸绘制)[。;；,，]*$')
MANAGEMENT=re.compile(r'^(?:领导|带领|组织|指导)(?:下属|团队|员工|人员).{1,80}(?:建设|提升|提高|培养|完成|执行|落实|做好)')
ADDITIONAL_WORK=re.compile(r'^(?:(?:依据|根据).{0,30}招聘计划.{0,55}发布.{0,15}招聘信息|(?:人员|人才|员工)招聘[,，].{0,40}招聘人才|.{2,40}(?:辅材|物料|材料|设备)验收[。;；,，]*$|.{2,70}(?:车辆|运力|车队).{0,50}(?:询价|询价工作)[。;；,，]*$|(?:及时|定期)?补足.{1,25}库存|满足.{1,25}(?:客户|销售|市场|业务)需求|服务好客户|介绍[、,，]销售.{2,}|(?:通过|使用).{0,25}电话\d+\*{1,6}系统呼出|供应商考评[:：].{1,140}对供应商进行考评)')
v3.MODAL_ACTION=re.compile(v3.MODAL_ACTION.pattern.replace('|开展|','|部署|驱动|改善|提升|开展|').replace('|制作|还原|吸引','|制作|还原|驱动|改善|提升|进行|吸引'))

def operational(t):
 t=v1.strip_clause(t)
 if re.match(r'^(?:及时|定期|深入|全面|充分)?(?:掌握|了解|熟悉|理解)',t) and re.search(r'竞争对手|竞品|供应商|经销商|价格策略|经营策略|经销手段',t) and not re.search('经验|能力|者优先|方法|知识',t):return True
 if re.match(r'^(?:及时|深入|全面|充分)?(?:了解|掌握|理解)',t) and re.search(r'(?:行业|市场|业务).{0,10}(?:现状|动态|变化|行情)',t) and not re.search('能力|经验|优先',t):return True
 return BASE_OP(t)
v1.operational=operational;v3.operational=operational

def is_task(t):
 t=v1.strip_clause(t)
 if TRAIT.match(t) or CREDENTIAL.match(t) or APPLICATION.match(t):return False
 if HR_WORK.match(t) or NOMINAL_INFO.match(t) or DRAWING.match(t) or MANAGEMENT.match(t) or ADDITIONAL_WORK.match(t):return True
 return BASE_TASK(t)
rules.is_task=is_task

def decide(text,role,previous=None):
 t=v1.strip_clause(text).lstrip('、').strip()
 if TRAIT.match(t):return 'N','R12V4_PERSONAL_COMMUNICATION_OR_ATTITUDE'
 if re.match(r'^(?:曾经|曾|过去)?(?:负责过|承担过|担任过|参与过|从事过)',t):return 'N','R12V4_PAST_WORK_EXPERIENCE'
 if role is None and v1.KNOW.match(t) and not v3.DYNAMIC_CONTEXT.search(t):return 'N','R12V4_UNHEADED_STATIC_KNOWLEDGE'
 if re.fullmatch(r'(?:承担|承受|接受)(?:工作|一定|较大|各种)?压力[。;；,，]*',t):return 'N','R12V4_PERSONAL_PRESSURE_TOLERANCE'
 if v1.KNOW.match(t) and re.search(r'经验[^。;；]{0,12}优先[。;；,，]*$',t):return 'N','R12V4_KNOWLEDGE_WITH_EXPERIENCE_GOVERNOR'
 if CREDENTIAL.match(t):return 'N','R12V4_APPLICANT_CREDENTIAL'
 if APPLICATION.match(t):return 'N','R12V4_APPLICATION_SUBMISSION'
 if RECRUIT.match(t) and not HR_WORK.match(t):return 'N','R12V4_RECRUITMENT_NOTICE'
 if re.match(r'^岗前(?:有|提供|带薪|免费)',t):return 'N','R12V4_PRE_EMPLOYMENT_TRAINING'
 if role in {None,'R'} and ADDITIONAL_WORK.match(t) and not re.search(r'经验|能力|优先|具备|熟悉|要求',t):return 'R','R12V4_COMPLETE_ADMINISTRATIVE_COMMERCIAL_OR_NOMINAL_WORK'
 if role in {'Q','Q_FIELD'}:
  if re.match(r'^(?:提供|提交|携带)(?:个人|本人|相关)?(?:简历|证件|照片|作品)(?=[,，;；。]|集|$)',t):return 'N','R12V4_APPLICANT_SUBMISSION_LIST'
  if re.match(r'^(?:遵守|服从|听从).{0,45}(?:制度|安排|纪律|管理|规定|文化)[。;；,，]*$',t):return 'N','R12V4_GENERIC_APPLICANT_COMPLIANCE'
  if Q_RESEARCH.match(t) or re.search(r'专业(?:者)?优先|专业不限|不受专业限制',t) and not v2.ASSIGN.match(t):return 'N','R12V4_EDUCATION_OR_KNOWLEDGE_BACKGROUND'
  if re.match(r'^(?:可以?|能(?:够)?|愿意)?(?:接受|适应|服从|听从)',t) and re.search(r'出差|外派|调配|安排|倒班|加班|企业文化',t):return 'N','R12V4_EMPLOYMENT_ACCEPTANCE'
 if role in {None,'R'} and not rules.DAMAGE.search(t):
  if HR_WORK.match(t):return 'R','R12V4_RECRUITMENT_AND_PAYROLL_ADMINISTRATION'
  if NOMINAL_INFO.match(t):return 'R','R12V4_NOMINAL_INFORMATION_DISTRIBUTION'
  if DRAWING.match(t):return 'R','R12V4_COMPLETE_DRAWING_TASK'
  if MANAGEMENT.match(t):return 'R','R12V4_MANAGING_OTHERS_AND_IMPROVING_CAPACITY'
  if re.match(r'^(?:固定|指定|负责)?区域.{0,15}(?:收派件|收件|派件|揽件|配送)',t):return 'R','R12V4_NOMINAL_DELIVERY_WORK'
  if operational(t) and not v1.HARD_PERSON.search(t):return 'R','R12V4_OPERATIONAL_INFORMATION'
 if re.match(r'^(?:\d+[、.])?\d*\s*(?:Six\s*Sigma|Sigma|6\s*Sigma|六西格玛).{0,30}(?:知识|能力|优先)',t,re.I):return 'N','R12V4_EXPLICIT_SKILL_CREDENTIAL'
 return BASE_DECIDE(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 cs=v1.clauses(s,a,b);points={a,b}
 for lo,hi in BASE_SPLIT(s,a,b,role):points.update((lo,hi))
 full=v1.strip_clause(s[a:b]);first=v1.strip_clause(s[cs[0][0]:cs[0][1]]) if cs else ''
 # Experience/ability governs its skill object list; actual assignments escape.
 if v1.KNOW.match(first) and (v1.EXPERIENCE.search(full) or re.search(r'经验[^。;；]{0,12}优先[。;；,，]*$',full)):
  return [(a,b)]
 if re.match(r'^(?:良好|优秀|较强|流利).{0,25}(?:英语|英文|外语|语言).{0,15}能力',first):return [(a,b)]
 if role in {'Q','Q_FIELD'}:
  for i,(lo,hi) in enumerate(cs):
   t=v1.strip_clause(s[lo:hi]).lstrip('、')
   if i and re.match(r'^(?:负责(?!人|过)|协助|主导|承担(?!过)|实现)',t) and not re.search(r'能力|经验|经历|者优先',t) and not (t.startswith('实现') and (v3.MODAL_PREFIX.match(first) or not v1.KNOW.match(first.lstrip('、')))):points.add(lo)
  if re.match(r'^(?:可以?|能(?:够)?|愿意)?(?:接受|适应)',first):
   for lo,hi in cs:points.update((lo,hi))
 # Current information may have a comma-separated object list before 现状.
 if role=='R' and v1.KNOW.match(first) and operational(full):
  for lo in list(points-{a,b}):
   suffix=v1.strip_clause(s[lo:b])
   if not re.match(r'^(?:并|同时|负责|协助|对|根据|针对|完成|制定|编写|确保|能|可|有|具备|具有|拥有)',suffix) and not v1.qualification(suffix):points.discard(lo)
 for m in re.finditer(r'岗前(?:有|提供)?(?:带薪|免费)?培训',s[a:b]):points.add(a+m.start())
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

@functools.lru_cache(maxsize=8192)
def _cached(raw):
 # The empty comparison prevents historical output from acting as evidence.
 # Historical exact-source reviews remain source-keyed, not record-keyed.
 p=v3._process(raw,dict(record_id='CACHE',responsibility_text=''));s,_=replay(raw,p['normalization'])
 changed=False
 for u in p['partition']:
  if u['label']=='S':continue
  lab,why=decide(s[u['a']:u['b']],u.get('section'))
  if why.startswith('R12V4_') and (lab in {'N','S','X'} or lab=='R' and u['label']!='X'):
   changed |= lab!=u['label'];u.update(label=lab,reason=why)
 # Preserve a complete work target attached to the following retained action.
 us=p['partition']
 for i,u in enumerate(us):
  t=v1.strip_clause(s[u['a']:u['b']])
  if u['label']=='N' and u['reason']=='SOURCE_DEPENDENT_CONTEXT_NOT_STANDALONE' and u.get('section')=='R' and re.match(r'^针对.{2,55}(?:客户|产品|项目|设备|系统)[,，;；。]*$',t):
   nxt=next((v for v in us[i+1:] if v['label']!='S'),None)
   if nxt and nxt['label']=='R' and nxt.get('heading')==u.get('heading') and not rules.DAMAGE.search(t):u.update(label='R',reason='R12V4_WORK_TARGET_OF_ADJACENT_ACTION');changed=True
 engine.rebuild(p,s);p['proposed_after']=p['after'];p['adopted']=True;p['preserve_parent_reason']=None
 p['policy_version']='R12_V4_SOURCE_ONLY_COMPLETE_CLAUSE'
 return p

def process(raw,row):
 p=dict(_cached(raw));before=row['responsibility_text']
 p.update(record_id=row['record_id'],before=before,before_sha256=engine.digest(before.encode()),text_changed=p['after']!=before,parent_role='COMPARISON_ONLY_NOT_CLASSIFICATION')
 return p
''',
'tools.r12_policy_v5': r'''"""Final scoped repairs after the V4 full-source baseline.

Every record is screened. A selected original is fully re-extracted; the
selection reasons and unchanged baseline are retained in the final receipt.
"""
import re,html,functools,json,hashlib
from pathlib import Path
from tools import r12_policy_v4 as v4
from tools.r11_verify_release import replay
v3=v4.v3;v2=v4.v2;v1=v4.v1;rules=v4.rules;engine=v4.engine
BASE_HEAD=rules.headings;BASE_NORM=rules.normalize;BASE_DECIDE=rules.decide;BASE_SPLIT=rules.split_mixed;BASE_TASK=rules.is_task
REVIEW_PATH=Path(__file__).resolve().parents[2]/'05_后续任务输出/三类共性问题修正_R12_20260928/V5完整原文定案补丁.json'
REVIEWS={x['raw_sha256']:x for x in BUNDLED_RESOURCES['v5_reviews']}
RAW_SIGNAL=re.compile(r'资格要求|上岗要求|职们要求|培养方向|培养期|厂购会|按时.{0,18}公司总部|主要在.{0,25}从事|熟练(?:进行|应用)|能(?:够)?(?:独立或|独立完|发现问题)|我们的优势|生活环境|(?:创立|成立)于\d{4}|(?<=[\u3400-\u9fff])[?？](?=[\u3400-\u9fff])|制作.{0,15}节日|培训期|具备.{0,35}能力[,，].{0,5}开展|(?:熟悉|熟知).{0,30}(?:付款方式|帐务|账务|加盟政策|企业文化|紧急事件)',re.I)
BODY_SIGNAL=re.compile(r'工作时间|资格要求|上岗要求|职们要求|薪资|福利|吃苦耐劳|坐姿为主|重体力|老员工带|家乡城市|调剂|(?:接受|适应).{0,20}出差|投简历|欢迎|创立于|作业员|装配工|储备干部|有一定的.{0,20}基础|结果导向|组建团推|来\s*自|更多数据|职能类|主要职责包括|(?m:^\s*(?:次要|导购|0[、.]|\d+:|\d+[、,]\d+[、,]|职责[一二三四五六七八九十]+|\*\s))|熟(?:悉|知|练)|精通|掌握',re.I)
QHEAD=re.compile(r'任职要求|任职资格|岗位要求|职位要求|资格要求|上岗要求|工作要求|应聘要求')
RHEAD=re.compile(r'岗位职责|工作职责|职责描述|工作内容|岗位内容')
def applicability(raw,body):
 reasons=[]
 if hashlib.sha256(raw.encode()).hexdigest() in REVIEWS:reasons.append('EXACT_COMPLETE_SOURCE_ADJUDICATION')
 if RAW_SIGNAL.search(raw):reasons.append('RAW_STRUCTURAL_OR_TASK_PATTERN')
 if BODY_SIGNAL.search(body) or '地点不限' in body:reasons.append('RETAINED_NON_DUTY_OR_SCOPE_PATTERN')
 # A whole saved line also in the trailing applicant block warrants inspection.
 # This is a trigger, never an instruction to drop that line.
 s=v4.engine.folded(raw);qs=list(QHEAD.finditer(s))
 if qs:
  q=s[qs[-1].end():];r=RHEAD.search(q)
  if r:q=q[:r.start()]
  compact=lambda t:re.sub(r'[\W_]+','',t)
  q=compact(q)
  if any(5<=len(z:=compact(line))<=100 and z in q for line in body.splitlines()):reasons.append('RETAINED_LINE_IN_APPLICANT_BLOCK')
 return reasons

for name,role in {'资格要求':'Q','上岗要求':'Q','职们要求':'Q','生活环境':'B','我们的优势':'B','我们向你提供':'B','基层培养期':'R','主管锻炼期':'R','经理提升期':'R','总经理的高端晋升期':'R'}.items():rules.HROLE[name.lower()]=role
rules.HEAD=re.compile('|'.join(sorted(map(re.escape,rules.HROLE),key=len,reverse=True)),re.I)
EXTRA_HEAD=re.compile(r'(资格要求|上岗要求|职们要求|生活环境|我们的优势|我们向你提供|工作时间)\s*[】\]]?\s*[:：]?')
def headings(s):
 hs=BASE_HEAD(s)
 for m in EXTRA_HEAD.finditer(s):
  a,b=m.span()
  if m[1]=='工作时间' and ':' not in m[0]:continue
  if a and s[a-1] in '[【':a-=1
  if any(h['a']<=a and b<=h['b'] for h in hs):continue
  hs=[h for h in hs if not(h['a']<b and a<h['b'])];hs.append(dict(a=a,b=b,role='A' if m[1]=='工作时间' else rules.HROLE[m[1]],name=m[1]))
 return sorted(hs,key=lambda h:(h['a'],h['b']))
rules.headings=headings

def normalize(raw):
 s,st=BASE_NORM(raw);es=[]
 review=REVIEWS.get(hashlib.sha256(raw.encode()).hexdigest())
 if review:
  assert review['raw']==raw
  for r in review['normalization']:
   for m in re.finditer(re.escape(r['old']),s):es.append(dict(a=m.start(),b=m.end(),old=m[0],new=r['new'],rule='R12V5_REVIEWED_TECHNICAL_TOKEN_SEPARATOR'))
  s,es=rules.apply(s,es)
  if es:st.append(dict(name='reviewed_literal_token_spacing',edits=es))
  es=[]
 # These are explicit repeated list/section markers, not numerical quantities.
 for m in re.finditer(r'(?m)(?:(?<=^)|(?<=[。;；\n:]))\s*(?:职责[一二三四五六七八九十]+[:：]+|0[、.]\s*|[1-9]\d?[:：](?=[\u3400-\u9fff]))',s):
  es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='R12V5_EXPLICIT_ORDINAL_LAYOUT'))
 for m in re.finditer(r'(?m)^\s*\*\s+(?=[\u3400-\u9fff])',s):es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='R12V5_ASTERISK_BULLET'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='r12v5_list_layout',edits=es))
 return s,st
rules.normalize=normalize

EXPLICIT_TASK=re.compile(r'^(?:(?:按时|按质|按量)[、,，]?)+(?:完成|提交|编写)|^(?:主要|日常)?在.{1,30}从事.{2,}|^熟练(?:进行.{2,}|应用.{1,35}(?:进行|编制|绘制|完成).{2,})|^能(?:够)?(?:独立或带领团队完成|独立完(?=现场)|发现问题并).{2,}|^.{0,45}制作宣传(?:节日|节气|新闻).{1,}')
NEGATIVE=re.compile(r'^(?:能(?:够)?吃苦耐劳|遇事懂得思考|有(?:一定|较强|良好)的.{0,30}基础|执行结果导向|目标导向及结果导向思维|服从公司调剂|急需储备干部|作业员[。;；]*$|产品装配工[。;；]*$|坐姿为主|无重体力劳动|没经验前期有老员工带|可根据员工家乡城市|同样享受国家|我们欢迎.{0,40}回家|本职位需要.{0,40}培训|注[:：]负责.{1,15}区域|地点不限|组建团推[。;；]*$)')
TRAVEL=re.compile(r'^(?:能(?:够)?|可以?|愿意)?接受(?:经常|长期|短期|频繁)?出差[。;；,，]*$')
PROFILE=re.compile(r'^(?!负责|协助|参与|管理|监督|制定|跟进|推动|组织).{1,40}(?:创立|成立|诞生)于\d{4}年')
EMPTY_META=re.compile(r'^(?:来\s*自|更多数据\s*[,，]?\s*详见|职能类|(?:该职位的)?主要职责包括|次要|导购)[。;；,，:：]*$')
SOFT_KNOWLEDGE=re.compile(r'^熟练(?:使用|掌握|应用).{1,80}(?:SQL语句|Linux基本命令|编程语言|软件工具)(?:[、,，].*)?$',re.I)
INFO=re.compile(r'^(?:熟悉|熟知)(?:所有付款方式|帐务的处理|账务的处理|公司全品牌加盟政策|司企业文化)|^熟知所有关于紧急事件的处理计划')
def is_task(t):return bool(EXPLICIT_TASK.match(v1.strip_clause(t))) or BASE_TASK(t)
rules.is_task=is_task

def decide(text,role,previous=None):
 t=v1.strip_clause(text)
 if EMPTY_META.fullmatch(t.strip('()[] ')):return 'S','R12V5_ORPHAN_METADATA_OR_HEADING'
 if t.strip('()[] 。;；')=='项目地' or re.match(r'^\d*:?一个月出差\d+天',t):return 'N','R12V5_LOCATION_AND_SHIFT_SCHEDULE'
 if NEGATIVE.match(t) or TRAVEL.fullmatch(t):return 'N','R12V5_EXPLICIT_APPLICANT_ENVIRONMENT_OR_RECRUITMENT'
 if PROFILE.match(t):return 'N','R12V5_BRAND_HISTORY_PREFACE'
 if len(re.findall(r'(?<=[\u3400-\u9fff])\?(?=[\u3400-\u9fff])',t))>=2:return 'X','R12V5_MULTIPLE_UNRECOVERABLE_WORD_GAPS'
 if SOFT_KNOWLEDGE.match(t) and not re.search(r'(?:进行|完成|编写|制作|生成|开发|设计).{2,}',t):return 'N','R12V5_SOFTWARE_PROFICIENCY_WITHOUT_ASSIGNED_ACTION'
 if EXPLICIT_TASK.match(t) and role not in {'Q','Q_FIELD','B','OFFER','NOTICE','COMPETENCY'} and not rules.DAMAGE.search(t):return 'R','R12V5_COMPLETE_MODAL_OR_NOMINAL_ASSIGNED_WORK'
 if role=='R' and INFO.match(t):return 'R','R12V5_IN_ROLE_BUSINESS_PREPARATION'
 return BASE_DECIDE(text,role,previous)
rules.decide=decide

def split_mixed(s,a,b,role):
 cs=v1.clauses(s,a,b);points={a,b};full=v1.strip_clause(s[a:b]);first=v1.strip_clause(s[cs[0][0]:cs[0][1]]) if cs else ''
 for lo,hi in BASE_SPLIT(s,a,b,role):points.update((lo,hi))
 if role in {'Q','Q_FIELD'} and (v1.KNOW.match(first) or re.search(r'(?:等)?相关专业[。;；,，]*$',full)):
  safe=[lo for lo,hi in cs[1:] if re.match(r'^(?:负责(?!过|人)|协助|开展|主导|承担(?!过)|严格按照|处理|实现)',v1.strip_clause(s[lo:hi])) and not re.search(r'能力|经验|经历',s[lo:hi])]
  return list(zip(sorted({a,b,*safe}),sorted({a,b,*safe})[1:]))
 for i,(lo,hi) in enumerate(cs):
  t=v1.strip_clause(s[lo:hi])
  if NEGATIVE.match(t) or TRAVEL.fullmatch(t) or role=='R' and EXPLICIT_TASK.match(t):points.add(lo)
  if t.strip(' ,，。;；')=='地点不限':points.add(hi)
  if role=='R' and i and NEGATIVE.match(v1.strip_clause(s[a:lo])) and re.match(r'^(?:对.{1,30}进行|负责|协助|完成|开展)',t):points.add(lo)
  if role in {'Q','Q_FIELD'} and i and re.match(r'^开展.{2,30}工作',t):points.add(lo)
 if role=='R' and re.match(r'^熟悉8D[,，]',full):return [(a,b)]
 return list(zip(sorted(points),sorted(points)[1:]))
rules.split_mixed=split_mixed

BASE_FINISH=rules.finish_body
def finish_body(body):
 s,st=BASE_FINISH(body);es=[]
 for m in re.finditer(r'(?m)^\s*(?:0[、.]\s*|([1-9]\d?)[、,]\1[、,]\s*|\*\s+)',s):es.append(dict(a=m.start(),b=m.end(),old=m[0],new='',rule='R12V5_RESIDUAL_PROVEN_LIST_MARKER'))
 cols=list(re.finditer(r'(?m)^\s*\d{1,2}:(?=[\u3400-\u9fff])',s))
 if len(cols)>=2:
  for m in cols:es.append(dict(a=m.start(),b=m.end(),old=m[0],new='',rule='R12V5_REPEATED_COLON_ORDINAL'))
 captions=list(re.finditer(r'(?:^|(?<=\s))职责[一二三四五六七八九十]+(?::+|(?=\n|$))',s))
 if len(captions)>=2:
  for m in captions:es.append(dict(a=m.start(),b=m.end(),old=m[0],new='\n',rule='R12V5_NUMBERED_DUTY_CAPTION'))
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='r12v5_residual_layout',edits=es))
 es=[dict(a=m.start(),b=m.end(),old=m[0],new='',rule='R12V5_EMPTY_OR_DUPLICATED_LEADING_CAPTION') for m in re.finditer(r'(?m)^主要负责:(?=负责)|[ \t]+(?=\n|$)',s)]
 s,es=rules.apply(s,es)
 if es:st.append(dict(name='r12v5_line_edge_cleanup',edits=es))
 return s,st
rules.finish_body=finish_body

def _overlay(p,s,changes):
 points={0,len(s)}
 for u in p['partition']:points.update((u['a'],u['b']))
 for c in changes:points.update((c['a'],c['b']))
 result=[];j=0
 for a,b in zip(sorted(points),sorted(points)[1:]):
  while p['partition'][j]['b']<=a:j+=1
  u=dict(p['partition'][j],a=a,b=b)
  for c in changes:
   if c['a']<=a<b<=c['b']:u.update(label=c['label'],reason=c['reason'])
  result.append(u)
 p['partition']=result

@functools.lru_cache(maxsize=8192)
def _cached(raw):
 # Clear the baseline cache between policies by using its private uncached body.
 p=v4._cached.__wrapped__(raw);s,_=replay(raw,p['normalization']);changes=[]
 duty_heads=[h for h in headings(s) if h['role']=='R'];first_duty=duty_heads[0]['a'] if duty_heads else None
 if first_duty and PROFILE.match(v1.strip_clause(s[:first_duty])):changes.append(dict(a=0,b=first_duty,label='N',reason='R12V5_COMPLETE_BRAND_HISTORY_BEFORE_EXPLICIT_DUTIES'))
 for u in p['partition']:
  if u['label']=='S':continue
  t=s[u['a']:u['b']];lab,why=decide(t,u.get('section'))
  if why.startswith('R12V5_'):u.update(label=lab,reason=why)
  if u.get('section')=='R' and re.match(r'^熟悉8D[,，]',v1.strip_clause(t)):u.update(label='N',reason='R12V5_SKILL_LIST_WITH_SHARED_KNOWLEDGE_PREDICATE')
 # A knowledge-led item with explicit experience/ability remains an eligibility
 # item, even when its source section is mislabeled as responsibilities.
 groups=[];group=[]
 for u in p['partition']:
  if u['label']=='S' and ('MARKER' in u['reason'] or 'ORDINAL' in u['reason'] or u['reason']=='EXPLICIT_SECTION_HEADING'):
   if group:groups.append(group);group=[]
  elif u['label']!='S':group.append(u)
 if group:groups.append(group)
 for group in groups:
  whole=''.join(s[u['a']:u['b']] for u in group);first=v1.strip_clause(whole)
  if v1.KNOW.match(first) and re.search(r'经验|经历|能力',whole):
   for u in group:
    if u['label']=='R' and v1.KNOW.match(v1.strip_clause(s[u['a']:u['b']])):u.update(label='N',reason='R12V5_KNOWLEDGE_GOVERNED_BY_EXPLICIT_EXPERIENCE_ITEM')
 # Explicit duties after a career-direction title are work, not the title.
 for m in re.finditer(r'培养方向\s*[:：]\s*[^。;；\n]{1,28}?工程师\s+(?P<t>[^。\n]+[。]?)',s):
  t=m['t']
  if re.search(r'推广|技术支持|收集|翻译|编制|客户|负责',t):changes.append(dict(a=m.start('t'),b=m.end('t'),label='R',reason='R12V5_ACTUAL_WORK_AFTER_CAREER_DIRECTION_TITLE'))
 review=REVIEWS.get(hashlib.sha256(raw.encode()).hexdigest())
 if review:
  assert review['raw']==raw
  for d in review['decisions']:
   matches=list(re.finditer(re.escape(d['text']),s));assert len(matches)==1,(review['draw_index'],d['text'],s)
   m=matches[0];changes.append(dict(a=m.start(),b=m.end(),label=d['label'],reason=d['reason']))
 if changes:_overlay(p,s,changes)
 engine.rebuild(p,s);p.update(proposed_after=p['after'],adopted=True,preserve_parent_reason=None,policy_version='R12_V5_FINAL_SCOPED_SOURCE_REPAIRS')
 return p
def process(raw,row):
 p=dict(_cached(raw));before=row['responsibility_text'];p.update(record_id=row['record_id'],before=before,before_sha256=engine.digest(before.encode()),text_changed=p['after']!=before,parent_role='COMPARISON_ONLY_NOT_CLASSIFICATION');return p
''',
'tools.r12_policy_v6': r'''"""Narrow final protection against Chinese substring ambiguities.

过程 is a current-work object, not the experiential aspect marker 过.
实现招聘目标 is assigned work, not the notice 现招聘. No past-experience
or advertisement statement is rescued merely by containing these characters.
"""
import copy,re
from tools import r12_policy_v5 as v5
from tools.r11_verify_release import replay
rules=v5.rules;engine=v5.engine
PROCESS_OBJECT=r'过程(?:质量|控制|管理|检验|检测|审核|监控|优化|改进|改善|策划|验证|分析|文件|文档|风险|异常|能力|中|的|设计|确认|审查)'
RAW=re.compile(r'(?:负责|参与|承担|从事)'+PROCESS_OBJECT+r'|实现招聘(?:目标|计划|指标|任务)')
START=re.compile(r'^(?:(?:负责|参与|承担|从事)'+PROCESS_OBJECT+r'|实现招聘(?:目标|计划|指标|任务))')
CONDITION=re.compile(r'经验|经历|者优先|优先考虑|优先录用|学历|学位|相关专业|(?:能力|条件|资格)[。;；,，]*$')
def applicable(raw):return bool(RAW.search(raw))
def process(raw,row):
 p=copy.deepcopy(v5.process(raw,row));s,_=replay(raw,p['normalization'])
 for u in p['partition']:
  if u['label'] in {'S','X'} or u.get('section') in {'A','B','C','OFFER','NOTICE','COMPETENCY','Q_FIELD'}:continue
  t=v5.v1.strip_clause(s[u['a']:u['b']])
  if START.match(t) and not CONDITION.search(t) and not rules.DAMAGE.search(t):
   u.update(label='R',reason='R12V6_CURRENT_PROCESS_OR_RECRUITMENT_GOAL_NOT_PAST_OR_ADVERTISEMENT')
 engine.rebuild(p,s);p.update(proposed_after=p['after'],adopted=True,text_changed=p['after']!=p['before'],preserve_parent_reason=None,policy_version='R12_V6_NARROW_CHINESE_SUBSTRING_DUTY_GUARD')
 return p
''',
'tools.r12_policy_v7': r'''"""Two fully reviewed original templates: deterministic literal-span cleanup."""
import copy,hashlib,json,re
from pathlib import Path
from tools import r12_policy_v6 as v6
from tools.r11_verify_release import replay
OUT=Path(__file__).resolve().parents[2]/'05_后续任务输出/三类共性问题修正_R12_20260928'
REVIEWS={x['raw_sha256']:x for x in BUNDLED_RESOURCES['v7_reviews']}
def process(raw,row):
 review=REVIEWS[hashlib.sha256(raw.encode()).hexdigest()];assert review['raw']==raw
 p=copy.deepcopy(v6.process(raw,row));s,_=replay(raw,p['normalization']);changes=[]
 for d in review['decisions']:
  matches=list(re.finditer(re.escape(d['text']),s));assert len(matches)==1,d['text'];m=matches[0]
  changes.append(dict(a=m.start(),b=m.end(),label=d['label'],reason=d['reason']))
 v6.v5._overlay(p,s,changes);v6.engine.rebuild(p,s)
 p.update(proposed_after=p['after'],adopted=True,text_changed=p['after']!=p['before'],preserve_parent_reason=None,policy_version='R12_V7_REVIEWED_COMPLETE_ORIGINAL_MIXED_TEXT',complete_source_review_sha256=hashlib.sha256(raw.encode()).hexdigest())
 return p
''',
}

# ===== Standalone execution layer (the decision rules above are frozen) =====
import builtins, functools, hashlib, inspect, json, sys, types
from pathlib import Path

class EmbeddedEngine:
    """Each instance owns isolated rule globals; V5 cannot mutate V4."""
    def __init__(self, version, memo=True):
        self.modules = {}
        self.version = version
        self.policy = self.load('tools.r12_policy_v4' if version == 'V4' else 'tools.r12_policy_v7')
        self.v5 = None if version == 'V4' else self.load('tools.r12_policy_v5')
        self.v6 = None if version == 'V4' else self.load('tools.r12_policy_v6')
        self.predicates = []
        if memo:
            pure={'cleantext','strip_clause','is_task','qualification','personal','operational','operational_knowledge','current','decide','actual','modal','_without_connector'}
            state={'_context_br','_parent_norm','_nested_context','_source_entity_names','_parent_events','_source_has_br','_source_has_letter','_br_active','_removed_markers'}
            replacements={};slots=[]
            for name,module in tuple(self.modules.items()):
                if name!='jdclean_unified.responsibility_repair_r11' and not name.startswith(('tools.r11_policy_','tools.r12_policy')):continue
                for attr,fn in tuple(vars(module).items()):
                    if inspect.isfunction(fn) and fn.__name__ in pure:
                        assert not set(fn.__code__.co_names)&state
                        if fn not in replacements:replacements[fn]=functools.lru_cache(maxsize=4096)(fn)
                        slots.append((module,attr,fn))
            for module,attr,fn in slots:setattr(module,attr,replacements[fn])
            self.predicates=list(replacements.values())
        target=self.policy if version=='V4' else self.v5
        target._cached=functools.lru_cache(maxsize=256)(target._cached.__wrapped__)

    def load(self, name):
        if name in self.modules:return self.modules[name]
        module=types.ModuleType('embedded_'+self.version+'.'+name)
        module.__file__='/__r12_embedded__/workspace/'+name.replace('.','/')+'.py'
        module.__package__=module.__name__.rpartition('.')[0]
        self.modules[name]=module
        if name in {'tools','jdclean_unified'}:
            module.__path__=[]
        else:
            env=dict(vars(builtins));env['__import__']=self.import_module
            module.__dict__.update(__builtins__=env,BUNDLED_RESOURCES=BUNDLED_RESOURCES)
            exec(compile(MODULE_SOURCES[name],'<embedded:'+name+'>','exec'),module.__dict__)
        if '.' in name:
            parent,attr=name.rsplit('.',1);setattr(self.load(parent),attr,module)
        return module

    def import_module(self,name,globals=None,locals=None,fromlist=(),level=0):
        if level==0 and (name in MODULE_SOURCES or name in {'tools','jdclean_unified'}):
            module=self.load(name)
            for item in fromlist:
                if item!='*' and not hasattr(module,item) and name+'.'+item in MODULE_SOURCES:self.load(name+'.'+item)
            return module if fromlist else self.load(name.split('.')[0])
        return builtins.__import__(name,globals,locals,fromlist,level)

    def process(self,raw,stage):
        for fn in self.predicates:fn.cache_clear()
        row={'record_id':'SOURCE_ONLY','responsibility_text':''}
        policy=self.policy if stage in {'V4','V7'} else (self.v5 if stage=='V5' else self.v6)
        return policy.process(raw,row)

def load_review_resources(path=None):
    """Load local adjudications; never distribute private originals in this repository."""
    global BUNDLED_RESOURCES
    if path is None:
        BUNDLED_RESOURCES = {'r10_reviews': [], 'v5_reviews': [], 'v7_reviews': []}
        return
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if set(data) != {'r10_reviews', 'v5_reviews', 'v7_reviews'}:
        raise ValueError('Unexpected review resource groups.')
    for rows in data.values():
        if not isinstance(rows, list):
            raise ValueError('Review resource groups must be lists.')
        for row in rows:
            if not isinstance(row, dict) or 'raw' not in row or 'raw_sha256' not in row:
                raise ValueError('Review resource schema is invalid.')
            if hashlib.sha256(row['raw'].encode('utf-8')).hexdigest() != row['raw_sha256']:
                raise ValueError('Local review raw-text checksum mismatch.')
    BUNDLED_RESOURCES = data

class Cleaner:
    def __init__(self,memo=True):
        self.base=EmbeddedEngine('V4',memo)
        self.later=EmbeddedEngine('V7',memo)
        self.cached=functools.lru_cache(maxsize=8192)(self._clean)
    def _clean(self,raw):
        p=self.base.process(raw,'V4');body=p['after'];stage='V4'
        if self.later.v5.applicability(raw,body):p=self.later.process(raw,'V5');body=p['after'];stage='V5'
        if self.later.v6.applicable(raw):p=self.later.process(raw,'V6');body=p['after'];stage='V6'
        if hashlib.sha256(raw.encode()).hexdigest() in self.later.policy.REVIEWS:p=self.later.process(raw,'V7');body=p['after'];stage='V7'
        return body,stage
    def clean(self,raw):return self.cached(raw)

import argparse, collections, concurrent.futures, csv, gzip, io, multiprocessing, os, platform, sqlite3, time

FIELDS=['record_id','stock_code','year','source','responsibility_text','raw_text_sha256']
RAW_COLUMNS=['关联股票代码','招聘发布年份','来源','职位描述']
_WORKER=None

def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
    return h.hexdigest()

def atomic_json(path,value):
    path=Path(path);temp=path.with_name(path.name+'.tmp')
    temp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');os.replace(temp,path)

def canonical(row):
    return (json.dumps([row[k] for k in FIELDS],ensure_ascii=False,separators=(',',':'))+'\n').encode('utf-8')

def worker_init(review_resources=None):
    global _WORKER
    load_review_resources(review_resources)
    _WORKER=Cleaner()

def worker_batch(batch):
    answer=[]
    for sid,raw_sha,raw in batch:
        try:body,stage=_WORKER.clean(raw)
        except Exception as error:raise RuntimeError('Frozen cleaning failed for unique source '+str(sid)+' SHA256 '+raw_sha) from error
        answer.append((body,stage,sid))
    return answer

def progress(output,phase,**values):
    info={'phase':phase,'utc_time':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),**values}
    atomic_json(output/'progress.json',info)
    print(json.dumps(info,ensure_ascii=False),flush=True)

def existing_result(output):
    manifest=output/'manifest.json'
    if not manifest.exists():return None
    m=json.loads(manifest.read_text(encoding='utf-8'))
    if m.get('status') not in {'PASS_EXACT_R12_V7_REPRODUCTION','COMPLETE_OTHER_INPUT','PARTIAL_SMOKE_RUN'}:raise RuntimeError('Previous output did not pass; use a new output directory.')
    for e in m['files']:
        p=output/e['file']
        if not p.is_file() or file_sha(p)!=e['sha256']:raise RuntimeError('Existing output checksum failed: '+str(p))
    return m

def ingest(db,input_path,limit,output):
    try:
        csv.field_size_limit(sys.maxsize)
    except OverflowError:
        # CPython uses C long here; Windows may have a 32-bit C long.
        csv.field_size_limit(2**31-1)
    known={};count=0;start=time.monotonic();last=start
    with input_path.open('r',encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f)
        if reader.fieldnames is None or any(k not in reader.fieldnames for k in RAW_COLUMNS):raise ValueError('Missing required raw CSV columns: '+', '.join(RAW_COLUMNS))
        if len(reader.fieldnames)!=len(set(reader.fieldnames)):raise ValueError('Duplicate CSV column names are not accepted.')
        db.execute('BEGIN')
        for row in reader:
            if limit and count>=limit:break
            if None in row or any(row.get(k) is None for k in RAW_COLUMNS):raise ValueError('Malformed CSV record at ordinal '+str(count+1))
            raw=row['职位描述'];digest=hashlib.sha256(raw.encode('utf-8')).digest()
            sid=known.get(digest)
            if sid is None:
                sid=len(known)+1;known[digest]=sid
                db.execute('INSERT INTO sources(sid,raw_sha,raw) VALUES(?,?,?)',(sid,digest.hex(),raw))
            count+=1
            db.execute('INSERT INTO records(seq,stock_code,year,source,sid) VALUES(?,?,?,?,?)',(count,row['关联股票代码'],row['招聘发布年份'],row['来源'],sid))
            if count%50000==0:
                db.commit();db.execute('BEGIN')
                if time.monotonic()-last>=10:
                    progress(output,'INGEST_RAW_INPUT',records=count,elapsed_seconds=round(time.monotonic()-start,1));last=time.monotonic()
        db.execute('INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)',('ingest_complete','true'))
        db.execute('INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)',('records',str(count)));db.commit()
    return count

def classify(db,args,output):
    total=db.execute('SELECT count(*) FROM sources').fetchone()[0]
    done,last_sid=db.execute('SELECT count(*),coalesce(max(sid),0) FROM results').fetchone()
    if done!=last_sid:raise RuntimeError('Resume results are not a contiguous source prefix.')
    start=time.monotonic();last=start;pending=collections.deque();exhausted=False
    progress(output,'CLEAN_UNIQUE_ORIGINALS',unique_total=total,unique_done=done,workers=args.workers)
    context=multiprocessing.get_context('spawn')
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers,mp_context=context,initializer=worker_init,initargs=(args.review_resources,)) as pool:
        while pending or not exhausted:
            while not exhausted and len(pending)<2*args.workers:
                batch=db.execute('SELECT sid,raw_sha,raw FROM sources WHERE sid>? ORDER BY sid LIMIT ?',(last_sid,args.batch_size)).fetchall()
                if not batch:exhausted=True;break
                last_sid=batch[-1][0];pending.append(pool.submit(worker_batch,batch))
            if not pending:break
            result=pending.popleft().result()
            db.executemany('INSERT INTO results(body,stage,sid) VALUES(?,?,?)',result);db.commit();done+=len(result)
            if time.monotonic()-last>=10 or done==total:
                progress(output,'CLEAN_UNIQUE_ORIGINALS',unique_total=total,unique_done=done,elapsed_seconds=round(time.monotonic()-start,1));last=time.monotonic()
    if db.execute('SELECT count(*) FROM results').fetchone()[0]!=total:raise RuntimeError('Some sources were not cleaned; incomplete output is not published.')
    return total

def export(db,args,output,input_sha,code_sha,unique_count):
    dest=output/'cleaned';dest.mkdir(exist_ok=True)
    h=hashlib.sha256();counts=collections.Counter();files=[];writer=stream=binary=None;part=0;part_rows=0;temp=None
    def finish_part():
        if stream is None:return
        stream.close();binary.close();target=dest/f'part_{part:05d}.csv.gz';os.replace(temp,target)
        files.append({'file':str(target.relative_to(output)),'records':part_rows,'bytes':target.stat().st_size,'sha256':file_sha(target)})
    query='SELECT r.seq,r.stock_code,r.year,r.source,x.body,s.raw_sha,x.stage FROM records r JOIN sources s ON s.sid=r.sid JOIN results x ON x.sid=r.sid ORDER BY r.seq'
    try:
        for seq,stock,year,source,body,raw_sha,stage in db.execute(query):
            if part_rows==50000 or writer is None:
                finish_part();part+=1;part_rows=0;temp=dest/f'part_{part:05d}.csv.gz.partial';binary=temp.open('wb')
                gz=gzip.GzipFile(filename='',fileobj=binary,mode='wb',compresslevel=6,mtime=0)
                stream=io.TextIOWrapper(gz,encoding='utf-8-sig',newline='');writer=csv.DictWriter(stream,fieldnames=FIELDS+['cleaning_version','applied_stage'],lineterminator='\n');writer.writeheader()
            if seq!=counts['records']+1:raise RuntimeError('Raw record order changed.')
            row=dict(record_id=f'R2_{seq:010d}',stock_code=stock,year=year,source=source,responsibility_text=body,raw_text_sha256=raw_sha)
            h.update(canonical(row));writer.writerow(dict(row,cleaning_version='R12_V7_FROZEN' if args.review_resources else 'R12_V7_PUBLIC_RULES',applied_stage=stage));part_rows+=1
            counts.update(records=1,nonempty_records=int(bool(body.strip())),empty_records=int(not body.strip()));counts['stage_'+stage]+=1
            if seq%250000==0:progress(output,'EXPORT_IN_ORIGINAL_ORDER',records=seq)
        finish_part();stream=binary=None
    finally:
        if stream is not None:stream.close()
        if binary is not None:binary.close()
    digest=h.hexdigest();full_known=input_sha==EXPECTED['input_sha256'] and not args.limit
    exact=full_known and counts['records']==EXPECTED['records'] and digest==EXPECTED['canonical_sha256']
    status='PASS_EXACT_R12_V7_REPRODUCTION' if exact else ('PARTIAL_SMOKE_RUN' if args.limit else 'COMPLETE_OTHER_INPUT')
    if full_known and not exact:status='FAILED_REFERENCE_EQUIVALENCE'
    manifest={'status':status,'scope':'Raw CSV to frozen responsibility text; does not compute semantic-drift indicators.','version':'R12 V7','counts':dict(counts),'unique_originals_computed':unique_count,'input_sha256':input_sha,'script_sha256':code_sha,'review_resources_sha256':args.review_resources_sha256,'private_reviews_loaded':bool(args.review_resources),'canonical_fields':FIELDS,'canonical_sha256':digest,'expected_canonical_sha256':EXPECTED['canonical_sha256'] if full_known else None,'frozen_reference_match':exact,'used_saved_cleaned_text_as_input':False,'external_network_calls':0,'human_gold_standard':False,'files':files,'environment':{'python':sys.version,'platform':platform.platform(),'sqlite':sqlite3.sqlite_version},'parameters':{'workers':args.workers,'batch_size':args.batch_size,'limit':args.limit,'exact_source_deduplication_for_compute_only':True,'record_order_and_weights_preserved':True}}
    atomic_json(output/'manifest.json',manifest)
    if full_known and not exact:raise RuntimeError('Rebuilt output differs from frozen R12 V7. Failed output is preserved for diagnosis; it is NOT accepted.')
    return manifest

def main(argv=None):
    parser=argparse.ArgumentParser(description='One-file frozen R12 V7 cleaning from the original recruitment CSV. No third-party packages or network required.')
    here=Path(__file__).resolve().parent
    parser.add_argument('--input',type=Path,default=here/'data/原始数据2.0版本.csv')
    parser.add_argument('--output-dir',type=Path,default=here/'output')
    parser.add_argument('--workers',type=int,default=min(6,max(1,(os.cpu_count() or 2)-2)))
    parser.add_argument('--batch-size',type=int,default=500)
    parser.add_argument('--limit',type=int,default=0,help='Smoke test only; a limited run is never marked as a full reproduction.')
    parser.add_argument('--review-resources',type=Path,help='Optional private local adjudications; needed for exact frozen-corpus reproduction.')
    parser.add_argument('--resume',action='store_true',help='Resume a complete raw-input index with identical code, input and limit.')
    parser.add_argument('--keep-work-db',action='store_true')
    parser.add_argument('--allow-other-input',action='store_true',help='Allow a different raw CSV; output is not certified as the research corpus.')
    args=parser.parse_args(argv)
    if sys.version_info[:2]!=(3,12):parser.error('Use CPython 3.12.x for the frozen research environment.')
    if args.workers<1 or args.batch_size<1 or args.limit<0:parser.error('Invalid workers, batch-size or limit.')
    args.input=args.input.resolve();output=args.output_dir.resolve()
    args.review_resources=args.review_resources.resolve() if args.review_resources else None
    load_review_resources(args.review_resources)
    args.review_resources_sha256=file_sha(args.review_resources) if args.review_resources else None
    if not args.input.is_file():parser.error('Raw input not found: '+str(args.input))
    if args.input.is_relative_to(output):parser.error('Output directory must not contain the raw input.')
    if output.exists() and any(output.iterdir()) and not args.resume:parser.error('Output directory is not empty; use a new directory or --resume.')
    output.mkdir(parents=True,exist_ok=True);start=time.monotonic();code_sha=file_sha(Path(__file__))
    progress(output,'CHECK_INPUT_SHA256',input=str(args.input));input_sha=file_sha(args.input)
    if input_sha!=EXPECTED['input_sha256'] and not args.allow_other_input:raise ValueError('Input SHA256 differs from the preserved original. No cleaning was performed. Use --allow-other-input only for a deliberately different dataset.')
    if input_sha==EXPECTED['input_sha256'] and not args.review_resources:
        raise ValueError('Frozen-corpus reproduction requires --review-resources with the separately held private local review JSON.')
    previous=existing_result(output) if args.resume else None
    if previous:
        if previous['script_sha256']!=code_sha or previous['input_sha256']!=input_sha or previous['parameters']['limit']!=args.limit or previous.get('review_resources_sha256')!=args.review_resources_sha256:raise RuntimeError('Existing output belongs to different code or input.')
        print('Existing output verified; no new reconstruction performed. Choose an empty output directory for a fresh run.',flush=True);return previous
    dbpath=output/'work.sqlite';new=not dbpath.exists();db=sqlite3.connect(dbpath)
    try:
        # The raw index is disposable and not resumable until complete. Avoid
        # writing each large original twice on removable storage. Cleaning
        # checkpoints switch to WAL after the complete raw index is flushed.
        db.execute('PRAGMA journal_mode='+('OFF' if new else 'WAL'))
        db.execute('PRAGMA synchronous='+('OFF' if new else 'NORMAL'))
        db.execute('PRAGMA temp_store=MEMORY');db.execute('PRAGMA cache_size=-131072')
        if new:
            db.executescript('CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT); CREATE TABLE sources(sid INTEGER PRIMARY KEY,raw_sha TEXT NOT NULL,raw TEXT NOT NULL); CREATE TABLE records(seq INTEGER PRIMARY KEY,stock_code TEXT NOT NULL,year TEXT NOT NULL,source TEXT NOT NULL,sid INTEGER NOT NULL); CREATE TABLE results(sid INTEGER PRIMARY KEY,body TEXT NOT NULL,stage TEXT NOT NULL);')
            db.executemany('INSERT INTO meta VALUES(?,?)',[('input_sha256',input_sha),('script_sha256',code_sha),('limit',str(args.limit)),('review_resources_sha256',args.review_resources_sha256 or '')]);db.commit()
            n=ingest(db,args.input,args.limit,output)
            with dbpath.open('r+b') as handle:os.fsync(handle.fileno())
            db.execute('PRAGMA journal_mode=WAL');db.execute('PRAGMA synchronous=NORMAL')
        else:
            m=dict(db.execute('SELECT key,value FROM meta'))
            if not args.resume or m.get('input_sha256')!=input_sha or m.get('script_sha256')!=code_sha or m.get('limit')!=str(args.limit) or m.get('review_resources_sha256')!=(args.review_resources_sha256 or ''):raise RuntimeError('Resume identity mismatch.')
            if m.get('ingest_complete')!='true':raise RuntimeError('Input indexing was interrupted; use a new empty output directory.')
            n=int(m['records'])
        if not args.limit and input_sha==EXPECTED['input_sha256'] and n!=EXPECTED['records']:raise RuntimeError('Original input row count differs from the frozen corpus.')
        unique_count=classify(db,args,output)
        manifest=export(db,args,output,input_sha,code_sha,unique_count)
        manifest['elapsed_seconds']=round(time.monotonic()-start,2);atomic_json(output/'manifest.json',manifest)
    finally:db.close()
    if not args.keep_work_db:
        dbpath.unlink()
        for suffix in ['-journal','-wal','-shm']:
            sidecar=Path(str(dbpath)+suffix)
            if sidecar.exists():sidecar.unlink()
    progress(output,manifest['status'],records=manifest['counts']['records'],canonical_sha256=manifest['canonical_sha256'],elapsed_seconds=manifest['elapsed_seconds'])
    return manifest

if __name__=='__main__':
    multiprocessing.freeze_support()
    try:main()
    except (Exception,KeyboardInterrupt) as error:
        print('FAILED: '+str(error),file=sys.stderr,flush=True);raise SystemExit(1)
