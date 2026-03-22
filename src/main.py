"""GitHub Trending Top 10 每日报告 - 主入口"""

import sys
from datetime import datetime, timezone, timedelta

from scraper import fetch_trending, fetch_readme
from analyzer import analyze_all
from pdf_generator import generate_pdf


def main():
    # 使用美国东部时间作为日期
    et = timezone(timedelta(hours=-5))
    today = datetime.now(et).strftime("%Y-%m-%d")

    print(f"=== GitHub Trending Top 10 日报 ({today}) ===\n")

    # 1. 爬取 Trending 数据
    print("[1/3] 正在爬取 GitHub Trending 页面...")
    projects = fetch_trending()
    if not projects:
        print("错误：未能获取到任何 Trending 项目")
        sys.exit(1)
    print(f"  已获取 {len(projects)} 个项目\n")

    # 2. 获取 README 并进行 AI 分析
    print("[2/3] 正在获取 README 并生成 AI 分析...")
    readmes = []
    for p in projects:
        print(f"  获取 README：{p['full_name']} ...")
        readmes.append(fetch_readme(p["owner"], p["name"]))

    analyses = analyze_all(projects, readmes)
    print()

    # 3. 生成 PDF
    print("[3/3] 正在生成 PDF 报告...")
    output = generate_pdf(projects, analyses, today)
    print(f"\n完成！报告已保存到：{output}")


if __name__ == "__main__":
    main()
