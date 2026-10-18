# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-18）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 51,636 | +2,213 | 🔥 2天 |
| 2 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 42,322 | +1,187 | 🔥 4天 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 216,020 | +1,417 | NEW |
| 4 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 12,535 | +351 | NEW |
| 5 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 76,317 | +502 | NEW |
| 6 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 10,231 | +513 | 🔥 2天 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 96,036 | +1,146 | 🔥 2天 |
| 8 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 54,359 | +582 | 🔥 3天 |
| 9 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 74,346 | +2,098 | 🔥 6天 |
| 10 | [android/skills](https://github.com/android/skills) | Kotlin | 8,621 | +381 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-10-18.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
