# 核心与前沿阅读清单

最后人工复审：2026-07-17。

## 基础机制

这些论文用于理解 Agent 的基本设计语言，不代表其中所有方法都适合生产。

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)：推理轨迹与行动交替。
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)：模型如何学习调用外部工具。
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)：利用反馈和语言记忆迭代任务。
- [Generative Agents](https://arxiv.org/abs/2304.03442)：记忆、反思和计划的组合。
- [Voyager](https://arxiv.org/abs/2305.16291)：技能库、自动课程和长期探索。

## 评测与真实环境

- [AgentBench](https://arxiv.org/abs/2308.03688)：跨环境 Agent 评测。
- [GAIA](https://arxiv.org/abs/2311.12983)：需要推理、工具和真实世界信息的问题。
- [WebArena](https://arxiv.org/abs/2307.13854)：可重复的网页任务环境。
- [OSWorld](https://arxiv.org/abs/2404.07972)：真实桌面应用中的多模态 Agent。
- [SWE-bench](https://arxiv.org/abs/2310.06770)：真实 GitHub Issue 的软件工程评测。
- [SWE-agent](https://arxiv.org/abs/2405.15793)：面向软件仓库的 Agent-Computer Interface。
- [tau-bench](https://arxiv.org/abs/2406.12045)：工具、规则约束与用户交互中的可靠性。

## 2025-2026 前沿观察

以下论文较新，首先作为研究和实验材料，不直接写入稳定核心。

- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)：整理能力、可靠性、安全和企业评测问题。
- [OdysseyBench](https://arxiv.org/abs/2508.09124)：跨办公应用的长程工作流评测。
- [PlanBench-XL](https://arxiv.org/abs/2606.22388)：大型工具生态、工具检索受限和失败恢复。
- [Beyond the Leaderboard](https://arxiv.org/abs/2607.05775)：归纳工具、规划、长程、多 Agent、安全和测量有效性问题。

## 协议和官方工程源

- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/latest)：MCP 的协议、生命周期、授权和安全要求。
- [MCP Changelog](https://modelcontextprotocol.io/specification/latest/changelog)：用于跟踪传输、授权、结构化输出等变化。

## 阅读顺序

主线课程阶段只精读 ReAct、SWE-bench 和 MCP 规范选段。其他论文按专修方向进入，不要求一次读完。每次阅读都要绑定一个可运行实验或现有项目观察。
