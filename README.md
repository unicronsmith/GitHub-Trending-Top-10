# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 230,528 | +3,362 | 🔥 3天 |
| 2 | [mahlernim/google-timeline-visualizer](https://github.com/mahlernim/google-timeline-visualizer) | Kotlin | 2,386 | +1,053 | NEW |
| 3 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 114,301 | +1,201 | 🔥 5天 |
| 4 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | Rust | 13,309 | +1,380 | 🔥 2天 |
| 5 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 38,402 | +335 | NEW |
| 6 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | Go | 110,429 | +65 | NEW |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 275,838 | +790 | 🔥 3天 |
| 8 | [santifer/career-ops](https://github.com/santifer/career-ops) | JavaScript | 67,661 | +921 | 🔥 3天 |
| 9 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 4,503 | +388 | 🔥 2天 |
| 10 | [modular/modular](https://github.com/modular/modular) | Mojo | 28,759 | +913 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-08-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
