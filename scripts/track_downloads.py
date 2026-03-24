#!/usr/bin/env python3
"""
伐木累分析大师 - 下载统计追踪器
每周自动收集各平台下载数据

Usage:
    python3 scripts/track_downloads.py
    python3 scripts/track_downloads.py --weekly-report
"""

import json
import argparse
import subprocess
import os
from pathlib import Path
from datetime import datetime, timedelta
import requests

# 项目配置
REPO = "zengury/family-analyzer"
PACKAGE_NAME = "family-analyzer"
STATS_DIR = Path(__file__).parent.parent / "stats"

def get_github_stats():
    """获取 GitHub 统计数据"""
    try:
        # Stars, Forks, Watchers
        url = f"https://api.github.com/repos/{REPO}"
        resp = requests.get(url, timeout=10)
        data = resp.json()
        return {
            "stars": data.get("stargazers_count", 0),
            "forks": data.get("forks_count", 0),
            "watchers": data.get("watchers_count", 0),
            "open_issues": data.get("open_issues_count", 0),
        }
    except Exception as e:
        print(f"GitHub API 错误: {e}")
        return {}

def get_pypi_stats():
    """获取 PyPI 下载统计 (需要 Google BigQuery 或第三方 API)"""
    # PyPI 官方不直接提供下载统计，需要用 pypistats 或 pepy.tech
    # 这里使用占位符
    try:
        # pepy.tech API
        url = f"https://api.pepy.tech/api/v2/projects/{PACKAGE_NAME}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return {
                "total_downloads": data.get("total_downloads", 0),
                "downloads_last_month": data.get("downloads_last_month", 0),
            }
    except:
        pass
    return {}

def get_npm_stats():
    """获取 npm 下载统计"""
    try:
        url = f"https://api.npmjs.org/downloads/point/last-week/{PACKAGE_NAME}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return {
                "weekly_downloads": data.get("downloads", 0),
            }
    except Exception as e:
        print(f"npm API 错误: {e}")
    return {}

def get_docker_stats():
    """获取 Docker Hub 统计"""
    try:
        url = f"https://hub.docker.com/v2/repositories/{REPO}/"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return {
                "pull_count": data.get("pull_count", 0),
                "star_count": data.get("star_count", 0),
            }
    except:
        pass
    return {}

def collect_all_stats():
    """收集所有平台数据"""
    stats = {
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "platforms": {}
    }
    
    print("🔍 正在收集统计数据...\n")
    
    # GitHub
    print("📦 GitHub...")
    gh = get_github_stats()
    if gh:
        stats["platforms"]["github"] = gh
        print(f"   ⭐ Stars: {gh.get('stars', 0)}")
        print(f"   🍴 Forks: {gh.get('forks', 0)}")
    
    # PyPI
    print("\n📦 PyPI...")
    pypi = get_pypi_stats()
    if pypi:
        stats["platforms"]["pypi"] = pypi
        print(f"   📥 Total: {pypi.get('total_downloads', 0)}")
    
    # npm
    print("\n📦 npm...")
    npm = get_npm_stats()
    if npm:
        stats["platforms"]["npm"] = npm
        print(f"   📥 Weekly: {npm.get('weekly_downloads', 0)}")
    
    # Docker
    print("\n📦 Docker Hub...")
    docker = get_docker_stats()
    if docker:
        stats["platforms"]["docker"] = docker
        print(f"   📥 Pulls: {docker.get('pull_count', 0)}")
    
    return stats

def save_stats(stats):
    """保存统计数据"""
    STATS_DIR.mkdir(exist_ok=True)
    
    # 按日期保存
    date_str = stats["date"]
    filepath = STATS_DIR / f"{date_str}.json"
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    # 更新最新统计
    latest_path = STATS_DIR / "latest.json"
    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 数据已保存: {filepath}")
    return filepath

def generate_weekly_report():
    """生成周报"""
    # 读取本周所有数据
    stats_files = sorted(STATS_DIR.glob("2026-*.json"))
    
    if len(stats_files) < 2:
        print("数据不足，无法生成周报")
        return
    
    # 对比本周 vs 上周
    latest = json.loads(stats_files[-1].read_text())
    previous = json.loads(stats_files[0].read_text())
    
    report = f"""# 📊 伐木累分析大师 - 周报

**统计周期**: {previous['date']} ~ {latest['date']}
**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M")}

## 📈 总体趋势

| 平台 | 上周 | 本周 | 增长 |
|-----|------|------|-----|
"""
    
    platforms = set(latest["platforms"].keys()) | set(previous["platforms"].keys())
    
    for platform in sorted(platforms):
        old_data = previous["platforms"].get(platform, {})
        new_data = latest["platforms"].get(platform, {})
        
        # 根据平台选择关键指标
        if platform == "github":
            old_val = old_data.get("stars", 0)
            new_val = new_data.get("stars", 0)
            metric = "⭐ Stars"
        elif platform == "pypi":
            old_val = old_data.get("total_downloads", 0)
            new_val = new_data.get("total_downloads", 0)
            metric = "📥 Downloads"
        elif platform == "npm":
            old_val = old_data.get("weekly_downloads", 0)
            new_val = new_data.get("weekly_downloads", 0)
            metric = "📥 Weekly"
        else:
            continue
        
        growth = new_val - old_val
        growth_pct = (growth / old_val * 100) if old_val > 0 else 0
        
        report += f"| {platform} ({metric}) | {old_val} | {new_val} | +{growth} ({growth_pct:+.1f}%) |\n"
    
    report += """
## 🎯 本周目标完成度

- [ ] GitHub Stars: 50/100
- [ ] PyPI Downloads: 100/500
- [ ] npm Downloads: 50/200
- [ ] 新平台发布: 3/5

## 📝 本周行动

1. 发布到 Product Hunt
2. 在 V2EX 发帖介绍
3. 更新文档和示例
4. 收集用户反馈

---
*自动生成 by track_downloads.py*
"""
    
    report_path = STATS_DIR / "weekly_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\n📄 周报已生成: {report_path}")
    return report_path

def main():
    parser = argparse.ArgumentParser(description="下载统计追踪器")
    parser.add_argument("--weekly-report", action="store_true", help="生成周报")
    parser.add_argument("--cron", action="store_true", help="定时模式（静默）")
    
    args = parser.parse_args()
    
    if args.weekly_report:
        generate_weekly_report()
    else:
        stats = collect_all_stats()
        save_stats(stats)
        
        if not args.cron:
            print("\n" + "="*50)
            print("💡 提示: 使用 --weekly-report 生成周报")
            print("📅 建议: 添加到 crontab 每周运行一次")
            print("="*50)

if __name__ == "__main__":
    main()
