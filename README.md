# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-25）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [pascalorg/editor](https://github.com/pascalorg/editor) | TypeScript | 6,367 | +1,449 | NEW |
| 2 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Python | 45,119 | +4,346 | 🔥 2天 |
| 3 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | TypeScript | 18,934 | +344 | NEW |
| 4 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Python | 25,212 | +3,006 | 🔥 4天 |
| 5 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 53,034 | +728 | NEW |
| 6 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | TypeScript | 15,871 | +2,513 | 🔥 4天 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 41,467 | +1,760 | 🔥 4天 |
| 8 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 6,104 | +209 | NEW |
| 9 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 25,521 | +1,397 | NEW |
| 10 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 12,905 | +1,278 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-03-25.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
