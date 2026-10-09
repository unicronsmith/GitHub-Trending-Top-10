# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-09）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 39,358 | +15,335 | 🔥 4天 |
| 2 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | C++ | 20,357 | +5,925 | 🔥 5天 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 282,287 | +1,696 | 🔥 4天 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 47,585 | +1,744 | 🔥 3天 |
| 5 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Go | 44,974 | +323 | NEW |
| 6 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 28,084 | +714 | 🔥 2天 |
| 7 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | Python | 60,529 | +95 | NEW |
| 8 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 103,777 | +523 | NEW |
| 9 | [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 10,516 | +3,723 | 🔥 2天 |
| 10 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | Python | 17,604 | +109 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-09.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
