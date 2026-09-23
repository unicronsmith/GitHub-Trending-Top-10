# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 36,751 | +665 | 🔥 4天 |
| 2 | [google/ax](https://github.com/google/ax) | Go | 8,523 | +1,542 | 🔥 2天 |
| 3 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Python | 31,355 | +393 | 🔥 2天 |
| 4 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | TypeScript | 6,405 | +609 | NEW |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 290,490 | +528 | NEW |
| 6 | [dream-num/univer](https://github.com/dream-num/univer) | TypeScript | 16,114 | +1,140 | 🔥 2天 |
| 7 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | TypeScript | 18,612 | +832 | NEW |
| 8 | [agent-substrate/substrate](https://github.com/agent-substrate/substrate) | Go | 3,306 | +560 | 🔥 2天 |
| 9 | [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Python | 7,662 | +96 | NEW |
| 10 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 49,776 | +41 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
