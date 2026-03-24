#!/bin/bash
# 伐木累分析大师 - 一键发布脚本
# 批量发布到多个平台

set -e

PROJECT_DIR="$HOME/.openclaw/workspace/skills/soul-forge"
cd "$PROJECT_DIR"

echo "🚀 开始批量发布..."
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查 GitHub
echo "📦 检查 GitHub..."
if git remote -v > /dev/null 2>&1; then
    echo -e "${GREEN}✓ GitHub 已配置${NC}"
else
    echo -e "${RED}✗ GitHub 未配置${NC}"
fi

# 检查 PyPI
echo "📦 检查 PyPI..."
if pip3 show twine > /dev/null 2>&1; then
    echo -e "${GREEN}✓ twine 已安装${NC}"
else
    echo -e "${YELLOW}⚠ 安装 twine...${NC}"
    pip3 install twine build --break-system-packages
fi

if [ -f "dist/*.whl" ]; then
    echo -e "${GREEN}✓ 包已构建${NC}"
else
    echo -e "${YELLOW}⚠ 构建包...${NC}"
    python3 -m build
fi

# 检查 npm
echo "📦 检查 npm..."
if command -v npm > /dev/null 2>&1; then
    echo -e "${GREEN}✓ npm 可用${NC}"
else
    echo -e "${RED}✗ npm 未安装${NC}"
fi

echo ""
echo "📋 发布清单:"
echo "  [ ] PyPI - pip install family-analyzer"
echo "  [ ] npm - npm install -g family-analyzer"
echo "  [ ] Product Hunt (手动)"
echo "  [ ] V2EX (手动)"
echo "  [ ] Coze (手动)"
echo "  [ ] Dify (手动)"
echo ""

echo "🎯 下一步操作:"
echo ""
echo "1. PyPI 发布:"
echo "   export PYPI_API_TOKEN='your-token-here'"
echo "   python3 -m twine upload dist/* --username __token__ --password \$PYPI_API_TOKEN"
echo ""
echo "2. npm 发布:"
echo "   npm login"
echo "   npm publish --access public"
echo ""
echo "3. 手动发布到 Product Hunt, V2EX 等平台"
echo "   参考 SUBMISSIONS.md 中的模板"
echo ""
