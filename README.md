# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-29）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | Rust | 38,686 | +11,955 | NEW |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 41,173 | +7,321 | 🔥 4天 |
| 3 | [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack) | Python | 11,080 | +967 | 🔥 2天 |
| 4 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | Python | 4,463 | +953 | 🔥 3天 |
| 5 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust | 1,005 | +386 | NEW |
| 6 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 33,017 | +1,607 | 🔥 3天 |
| 7 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Python | 45,365 | +1,483 | 🔥 3天 |
| 8 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | Go | 2,556 | +417 | 🔥 2天 |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 172,396 | +1,683 | NEW |
| 10 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | Python | 32,373 | +278 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-29.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
