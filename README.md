# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-17）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 526,779 | +435 | NEW |
| 2 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 36,027 | +77 | 🔥 2天 |
| 3 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | TypeScript | 6,352 | +511 | NEW |
| 4 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | CSS | 11,573 | +3,372 | 🔥 5天 |
| 5 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | Java | 9,740 | +13 | NEW |
| 6 | [anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) | TypeScript | 1,489 | +37 | NEW |
| 7 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | Shell | 1,641 | +196 | 🔥 2天 |
| 8 | [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf) | C++ | 71,508 | +11 | NEW |
| 9 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Python | 19,584 | +57 | NEW |
| 10 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | Ruby | 17,701 | +152 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-17.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
