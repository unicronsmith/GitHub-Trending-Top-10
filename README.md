# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-31）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 133,679 | +2,470 | 🔥 4天 |
| 2 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 72,945 | +2,768 | 🔥 4天 |
| 3 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Python | 128,611 | +592 | 🔥 3天 |
| 4 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 1,558 | +205 | 🔥 3天 |
| 5 | [revfactory/harness](https://github.com/revfactory/harness) | HTML | 4,411 | +55 | NEW |
| 6 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | TypeScript | 18,528 | +349 | 🔥 3天 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 199,742 | +908 | NEW |
| 8 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Python | 23,083 | +779 | NEW |
| 9 | [galilai-group/stable-worldmodel](https://github.com/galilai-group/stable-worldmodel) | Python | 1,530 | +318 | 🔥 3天 |
| 10 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | TypeScript | 27,501 | +469 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-31.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
