# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Python | 18,949 | +1,772 | NEW |
| 2 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 36,447 | +1,108 | NEW |
| 3 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | Go | 11,586 | +1,015 | NEW |
| 4 | [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | Python | 4,636 | +235 | NEW |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | JavaScript | 96,806 | +3,370 | NEW |
| 6 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | JavaScript | 11,006 | +832 | NEW |
| 7 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | TypeScript | 8,309 | +2,294 | NEW |
| 8 | [systemd/systemd](https://github.com/systemd/systemd) | C | 15,907 | +313 | NEW |
| 9 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 82,257 | +405 | NEW |
| 10 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Python | 29,942 | +203 | NEW |

📄 [查看完整 PDF 报告](reports/2026-03-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
