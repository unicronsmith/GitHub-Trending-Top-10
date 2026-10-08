# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-08）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | C++ | 14,204 | +4,640 | 🔥 4天 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 45,923 | +1,163 | 🔥 2天 |
| 3 | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 21,017 | +7,744 | 🔥 3天 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 280,724 | +1,770 | 🔥 3天 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 98,232 | +662 | 🔥 4天 |
| 6 | [EpicGames/raddebugger](https://github.com/EpicGames/raddebugger) | C | 8,034 | +283 | 🔥 2天 |
| 7 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 27,373 | +309 | NEW |
| 8 | [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 6,834 | +2,510 | NEW |
| 9 | [liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes) | Unknown | 24,385 | +398 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-08.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
