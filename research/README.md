# AI Agent 研究雷达

## 目的

研究雷达帮助课程持续跟踪 Agent 架构、工具使用、规划、记忆、评测、安全、软件工程和企业部署的发展。

它不是“每日 AI 新闻”，也不把最新等同于最好。自动脚本负责发现候选，维护者负责判断证据，学习者通过复现实验把研究转化为能力。

## 文件

- `sources.json`：自动检索主题和关键词。
- `radar/latest.md`：每周自动生成的候选论文。
- `reading-list.md`：经过人工筛选的核心与前沿阅读。
- [教育资源观察库](education-source-watchlist.md)：大学课程、作者 GitHub 与教育检索工具候选。
- `paper-note-template.md`：深读、复现和课程转化模板。

## 更新节奏

- 每周：GitHub Actions 生成候选并创建 Pull Request。
- 每月：选择 1-2 篇深读，至少完成一个小实验。
- 每季度：评估是否更新方向专修。
- 每年：检查是否有足够证据影响稳定核心。

## 检索主题

- LLM Agent 的工具使用与规划
- 长程任务、状态、记忆与失败恢复
- Agent 评测、基准和线上可观测性
- RAG、知识工程和证据引用
- MCP、权限、隐私与工具安全
- Coding Agent 和软件工程
- 人机协作、FDE 和企业采用

## 手动运行

```powershell
python scripts\update_research_radar.py
```

脚本只使用 Python 标准库。网络不可用时不会修改正式阅读清单。
