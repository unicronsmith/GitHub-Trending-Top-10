# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-28）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) | TypeScript | 4,748 | +1,075 | 🔥 4天 |
| 2 | [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | Unknown | 10,820 | +1,395 | NEW |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 307,168 | +1,096 | 🔥 2天 |
| 4 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Python | 47,597 | +2,376 | 🔥 2天 |
| 5 | [macro-inc/macro](https://github.com/macro-inc/macro) | Rust | 5,280 | +106 | NEW |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | CSS | 40,295 | +2,109 | 🔥 5天 |
| 7 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Rust | 92,011 | +1,471 | 🔥 5天 |
| 8 | [makecindy/cindy](https://github.com/makecindy/cindy) | TypeScript | 7,912 | +740 | 🔥 5天 |
| 9 | [nightly-labs/openbot](https://github.com/nightly-labs/openbot) | TypeScript | 3,038 | +1,053 | 🔥 3天 |
| 10 | [togg53192-cmd/jailbreaks](https://github.com/togg53192-cmd/jailbreaks) | Unknown | 6,679 | +1,478 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-10-28.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
