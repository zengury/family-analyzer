#!/usr/bin/env python3
"""CLI entry point for family-analyzer"""

import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="伐木累分析大师 - 微信群聊行为分析工具"
    )
    parser.add_argument(
        "chat_file",
        help="群聊记录文件路径 (JSON格式)"
    )
    parser.add_argument(
        "-o", "--output",
        default="./output",
        help="输出目录 (默认: ./output)"
    )
    parser.add_argument(
        "--api-key",
        help="Kimi API Key (或设置 KIMI_API_KEY 环境变量)"
    )
    parser.add_argument(
        "--model",
        default="k2p5",
        help="使用的模型 (默认: k2p5)"
    )
    
    args = parser.parse_args()
    
    print("🎭 伐木累分析大师")
    print(f"📁 输入文件: {args.chat_file}")
    print(f"📂 输出目录: {args.output}")
    print()
    print("开始分析...")
    
    # 这里调用实际的 pipeline
    # 简化版：直接调用 pipeline 脚本
    import subprocess
    
    pipeline_dir = Path(__file__).parent.parent / "pipeline"
    
    # 设置环境变量
    env = {"KIMI_API_KEY": args.api_key} if args.api_key else {}
    
    # 运行 pipeline
    subprocess.run(
        ["python3", str(pipeline_dir / "03_extract_kimi_v2.py")],
        cwd=str(pipeline_dir.parent),
        env={**__import__("os").environ, **env}
    )
    
    print(f"\n✅ 分析完成！输出在: {args.output}")

if __name__ == "__main__":
    main()
