# 贡献指南

本仓库只维护索引与规范。每个 Skill 应放在独立仓库中，由作者自行维护。

## 提交前检查

- 仓库位于 HQU-AIoT 组织并设为公开。
- 仓库名称推荐使用 `skill-功能名称`。
- 至少包含 `SKILL.md`、`README.md` 和 `LICENSE`。
- `SKILL.md` 的 YAML frontmatter 至少包含 `name` 和 `description`。
- README 说明功能、适用场景、安装方法和一个最小示例。
- 已移除 Token、密码、Cookie、个人信息及无权公开的材料。
- 可执行脚本的网络访问、文件修改和高风险操作已经明确说明。
- 已在干净环境中完成一次自测。

## 提交流程

1. 创建 Skill 收录申请 Issue。
2. 维护者检查结构、安全性、许可证和最小可用示例。
3. 需要修改时，作者在自己的仓库中更新并回复 Issue。
4. 审核通过后，由维护者更新 `README.md` 和 `catalog.yaml`。
5. Skill 有重大变更、停止维护或仓库迁移时，请再次提交 Issue。

## 索引字段

每个条目应包含 `name`、`repository`、`description`、`author`、`category`、`platforms`、`status`、`license` 和 `updated`。状态使用 `experimental`、`usable`、`stable` 或 `unmaintained`；日期格式使用 `YYYY-MM-DD`。

修改索引时请提交 Pull Request，不要直接改动他人的 Skill 仓库。
