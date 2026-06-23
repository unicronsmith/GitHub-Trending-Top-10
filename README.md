# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 14,093 | +3,590 | 🔥 5天 |
| 2 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | Python | 46,545 | +1,121 | NEW |
| 3 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 19,235 | +1,040 | 🔥 3天 |
| 4 | [garrytan/gstack](https://github.com/garrytan/gstack) | TypeScript | 113,683 | +1,012 | 🔥 2天 |
| 5 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Python | 73,690 | +741 | 🔥 3天 |
| 6 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 58,781 | +279 | NEW |
| 7 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | Swift | 8,183 | +1,631 | 🔥 5天 |
| 8 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 30,688 | +66 | NEW |
| 9 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | HTML | 59,061 | +329 | NEW |
| 10 | [revfactory/harness](https://github.com/revfactory/harness) | HTML | 7,314 | +123 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
