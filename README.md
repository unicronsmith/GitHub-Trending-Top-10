# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-19）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 19,527 | +3,991 | 🔥 9天 |
| 2 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 37,317 | +1,027 | 🔥 3天 |
| 3 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Python | 13,509 | +3,184 | 🔥 2天 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 197,738 | +1,620 | NEW |
| 5 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 19,829 | +127 | NEW |
| 6 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | TypeScript | 13,606 | +1,244 | NEW |
| 7 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Python | 16,018 | +1,466 | 🔥 2天 |
| 8 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Rust | 50,387 | +667 | NEW |
| 9 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 100,704 | +983 | NEW |
| 10 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 5,772 | +952 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-19.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
