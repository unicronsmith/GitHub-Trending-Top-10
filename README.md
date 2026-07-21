# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-21）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 63,290 | +1,167 | NEW |
| 2 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | Python | 13,213 | +4,434 | NEW |
| 3 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Python | 24,184 | +1,833 | 🔥 5天 |
| 4 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Unknown | 5,900 | +1,846 | NEW |
| 5 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | JavaScript | 8,759 | +297 | NEW |
| 6 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust | 10,039 | +568 | 🔥 2天 |
| 7 | [oblien/openship](https://github.com/oblien/openship) | TypeScript | 5,462 | +1,641 | NEW |
| 8 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | Python | 37,304 | +317 | NEW |
| 9 | [every-app/open-seo](https://github.com/every-app/open-seo) | TypeScript | 6,234 | +939 | 🔥 2天 |
| 10 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | JavaScript | 4,600 | +28 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-21.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
