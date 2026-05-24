# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-24）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | TypeScript | 23,423 | +2,299 | 🔥 3天 |
| 2 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 14,462 | +1,521 | 🔥 5天 |
| 3 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 26,985 | +2,193 | 🔥 6天 |
| 4 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 13,067 | +486 | NEW |
| 5 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Unknown | 150,705 | +3,507 | 🔥 2天 |
| 6 | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 53,571 | +444 | NEW |
| 7 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 28,815 | +565 | NEW |
| 8 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 20,801 | +2,456 | 🔥 6天 |
| 9 | [multica-ai/multica](https://github.com/multica-ai/multica) | TypeScript | 32,175 | +410 | NEW |
| 10 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 25,671 | +96 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-24.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
