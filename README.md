# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-17）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | C | 4,340 | +367 | NEW |
| 2 | [n0-computer/iroh](https://github.com/n0-computer/iroh) | Rust | 9,496 | +422 | NEW |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 32,712 | +2,025 | NEW |
| 4 | [meshery/meshery](https://github.com/meshery/meshery) | TypeScript | 10,948 | +199 | 🔥 4天 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 230,582 | +1,109 | NEW |
| 6 | [google-research/timesfm](https://github.com/google-research/timesfm) | Python | 21,553 | +84 | NEW |
| 7 | [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) | TypeScript | 45,507 | +15 | NEW |
| 8 | [continuedev/continue](https://github.com/continuedev/continue) | TypeScript | 33,779 | +38 | NEW |
| 9 | [penpot/penpot](https://github.com/penpot/penpot) | Clojure | 49,917 | +94 | NEW |
| 10 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | Java | 127,363 | +516 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-17.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
