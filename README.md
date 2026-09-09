# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-09）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Python | 33,119 | +4,624 | 🔥 2天 |
| 2 | [Tencent/teamai-cli](https://github.com/Tencent/teamai-cli) | TypeScript | 2,730 | +1,083 | NEW |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 283,770 | +690 | 🔥 2天 |
| 4 | [pascalorg/editor](https://github.com/pascalorg/editor) | TypeScript | 22,717 | +442 | NEW |
| 5 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Python | 14,878 | +97 | NEW |
| 6 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 36,110 | +2,286 | 🔥 2天 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 103,637 | +506 | NEW |
| 8 | [liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes) | Unknown | 17,625 | +910 | NEW |
| 9 | [openai/plugins](https://github.com/openai/plugins) | JavaScript | 6,075 | +505 | NEW |
| 10 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | JavaScript | 29,743 | +612 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-09.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
