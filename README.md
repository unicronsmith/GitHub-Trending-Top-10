# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-07）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 24,015 | +857 | 🔥 2天 |
| 2 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | Kotlin | 18,318 | +1,107 | 🔥 2天 |
| 3 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | 38,596 | +1,523 | NEW |
| 4 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | C++ | 2,273 | +483 | 🔥 2天 |
| 5 | [immich-app/immich](https://github.com/immich-app/immich) | TypeScript | 97,148 | +152 | 🔥 2天 |
| 6 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | TypeScript | 37,025 | +733 | 🔥 2天 |
| 7 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 29,400 | +1,574 | 🔥 2天 |
| 8 | [tobi/qmd](https://github.com/tobi/qmd) | TypeScript | 19,136 | +394 | 🔥 2天 |
| 9 | [TelegramMessenger/Telegram-iOS](https://github.com/TelegramMessenger/Telegram-iOS) | Swift | 8,393 | +25 | 🔥 2天 |
| 10 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Unknown | 21,126 | +429 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-04-07.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
