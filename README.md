# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [openai/codex](https://github.com/openai/codex) | Rust | 114,522 | +1,544 | NEW |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 232,985 | +2,683 | 🔥 4天 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 242,325 | +411 | NEW |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 276,431 | +592 | 🔥 4天 |
| 5 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | Go | 38,941 | +278 | NEW |
| 6 | [makeplane/plane](https://github.com/makeplane/plane) | TypeScript | 57,397 | +263 | NEW |
| 7 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | TypeScript | 202,008 | +149 | NEW |
| 8 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Python | 142,690 | +127 | NEW |
| 9 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | Rust | 14,315 | +959 | 🔥 3天 |
| 10 | [modular/modular](https://github.com/modular/modular) | Mojo | 28,912 | +395 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-08-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
