# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-25）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 49,494 | +891 | 🔥 2天 |
| 2 | [openai/codex](https://github.com/openai/codex) | Rust | 117,733 | +1,994 | 🔥 3天 |
| 3 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 34,596 | +434 | NEW |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Unknown | 206,865 | +588 | NEW |
| 5 | [makeplane/plane](https://github.com/makeplane/plane) | TypeScript | 58,181 | +243 | NEW |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 236,140 | +896 | NEW |
| 7 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | Python | 1,515 | +489 | NEW |
| 8 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | Rust | 16,190 | +1,097 | 🔥 5天 |
| 9 | [apache/maka](https://github.com/apache/maka) | TypeScript | 3,097 | +411 | 🔥 2天 |
| 10 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 39,113 | +83 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-25.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
