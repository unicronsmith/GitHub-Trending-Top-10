# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-08）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 33,313 | +3,558 | 🔥 4天 |
| 2 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | Python | 8,117 | +1,730 | NEW |
| 3 | [google/skills](https://github.com/google/skills) | Python | 12,146 | +481 | NEW |
| 4 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | TypeScript | 13,296 | +649 | NEW |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 23,697 | +961 | 🔥 4天 |
| 6 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | TypeScript | 15,250 | +337 | 🔥 2天 |
| 7 | [santifer/career-ops](https://github.com/santifer/career-ops) | JavaScript | 50,077 | +665 | NEW |
| 8 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | Unknown | 12,419 | +112 | NEW |
| 9 | [openai/plugins](https://github.com/openai/plugins) | JavaScript | 2,209 | +296 | 🔥 2天 |
| 10 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | Python | 3,219 | +103 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-08.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
