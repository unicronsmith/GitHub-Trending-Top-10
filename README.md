# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-21）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [modular/modular](https://github.com/modular/modular) | Mojo | 28,323 | +268 | NEW |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 227,916 | +2,192 | 🔥 2天 |
| 3 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | Rust | 12,379 | +1,545 | NEW |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 275,299 | +727 | 🔥 2天 |
| 5 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 4,228 | +449 | NEW |
| 6 | [santifer/career-ops](https://github.com/santifer/career-ops) | JavaScript | 67,084 | +816 | 🔥 2天 |
| 7 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 3,813 | +332 | 🔥 4天 |
| 8 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 113,440 | +2,761 | 🔥 4天 |
| 9 | [agent-substrate/substrate](https://github.com/agent-substrate/substrate) | Go | 1,499 | +22 | NEW |
| 10 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | TypeScript | 3,262 | +507 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-08-21.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
