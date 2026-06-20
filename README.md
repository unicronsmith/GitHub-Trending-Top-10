# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-20）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | Swift | 2,282 | +756 | 🔥 2天 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot) | Clojure | 50,781 | +85 | NEW |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 6,560 | +156 | 🔥 2天 |
| 4 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | Rust | 20,002 | +774 | NEW |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | C | 8,777 | +1,058 | 🔥 4天 |
| 6 | [google-research/timesfm](https://github.com/google-research/timesfm) | Python | 24,256 | +1,510 | 🔥 4天 |
| 7 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 50,667 | +140 | NEW |
| 8 | [Kong/insomnia](https://github.com/Kong/insomnia) | TypeScript | 39,119 | +292 | NEW |
| 9 | [tw93/Pake](https://github.com/tw93/Pake) | Rust | 53,082 | +2,398 | NEW |
| 10 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | Python | 40,253 | +4,005 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-20.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
