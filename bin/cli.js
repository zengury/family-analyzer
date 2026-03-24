#!/usr/bin/env node

/**
 * Family Analyzer CLI
 * 微信群聊行为分析工具
 */

const { execSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);

function showHelp() {
  console.log(`
伐木累分析大师 (Family Analyzer) v0.1.0

Usage:
  family-analyzer <command> [options]

Commands:
  parse <file>          解析微信聊天记录 JSON 文件
  analyze <file>        分析并生成人格画像
  help                  显示帮助信息

Examples:
  family-analyzer parse chat.json
  family-analyzer analyze chat.json

更多信息: https://github.com/zengury/family-analyzer
`);
}

function main() {
  if (args.length === 0 || args[0] === 'help' || args[0] === '--help' || args[0] === '-h') {
    showHelp();
    process.exit(0);
  }

  const command = args[0];
  const filePath = args[1];

  if (!filePath && command !== 'help') {
    console.error('Error: 请提供文件路径');
    showHelp();
    process.exit(1);
  }

  // 调用 Python CLI
  const pythonScript = path.join(__dirname, '..', 'pipeline', 'cli.py');
  
  try {
    execSync(`python3 "${pythonScript}" ${command} "${filePath}"`, {
      stdio: 'inherit',
      cwd: process.cwd()
    });
  } catch (error) {
    console.error('执行失败:', error.message);
    process.exit(1);
  }
}

main();
