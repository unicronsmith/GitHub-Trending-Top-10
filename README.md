# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-12）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 8,075 | +1,616 | NEW |
| 2 | [macro-inc/macro](https://github.com/macro-inc/macro) | Rust | 1,085 | +248 | NEW |
| 3 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Python | 5,337 | +893 | 🔥 3天 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 43,297 | +875 | NEW |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 144,183 | +958 | 🔥 3天 |
| 6 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 36,790 | +238 | NEW |
| 7 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Python | 61,805 | +855 | 🔥 3天 |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Python | 45,084 | +364 | NEW |
| 9 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Go | 87,354 | +85 | NEW |
| 10 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | TypeScript | 77,422 | +748 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-08-12.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
