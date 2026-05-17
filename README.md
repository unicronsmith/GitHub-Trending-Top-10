# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-17）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 11,461 | +1,549 | 🔥 7天 |
| 2 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 35,198 | +333 | NEW |
| 3 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | TypeScript | 42,973 | +425 | NEW |
| 4 | [oven-sh/bun](https://github.com/oven-sh/bun) | Rust | 91,577 | +397 | 🔥 3天 |
| 5 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | JavaScript | 14,744 | +317 | 🔥 2天 |
| 6 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | Python | 6,675 | +165 | NEW |
| 7 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | TypeScript | 2,560 | +44 | NEW |
| 8 | [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | Jupyter Notebook | 19,703 | +225 | NEW |
| 9 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | Python | 1,392 | +287 | NEW |
| 10 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 23,506 | +673 | 🔥 5天 |

📄 [查看完整 PDF 报告](reports/2026-05-17.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
