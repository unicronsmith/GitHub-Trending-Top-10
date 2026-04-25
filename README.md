# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-25）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 10,456 | +2,638 | 🔥 3天 |
| 2 | [huggingface/ml-intern](https://github.com/huggingface/ml-intern) | Python | 5,829 | +2,985 | 🔥 3天 |
| 3 | [google/osv-scanner](https://github.com/google/osv-scanner) | Go | 9,688 | +141 | 🔥 2天 |
| 4 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | Python | 62,837 | +1,378 | 🔥 3天 |
| 5 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | TypeScript | 9,210 | +706 | 🔥 5天 |
| 6 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | TypeScript | 13,500 | +530 | 🔥 4天 |
| 7 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 33,284 | +85 | 🔥 2天 |
| 8 | [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | Rust | 59,242 | +268 | 🔥 2天 |
| 9 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | JavaScript | 7,958 | +842 | NEW |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 495,341 | +991 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-04-25.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
