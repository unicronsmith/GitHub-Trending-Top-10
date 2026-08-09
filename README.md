# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-09）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | TypeScript | 9,735 | +2,483 | 🔥 2天 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 84,815 | +779 | 🔥 5天 |
| 3 | [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | Roff | 78,117 | +118 | NEW |
| 4 | [google/skills](https://github.com/google/skills) | Python | 16,947 | +481 | NEW |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 210,503 | +1,359 | 🔥 4天 |
| 6 | [goauthentik/authentik](https://github.com/goauthentik/authentik) | Python | 24,097 | +467 | 🔥 4天 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 96,766 | +153 | NEW |
| 8 | [google/guava](https://github.com/google/guava) | Java | 51,885 | +93 | NEW |
| 9 | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | C++ | 65,091 | +48 | NEW |
| 10 | [denoland/celld](https://github.com/denoland/celld) | Rust | 2,755 | +432 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-09.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
