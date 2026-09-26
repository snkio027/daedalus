# Daedalus

> Agent-native Engineering Delivery System

Daedalus 将目标、工程知识、人、Agent、工具与计算资源组织起来，交付经过验证、可以使用和维护的软件能力。

系统以完整能力增量（Capability Increment）组织工作，在明确范围内自主执行、修复和恢复，并用可追溯证据支持集中验收。它负责工程交付协调；仓库现有 Git/GitHub Workflow 负责变更验证、审查、集成与发布。

## 当前状态

Architecture v0，设计草案。当前交付物是产品范围、领域关系、控制边界和验收场景，尚未实现执行器、CLI、持久化或 GitHub 集成。文档描述的目标能力不代表已经运行或验收通过。

## 阅读入口

| 文档 | 内容 |
| --- | --- |
| [产品目标与首个能力增量](docs/product.md) | 优化目标、项目边界、建设顺序与首个纵向切片 |
| [Architecture v0](docs/architecture.md) | Capability、Task、Execution、Evidence / Acceptance 的语义与关系 |
| [工程约定](docs/engineering.md) | 文档权威、项目开发与验证、外部 Workflow 基线及适配 |
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

接入一个已有交付工作流的仓库，从 Capability 和 Task 出发，解析上下文与策略，在隔离工作区中执行任务、调用仓库验证入口，形成 PR；观察现有工作流完成集成后，针对实际集成版本和所需制品进行能力级验收。

其中，形成可审查 PR 与结构化证据是中间检查点；完整切片的完成条件包含能力级验收。合并和发布由已有仓库工作流及有效授权控制。

## 设计来源

- 项目发起阶段的设计讨论：项目目标、命名、Daedalus Engineering Control Plane 与 Repository Delivery Plane 的边界，以及能力级验收要求。讨论中的有效设计已整理进本仓库，无需访问私人会话。
- 《Git & GitHub Engineering Workflow Best Practices》v1.0：外部仓库交付基线；版本、摘要和适用边界见 [工程约定](docs/engineering.md)。

本地文档应足以解释本项目设计；原始会话中的建议不自动成为已验证的平台能力或执行授权。
