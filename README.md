# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-16）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 39,979 | +1,552 | 🔥 2天 |
| 2 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 51,161 | +1,158 | 🔥 3天 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 280,998 | +1,057 | 🔥 2天 |
| 4 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 53,264 | +716 | NEW |
| 5 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 30,045 | +449 | 🔥 5天 |
| 6 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 75,460 | +672 | 🔥 2天 |
| 7 | [android/skills](https://github.com/android/skills) | Kotlin | 7,904 | +35 | NEW |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 300,433 | +973 | 🔥 2天 |
| 9 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 11,800 | +214 | NEW |
| 10 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 70,275 | +2,301 | 🔥 4天 |

📄 [查看完整 PDF 报告](reports/2026-10-16.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
