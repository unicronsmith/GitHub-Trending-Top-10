# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-04）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | TypeScript | 14,753 | +3,047 | 🔥 2天 |
| 2 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | Python | 23,632 | +1,852 | NEW |
| 3 | [google-research/timesfm](https://github.com/google-research/timesfm) | Python | 14,383 | +916 | NEW |
| 4 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | TypeScript | 18,736 | +2,771 | 🔥 2天 |
| 5 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | Rust | 3,429 | +750 | NEW |
| 6 | [f/prompts.chat](https://github.com/f/prompts.chat) | HTML | 157,365 | +375 | NEW |
| 7 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | Python | 78,825 | +1,192 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-04-04.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
