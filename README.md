# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-20）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 7,695 | +1,910 | 🔥 2天 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Python | 15,127 | +1,639 | 🔥 3天 |
| 3 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 23,029 | +3,603 | 🔥 10天 |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Unknown | 139,694 | +2,620 | NEW |
| 5 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 8,980 | +762 | NEW |
| 6 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 38,222 | +930 | 🔥 4天 |
| 7 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | TypeScript | 5,191 | +237 | NEW |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 199,461 | +1,776 | 🔥 2天 |
| 9 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 20,520 | +706 | 🔥 2天 |
| 10 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 102,349 | +1,714 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-05-20.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
