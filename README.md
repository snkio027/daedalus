# Daedalus

> Agent-native Engineering Delivery System

Daedalus 是一套能够持续交付优秀项目的完整工程系统：将值得解决的问题转化为经过验证、可以交付、能够维护的产品能力；尽可能减少等待、重复劳动和人工协调，同时持续提高产品与工程质量。

系统连接探索、交付和改进三个循环，以完整能力增量（Capability Increment）组织工作，实行批内自主修复和集中验收。人、模型、确定性工具、平台与计算资源按实际效果分工；Codex、GitHub、CI 和云平台都是可选择、可替换的组成部分。

自研的 Engineering Control Plane 承担必要的协调语义，现有仓库工作流承接变更验证、审查、集成与发布。实现范围可以逐步投入；目标架构覆盖从问题发现到运行反馈的完整系统。

## 当前状态

Architecture v0 Design Baseline 已于 2026-09-26 经[维护者决定接受](https://github.com/snkio027/daedalus/pull/1#issuecomment-5846965755)。G0/G1 PASS；G2 未启动。尚未实现执行器、CLI、持久化或 GitHub 集成，也没有控制面实现验证、运行恢复测试或生产就绪结论。本仓库提供文档及本地文档维护检查；检查器测试不构成系统实现或 G2 验收。

## 阅读入口

| 使用目的 | 阅读路径 |
| --- | --- |
| 在我的项目采用共享内容 | [内容目录](docs/standards/README.md#选择内容) → [采用方式](docs/standards/README.md#消费项目怎样采用) → 消费项目自己的入口与工程配置 |
| 参与开发 Daedalus | [产品契约](docs/product.md) → [架构问题导航](docs/architecture.md#按问题阅读) → [本仓库工程约定](docs/engineering.md) |

消费项目选择固定版本并自行决定采用；目前没有 Daedalus 产品安装或运行入口。准备中的消费者与任务见下列 G2 方案，方案本身不放行执行。

| 文档 | 内容 |
| --- | --- |
| [产品目标与首个能力增量](docs/product.md) | 优化目标、项目边界、建设顺序与首个纵向切片 |
| [Architecture v0](docs/architecture.md) | 三循环目标架构、资源与控制模型、验证、发布运行、反馈与核心领域语义 |
| [工程约定](docs/engineering.md) | Daedalus 自身的设计审查、本地验证与规范采用关系 |
| [Agent 工程工作流](docs/agent-workflow.md) | Proposed：跨 Agent 的任务、执行、交接与恢复方法 |
| [消费项目接入与 G2 准备方案](docs/plans/consumer-adoption-g2.md) | Proposed：消费入口、真实候选任务、G2 绑定与工具适配评估；不代表实现放行 |
| [共享工程规范](docs/standards/README.md) | 集中维护的公共开发规范、固定版本与消费仓库采用边界 |
| [需求、设计与验证衔接方法](docs/standards/requirements-design-verification/v0.1-draft.md) | Proposed：复用固定知识源，连接能力定义、方案取舍与有效检查；待真实任务校准 |
| [供应链安全指南](docs/standards/software-supply-chain-security/2026-edition-draft.md) | Proposed 专题：构建、制品、证据、身份与部署准入；尚未采用或运行验收 |
| [架构决策入口](docs/adr/README.md) | 何时记录 ADR、怎样说明取舍与变更状态 |
| [Agent 工作入口](AGENTS.md) | 本仓库的上下文与交付约定 |

## 开始参与

从 `docs/product.md` 理解目标，再阅读 `docs/architecture.md` 的模型与开放问题。开发和验证要求见 `docs/engineering.md`；重要设计取舍按 `docs/adr/README.md` 记录。当前处于文档设计阶段，没有应用安装、构建或运行命令。

已有提交后的文档变更可先执行：

```bash
git status --short --branch
./scripts/check-docs
git diff --check
git diff --cached --check
```

文档检查入口需要 Python 3.10+ 和 Git，覆盖未忽略的未跟踪 Markdown；Git 空白检查作为补充。检查器本身变更时还需运行失败场景测试，范围与命令见[工程约定](docs/engineering.md#文档阶段的验证)。本地检查不验证架构语义或线上门禁。

## 第一条纵向能力

接入一个已有交付工作流的真实项目，从问题、Capability 和 Task 出发，解析上下文与策略，执行并验证变更；通过现有工作流集成、形成可用制品，完成能力验收，并把实际使用反馈转化为后续判断。首个执行器与环境在切片绑定时核验。

可审查 PR 是中间检查点。首个切片是完整目标架构的最小实例，不能反过来限制产品范围；自动合并、常驻调度或统一平台不是它的前提。

## 设计来源

- 核心指南：项目发起者于 2026-09-26 提供的完整工程系统总体方案。目标、四维质量、三循环、自治方式和阶段建设原则以 [产品契约](docs/product.md) 为入口，逐项落点见 [工程约定](docs/engineering.md)；无需访问私人会话。
- 架构审阅意见：围绕 Identity、Lifecycle、Authority、Failure、Evidence 和 Recovery 检验模型；评审结论与待决事项记录在对应 PR / 任务中。
- [《Git & GitHub Engineering Workflow Best Practices》v1.1](docs/standards/git-github-workflow/v1.1.md)：2026-10-24 经维护者批准替代 v1.0，正文在本仓库集中维护；版本、摘要和适用边界见 [工程约定](docs/engineering.md)。规范采用不代表线上实施或运行验收完成。

本地文档应足以解释本项目设计；原始会话中的建议不自动成为已验证的平台能力或执行授权。
