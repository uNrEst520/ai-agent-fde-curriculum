# Build Your Own AI

> 我无法创造的东西，我就无法理解。

这里不是成品代码合集，而是一条从空目录开始的 AI 系统构建阶梯。每个项目都把复杂系统拆成 6-8 个连续关卡；每一关必须完成构建、验证和解释，才进入下一关。

## 使用方法

1. 先完成对应课程的先修诊断。
2. 阅读最终接口和第一遍约束，不查看完整实现。
3. 每关先写假设、接口和测试，再让 AI 参与。
4. 保留阶段 commit、失败样本和 AI 决策记录。
5. 通过核心正确性后，再接成熟库做对照。
6. 用口试和现场修改证明理解，而不是用代码行数证明。

## 工程与数据地基

| ID | 构建项目 | 对应课程 | 小时 | 难度 |
| --- | --- | --- | ---: | --- |
| B00 | [个人学习操作系统](personal-learning-os.md) | [O00](../curriculum/modules/00-learning-operating-system.md) | 12-20 | 入门 |
| B01 | [命令行数据应用](cli-data-app.md) | [SE01](../curriculum/modules/01-python-computational-thinking.md) | 35-50 | 入门 |
| B02 | [HTTP 与完整 Web 服务](http-web-service.md) | [SE02](../curriculum/modules/02-web-api-databases.md) | 45-65 | 基础 |
| B03 | [AI 辅助工程流水线](ai-engineering-pipeline.md) | [SE03](../curriculum/modules/03-software-engineering-with-ai.md) | 35-55 | 基础 |
| B04 | [进程、网络与缓存实验室](systems-network-lab.md) | [SE04](../curriculum/modules/04-computer-systems-networks.md) | 35-50 | 基础 |
| B05 | [可复现数据管道](reproducible-data-pipeline.md) | [DE01](../curriculum/modules/05-data-engineering.md) | 35-55 | 基础 |

## AI 模型从零实现

| ID | 构建项目 | 对应课程 | 小时 | 难度 |
| --- | --- | --- | ---: | --- |
| B06 | [数学与优化可视化实验室](math-optimization-lab.md) | [AI01](../curriculum/modules/06-math-for-ai.md) | 45-65 | 基础 |
| B07 | [搜索、约束与规划引擎](search-planning-engine.md) | [AI02](../curriculum/modules/07-classical-ai-search-planning.md) | 40-60 | 基础 |
| B08 | [微型机器学习库](tiny-ml-library.md) | [ML01](../curriculum/modules/08-machine-learning-from-scratch.md) | 55-80 | 中级 |
| B09 | [自动微分与神经网络引擎](autograd-engine.md) | [DL01](../curriculum/modules/09-deep-learning-autograd.md) | 60-90 | 中级 |
| B10 | [微型 Transformer 语言模型](tiny-transformer.md) | [LM01](../curriculum/modules/10-transformer-language-model.md) | 80-120 | 中高级 |

## AI 应用、Agent 与生产交付

| ID | 构建项目 | 对应课程 | 小时 | 难度 |
| --- | --- | --- | ---: | --- |
| B11 | [供应商无关模型客户端](model-client-runtime.md) | [AP01](../curriculum/modules/11-model-api-ai-ux.md) | 30-45 | 中级 |
| B12 | [从零构建 RAG 引擎](rag-engine.md) | [AP02](../curriculum/modules/12-rag-knowledge-engineering.md) | 45-70 | 中级 |
| B13 | [工具协议与 MCP 系统](mcp-tool-system.md) | [AP03](../curriculum/modules/13-tool-use-mcp.md) | 45-65 | 中级 |
| B14 | [可恢复 Agent Runtime](agent-runtime.md) | [AG01](../curriculum/modules/14-agent-runtime.md) | 55-85 | 高级 |
| B15 | [AI 评测与红队框架](ai-eval-harness.md) | [EV01](../curriculum/modules/15-evaluation-safety-security.md) | 45-70 | 高级 |
| B16 | [生产模型网关](model-gateway.md) | [PR01](../curriculum/modules/16-production-ai-llmops.md) | 55-85 | 高级 |
| B17 | [FDE 业务发现工具箱](fde-discovery-kit.md) | [FD01](../curriculum/modules/17-fde-discovery-roi.md) | 25-40 | 中高级 |
| B18 | [企业 AI 上岗交付](enterprise-ai-deployment.md) | [FD02](../curriculum/modules/18-enterprise-capstone.md) | 120-180 | 毕业项目 |

## AI 方向实验室

| ID | 构建项目 | 对应课程 | 小时 | 难度 |
| --- | --- | --- | ---: | --- |
| B19 | [视觉与视频分析流水线](vision-video-pipeline.md) | [XCV](../curriculum/electives/computer-vision-multimodal.md) | 70-110 | 高级选修 |
| B20 | [实时语音助手](realtime-voice-assistant.md) | [XSP](../curriculum/electives/speech-audio.md) | 55-85 | 高级选修 |
| B21 | [微型扩散模型](diffusion-model.md) | [XGM](../curriculum/electives/generative-media-diffusion.md) | 70-110 | 高级选修 |
| B22 | [强化学习智能体](reinforcement-learning-agent.md) | [XRL](../curriculum/electives/reinforcement-learning-embodied.md) | 70-110 | 高级选修 |
| B23 | [推荐与预测实验室](recommender-forecast-lab.md) | [XRS](../curriculum/electives/recommender-time-series.md) | 50-80 | 高级选修 |
| B24 | [语言模型训练与对齐实验](lm-training-alignment.md) | [XLM](../curriculum/electives/lm-training-alignment.md) | 100-160 | 高级选修 |
| B25 | [论文复现实验包](paper-reproduction.md) | [XRE](../curriculum/electives/research-reproduction.md) | 45-90 | 高级选修 |
| B26 | [领域 AI 产品](domain-ai-product.md) | [XDS](../curriculum/electives/domain-ai-studio.md) | 90-140 | 高级选修 |
| B27 | [因果与实验实验室](causal-experiment-lab.md) | [XCA](../curriculum/electives/causal-inference-experimentation.md) | 45-70 | 高级选修 |
| B28 | [知识图谱与推理引擎](knowledge-graph-engine.md) | [XKG](../curriculum/electives/knowledge-graphs-neurosymbolic.md) | 50-80 | 高级选修 |
| B29 | [二维机器人闭环模拟器](robot-simulator.md) | [XRO](../curriculum/electives/robotics-embodied-systems.md) | 80-130 | 高级选修 |
| B30 | [AI 用例治理登记系统](ai-governance-registry.md) | [XGV](../curriculum/electives/ai-governance-society.md) | 35-55 | 高级选修 |

## 两遍构建法

### 第一遍：为了理解

- 限制高层框架，亲手实现关键算法、协议或状态机。
- 优先小数据、小模型和确定性测试。
- 目标是正确、可解释、能暴露失败，不追求生产规模。

### 第二遍：为了交付

- 使用成熟库、框架和 AI 编程工具。
- 增加权限、安全、性能、体验、监控和运维。
- 与第一遍比较：成熟工具替你承担了什么，又引入了什么边界。

## 项目毕业判据

一个项目只有同时满足以下条件才算完成：

- 能从空白描述关键接口和数据结构。
- 正常、边界、异常和故障测试均可重复。
- 能解释一个核心机制和一个失败机制。
- 能现场修改一个小行为并预测影响。
- 有成熟实现对照，而不是把教学实现冒充生产系统。
- 有真实用户任务或明确业务价值说明。

[返回完整课程地图](../../README.md#完整课程地图)
