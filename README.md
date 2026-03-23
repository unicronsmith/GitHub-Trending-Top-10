# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Python | 21,199 | +1,787 | 🔥 2天 |
| 2 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 38,368 | +1,051 | 🔥 2天 |
| 3 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | Go | 12,550 | +1,069 | 🔥 2天 |
| 4 | [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | Python | 5,011 | +237 | 🔥 2天 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | JavaScript | 100,068 | +3,724 | 🔥 2天 |
| 6 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | JavaScript | 11,666 | +834 | 🔥 2天 |
| 7 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | TypeScript | 11,636 | +2,300 | 🔥 2天 |
| 8 | [systemd/systemd](https://github.com/systemd/systemd) | C | 16,100 | +313 | 🔥 2天 |
| 9 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 83,125 | +428 | 🔥 2天 |
| 10 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Python | 30,239 | +220 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-03-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
