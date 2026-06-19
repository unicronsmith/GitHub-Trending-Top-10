# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-19）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | C | 7,617 | +1,055 | 🔥 3天 |
| 2 | [google-research/timesfm](https://github.com/google-research/timesfm) | Python | 23,879 | +1,516 | 🔥 3天 |
| 3 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | Swift | 1,461 | +749 | NEW |
| 4 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 56,897 | +133 | NEW |
| 5 | [aishwaryanr/awesome-generative-ai-guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) | HTML | 27,456 | +203 | NEW |
| 6 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | TypeScript | 840 | +172 | NEW |
| 7 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | Python | 36,870 | +3,938 | NEW |
| 8 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 5,942 | +738 | NEW |
| 9 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | Unknown | 4,371 | +478 | 🔥 2天 |
| 10 | [withastro/flue](https://github.com/withastro/flue) | TypeScript | 5,667 | +305 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-19.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
