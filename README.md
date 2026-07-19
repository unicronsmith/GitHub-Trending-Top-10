# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-19）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Python | 20,428 | +355 | 🔥 3天 |
| 2 | [kvcache-ai/ktransformers](https://github.com/kvcache-ai/ktransformers) | Python | 18,123 | +328 | NEW |
| 3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 39,328 | +191 | 🔥 2天 |
| 4 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 42,961 | +629 | NEW |
| 5 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | TypeScript | 1,506 | +203 | 🔥 2天 |
| 6 | [andrewrabert/jellium-desktop](https://github.com/andrewrabert/jellium-desktop) | Rust | 1,200 | +55 | NEW |
| 7 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | Java | 9,877 | +111 | NEW |
| 8 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 36,762 | +338 | 🔥 4天 |
| 9 | [microsoft/terminal](https://github.com/microsoft/terminal) | C++ | 104,002 | +13 | NEW |
| 10 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | Python | 36,577 | +62 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-19.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
