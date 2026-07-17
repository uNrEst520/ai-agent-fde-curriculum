# XRL · 强化学习与具身智能基础

- **建议时长：**8 周 · 每周 12-15 小时
- **先修课程：**ML01、DL01
- **课程性质：**兴趣选修
- **验收方式：**从零构建 + 方向项目 + 口试

## 方向目标

学习智能体如何通过环境反馈学习决策，并理解奖励设计、探索、离线数据、安全和仿真到现实的边界。

## 周计划

| 周 | 主题与实践 |
| --- | --- |
| 1 | MDP、状态、动作、奖励与回报 |
| 2 | 动态规划与 Bellman 方程 |
| 3 | Monte Carlo、TD 和 Q-learning |
| 4 | 函数逼近与 DQN |
| 5 | 策略梯度、actor-critic 与稳定性 |
| 6 | 离线 RL、模仿学习和偏好学习 |
| 7 | 环境、传感、控制、仿真到现实与安全 |
| 8 | 环境基准、训练曲线和策略评测 |

## 从零构建

[进入逐步构建指南](../../builds/reinforcement-learning-agent.md)

实现 Gridworld 环境、动态规划、Q-learning 和 DQN，记录随机种子、学习曲线和策略行为。

## 真实交付

在标准或自建环境解决一个控制任务，报告奖励黑客、分布变化、安全约束和可重复性。

## 主要资源

- [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/)
- [Spinning Up in Deep RL](https://spinningup.openai.com/)
- [Gymnasium 文档](https://gymnasium.farama.org/)

最新论文只从 [研究雷达](../../../research/README.md) 进入候选，经最小复现和课程 RFC 后才成为正式必修内容。

## 必交证据

- 可运行代码与可复现实验环境
- 基线、切片指标、失败样本和风险记录
- 面向用户或业务负责人的演示与价值说明

## 反 bypass 口试

1. 奖励提高为什么可能意味着策略变坏？
2. on-policy 与 off-policy 的数据使用有何不同？
3. 仿真环境遗漏的变量如何伤害真实部署？

[返回兴趣选修表](../../../README.md#兴趣选修)
