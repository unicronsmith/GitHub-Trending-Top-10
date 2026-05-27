# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-27）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | TypeScript | 38,352 | +4,466 | 🔥 6天 |
| 2 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | Unknown | 5,376 | +664 | 🔥 2天 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 195,461 | +2,062 | 🔥 3天 |
| 4 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 17,002 | +695 | 🔥 4天 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Shell | 23,286 | +2,715 | 🔥 2天 |
| 6 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 21,827 | +314 | NEW |
| 7 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 26,706 | +425 | NEW |
| 8 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 10,588 | +885 | 🔥 3天 |
| 9 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 47,110 | +520 | NEW |
| 10 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | TypeScript | 35,032 | +137 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-27.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
