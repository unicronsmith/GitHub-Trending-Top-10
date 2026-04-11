# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-11）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 100,806 | +2,352 | 🔥 2天 |
| 2 | [coleam00/Archon](https://github.com/coleam00/Archon) | TypeScript | 16,094 | +756 | 🔥 3天 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 54,994 | +7,671 | 🔥 3天 |
| 4 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | TypeScript | 11,950 | +507 | 🔥 2天 |
| 5 | [multica-ai/multica](https://github.com/multica-ai/multica) | TypeScript | 6,910 | +1,506 | 🔥 2天 |
| 6 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 12,201 | +1,450 | 🔥 4天 |
| 7 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 12,917 | +601 | 🔥 3天 |
| 8 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Python | 16,307 | +1,424 | 🔥 3天 |
| 9 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | Java | 15,109 | +1,306 | 🔥 3天 |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 146,368 | +2,150 | 🔥 4天 |

📄 [查看完整 PDF 报告](reports/2026-04-11.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
