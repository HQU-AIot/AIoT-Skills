import json
from pathlib import Path
from urllib.parse import urlparse

data = json.loads(Path("catalog.yaml").read_text(encoding="utf-8"))
required_root = {"version", "organization", "repository", "categories", "skills"}
missing_root = required_root - data.keys()
if missing_root:
    raise SystemExit(f"catalog.yaml 缺少根字段: {sorted(missing_root)}")

categories = data["categories"]
if not isinstance(categories, list) or not categories or len(categories) != len(set(categories)):
    raise SystemExit("categories 必须是非空且不重复的数组")

required_skill = {"name", "repository", "description", "author", "category", "platforms", "status", "license", "updated"}
allowed_status = {"experimental", "usable", "stable", "unmaintained"}
names = set()
repositories = set()

for index, skill in enumerate(data["skills"], start=1):
    missing = required_skill - skill.keys()
    if missing:
        raise SystemExit(f"第 {index} 个 Skill 缺少字段: {sorted(missing)}")
    if skill["name"] in names:
        raise SystemExit(f"Skill 名称重复: {skill['name']}")
    if skill["repository"] in repositories:
        raise SystemExit(f"仓库地址重复: {skill['repository']}")
    if skill["category"] not in categories:
        raise SystemExit(f"未知分类: {skill['category']}")
    if skill["status"] not in allowed_status:
        raise SystemExit(f"未知状态: {skill['status']}")
    parsed = urlparse(skill["repository"])
    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
        raise SystemExit(f"仓库地址必须是 GitHub HTTPS URL: {skill['repository']}")
    names.add(skill["name"])
    repositories.add(skill["repository"])

print(f"catalog.yaml 校验通过，共 {len(data['skills'])} 个 Skill")
