# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-24）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Python | 24,146 | +2,880 | 🔥 3天 |
| 2 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Python | 41,360 | +3,546 | NEW |
| 3 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | TypeScript | 14,159 | +4,138 | 🔥 3天 |
| 4 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | Go | 13,318 | +1,309 | 🔥 3天 |
| 5 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 84,097 | +1,157 | 🔥 3天 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 40,092 | +2,530 | 🔥 3天 |
| 7 | [tinygrad/tinygrad](https://github.com/tinygrad/tinygrad) | Python | 31,969 | +56 | NEW |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | JavaScript | 103,394 | +4,458 | 🔥 3天 |
| 9 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 12,007 | +919 | NEW |
| 10 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | Python | 42,972 | +487 | NEW |

📄 [查看完整 PDF 报告](reports/2026-03-24.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
