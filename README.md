# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-05）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | Rust | 5,267 | +1,274 | 🔥 3天 |
| 2 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 42,432 | +2,598 | 🔥 3天 |
| 3 | [virattt/dexter](https://github.com/virattt/dexter) | TypeScript | 23,439 | +409 | 🔥 2天 |
| 4 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | Ruby | 13,589 | +535 | NEW |
| 5 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | PowerShell | 7,573 | +665 | NEW |
| 6 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 12,678 | +306 | NEW |
| 7 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | Python | 8,180 | +166 | NEW |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 93,114 | +1,189 | 🔥 2天 |
| 9 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | Unknown | 345,474 | +497 | NEW |
| 10 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | Python | 10,853 | +170 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-05.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
