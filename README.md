# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-13）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | TypeScript | 64,350 | +1,077 | NEW |
| 2 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Rust | 3,611 | +1,290 | 🔥 2天 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Python | 21,198 | +1,148 | 🔥 2天 |
| 4 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | TypeScript | 41,673 | +57 | NEW |
| 5 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 119,200 | +1,006 | 🔥 2天 |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | CSS | 4,730 | +802 | NEW |
| 7 | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | PowerShell | 50,525 | +74 | NEW |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 83,810 | +1,028 | NEW |
| 9 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | HTML | 12,243 | +435 | NEW |
| 10 | [github/spec-kit](https://github.com/github/spec-kit) | Python | 120,261 | +508 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-13.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
