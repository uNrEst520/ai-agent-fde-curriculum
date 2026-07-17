# Week 1：从 bypass 到看懂系统地图

> 完整第一周课程已经整理到 [docs/course/week-01/README.md](course/week-01/README.md)。  
> 本文件保留为快速启动版，适合你当天打开项目时快速查看命令和验收目标。

## 本周目标

你这周不用追求“会写完整项目”，目标只有一个：**能把主项目从用户操作到后端报告的完整链路讲清楚**。

本周结束时，你应该能用 5 分钟解释：

```text
用户上传网球动作视频
  -> 前端把视频和训练目标发给后端
  -> 后端保存文件并做视频预检/转码
  -> MediaPipe Pose 提取人体关键点
  -> report.py 把指标转成中文报告、训练计划和训练处方
  -> 前端报告页展示结果
  -> 用户导出 Markdown / 素材包 / 样本包
```

## 本周不做什么

- 不从零学完 JavaScript。
- 不从零学完 Python。
- 不重构项目。
- 不强行合并四个网球项目。
- 不追求完全手写代码。

只做一件事：**理解主项目的工程地图**。

## Day 1：跑起来

工作目录：

```powershell
cd "<PROJECT_ROOT>\网球视频识别"
```

启动项目：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-dev.ps1 -Restart
```

打开：

```text
http://127.0.0.1:5173
```

验证：

```powershell
npm run build
.\.server-venv\Scripts\python.exe -m pytest -p no:cacheprovider backend\tests\test_report.py
```

你要写下：

- 前端页面大概有哪些区域？
- 上传视频后页面发生了什么？
- 报告页有哪些模块？
- “AI 教练训练处方”出现在什么位置？

## Day 2：看前端入口

读这个文件：

```text
<PROJECT_ROOT>\网球视频识别\src\App.jsx
```

只找 4 个东西：

- `Report`：报告页怎么展示。
- `TrainingPrescription`：训练处方怎么展示。
- `TrainingPlan`：下一组训练怎么展示。
- `fetch`：前端怎么请求后端。

你不用逐行看懂，只需要能回答：

```text
哪个组件负责报告页？
哪个组件负责训练处方？
前端从哪里拿到 report 数据？
```

## Day 3：看后端 API

读这个文件：

```text
<PROJECT_ROOT>\网球视频识别\backend\app\main.py
```

只找 4 个接口：

- `POST /api/videos`
- `POST /api/analysis`
- `GET /api/analysis/{job_id}`
- `GET /api/analysis/{job_id}/report.md`

你要能解释：

```text
/api/videos 负责什么？
/api/analysis 负责什么？
/api/analysis/{job_id} 返回什么？
/report.md 为什么适合面试展示？
```

## Day 4：看报告生成

读这个文件：

```text
<PROJECT_ROOT>\网球视频识别\backend\app\report.py
```

重点看：

- `build_job_report`
- `build_generic_stroke_job_report`
- `build_training_plan`
- `build_training_prescription`
- `build_retake_prescription`

你要能解释：

```text
训练计划 training_plan 是怎么来的？
训练处方 training_prescription 比普通建议多了什么？
为什么它可以被讲成 Agent 决策层？
```

## Day 5：看测试

读这个文件：

```text
<PROJECT_ROOT>\网球视频识别\backend\tests\test_report.py
```

重点看新增的两个测试：

- `test_build_report_for_valid_attempt`
- `test_build_report_exposes_training_prescription_for_stroke`

你要能解释：

```text
测试在验证什么？
如果训练处方字段没生成，测试会怎么失败？
为什么测试能帮你摆脱 bypass？
```

## Day 6：做一个小改动

请让 Codex 帮你做一个非常小的改动，例如：

```text
把训练处方里的“Agent 决策链”文案改成“AI 决策链”，并更新测试或截图。
```

你必须自己完成 6 件事：

1. 说清这个改动解决什么表达问题。
2. 找到改动发生在哪个文件。
3. 跑测试。
4. 看浏览器或 smoke 截图。
5. 记录是否有副作用。
6. 写 5 行复盘。

## Day 7：写反 bypass 复盘

复制这个模板：

```text
<CURRICULUM_ROOT>\docs\weekly-anti-bypass-template.md
```

新建你的 Week 1 复盘：

```text
<CURRICULUM_ROOT>\docs\weekly-reviews\week-01.md
```

本周最重要的验收不是代码，而是你能不能写清楚：

```text
我现在理解了主项目的哪条数据流？
我还不懂哪里？
下周我要补哪个最小概念？
```

## Week 1 面试表达

你本周最终要练熟这段话：

```text
这个项目的主链路是：前端上传网球动作视频，FastAPI 后端保存并触发分析，MediaPipe Pose 提取人体关键点，report.py 把视觉指标转成中文报告、训练计划和训练处方，前端报告页再把这些结果展示给用户。训练处方不是简单文案，它把用户目标、视频证据、阶段弱项和训练规则组合成下一步行动，所以它是一个可解释的规则 Agent 决策层。
```

## 你可以问 Codex 的好问题

- 帮我用初学者能懂的话解释 `POST /api/analysis` 的数据流。
- 帮我画出 `training_prescription` 从生成到展示的链路。
- 帮我找出报告页里展示训练处方的组件。
- 帮我解释这个测试为什么能保护训练处方功能。
- 帮我把这段技术解释改成适合创始人听的版本。
