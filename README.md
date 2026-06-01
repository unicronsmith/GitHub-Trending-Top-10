# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-01）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 137,394 | +3,086 | 🔥 5天 |
| 2 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | Python | 10,769 | +984 | NEW |
| 3 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | TypeScript | 23,793 | +660 | NEW |
| 4 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 76,554 | +3,325 | 🔥 5天 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Python | 57,698 | +1,475 | NEW |
| 6 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | JavaScript | 32,420 | +317 | NEW |
| 7 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 22,937 | +241 | NEW |
| 8 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | TypeScript | 19,010 | +428 | 🔥 4天 |
| 9 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 81,562 | +284 | NEW |
| 10 | [revfactory/harness](https://github.com/revfactory/harness) | HTML | 5,011 | +527 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-01.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
