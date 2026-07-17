# SE01 · Python 与计算思维

- **建议时长：**6 周 · 每周 12-15 小时
- **先修课程：**O00
- **课程性质：**主线课
- **验收方式：**CS50P 精选作业 + 构建项目 + 口试

## 为什么学

Python 是 AI 工程最常见的胶水语言。重点不是背语法，而是学会把模糊任务拆成数据、状态、函数、边界和测试。

## 学习目标

- 阅读并追踪中小型 Python 程序
- 使用数据结构、函数、模块、异常和类型表达问题
- 独立定位输入、状态和边界条件导致的错误
- 能向 Codex 描述改动，并用测试而不是“看起来能跑”完成验收

## 主课与使用方式

**主课：**Harvard CS50P [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)。

CS50P 提供完整讲座、讲义、字幕、源代码和 Problem Sets。本课程不要求按原课十周全部完成，而是把最相关内容压缩成六周；每周只做下表列出的精选作业，再把知识迁移到自己的命令行数据应用。

## 周计划

| 周 | 必学内容 | 精选外部作业 | 本课程迁移任务 | 建议用时 |
| --- | --- | --- | --- | ---: |
| 1 | [Week 0: Functions, Variables](https://cs50.harvard.edu/python/weeks/0/) | [Einstein](https://cs50.harvard.edu/python/psets/0/einstein/)、[Tip Calculator](https://cs50.harvard.edu/python/psets/0/tip/) | 实现单位转换器；闭卷解释参数、返回值、作用域 | 12-14 小时 |
| 2 | [Week 1: Conditionals](https://cs50.harvard.edu/python/weeks/1/) + [Week 2: Loops](https://cs50.harvard.edu/python/weeks/2/) | [Meal Time](https://cs50.harvard.edu/python/psets/1/meal/)、[twttr](https://cs50.harvard.edu/python/psets/2/twttr/)、[Vanity Plates](https://cs50.harvard.edu/python/psets/2/plates/) | 把网球训练规则写成分支/循环规则引擎 | 13-15 小时 |
| 3 | [Week 3: Exceptions](https://cs50.harvard.edu/python/weeks/3/) + [Week 4: Libraries](https://cs50.harvard.edu/python/weeks/4/) | [Fuel Gauge](https://cs50.harvard.edu/python/psets/3/fuel/)、[Outdated](https://cs50.harvard.edu/python/psets/3/outdated/)、[Little Professor](https://cs50.harvard.edu/python/psets/4/professor/) | 为错误输入设计提示、重试和日志；记录三类失败 | 13-15 小时 |
| 4 | [Week 5: Unit Tests](https://cs50.harvard.edu/python/weeks/5/) + pytest [Get Started](https://docs.pytest.org/en/stable/getting-started.html) | [Testing my twttr](https://cs50.harvard.edu/python/psets/5/test_twttr/)、[Refueling](https://cs50.harvard.edu/python/psets/5/test_fuel/) | 给 CLI 项目写至少 20 个测试，覆盖正常、边界和失败输入 | 12-14 小时 |
| 5 | [Week 6: File I/O](https://cs50.harvard.edu/python/weeks/6/) + [Week 8: OOP](https://cs50.harvard.edu/python/weeks/8/) | [Scourgify](https://cs50.harvard.edu/python/psets/6/scourgify/)、[Cookie Jar](https://cs50.harvard.edu/python/psets/8/jar/) | 读取 CSV/JSON，拆分模块，用类建模一个任务队列 | 13-15 小时 |
| 6 | [Week 9: Et Cetera](https://cs50.harvard.edu/python/weeks/9/) 的类型提示、文档字符串与打包部分 | 不另做 CS50P Final Project | 完成[命令行数据应用](../../builds/cli-data-app.md)，补到 30 个测试并做 5 分钟演示 | 12-15 小时 |

## 明确跳过什么

- Week 7 Regular Expressions 暂不作为必修；在后续文本处理或日志解析需要时再回看。
- 每个 Problem Set 中未列出的题目均为选做，不为“刷完课程”牺牲迁移项目。
- Python 官方教程不是第二门主课，不从头通读。遇到概念不清时只查：
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
  - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  - [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
  - [Classes](https://docs.python.org/3/tutorial/classes.html)

## 为什么选 CS50P

- Harvard 提供免费、稳定、可直接定位到周和题目的公开内容。
- 每个概念后都有可自动检查的作业，适合防止“只看视频、没有写过”。
- 课程使用 Python 标准能力，不会过早把理解藏在 AI 框架后面。
- 现成 Problem Sets 负责基础训练，本仓库项目负责迁移到 AI/FDE 真实场景。

## AI 使用边界

| 环节 | 可以使用 Codex | 必须亲自完成 |
| --- | --- | --- |
| 听课与笔记 | 解释陌生概念、生成反例 | 闭卷写概念卡，自己预测代码输出 |
| 外部作业 | 解释报错、提示测试思路 | 第一版方案和核心函数；遵守 CS50 的 Academic Honesty 规则 |
| 迁移项目 | 讨论架构、审查代码、补测试建议 | 逐文件解释、主动注入失败、验收结果 |
| 口试 | 用 AI 模拟提问 | 关闭 AI 后回答并现场修改 |

## 从零构建

[进入逐步构建指南](../../builds/cli-data-app.md)

只使用标准库构建一个命令行数据应用，并亲手写一个最小断言测试器。

## 真实交付

把应用升级为有配置、日志、错误提示、自动测试和使用说明的可交付工具。

## 必交证据

- 精选 CS50P 作业的完成记录，不提交或公开课程答案
- 至少 30 个自己能解释的自动测试
- 三类失败输入和修复记录
- 闭卷重写一个核心模块
- 一段 5 分钟演示：业务问题、输入输出、错误边界、验证证据

## 反 bypass 口试

1. 列表、集合和字典的选择会如何影响行为与性能？
2. 异常应在哪里捕获，为什么？
3. 如何证明一个重构没有改变外部行为？
4. 给你一个失败测试时，如何区分测试错了、实现错了还是需求不清？

## 资源状态

- 本课链接与访问方式最后核验：2026-07-17。
- 结构化记录见[资源目录](../../resources/catalog.json)。
- 若主课不可访问，不自行搜索随机替代课，先按[资源替换规则](../../resources/README.md#资源失效或收费时怎么办)处理。

## 后续课程

SE02、SE03、SE04、AI01、AI02

[返回完整课程地图](../../../README.md#完整课程地图)
