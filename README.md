# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-15）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 261,448 | +32,282 | 🔥 10天 |
| 2 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 38,477 | +525 | NEW |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 50,090 | +1,091 | 🔥 2天 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Go | 112,198 | +398 | NEW |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 68,158 | +3,027 | 🔥 3天 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 299,579 | +534 | NEW |
| 7 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 74,851 | +224 | NEW |
| 8 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 29,635 | +902 | 🔥 4天 |
| 9 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | Java | 88,292 | +1,366 | NEW |
| 10 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 279,973 | +1,015 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-15.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
