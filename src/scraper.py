"""GitHub Trending 页面爬虫模块"""

import requests
from bs4 import BeautifulSoup


def fetch_trending(language: str = "", since: str = "daily") -> list[dict]:
    """爬取 GitHub Trending 页面，返回前 10 个项目信息。

    Args:
        language: 编程语言筛选，默认为全部语言
        since: 时间范围 (daily/weekly/monthly)

    Returns:
        包含项目信息的字典列表
    """
    url = f"https://github.com/trending/{language}"
    params = {"since": since}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(url, params=params, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("article.Box-row")

    projects = []
    for article in articles[:10]:
        project = _parse_article(article)
        if project:
            projects.append(project)

    return projects


def _parse_article(article) -> dict | None:
    """解析单个项目的 HTML 元素。"""
    try:
        # 项目名称和链接
        h2 = article.select_one("h2 a")
        if not h2:
            return None
        repo_path = h2.get("href", "").strip("/")
        parts = repo_path.split("/")
        if len(parts) < 2:
            return None
        owner, name = parts[0], parts[1]

        # 项目描述
        desc_tag = article.select_one("p")
        description = desc_tag.get_text(strip=True) if desc_tag else ""

        # 编程语言
        lang_tag = article.select_one("[itemprop='programmingLanguage']")
        language = lang_tag.get_text(strip=True) if lang_tag else "Unknown"

        # 语言颜色
        lang_color_tag = article.select_one(".repo-language-color")
        lang_color = ""
        if lang_color_tag:
            style = lang_color_tag.get("style", "")
            if "background-color:" in style:
                lang_color = style.split("background-color:")[-1].strip().rstrip(";")

        # 总星标数
        stars_tag = article.select_one("a[href$='/stargazers']")
        total_stars = _parse_number(stars_tag.get_text(strip=True)) if stars_tag else 0

        # 总 Fork 数
        forks_tag = article.select_one("a[href$='/forks']")
        total_forks = _parse_number(forks_tag.get_text(strip=True)) if forks_tag else 0

        # 今日新增星标
        today_stars_tag = article.select_one("span.d-inline-block.float-sm-right")
        today_stars = 0
        if today_stars_tag:
            today_stars = _parse_number(today_stars_tag.get_text(strip=True))

        return {
            "owner": owner,
            "name": name,
            "full_name": f"{owner}/{name}",
            "url": f"https://github.com/{owner}/{name}",
            "description": description,
            "language": language,
            "language_color": lang_color,
            "total_stars": total_stars,
            "total_forks": total_forks,
            "today_stars": today_stars,
        }
    except Exception:
        return None


def fetch_readme(owner: str, name: str) -> str:
    """通过 GitHub API 获取项目的 README 内容。"""
    url = f"https://api.github.com/repos/{owner}/{name}/readme"
    headers = {
        "Accept": "application/vnd.github.v3.raw",
        "User-Agent": "GitHub-Trending-Bot",
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        readme = response.text
        # 截断过长的 README，避免 API 调用过贵
        if len(readme) > 5000:
            readme = readme[:5000] + "\n\n... (内容已截断)"
        return readme
    except requests.RequestException:
        return "无法获取 README 内容"


def _parse_number(text: str) -> int:
    """解析带逗号或 k 后缀的数字。"""
    text = text.strip().replace(",", "")
    # 提取数字部分
    num_str = ""
    for ch in text:
        if ch.isdigit() or ch == ".":
            num_str += ch
    if not num_str:
        return 0
    if "k" in text.lower():
        return int(float(num_str) * 1000)
    return int(float(num_str))
