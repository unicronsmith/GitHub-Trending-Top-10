# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-12）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Rust | 2,273 | +444 | NEW |
| 2 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | TypeScript | 7,852 | +909 | 🔥 4天 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Python | 20,000 | +776 | NEW |
| 4 | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | Python | 22,994 | +55 | NEW |
| 5 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 118,183 | +549 | NEW |
| 6 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Jupyter Notebook | 48,110 | +219 | NEW |
| 7 | [home-assistant/core](https://github.com/home-assistant/core) | Python | 88,835 | +80 | NEW |
| 8 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | TypeScript | 33,589 | +122 | NEW |
| 9 | [ColeMurray/background-agents](https://github.com/ColeMurray/background-agents) | TypeScript | 2,144 | +9 | NEW |
| 10 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | C# | 6,516 | +661 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-12.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
