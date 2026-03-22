"""GitHub Trending Top 10 每日报告 - 主入口"""

import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from scraper import fetch_trending, fetch_readme
from analyzer import analyze_all
from pdf_generator import generate_pdf

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"


def load_yesterday_data(today: str) -> dict[str, dict]:
    """加载昨天的 JSON 数据用于趋势对比。"""
    from datetime import timedelta
    yesterday = (datetime.strptime(today, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    json_path = REPORTS_DIR / f"{yesterday}.json"
    if json_path.exists():
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        return {p["full_name"]: p for p in data.get("projects", [])}
    return {}


def enrich_with_trends(projects: list[dict], yesterday_data: dict[str, dict]) -> list[dict]:
    """为每个项目添加趋势信息：是否新上榜、连续上榜天数。"""
    for p in projects:
        name = p["full_name"]
        if name in yesterday_data:
            prev = yesterday_data[name]
            p["is_new"] = False
            p["streak_days"] = prev.get("streak_days", 1) + 1
        else:
            p["is_new"] = True
            p["streak_days"] = 1
    return projects


def save_json(projects: list[dict], analyses: list[str], date: str) -> str:
    """保存原始数据为 JSON 文件。"""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "date": date,
        "generated_at": datetime.now(ZoneInfo("America/New_York")).isoformat(),
        "projects": projects,
        "analyses": analyses,
    }
    path = REPORTS_DIR / f"{date}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  JSON 已保存：{path}")
    return str(path)


def update_readme(projects: list[dict], date: str):
    """自动更新仓库 README.md，展示最新 Top 10。"""
    readme_path = Path(__file__).resolve().parent.parent / "README.md"
    lines = [
        "# GitHub Trending Top 10",
        "",
        "每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。",
        "",
        "## 工作原理",
        "",
        "1. 每天美东 6:00 AM 由 GitHub Actions 自动触发",
        "2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目",
        "3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析",
        "4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录",
        "",
        f"## 今日榜单（{date}）",
        "",
        "| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |",
        "| :---: | --- | :---: | ---: | ---: | :---: |",
    ]
    for i, p in enumerate(projects, 1):
        status = "NEW" if p.get("is_new") else f"🔥 {p.get('streak_days', 1)}天"
        lines.append(
            f"| {i} | [{p['full_name']}]({p['url']}) | {p['language']} "
            f"| {p['total_stars']:,} | +{p['today_stars']:,} | {status} |"
        )
    lines.extend([
        "",
        f"📄 [查看完整 PDF 报告](reports/{date}.pdf)",
        "",
        "## 历史报告",
        "",
        "所有历史报告保存在 [`reports/`](reports/) 目录中。",
        "",
        "---",
        "",
        "*由 GitHub Actions + DeepSeek AI 自动生成*",
        "",
    ])
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  README.md 已更新")


def main():
    # 使用美国东部时间（自动处理夏令时）
    today = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")

    print(f"=== GitHub Trending Top 10 日报 ({today}) ===\n")

    # 1. 爬取 Trending 数据
    print("[1/5] 正在爬取 GitHub Trending 页面...")
    projects = fetch_trending()
    if not projects:
        print("错误：未能获取到任何 Trending 项目")
        sys.exit(1)
    print(f"  已获取 {len(projects)} 个项目\n")

    # 2. 趋势对比
    print("[2/5] 正在对比历史数据...")
    yesterday_data = load_yesterday_data(today)
    projects = enrich_with_trends(projects, yesterday_data)
    new_count = sum(1 for p in projects if p.get("is_new"))
    print(f"  新上榜：{new_count} 个，连续上榜：{len(projects) - new_count} 个\n")

    # 3. 获取 README 并进行 AI 分析
    print("[3/5] 正在获取 README 并生成 AI 分析...")
    readmes = []
    for p in projects:
        print(f"  获取 README：{p['full_name']} ...")
        readmes.append(fetch_readme(p["owner"], p["name"]))

    analyses = analyze_all(projects, readmes)
    print()

    # 4. 保存数据并生成 PDF
    print("[4/5] 正在保存数据并生成 PDF 报告...")
    save_json(projects, analyses, today)
    output = generate_pdf(projects, analyses, today)

    # 5. 更新 README
    print("[5/5] 正在更新 README.md...")
    update_readme(projects, today)

    print(f"\n完成！报告已保存到：{output}")


if __name__ == "__main__":
    main()
