# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-17）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 41,204 | +1,383 | 🔥 3天 |
| 2 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 49,344 | +1,397 | NEW |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 281,994 | +1,145 | 🔥 3天 |
| 4 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 53,801 | +580 | 🔥 2天 |
| 5 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 51,969 | +879 | 🔥 4天 |
| 6 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 9,704 | +159 | NEW |
| 7 | [android/skills](https://github.com/android/skills) | Kotlin | 8,277 | +368 | 🔥 2天 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 94,895 | +1,102 | NEW |
| 9 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | TypeScript | 151,393 | +168 | NEW |
| 10 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 72,305 | +2,135 | 🔥 5天 |

📄 [查看完整 PDF 报告](reports/2026-10-17.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
