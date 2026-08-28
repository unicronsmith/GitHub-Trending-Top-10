# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-28）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | JavaScript | 27,000 | +4,561 | 🔥 2天 |
| 2 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 36,437 | +720 | 🔥 2天 |
| 3 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 34,991 | +457 | 🔥 2天 |
| 4 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | JavaScript | 10,866 | +3,398 | 🔥 2天 |
| 5 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 46,128 | +189 | NEW |
| 6 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | Go | 2,556 | +574 | 🔥 2天 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 53,218 | +1,144 | 🔥 2天 |
| 8 | [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | Python | 75,498 | +309 | NEW |
| 9 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 5,920 | +257 | NEW |
| 10 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | JavaScript | 24,188 | +1,687 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-08-28.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
