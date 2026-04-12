# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-12）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 62,321 | +6,438 | 🔥 4天 |
| 2 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 103,276 | +3,086 | 🔥 3天 |
| 3 | [coleam00/Archon](https://github.com/coleam00/Archon) | TypeScript | 16,692 | +1,346 | 🔥 4天 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 14,385 | +1,066 | 🔥 5天 |
| 5 | [multica-ai/multica](https://github.com/multica-ai/multica) | TypeScript | 8,580 | +1,948 | 🔥 3天 |
| 6 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | HTML | 37,820 | +1,475 | NEW |
| 7 | [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | Roff | 68,001 | +361 | NEW |
| 8 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Python | 10,458 | +1,084 | NEW |
| 9 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 14,900 | +595 | 🔥 4天 |
| 10 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | Java | 15,839 | +775 | 🔥 4天 |

📄 [查看完整 PDF 报告](reports/2026-04-12.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
