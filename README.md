# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-07）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 13,185 | +4,666 | 🔥 2天 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 279,202 | +1,406 | 🔥 2天 |
| 3 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | C++ | 9,280 | +2,725 | 🔥 3天 |
| 4 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Python | 54,903 | +620 | 🔥 2天 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 44,695 | +828 | NEW |
| 6 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 102,556 | +453 | NEW |
| 7 | [EpicGames/raddebugger](https://github.com/EpicGames/raddebugger) | C | 7,768 | +82 | NEW |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 97,541 | +578 | 🔥 3天 |
| 9 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | Swift | 27,760 | +96 | NEW |
| 10 | [trycua/cua](https://github.com/trycua/cua) | Rust | 28,644 | +229 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-07.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
