# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-02）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 60,656 | +2,112 | 🔥 3天 |
| 2 | [soxoj/maigret](https://github.com/soxoj/maigret) | Python | 22,075 | +535 | 🔥 3天 |
| 3 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | Rust | 52,130 | +3,401 | 🔥 4天 |
| 4 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust | 2,536 | +403 | 🔥 4天 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 53,701 | +3,645 | 🔥 7天 |
| 6 | [browserbase/skills](https://github.com/browserbase/skills) | JavaScript | 1,314 | +334 | 🔥 2天 |
| 7 | [simstudioai/sim](https://github.com/simstudioai/sim) | TypeScript | 28,270 | +56 | 🔥 2天 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 176,084 | +1,096 | 🔥 4天 |
| 9 | [Flowseal/zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) | Batchfile | 27,022 | +145 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-05-02.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
