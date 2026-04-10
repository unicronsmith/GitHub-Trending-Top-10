# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-10）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 97,672 | +2,353 | NEW |
| 2 | [coleam00/Archon](https://github.com/coleam00/Archon) | TypeScript | 14,697 | +185 | 🔥 2天 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 48,694 | +6,485 | 🔥 2天 |
| 4 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | TypeScript | 11,360 | +1,187 | NEW |
| 5 | [multica-ai/multica](https://github.com/multica-ai/multica) | TypeScript | 4,981 | +1,680 | NEW |
| 6 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 11,168 | +1,364 | 🔥 3天 |
| 7 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 12,453 | +245 | 🔥 2天 |
| 8 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Python | 15,498 | +1,310 | 🔥 2天 |
| 9 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | Java | 14,355 | +1,124 | 🔥 2天 |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 144,795 | +2,299 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-04-10.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
