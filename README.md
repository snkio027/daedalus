# Daedalus

> Agent-native Engineering Delivery System

Daedalus 是一套能够持续交付优秀项目的完整工程系统：将值得解决的问题转化为经过验证、可以交付、能够维护的产品能力；尽可能减少等待、重复劳动和人工协调，同时持续提高产品与工程质量。

系统连接探索、交付和改进三个循环，以完整能力增量（Capability Increment）组织工作，实行批内自主修复和集中验收。人、模型、确定性工具、平台与计算资源按实际效果分工；Codex、GitHub、CI 和云平台都是可选择、可替换的组成部分。

自研的 Engineering Control Plane 承担必要的协调语义，现有仓库工作流承接变更验证、审查、集成与发布。实现范围可以逐步投入；目标架构覆盖从问题发现到运行反馈的完整系统。

## 当前状态

Architecture v0，设计草案。先审查完整目标架构，再按可验收的能力增量建设；尚未实现执行器、CLI、持久化或 GitHub 集成。文档、PR 和格式检查不代表架构已经接受或目标能力已经运行。

## 阅读入口

| 文档 | 内容 |
| --- | --- |
| [产品目标与首个能力增量](docs/product.md) | 优化目标、项目边界、建设顺序与首个纵向切片 |
| [Architecture v0](docs/architecture.md) | 三循环目标架构、资源与控制模型、验证、发布运行、反馈与核心领域语义 |
| [工程约定](docs/engineering.md) | 核心指南映射、G0 / G1 / G2 设计审查、项目验证与外部 Workflow 适配 |
| [架构决策入口](docs/adr/README.md) | 何时记录 ADR、怎样说明取舍与变更状态 |
| [Agent 工作入口](AGENTS.md) | 本仓库的上下文与交付约定 |

## 开始参与

从 `docs/product.md` 理解目标，再阅读 `docs/architecture.md` 的模型与开放问题。开发和验证要求见 `docs/engineering.md`；重要设计取舍按 `docs/adr/README.md` 记录。当前处于文档设计阶段，没有应用安装、构建或运行命令。

已有提交后的文档变更可先执行：

```bash
git status --short --branch
git diff --check
git diff --cached --check
```

这些 Git 检查不覆盖未跟踪文件，也不验证链接或架构语义；完整的文档检查范围见工程约定。

## 第一条纵向能力

接入一个已有交付工作流的真实项目，从问题、Capability 和 Task 出发，解析上下文与策略，执行并验证变更；通过现有工作流集成、形成可用制品，完成能力验收，并把实际使用反馈转化为后续判断。首个执行器与环境在切片绑定时核验。

可审查 PR 是中间检查点。首个切片是完整目标架构的最小实例，不能反过来限制产品范围；自动合并、常驻调度或统一平台不是它的前提。

## 设计来源

- 核心指南：项目发起者于 2026-09-26 提供的完整工程系统总体方案。目标、四维质量、三循环、自治方式和阶段建设原则以 [产品契约](docs/product.md) 为入口，逐项落点见 [工程约定](docs/engineering.md)；无需访问私人会话。
- 架构审阅意见：围绕 Identity、Lifecycle、Authority、Failure、Evidence 和 Recovery 检验模型；评审结论与待决事项记录在对应 PR / 任务中。
- 《Git & GitHub Engineering Workflow Best Practices》v1.0：外部仓库交付基线；版本、摘要和适用边界见 [工程约定](docs/engineering.md)。

本地文档应足以解释本项目设计；原始会话中的建议不自动成为已验证的平台能力或执行授权。
