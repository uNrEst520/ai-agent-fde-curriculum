# 从 AI 使用者到 AI 业务交付者

<p align="center">
  <img src="assets/readme/ai-agent-fde-hero.png" alt="从 AI 使用者到 AI 业务交付者：AI Agent 与 FDE 课程" width="100%">
</p>


一套面向非科班转型者、AI Builder、Agent Product Engineer 与 FDE（Forward-Deployed Engineer）的长期开放课程。

这不是一门只持续 12 周的工具速成课。12 周只是共同核心，用来建立工程地图、Agent 原理、评测风控和第一次完整交付。之后继续进入方向专修、前沿论文实验、真实业务项目和周期性能力复评。

## 培养目标

课程最终训练五种不会因为工具更新而快速过时的能力：

1. 发现高价值问题。
2. 设计人机协作流程。
3. 验收 AI 输出并控制风险。
4. 把原型工程化为可运行、可维护、可观测的产品。
5. 把领域知识与 AI 组合成真实业务结果。

学习者可以使用 Codex、Claude Code 或其他 AI 编程工具完成大量代码工作，但必须能够解释系统、追踪数据、识别风险、运行验证并对交付结果负责。

## 课程架构

```text
共同核心（12周）
    ↓
方向专修（每个模块6-10周）
    ↓
前沿研究实验室（持续更新）
    ↓
FDE真实业务交付项目（每半年至少一次）
    ↓
作品集、求职、接单、企业内部落地或创业验证
```

| 层级 | 目的 | 主要产出 |
| --- | --- | --- |
| 共同核心 | 从 AI 使用者进入可解释工程状态 | 工程地图、API 实验、Agent Demo、评测集 |
| 方向专修 | 形成一个可就业或可接单的技术方向 | RAG、Agent 可靠性、MCP、部署或行业方案 |
| 研究实验室 | 追踪论文、协议和平台变化 | 论文卡片、复现实验、课程变更提案 |
| FDE 项目 | 让 AI 从“能演示”走向“能上岗” | 诊断、方案、系统、评测、上线与复盘 |

## 从这里开始

- [完整课程地图](docs/curriculum/README.md)
- [能力等级模型](docs/curriculum/competency-framework.md)
- [12 周共同核心](docs/curriculum/foundation-12-weeks.md)
- [长期进阶路线](docs/curriculum/lifelong-pathways.md)
- [学习与反 bypass 契约](docs/curriculum/learning-contract.md)
- [FDE 毕业项目标准](docs/curriculum/fde-capstone.md)
- [评测与毕业标准](docs/curriculum/assessment.md)
- [Week 01：工程地图与反 bypass](docs/course/week-01/README.md)

## 前沿研究与课程治理

- [研究雷达](research/README.md)
- [核心与前沿阅读清单](research/reading-list.md)
- [最新论文候选](research/radar/latest.md)
- [论文如何进入正式课程](docs/governance/research-to-course.md)
- [课程治理与版本规则](docs/governance/course-governance.md)
- [课程资料选择标准](docs/governance/source-selection-standard.md)
- [长期路线图](ROADMAP.md)
- [参与贡献](CONTRIBUTING.md)

研究雷达每周从 arXiv 等原始来源生成候选清单。自动收录不代表课程推荐；论文需要经过相关性判断、证据审查、最小复现和教学转化，才能进入共同核心或方向专修。
- [公开仓库隐私与发布安全](docs/governance/publication-safety.md)

## 每周学习节奏

工作日每天 2-3 小时，建议每周 10-15 小时：

```text
20% 原理与官方资料
25% 阅读和追踪现有项目
30% 使用 AI 编程工具完成改动
15% 测试、评测和风险检查
10% 复盘与业务表达
```

每周必须留下可检查证据：概念解释、工程链路、代码改动、命令结果、失败案例、评测记录和业务复盘。

## 本地验证

```powershell
python scripts\validate_curriculum.py
python -m unittest discover -s tests -v
```

## 现有作品集与学习记录

以下网球 AI 作品集继续作为课程的第一条真实领域实践线。

### 网球 AI Builder 作品集

这是一个面向创业公司、一人公司和垂直行业 AI 产品岗位的作品集总入口。核心叙事不是“传统程序员求职”，而是展示如何用 AI、Codex、MCP、自动化工作流和领域理解，把网球训练场景做成可试用、可复盘、可迭代的 AI 产品系统。

## 定位

- 求职标题：AI Builder / Agent Product Engineer / AI Application Engineer
- 主展示项目：`<PROJECT_ROOT>\网球视频识别`
- 产品主线：比赛复盘发现问题 -> 训练计划生成方案 -> 视频识别验证动作 -> 战术板解释打法
- 面试表达：我能把 AI、视觉分析、训练知识和产品体验组合成可用工具，而不是只会调 API。

## 项目矩阵

| 项目 | 角色 | 面试价值 |
| --- | --- | --- |
| 随身网球教练 MVP | 主入口 | Web + FastAPI + MediaPipe Pose + 报告导出 + 训练处方 |
| 网球训练计划 | 计划大脑 | 球员画像、训练库、训练闭环、长期成长数据 |
| 网球记分复盘 | 数据来源 | 计分、技术统计、赛后复盘、比赛问题转训练 |
| 网球战术板 | 可视化工具 | 站位、跑动、击球线路、战术动画和教练表达 |

## 关键材料

- [作品集首页](index.html)
- [正式课程 Week 01：工程地图与反 bypass 启动](docs/course/week-01/README.md)
- [项目一页纸：随身网球教练 MVP](docs/projects/tennis-ai-coach.md)
- [项目一页纸：网球训练计划](docs/projects/tennis-training-planner.md)
- [项目一页纸：网球记分复盘](docs/projects/tennis-score-review.md)
- [项目一页纸：网球战术板](docs/projects/tennis-tactics-board.md)
- [Agent 流程与主项目架构](docs/agent-flow-and-architecture.md)
- [3 个月双轨转型计划](docs/combined-3-month-roadmap.md)
- [Week 1 启动指南](docs/week-01-start-here.md)
- [Week 1 作业提交模板](docs/course/week-01/homework-template.md)
- [每周反 bypass 复盘模板](docs/weekly-anti-bypass-template.md)
- [面试故事与表达](docs/interview-stories.md)

## 3 分钟讲法

我原本是建筑设计师，优势不是传统代码背景，而是能理解复杂业务流程、把模糊需求拆成可执行系统。过去我从 GPT-3.5、ComfyUI、Sora/可灵、N8N/Opal、OpenClaw、Codex 和 MCP 一路实践下来，逐步形成了 AI Builder 工作流。

这个作品集用网球训练做垂直场景：比赛数据发现问题，训练计划安排练习，视频识别验证动作，战术板解释打法。主项目已经能上传动作视频、提取姿态、生成中文报告，并新增 AI 教练训练处方，把视觉证据转成下一组训练建议。

## 学习路线

作品集路线和系统学习路线合并推进：一边用现有网球项目做可展示产品，一边按 [3 个月双轨转型计划](docs/combined-3-month-roadmap.md) 补工程地图、API、数据流、测试、Agent 原理和反 bypass 工作法。

## 验证命令

主项目：

```powershell
cd "<PROJECT_ROOT>\网球视频识别"
npm run build
.\.server-venv\Scripts\python.exe -m pytest -p no:cacheprovider backend\tests
npm run smoke:ui
npm run smoke:retake
```

训练计划：

```powershell
cd "<PROJECT_ROOT>\网球训练计划"
node .\scripts\e2e-training-flow-check.js
node .\scripts\validate-templates.js
node .\scripts\blueprint-coverage-report.js
```

记分复盘：

```powershell
cd "<PROJECT_ROOT>\网球记分复盘"
npm test
```
