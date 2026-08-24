# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-24）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [openai/codex](https://github.com/openai/codex) | Rust | 116,546 | +2,715 | 🔥 2天 |
| 2 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | JavaScript | 14,651 | +401 | NEW |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 234,672 | +2,447 | 🔥 5天 |
| 4 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | Shell | 29,587 | +750 | NEW |
| 5 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | Rust | 15,409 | +1,009 | 🔥 4天 |
| 6 | [block/buzz](https://github.com/block/buzz) | Rust | 30,343 | +410 | NEW |
| 7 | [apache/maka](https://github.com/apache/maka) | TypeScript | 2,522 | +51 | NEW |
| 8 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 48,359 | +1,081 | NEW |
| 9 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 36,985 | +39 | NEW |
| 10 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 242,748 | +427 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-08-24.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
