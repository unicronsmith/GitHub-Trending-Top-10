# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-05）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | Python | 1,731 | +585 | NEW |
| 2 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TypeScript | 14,630 | +1,111 | 🔥 4天 |
| 3 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Python | 361,149 | +637 | NEW |
| 4 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | Rust | 10,807 | +2,540 | 🔥 3天 |
| 5 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | Go | 31,202 | +922 | NEW |
| 6 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 81,753 | +203 | NEW |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 266,921 | +653 | 🔥 2天 |
| 8 | [roboflow/supervision](https://github.com/roboflow/supervision) | Python | 48,755 | +132 | NEW |
| 9 | [vercel/next.js](https://github.com/vercel/next.js) | JavaScript | 141,385 | +58 | NEW |
| 10 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | TypeScript | 96,654 | +52 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-05.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
