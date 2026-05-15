# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-15）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 8,393 | +3,329 | 🔥 5天 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 192,147 | +1,780 | 🔥 3天 |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 22,109 | +654 | 🔥 3天 |
| 4 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Swift | 5,643 | +1,128 | 🔥 3天 |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 56,871 | +1,715 | 🔥 2天 |
| 6 | [influxdata/telegraf](https://github.com/influxdata/telegraf) | Go | 17,309 | +215 | 🔥 3天 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills) | Python | 134,627 | +625 | NEW |
| 8 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | 20,751 | +68 | NEW |
| 9 | [NVIDIA-AI-Blueprints/video-search-and-summarization](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) | Python | 990 | +62 | NEW |
| 10 | [oven-sh/bun](https://github.com/oven-sh/bun) | Rust | 90,437 | +289 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-15.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
