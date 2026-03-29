# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-29）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | Python | 84,717 | +1,814 | 🔥 2天 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 121,658 | +2,292 | 🔥 2天 |
| 3 | [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | Python | 3,690 | +506 | 🔥 2天 |
| 4 | [virattt/dexter](https://github.com/virattt/dexter) | TypeScript | 20,385 | +581 | 🔥 4天 |
| 5 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 42,580 | +563 | 🔥 4天 |
| 6 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | Python | 19,978 | +880 | NEW |
| 7 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | Python | 7,788 | +687 | 🔥 4天 |
| 8 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | Python | 21,819 | +398 | NEW |
| 9 | [apache/superset](https://github.com/apache/superset) | TypeScript | 71,617 | +31 | NEW |

📄 [查看完整 PDF 报告](reports/2026-03-29.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
