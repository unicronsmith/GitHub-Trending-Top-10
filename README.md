# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-03）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 37,386 | +1,299 | NEW |
| 2 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 63,974 | +2,225 | 🔥 4天 |
| 3 | [soxoj/maigret](https://github.com/soxoj/maigret) | Python | 23,166 | +1,064 | 🔥 4天 |
| 4 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | Rust | 1,771 | +564 | NEW |
| 5 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | Python | 9,366 | +478 | NEW |
| 6 | [browserbase/skills](https://github.com/browserbase/skills) | JavaScript | 1,643 | +346 | 🔥 3天 |
| 7 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | 19,230 | +264 | NEW |
| 8 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust | 3,097 | +482 | 🔥 5天 |
| 9 | [openwrt/openwrt](https://github.com/openwrt/openwrt) | C | 26,489 | +14 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-03.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
