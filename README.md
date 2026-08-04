# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-04）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TypeScript | 12,748 | +1,090 | 🔥 3天 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | PowerShell | 17,081 | +2,446 | 🔥 5天 |
| 3 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | Rust | 9,237 | +1,699 | 🔥 2天 |
| 4 | [uber/ADR](https://github.com/uber/ADR) | Python | 511 | +140 | NEW |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 266,056 | +617 | NEW |
| 6 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Jupyter Notebook | 115,992 | +775 | 🔥 3天 |
| 7 | [cypress-io/cypress](https://github.com/cypress-io/cypress) | TypeScript | 50,663 | +6 | NEW |
| 8 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 27,941 | +1,085 | 🔥 3天 |
| 9 | [webpack/webpack](https://github.com/webpack/webpack) | JavaScript | 65,885 | +8 | NEW |
| 10 | [gabime/spdlog](https://github.com/gabime/spdlog) | C++ | 29,342 | +9 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-04.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
