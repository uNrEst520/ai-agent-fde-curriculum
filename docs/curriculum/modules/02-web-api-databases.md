# SE02 · Web、API 与数据库

- **建议时长：**6 周 · 每周 12-15 小时
- **先修课程：**SE01
- **课程性质：**主线课
- **验收方式：**构建项目 + 交付任务 + 口试

## 为什么学

大多数 AI 产品都通过 Web、API 和数据库连接用户与模型。理解请求、状态和持久化，才能看懂前后端为何这样协作。

## 学习目标

- 从页面操作追踪到 HTTP 请求、后端函数和数据库记录
- 设计清晰的资源、状态码、数据模型和事务边界
- 区分浏览器、服务端、数据库各自负责什么

## 周计划

| 周 | 主题与实践 |
| --- | --- |
| 1 | HTML、CSS、JavaScript 与浏览器事件 |
| 2 | HTTP、JSON、Cookie、跨域和接口契约 |
| 3 | 用 socket/标准库实现最小 HTTP 服务 |
| 4 | FastAPI、验证、错误处理和自动接口文档 |
| 5 | SQL、关系模型、索引、事务与迁移 |
| 6 | 前后端联调、认证边界和完整 CRUD 项目 |

## 从零构建

[进入逐步构建指南](../../builds/http-web-service.md)

不依赖 Web 框架处理一次 HTTP 请求，手写解析、路由和响应；再用 SQL 实现持久化。

## 真实交付

使用 FastAPI 和关系数据库交付一个包含前端、API、数据迁移、测试和接口文档的小型应用。

## 主要资源

- [MDN Web 开发指南](https://developer.mozilla.org/en-US/docs/Learn_web_development)
- [FastAPI 官方教程](https://fastapi.tiangolo.com/tutorial/)
- [PostgreSQL 官方教程](https://www.postgresql.org/docs/current/tutorial.html)

资源用于建立主线，最新论文与工具变化从 [研究雷达](../../../research/README.md) 进入候选，不会未经验证直接替换稳定原理。

## 必交证据

- 用户操作到数据库的完整链路图
- API 契约与至少 20 个接口测试
- 一次事务或并发错误实验

## 反 bypass 口试

1. 刷新页面后哪些状态会消失，哪些不会？
2. 为什么接口返回 200 仍可能是错误设计？
3. 索引提高了什么，又付出了什么代价？

## 后续课程

DE01、AP01

[返回完整课程地图](../../../README.md#完整课程地图)
