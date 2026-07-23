# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [block/buzz](https://github.com/block/buzz) | Rust | 5,100 | +3,252 | NEW |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 70,517 | +3,196 | 🔥 3天 |
| 3 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 32,815 | +398 | 🔥 2天 |
| 4 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Python | 8,911 | +1,329 | 🔥 3天 |
| 5 | [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | Rust | 8,675 | +563 | NEW |
| 6 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | JavaScript | 1,237 | +219 | NEW |
| 7 | [chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11) | Assembly | 70,860 | +599 | 🔥 2天 |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | TypeScript | 26,224 | +1,925 | 🔥 2天 |
| 9 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Python | 69,108 | +637 | 🔥 2天 |
| 10 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | JavaScript | 9,719 | +621 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
