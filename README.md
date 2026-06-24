# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-24）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 17,717 | +3,703 | 🔥 6天 |
| 2 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | Python | 47,974 | +1,461 | 🔥 2天 |
| 3 | [apple/container](https://github.com/apple/container) | Swift | 41,450 | +1,746 | NEW |
| 4 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | Python | 1,847 | +152 | NEW |
| 5 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | TypeScript | 18,913 | +693 | NEW |
| 6 | [revfactory/harness](https://github.com/revfactory/harness) | HTML | 7,579 | +274 | 🔥 2天 |
| 7 | [flutter/flutter](https://github.com/flutter/flutter) | Dart | 177,115 | +44 | NEW |
| 8 | [andreknieriem/headunit-revived](https://github.com/andreknieriem/headunit-revived) | Kotlin | 1,355 | +79 | NEW |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 6,487 | +265 | NEW |
| 10 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | TypeScript | 16,704 | +504 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-24.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
