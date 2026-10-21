# Skill 规范

## 基本结构

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
├── references/
├── assets/
├── LICENSE
└── README.md
```

`SKILL.md`、`README.md` 和 `LICENSE` 为最低要求，其余目录按实际需要添加，不创建空目录。

## 命名

- Skill 名称使用小写字母、数字和连字符，且不超过 64 个字符。
- 仓库推荐命名为 `skill-功能名称`。
- 名称应能直接说明功能，避免宽泛的 `tools`、`helper` 等名称。

## SKILL.md

frontmatter 至少包含：

```yaml
---
name: example-skill
description: 说明 Skill 做什么、何时使用，以及容易混淆时何时不使用。
---
```

正文只保留影响执行质量的流程、约束和判断标准。较长的格式说明、领域资料或示例放入 `references/`；重复执行且需要确定性的操作放入 `scripts/`。

## README

README 至少说明功能与适用场景、安装位置、最小使用示例、工具与权限、脚本行为、作者、维护状态和许可证。

## 审核标准

1. 能否被正确触发且不会误导其他任务。
2. 指令是否简洁、明确并保持用户授权边界。
3. 是否存在秘密信息、隐私或许可证风险。
4. 脚本是否可读、可复现并具有合理停止条件。
5. 示例是否能完成一次最小可用测试。
