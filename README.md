# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-13）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | TypeScript | 118,276 | +179 | NEW |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 57,586 | +2,656 | 🔥 4天 |
| 3 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | Ruby | 30,630 | +437 | NEW |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 226,454 | +1,275 | 🔥 4天 |
| 5 | [apple/container](https://github.com/apple/container) | Swift | 35,723 | +3,504 | 🔥 3天 |
| 6 | [music-assistant/server](https://github.com/music-assistant/server) | Python | 1,896 | +20 | NEW |
| 7 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | Go | 2,141 | +530 | NEW |
| 8 | [LMCache/LMCache](https://github.com/LMCache/LMCache) | Python | 8,745 | +28 | NEW |
| 9 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | C | 134,488 | +103 | NEW |
| 10 | [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | Python | 13,976 | +132 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-13.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
