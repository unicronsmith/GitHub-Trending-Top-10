# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-30）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 71,015 | +3,567 | 🔥 3天 |
| 2 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 130,958 | +1,873 | 🔥 3天 |
| 3 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | TypeScript | 18,285 | +353 | 🔥 2天 |
| 4 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 48,597 | +578 | 🔥 4天 |
| 5 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Python | 128,132 | +395 | 🔥 2天 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Shell | 28,703 | +2,062 | 🔥 5天 |
| 7 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 1,362 | +134 | 🔥 2天 |
| 8 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | Rust | 7,615 | +701 | 🔥 2天 |
| 9 | [galilai-group/stable-worldmodel](https://github.com/galilai-group/stable-worldmodel) | Python | 1,346 | +362 | 🔥 2天 |
| 10 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | Unknown | 49,927 | +1,566 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-05-30.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
