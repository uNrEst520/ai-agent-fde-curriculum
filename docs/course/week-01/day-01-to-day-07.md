# Week 01 每日课程

## Day 1：把项目跑起来，先做产品观察

### 今日目标

你今天不学习复杂代码，只完成三件事：

1. 启动主项目。
2. 像用户一样体验页面。
3. 记录“我看到了什么”和“我还不知道什么”。

### 课前教程

- **必学，35 分钟：**Microsoft Learn [PowerShell 101 · Chapter 1](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started)
  - 只读 `What is PowerShell?`、`How to launch PowerShell`、`Execution policy` 和结尾 Review。
  - 学完要能解释：Shell、普通/管理员权限、执行策略分别是什么。

今天不看随机搜索结果，也不要求学脚本语法。只理解命令、参数、路径和“为什么这个脚本能被执行”。

### 实操任务

进入项目目录：

```powershell
cd "<PROJECT_ROOT>\网球视频识别"
```

启动项目：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-dev.ps1 -Restart
```

打开页面：

```text
http://127.0.0.1:5173
```

运行两个验证命令：

```powershell
npm run build
.\.server-venv\Scripts\python.exe -m pytest -p no:cacheprovider backend\tests\test_report.py
```

### 今天要看懂什么

- `cd` 是进入目录。
- 带引号的路径是因为路径里有中文或空格。
- `powershell -File` 是运行一个脚本文件。
- `npm run build` 是让前端项目做一次正式构建检查。
- `pytest` 是跑后端测试。

### 今日作业

写 300-500 字：

```text
我今天像用户一样体验了这个项目。页面上最重要的 3 个区域是：
1.
2.
3.

我认为这个项目解决的业务问题是：

我今天运行了这些命令：

其中我看懂的部分是：

我还不懂的部分是：
```

### 今日必须记住

```text
启动成功 ≠ 学会工程
能解释启动链路，才是工程学习的开始
```

## Day 2：PowerShell、路径与项目目录

### 今日目标

你今天要建立“项目是由很多文件夹分工合作”的意识。以后看任何项目，先看结构，不急着看代码。

### 课前教程

- **必学，35 分钟：**Microsoft Learn [PowerShell 101 · Chapter 2: The Help System](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/02-help-system)
  - 只练 `Get-Help`、`Get-Command`、`Get-Member`；其余部分略读。
- **选学，40 分钟：**MIT [The Missing Semester · Course Overview + The Shell](https://missing.csail.mit.edu/2020/course-shell/)
  - 只看 navigating in the shell、connecting programs 两部分。
  - 课程使用 Bash，重点比较“路径、当前目录、命令+参数”的共同模型，不照抄 Bash 命令到 PowerShell。

### 实操任务

在主项目目录运行：

```powershell
Get-ChildItem
```

查看前端目录：

```powershell
Get-ChildItem .\src
```

查看后端目录：

```powershell
Get-ChildItem .\backend\app
```

查看脚本目录：

```powershell
Get-ChildItem .\scripts
```

### 今天要看懂什么

你要把项目目录分成 5 类：

```text
src/              前端页面
backend/app/      后端接口和业务逻辑
backend/tests/    后端测试
scripts/          启动、检查、自动化脚本
package.json      前端命令入口
```

### 今日作业

画一张文字版目录地图：

```text
网球视频识别
├─ src：负责什么？
├─ backend/app：负责什么？
├─ backend/tests：负责什么？
├─ scripts：负责什么？
└─ package.json：负责什么？
```

再回答：

```text
如果我是新同事，我会先打开哪 3 个文件？为什么？
```

### 今日必须记住

```text
不会代码的人也可以先读目录
目录是工程项目的地图
```

## Day 3：Git/GitHub 与 README，学习“别人如何理解你的项目”

### 今日目标

今天你要理解：项目不只是代码，项目还需要被别人看懂。README、提交记录、测试命令，都是交付的一部分。

### 课前教程

- **必学并完成，45-60 分钟：**GitHub Skills [Introduction to GitHub](https://github.com/skills/introduction-to-github)
  - 在自己的账号复制练习仓库，依次完成 branch、commit、pull request、merge。
  - 不只阅读 README；出现自动反馈才算完成。
- **查漏，20 分钟：**GitHub Docs [Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)
  - 只复习 repository、branch、commit、pull request 四个词。

### 实操任务

在主项目目录运行：

```powershell
git status
```

查看 README：

```powershell
Get-Content .\README.md
```

查看可用命令：

```powershell
Get-Content .\package.json
```

### 今天要看懂什么

- `git status`：当前有哪些文件改动。
- `README.md`：项目给外人看的说明书。
- `package.json`：前端项目的命令菜单。
- 面试官不会只看代码，也会看你能不能写清“这个项目有什么价值”。

### 今日作业

写一版 1 分钟项目介绍：

```text
这个项目是一个 ______。
它服务的用户是 ______。
用户上传 ______ 后，系统会 ______。
目前已经具备的能力包括 ______。
如果要商业化，下一步应该补 ______。
```

### 今日必须记住

```text
README 是你的销售页，也是你的交付说明书
```

## Day 4：前端入口，理解用户动作如何变成请求

### 今日目标

今天不要求你学完 React。你只需要知道：用户点击、上传、选择目标后，前端如何把数据发给后端。

### 课前教程

- **必学，45 分钟：**React [Quick Start](https://react.dev/learn)
  - 只读 creating/nesting components、displaying data、responding to events、updating the screen。
  - 暂时跳过列表渲染、组件间共享数据和后续完整教程。
- **必学，30 分钟：**MDN [Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
  - 只读 making a request、setting a body、checking response status、reading JSON。
  - 学完后回到项目里给一次 `fetch` 标出 URL、method、body、response 四部分。

### 实操任务

打开文件：

```text
<PROJECT_ROOT>\网球视频识别\src\App.jsx
```

只搜索这些关键词：

```text
fetch
Report
TrainingPrescription
TrainingPlan
```

### 今天要看懂什么

你只回答 4 个问题：

```text
哪个组件负责展示报告？
哪个组件负责展示训练处方？
前端向哪个 API 发请求？
前端拿到 report 数据后放在哪里展示？
```

### 今日作业

画一条前端链路：

```text
用户动作
  -> 前端状态变化
  -> fetch 请求
  -> 等待后端结果
  -> 展示报告 / 训练处方
```

然后写：

```text
我现在还看不懂 React 的地方是：
但我已经看懂的用户链路是：
```

### 今日必须记住

```text
前端不是“页面美化”
前端负责把用户动作变成系统输入
```

## Day 5：FastAPI 与后端 API，理解请求如何变成结果

### 今日目标

今天你要看懂后端的“门口”在哪里。API 就是前端和后端对话的门。

### 课前教程

- **必学，45 分钟：**FastAPI [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
  - 跟着实现最小接口，重点理解 path operation、装饰器、返回 JSON。
  - 必须打开页面中的 `/docs` 示例，观察 Swagger UI 如何由 OpenAPI 自动生成。
- **项目对照，15 分钟：**打开当前项目自己的 `/docs`，只找本日列出的四个接口并展开请求/响应 schema。

### 实操任务

打开文件：

```text
<PROJECT_ROOT>\网球视频识别\backend\app\main.py
```

只找这些接口：

```text
POST /api/videos
POST /api/analysis
GET /api/analysis/{job_id}
GET /api/analysis/{job_id}/report.md
```

### 今天要看懂什么

你要能解释：

```text
/api/videos 负责什么？
/api/analysis 负责什么？
/api/analysis/{job_id} 为什么要用 job_id？
/report.md 为什么适合面试展示和客户交付？
```

### 今日作业

写一段后端链路说明：

```text
前端请求 ______ 接口后，后端会 ______。
后端用 job_id 代表 ______。
用户再次查询 ______ 时，系统返回 ______。
Markdown 报告适合交付，因为 ______。
```

### 今日必须记住

```text
API 是产品能力的边界
会讲 API，才开始会讲工程交付
```

## Day 6：测试与小改动，第一次摆脱 bypass

### 今日目标

今天你要让 Codex 帮你做一个非常小的改动，但你必须自己验收。重点不是改动本身，而是“我如何知道它没有改坏”。

### 课前教程

- **必学并动手，40 分钟：**pytest [Get Started](https://docs.pytest.org/en/stable/getting-started.html)
  - 完成 create your first test、run multiple tests、assert an exception 三部分。
  - 故意保留一次失败，先预测错误信息，再运行并核对。
- **项目对照，20 分钟：**阅读当前项目两个指定测试，写出每个测试的输入、动作和断言。

### 实操任务

打开文件：

```text
<PROJECT_ROOT>\网球视频识别\backend\tests\test_report.py
```

重点看：

```text
test_build_report_for_valid_attempt
test_build_report_exposes_training_prescription_for_stroke
```

然后让 Codex 做一个小改动，例如：

```text
把训练处方里的“Agent 决策链”文案改成“AI 决策链”，并同步更新相关测试。
```

改完后运行：

```powershell
.\.server-venv\Scripts\python.exe -m pytest -p no:cacheprovider backend\tests\test_report.py
npm run build
```

### 今天要看懂什么

- 测试不是给程序员看的仪式，而是你的验收工具。
- AI 可以写代码，但你要知道用什么证据证明它写对了。
- 小改动也要有业务理由、影响范围和验证结果。

### 今日作业

提交一份小改动记录：

```text
我让 Codex 改了什么：

为什么这个改动有必要：

改动涉及哪些文件：

我运行了哪些验证命令：

结果是否通过：

我担心的副作用是：
```

### 今日必须记住

```text
AI 可以替你写代码
但不能替你承担验收责任
```

## Day 7：FDE 式工程地图复盘

### 今日目标

今天你要把一周学习整理成一份可批改的交付物。这份作业不是学习笔记，而是“我能不能把一个 AI 项目讲清楚”的证据。

### 课前教程

- **必学，30 分钟：**Anthropic [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
  - 只读 `What are agents?`、`When (and when not) to use agents` 和 `Summary`。
  - 暂时跳过框架清单和各工作流实现细节。
- **提取任务，15 分钟：**写出 workflow 与 agent 的区别，以及“何时不该做 Agent”的两个判断条件。

今天看 Agent 资料只是预告，不需要学框架。你只要带着一个问题看：

```text
Agent 不是聊天机器人，而是围绕目标、工具、步骤和验收组成的工作流。
```

### 实操任务

根据 [作业提交模板](homework-template.md) 写 Week 1 复盘。

建议保存为：

```text
docs\weekly-reviews\week-01.md
```

### 今天要看懂什么

你要把项目讲成两条链路：

```text
业务链路：
网球学习者想改进动作
  -> 上传视频
  -> 得到动作问题和训练处方
  -> 下次训练按建议执行
  -> 再次拍摄验证

工程链路：
前端上传
  -> FastAPI 接口
  -> 视频/姿态分析
  -> report.py 生成报告
  -> 前端展示
  -> 测试验证关键字段
```

### 今日作业

完成 Week 1 最终作业，并准备向我提交。提交时可以直接说：

```text
请批改我的 Week 1 作业
```

然后附上你的复盘正文。

### 今日必须记住

```text
FDE 的第一步不是炫技
而是进入现场后，把业务流程、系统流程和验收标准讲清楚
```

