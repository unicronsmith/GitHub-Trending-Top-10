# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-29）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 68,492 | +3,563 | 🔥 2天 |
| 2 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 128,678 | +1,876 | 🔥 2天 |
| 3 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | TypeScript | 17,959 | +354 | NEW |
| 4 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 48,154 | +575 | 🔥 3天 |
| 5 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Python | 127,609 | +319 | NEW |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Shell | 27,495 | +2,066 | 🔥 4天 |
| 7 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 1,169 | +129 | NEW |
| 8 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | Rust | 6,745 | +932 | NEW |
| 9 | [galilai-group/stable-worldmodel](https://github.com/galilai-group/stable-worldmodel) | Python | 1,053 | +346 | NEW |
| 10 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | Unknown | 49,311 | +1,564 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-05-29.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
