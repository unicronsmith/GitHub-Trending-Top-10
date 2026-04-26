# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-26）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 12,115 | +4,007 | 🔥 4天 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 21,057 | +1,139 | NEW |
| 3 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | Python | 64,518 | +1,200 | 🔥 4天 |
| 4 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 33,634 | +471 | 🔥 3天 |
| 5 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Python | 25,481 | +87 | NEW |
| 6 | [deepseek-ai/DeepEP](https://github.com/deepseek-ai/DeepEP) | Cuda | 9,549 | +189 | NEW |
| 7 | [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | C# | 53,152 | +48 | NEW |
| 8 | [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) | TypeScript | 23,619 | +57 | NEW |
| 9 | [huggingface/ml-intern](https://github.com/huggingface/ml-intern) | Python | 6,520 | +1,240 | 🔥 4天 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 496,353 | +1,432 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-04-26.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
