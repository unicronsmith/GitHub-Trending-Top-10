# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-13）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 12,518 | +2,855 | 🔥 2天 |
| 2 | [macro-inc/macro](https://github.com/macro-inc/macro) | Rust | 2,350 | +227 | 🔥 2天 |
| 3 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Python | 6,040 | +845 | 🔥 4天 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 44,501 | +1,235 | 🔥 2天 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 144,945 | +1,873 | 🔥 4天 |
| 6 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 37,056 | +266 | 🔥 2天 |
| 7 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Python | 62,279 | +215 | 🔥 4天 |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Python | 46,294 | +476 | 🔥 2天 |
| 9 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Go | 87,796 | +139 | 🔥 2天 |
| 10 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | TypeScript | 77,975 | +571 | 🔥 4天 |

📄 [查看完整 PDF 报告](reports/2026-08-13.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
