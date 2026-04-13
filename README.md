# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-13）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 20,024 | +2,369 | 🔥 6天 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 73,895 | +7,454 | 🔥 5天 |
| 3 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 16,555 | +1,985 | 🔥 5天 |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 51,577 | +753 | NEW |
| 5 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 106,159 | +2,513 | 🔥 4天 |
| 6 | [multica-ai/multica](https://github.com/multica-ai/multica) | TypeScript | 10,329 | +1,609 | 🔥 4天 |
| 7 | [coleam00/Archon](https://github.com/coleam00/Archon) | TypeScript | 17,384 | +612 | 🔥 5天 |
| 8 | [snarktank/ralph](https://github.com/snarktank/ralph) | TypeScript | 16,298 | +463 | NEW |
| 9 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | Python | 52,632 | +663 | NEW |
| 10 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Jupyter Notebook | 38,951 | +328 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-13.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
