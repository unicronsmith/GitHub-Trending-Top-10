# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-18）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | Python | 12,398 | +827 | NEW |
| 2 | [apache/ossie](https://github.com/apache/ossie) | Python | 1,162 | +48 | NEW |
| 3 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 36,341 | +438 | 🔥 3天 |
| 4 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | TypeScript | 4,658 | +529 | NEW |
| 5 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 38,848 | +232 | NEW |
| 6 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Python | 19,928 | +74 | 🔥 2天 |
| 7 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | TypeScript | 9,346 | +63 | NEW |
| 8 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 23,128 | +242 | NEW |
| 9 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | TypeScript | 906 | +192 | NEW |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 527,854 | +1,068 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-07-18.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
