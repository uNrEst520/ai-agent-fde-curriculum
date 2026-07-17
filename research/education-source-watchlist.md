# AI 与工程教育资源观察库

> 状态：候选，不等于正式课程。最后人工检查：2026-07-17。

这个清单用于持续发现高质量课程，不要求学习者现在全部学习。资源只有在被拆到具体章节、预计时间和作业后，才会进入 [正式资源目录](../docs/resources/catalog.json)。

## 大学与结构化课程

| 候选 | 适合能力 | 为什么值得继续评估 | 当前不直接纳入的原因 |
| --- | --- | --- | --- |
| [MIT 6.102 Software Construction](https://web.mit.edu/6.102/www/sp26/) | 测试、规格、抽象、代码审查、并发 | 阅读与 Problem Sets 完整，软件工程标准高 | 工作量大，需要为 AI Builder 路线精选章节 |
| [MIT The Missing Semester](https://missing.csail.mit.edu/2020/) | Shell、Git、调试、构建工具、安全 | 免费、短、工程缺口针对性强 | Bash 环境与 Windows 学习者需要做命令映射 |
| [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) | 操作系统、进程、内存、并发、持久化 | University of Wisconsin 教材，章节与作业公开 | 需要只选与部署和 Agent Runtime 相关章节 |
| [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/) | tokenizer、Transformer、训练系统、数据、评测 | 从零构建导向强，课程和作业持续更新 | 先修要求高，适合 LM01 而非当前阶段 |
| [Berkeley RDI Education](https://rdi.berkeley.edu/education) | LLM Agent、Agentic AI、安全与研究 | 汇集 Berkeley 多期 Agent 课程 | 期次多，需选定稳定版本和具体 lecture |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com/) | AI 产品全生命周期、部署、团队与 LLM 应用 | 强调从问题到生产，而不只训练模型 | 要按 PR01/FDE 目标重新拆分，不整门照搬 |
| [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) | Agent 基础、框架、Agentic RAG、评测 | 免费、有作业与最终项目，每单元约 3-4 小时 | 框架内容变化快，要与无框架原理课配对 |
| [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | Docker、工作流、仓库、dbt、批流处理 | 开源、项目驱动、有完整模块和作业 | 需要压缩到 AI 应用真正需要的数据工程子集 |

## 作者与高质量 GitHub 课程

| 候选 | 作者/组织 | 可用于 | 观察重点 |
| --- | --- | --- | --- |
| [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) | Andrej Karpathy | DL01、LM01 | 从 micrograd 到 GPT/tokenizer 的讲练一致性很强 |
| [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch) | Sebastian Raschka | LM01、XLM | 章节、notebook、练习答案和更新记录完整 |
| [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | DataTalksClub | AP02、EV01、PR01 | RAG、评测、监控、用户界面与 capstone 形成闭环 |
| [Hugging Face Course](https://github.com/huggingface/course) | Hugging Face | NLP、Transformer、模型生态 | 内容开源且有多语言，但工具导向较强 |
| [Hugging Face Agents Course Source](https://github.com/huggingface/agents-course) | Hugging Face | AG01 | 可追踪课程具体单元和代码变更 |
| [OpenAI Cookbook](https://github.com/openai/openai-cookbook) | OpenAI | AP01、EV01 | 适合作为精确实验材料，不作为系统理论主课 |
| [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) | Anthropic | AP01、AG01、EV01 | 适合工具调用、评测和工作流实验，需核验版本 |
| [CS336 Lectures](https://github.com/stanford-cs336/lectures) | Stanford CS336 | LM01、XLM | 可对照每期课程代码和资源核算实验 |

## 教育资源检索工具

这些工具用于发现，不直接决定课程质量：

- [Class Central](https://www.classcentral.com/)：跨 Coursera、edX、大学公开课检索课程与学习者反馈。
- [OER Commons](https://oercommons.org/)：检索开放教育资源、教材和课程单元。
- [MIT OpenCourseWare](https://ocw.mit.edu/search/)：按主题检索 MIT 的公开课程材料。
- [GitHub Search](https://github.com/search)：组合组织、主题、更新时间、stars 与文件名发现课程仓库；必须回到作者和课程主页核验。
- [OpenAlex](https://openalex.org/) 与 [Papers with Code](https://paperswithcode.com/)：用于论文和代码发现，进入研究雷达而不是直接进入教学主线。

## 下一批筛选顺序

第一阶段试学完成后，只推进一个批次：

1. SE02 Web、API 与数据库。
2. SE03 AI 辅助软件工程。
3. AP01 模型 API 与 AI 体验的提前体验单元。

每个批次先比较 3-5 个候选，选 1 条主课，再写章节、跳过项和迁移作业。不会同时铺开所有后续课程。
