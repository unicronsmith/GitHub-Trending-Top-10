# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-13）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 198,135 | +54,706 | 🔥 8天 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | JavaScript | 54,942 | +1,961 | 🔥 3天 |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 62,311 | +2,277 | NEW |
| 4 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 27,988 | +978 | 🔥 2天 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 53,765 | +1,813 | 🔥 7天 |
| 6 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | TypeScript | 34,302 | +187 | NEW |
| 7 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 38,140 | +1,004 | 🔥 3天 |
| 8 | [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 24,828 | +4,078 | 🔥 6天 |
| 9 | [xtool-org/xtool](https://github.com/xtool-org/xtool) | Swift | 8,937 | +1,182 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-13.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
