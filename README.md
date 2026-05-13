# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-13）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 3,719 | +1,595 | 🔥 3天 |
| 2 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | TypeScript | 6,648 | +1,335 | 🔥 2天 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 188,826 | +1,419 | NEW |
| 4 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | TypeScript | 12,480 | +987 | 🔥 3天 |
| 5 | [influxdata/telegraf](https://github.com/influxdata/telegraf) | Go | 16,895 | +6 | NEW |
| 6 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | TypeScript | 9,031 | +620 | 🔥 3天 |
| 7 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 20,843 | +83 | NEW |
| 8 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | TypeScript | 13,061 | +620 | NEW |
| 9 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Swift | 3,801 | +53 | NEW |
| 10 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Python | 8,886 | +1,829 | 🔥 4天 |

📄 [查看完整 PDF 报告](reports/2026-05-13.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
