# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-14）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 55,006 | +1,757 | NEW |
| 2 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 7,104 | +3,476 | 🔥 4天 |
| 3 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | TypeScript | 8,562 | +1,978 | 🔥 3天 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 190,526 | +1,801 | 🔥 2天 |
| 5 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 21,465 | +637 | 🔥 2天 |
| 6 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 24,577 | +359 | NEW |
| 7 | [roboflow/supervision](https://github.com/roboflow/supervision) | Python | 38,705 | +59 | NEW |
| 8 | [influxdata/telegraf](https://github.com/influxdata/telegraf) | Go | 17,097 | +211 | 🔥 2天 |
| 9 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Swift | 4,938 | +1,163 | 🔥 2天 |
| 10 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | C | 140,997 | +589 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-14.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
