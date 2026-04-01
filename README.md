# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-01）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Shell | 95,832 | +3,905 | NEW |
| 2 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Python | 33,826 | +3,863 | 🔥 3天 |
| 3 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | HTML | 29,737 | +2,407 | 🔥 3天 |
| 4 | [google-research/timesfm](https://github.com/google-research/timesfm) | Python | 11,591 | +495 | NEW |
| 5 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Python | 14,538 | +2,390 | 🔥 3天 |
| 6 | [axios/axios](https://github.com/axios/axios) | JavaScript | 108,752 | +88 | NEW |
| 7 | [openai/codex](https://github.com/openai/codex) | Rust | 70,906 | +2,345 | NEW |
| 8 | [f/prompts.chat](https://github.com/f/prompts.chat) | HTML | 155,496 | +421 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-01.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
