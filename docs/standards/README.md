# 共享工程规范

这里集中维护供 Daedalus 与消费项目复用的公共开发规范。规范正文在本仓库版本管理和评审；[工程约定](../engineering.md) 记录 Daedalus 的采用决定与适配，消费仓库维护自己的构建、验证、CI、权限及发布配置。

| 文档 | 状态 | 原始字节 SHA-256 |
| --- | --- | --- |
| [Git & GitHub Engineering Workflow v1.1](git-github-workflow/v1.1.md) | 2026-10-24 已采用，替代 v1.0；线上实施与收益待验收 | `de77bfd55da3811ed553985db8d61938467a2a3b2c0215e225b607428b667a86` |
| [Git & GitHub Engineering Workflow v1.0](git-github-workflow/v1.0.md) | 历史归档，已被 v1.1 替代；保留原文及其历史元数据 | `ae53bb825f902e4814fb88840e1069966913cba9b37cad77c179258b391f773f` |

上述 Git/GitHub 两个版本均按原始字节迁入。历史版本用于追溯既有决定，不因文件内保留原始 Stable 状态就重新成为现行规范。

待评审专题：[云原生软件供应链安全工程指南](software-supply-chain-security/2026-edition-draft.md)，`2026-edition-draft` r2，**Proposed**。由 `uv-demo` 的原有指南整理，来源提交与原始摘要见正文；本版经过修订，不是原始字节归档。它补充构建、制品、来源证明和部署准入，不替代已采用的 Git/GitHub v1.1，也不代表实际控制已部署或通过运行验收。

待评审专题：[AI-Native 数据建模与平台组织架构](ai-native-data-modeling/v1.0-draft.md)，`v1.0-draft` r2，**Proposed**。由维护者提供的 `AN-DM-ARCH-001` v1.0 原文整合，保留 14 章、3 个附录与来源记录，补充现有契约适配和恢复边界。原文 SHA-256 为 `b1d122b91f1228686ff681424b882f7d83fc52ca40221024ef2e0756d97f211f`；整合版摘要如下，两者不可混用。

| 本仓库候选 | 完整文件 SHA-256 |
| --- | --- |
| [数据建模 v1.0-draft r2](ai-native-data-modeling/v1.0-draft.md) | `46f47808bfb48c57727cb27c2a2ba50112be2046d2a5729de8d136c6230e9396` |

数据专题服务消费项目的数据产品设计，不预先选择 Daedalus 的实现技术；其数据 Gate 与 M0–M3 不构成 G2 放行。收录、设计评审、项目采用和实际验收分别记录，未运行项保持 NOT RUN；它不改变 Git/GitHub v1.1 的已采用状态，也不将 Agent 工作流或供应链指南提升为已采用规范。

消费项目须记录本仓库地址、包含目标文档的完整 Git 提交 SHA、文档相对路径、文件摘要，以及自身采用范围和例外；执行环境实际读取并校验该对象。不能只跟随 main 或最新版本。集中维护文档不自动迁移消费项目，也不授予 CI、Ruleset、合并或发布权限。

已采用的 Frozen 版本不原地改写技术内容；后续修订另立版本，经评审和明确采用后更新索引。新增公共说明按实际复用需求归档；项目专用配置与运行证据保留在相应项目或任务，不集中复制。

跨 Agent 工作方法目前在 [Agent Engineering Workflow](../engineering.md#agent-engineering-workflow) 中形成 Proposed 候选，尚未发布为共享规范或经过实际任务验证。它补充任务输入、自主执行与交接方法，引用而不改写上述 v1.1；稳定后再按实际复用需求提取版本，保持单一正文来源。
