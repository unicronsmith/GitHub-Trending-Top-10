# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-25）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [block/buzz](https://github.com/block/buzz) | Rust | 10,820 | +3,270 | 🔥 3天 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 73,805 | +2,184 | 🔥 5天 |
| 3 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Python | 70,318 | +663 | 🔥 4天 |
| 4 | [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | Rust | 9,474 | +473 | 🔥 3天 |
| 5 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 33,638 | +499 | 🔥 4天 |
| 6 | [Automattic/harper](https://github.com/Automattic/harper) | Rust | 13,195 | +876 | 🔥 2天 |
| 7 | [likec4/likec4](https://github.com/likec4/likec4) | TypeScript | 5,131 | +337 | 🔥 2天 |
| 8 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | JavaScript | 3,063 | +880 | 🔥 3天 |
| 9 | [yorukot/superfile](https://github.com/yorukot/superfile) | Go | 19,810 | +338 | 🔥 2天 |
| 10 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 86,168 | +1,022 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-07-25.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
