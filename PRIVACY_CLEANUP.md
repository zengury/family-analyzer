# 隐私清理清单 - family-analyzer

## 🔴 必须删除的文件（含真实隐私数据）

```bash
# 原始聊天记录
data/raw/群聊_修身，齐家，尝小烹@深圳.json

# 处理中间产物  
data/parsed/messages.jsonl
data/denoised/chunks.jsonl
data/extracted/*
data/observations/*

# 生成的分析报告（含成员ID和昵称）
outputs/soul.md
```

## 🛡️ 添加到 .gitignore

```gitignore
# 数据目录（所有用户数据）
data/
outputs/
*.json
*.jsonl

# 打包文件
dist/
*.tgz
*.tar.gz
*.egg-info/

# 其他
__pycache__/
.DS_Store
```

## ✅ 保留的安全文件

- `pipeline/` - 处理脚本（无数据）
- `prompts/` - AI提示词模板
- `scripts/` - 工具脚本
- `SKILL.md` - 使用说明
- `README.md` - 项目文档
- `requirements.txt` - 依赖

## 📝 清理后提交

```bash
git rm -r --cached data/ outputs/ *.tgz
git add .gitignore
git commit -m "Remove private data and add .gitignore"
git push
```

## ⚠️ 如果已推送到GitHub

由于Git历史会保留文件，需要：
1. 使用 BFG Repo-Cleaner 或 git-filter-branch 彻底清除历史
2. 或删除仓库重新创建

参考: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
