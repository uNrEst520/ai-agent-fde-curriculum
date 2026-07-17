# LM01 · Transformer 与语言模型

- **建议时长：**8 周 · 每周 12-15 小时
- **先修课程：**DL01、SE04
- **课程性质：**主线课
- **验收方式：**构建项目 + 交付任务 + 口试

## 为什么学

理解 tokenizer、注意力、训练目标、推理缓存和评测，才能跨模型与框架做可靠判断，而不是把模型能力当作不可解释的黑箱。

## 学习目标

- 解释文本如何变成 token、向量、概率与输出
- 实现并训练一个微型 Transformer 语言模型
- 分析数据、规模、推理策略和系统约束对能力的影响

## 周计划

| 周 | 主题与实践 |
| --- | --- |
| 1 | 语言建模、n-gram、tokenization 与数据集 |
| 2 | embedding、位置、注意力与掩码 |
| 3 | 多头注意力、残差、归一化与 Transformer block |
| 4 | 训练目标、优化、检查点和实验追踪 |
| 5 | 采样、温度、top-k/p、KV cache 与推理 |
| 6 | 预训练数据、扩展规律、MoE 与效率直觉 |
| 7 | 指令微调、偏好对齐与安全概览 |
| 8 | 端到端微型语言模型与评测 |

## 从零构建

实现 BPE 或等价 tokenizer、因果注意力、Transformer block、训练循环和生成器，在小数据集上训练可运行模型。

## 真实交付

使用成熟开源组件完成一个可复现实验，报告数据、参数、算力、损失、任务评测和已知失败。

## 主要资源

- [Stanford CS336: Language Modeling from Scratch](https://stanford-cs336.github.io/)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [nanoGPT](https://github.com/karpathy/nanoGPT)

资源用于建立主线，最新论文与工具变化从 [研究雷达](../../../research/README.md) 进入候选，不会未经验证直接替换稳定原理。

## 必交证据

- 自实现组件的形状和梯度测试
- 不同采样策略的对照报告
- 数据、训练与推理成本账单

## 反 bypass 口试

1. 因果掩码阻止了什么信息泄漏？
2. KV cache 用空间换取了什么？
3. 困惑度下降为何不一定改善用户任务？

## 后续课程

AP01、XLM

[返回完整课程地图](../../../README.md#完整课程地图)
