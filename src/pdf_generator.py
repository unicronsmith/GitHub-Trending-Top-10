"""PDF 生成模块 - 使用 WeasyPrint 生成精美杂志风格 PDF"""

from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


# 项目根目录
ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = ROOT_DIR / "templates"
REPORTS_DIR = ROOT_DIR / "reports"


def generate_pdf(projects: list[dict], analyses: list[str], date: str) -> str:
    """生成 PDF 报告。

    Args:
        projects: 项目信息列表
        analyses: AI 分析结果列表
        date: 报告日期 (YYYY-MM-DD)

    Returns:
        生成的 PDF 文件路径
    """
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # 将 Markdown 分析转换为 HTML
    analyses_html = [markdown.markdown(a) for a in analyses]

    # 渲染 HTML
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=False)
    template = env.get_template("report.html")

    html_content = template.render(
        projects=projects,
        analyses=analyses_html,
        date=date,
    )

    # 生成 PDF
    output_path = REPORTS_DIR / f"{date}.pdf"
    HTML(string=html_content, base_url=str(TEMPLATE_DIR)).write_pdf(str(output_path))

    print(f"  PDF 已生成：{output_path}")
    return str(output_path)
