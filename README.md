# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-27）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) | Swift | 31,569 | +2,344 | 🔥 2天 |
| 2 | [amnezia-vpn/amnezia-client](https://github.com/amnezia-vpn/amnezia-client) | C++ | 13,585 | +515 | NEW |
| 3 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | TypeScript | 43,729 | +554 | NEW |
| 4 | [yorukot/superfile](https://github.com/yorukot/superfile) | Go | 20,569 | +600 | 🔥 4天 |
| 5 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Python | 57,957 | +349 | NEW |
| 6 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | JavaScript | 51,136 | +849 | 🔥 2天 |
| 7 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 34,401 | +442 | 🔥 6天 |
| 8 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Go | 14,405 | +980 | NEW |
| 9 | [jenkinsci/jenkins](https://github.com/jenkinsci/jenkins) | Java | 25,805 | +179 | NEW |
| 10 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | Python | 10,689 | +412 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-27.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
