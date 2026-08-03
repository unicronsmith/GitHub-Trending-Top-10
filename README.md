# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-03）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 26,303 | +1,081 | 🔥 2天 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | PowerShell | 14,946 | +2,442 | 🔥 4天 |
| 3 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | Rust | 6,799 | +1,769 | NEW |
| 4 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | Go | 29,603 | +877 | NEW |
| 5 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TypeScript | 11,683 | +1,091 | 🔥 2天 |
| 6 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | Jupyter Notebook | 60,315 | +1,902 | 🔥 5天 |
| 7 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Jupyter Notebook | 115,251 | +776 | 🔥 2天 |
| 8 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Python | 360,284 | +138 | NEW |
| 9 | [antirez/ds4](https://github.com/antirez/ds4) | C | 20,218 | +385 | NEW |
| 10 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 35,720 | +217 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-03.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
