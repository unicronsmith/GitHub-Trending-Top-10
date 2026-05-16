# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-16）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun) | Rust | 90,721 | +448 | 🔥 2天 |
| 2 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 22,743 | +646 | 🔥 4天 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 193,366 | +1,648 | 🔥 4天 |
| 4 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | JavaScript | 14,032 | +356 | NEW |
| 5 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Swift | 6,346 | +719 | 🔥 4天 |
| 6 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 9,813 | +1,271 | 🔥 6天 |
| 7 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 57,833 | +1,859 | 🔥 3天 |
| 8 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | Go | 16,493 | +484 | NEW |
| 9 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 2,063 | +397 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-16.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
