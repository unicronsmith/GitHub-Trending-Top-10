# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-26）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | JavaScript | 20,242 | +1,698 | NEW |
| 2 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | Python | 1,998 | +351 | 🔥 2天 |
| 3 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 35,883 | +1,265 | 🔥 2天 |
| 4 | [apache/maka](https://github.com/apache/maka) | TypeScript | 3,529 | +543 | 🔥 3天 |
| 5 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 100,608 | +218 | NEW |
| 6 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Python | 13,058 | +813 | NEW |
| 7 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 49,357 | +569 | NEW |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 37,988 | +542 | NEW |
| 9 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | Shell | 31,624 | +1,083 | NEW |
| 10 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 134,465 | +161 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-26.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
