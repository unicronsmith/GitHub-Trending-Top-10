"""AI 分析模块 - 使用 DeepSeek API 生成项目深度解读"""

import os
from openai import OpenAI


def get_client() -> OpenAI:
    """创建 DeepSeek API 客户端。"""
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("未设置 DEEPSEEK_API_KEY 环境变量")
    return OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


def analyze_project(project: dict, readme: str) -> str:
    """使用 DeepSeek 分析单个项目，生成中文深度解读。

    Args:
        project: 项目基本信息字典
        readme: 项目 README 内容

    Returns:
        中文分析文本
    """
    client = get_client()

    prompt = f"""请分析以下 GitHub 开源项目，用中文撰写一份简洁但有深度的解读。

## 项目信息
- 名称：{project['full_name']}
- 描述：{project['description']}
- 编程语言：{project['language']}
- 总星标：{project['total_stars']}
- 今日新增星标：{project['today_stars']}

## README 内容
{readme}

## 请按以下结构输出（每部分 2-3 句话即可）：

**项目简介**：这个项目是什么，解决什么问题

**核心功能**：最重要的 3-5 个功能点

**适用场景**：谁会用到这个项目，在什么场景下使用

**技术亮点**：技术实现上有什么值得关注的地方

**上手建议**：想要使用或贡献这个项目，应该从哪里开始
"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一位资深的开源技术分析师，擅长用通俗易懂的中文解读技术项目。"},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1500,
            temperature=0.7,
        )
        content = response.choices[0].message.content
        return content.strip() if content else "AI 未返回分析内容"
    except Exception as e:
        return f"AI 分析生成失败：{e}"


def analyze_all(projects: list[dict], readmes: list[str]) -> list[str]:
    """批量分析所有项目。"""
    analyses = []
    for project, readme in zip(projects, readmes):
        print(f"  正在分析：{project['full_name']} ...")
        analysis = analyze_project(project, readme)
        analyses.append(analysis)
    return analyses
