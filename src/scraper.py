"""GitHub Trending 页面爬虫模块"""

import os
import time
import requests
from bs4 import BeautifulSoup


def _request_with_retry(url: str, headers: dict, params: dict | None = None,
                        max_retries: int = 3, backoff: float = 2.0) -> requests.Response:
    """带重试机制的 HTTP GET 请求。"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait = backoff * (attempt + 1)
                print(f"    请求失败，{wait}s 后重试（{attempt + 1}/{max_retries}）：{e}")
                time.sleep(wait)
            else:
                raise
    raise requests.RequestException("所有重试均失败")


def fetch_trending(language: str = "", since: str = "daily") -> list[dict]:
    """爬取 GitHub Trending 页面，返回前 10 个项目信息。"""
    url = f"https://github.com/trending/{language}"
    params = {"since": since}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = _request_with_retry(url, headers, params)
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
        h2 = article.select_one("h2 a")
        if not h2:
            return None
        repo_path = h2.get("href", "").strip("/")
        parts = repo_path.split("/")
        if len(parts) < 2:
            return None
        owner, name = parts[0], parts[1]

        desc_tag = article.select_one("p")
        description = desc_tag.get_text(strip=True) if desc_tag else ""

        lang_tag = article.select_one("[itemprop='programmingLanguage']")
        language = lang_tag.get_text(strip=True) if lang_tag else "Unknown"

        lang_color_tag = article.select_one(".repo-language-color")
        lang_color = ""
        if lang_color_tag:
            style = lang_color_tag.get("style", "")
            if "background-color:" in style:
                lang_color = style.split("background-color:")[-1].strip().rstrip(";")

        stars_tag = article.select_one("a[href$='/stargazers']")
        total_stars = _parse_number(stars_tag.get_text(strip=True)) if stars_tag else 0

        forks_tag = article.select_one("a[href$='/forks']")
        total_forks = _parse_number(forks_tag.get_text(strip=True)) if forks_tag else 0

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
    """通过 GitHub API 获取项目的 README 内容。支持 GITHUB_TOKEN 认证。"""
    url = f"https://api.github.com/repos/{owner}/{name}/readme"
    headers = {
        "Accept": "application/vnd.github.v3.raw",
        "User-Agent": "GitHub-Trending-Bot",
    }
    # 如果有 GITHUB_TOKEN，使用认证以提高 API 限额
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = _request_with_retry(url, headers)
        readme = response.text
        if len(readme) > 5000:
            readme = readme[:5000] + "\n\n... (内容已截断)"
        return readme
    except requests.RequestException:
        return "无法获取 README 内容"


def _parse_number(text: str) -> int:
    """解析带逗号或 k 后缀的数字。"""
    text = text.strip().replace(",", "")
    num_str = ""
    for ch in text:
        if ch.isdigit() or ch == ".":
            num_str += ch
    if not num_str:
        return 0
    if "k" in text.lower():
        return int(float(num_str) * 1000)
    return int(float(num_str))
