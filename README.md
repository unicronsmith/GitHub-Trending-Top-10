# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-16）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | TypeScript | 448,309 | +640 | 🔥 3天 |
| 2 | [swc-project/swc](https://github.com/swc-project/swc) | Rust | 33,914 | +21 | NEW |
| 3 | [teslamate-org/teslamate](https://github.com/teslamate-org/teslamate) | Elixir | 8,365 | +214 | 🔥 2天 |
| 4 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | TypeScript | 123,699 | +1,196 | 🔥 4天 |
| 5 | [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | TypeScript | 94,817 | +171 | NEW |
| 6 | [meshery/meshery](https://github.com/meshery/meshery) | TypeScript | 10,769 | +229 | 🔥 3天 |
| 7 | [cypress-io/cypress](https://github.com/cypress-io/cypress) | TypeScript | 50,116 | +11 | NEW |
| 8 | [music-assistant/server](https://github.com/music-assistant/server) | Python | 2,495 | +157 | NEW |
| 9 | [Universal-Debloater-Alliance/universal-android-debloater-next-generation](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) | Rust | 7,128 | +146 | NEW |
| 10 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Python | 30,000 | +413 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-16.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
