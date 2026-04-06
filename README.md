# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-06）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 22,828 | +837 | NEW |
| 2 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | Kotlin | 17,437 | +389 | NEW |
| 3 | [block/goose](https://github.com/block/goose) | Rust | 37,523 | +882 | 🔥 2天 |
| 4 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | C++ | 1,752 | +124 | NEW |
| 5 | [immich-app/immich](https://github.com/immich-app/immich) | TypeScript | 96,508 | +155 | NEW |
| 6 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | TypeScript | 35,983 | +703 | NEW |
| 7 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 27,005 | +1,251 | NEW |
| 8 | [tobi/qmd](https://github.com/tobi/qmd) | TypeScript | 18,288 | +298 | NEW |
| 9 | [TelegramMessenger/Telegram-iOS](https://github.com/TelegramMessenger/Telegram-iOS) | Swift | 8,221 | +14 | NEW |
| 10 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Unknown | 20,055 | +281 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-06.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
