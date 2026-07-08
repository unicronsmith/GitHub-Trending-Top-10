# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-08）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | TypeScript | 13,297 | +2,514 | 🔥 2天 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 72,773 | +1,317 | 🔥 3天 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 78,843 | +1,129 | 🔥 3天 |
| 4 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TypeScript | 7,318 | +610 | NEW |
| 5 | [prisma/prisma](https://github.com/prisma/prisma) | TypeScript | 46,380 | +30 | NEW |
| 6 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 50,481 | +659 | NEW |
| 7 | [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | Go | 23,358 | +20 | NEW |
| 8 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | C# | 10,934 | +893 | 🔥 2天 |
| 9 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 53,584 | +1,691 | 🔥 5天 |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 249,371 | +999 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-08.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
