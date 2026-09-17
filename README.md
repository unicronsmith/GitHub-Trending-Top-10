# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-17）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Go | 33,906 | +3,290 | 🔥 4天 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 9,565 | +3,606 | 🔥 2天 |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 95,890 | +680 | NEW |
| 4 | [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) | TypeScript | 3,761 | +1,350 | NEW |
| 5 | [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) | Rust | 4,924 | +940 | NEW |
| 6 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | TypeScript | 145,819 | +538 | NEW |
| 7 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | Java | 78,255 | +912 | 🔥 3天 |
| 8 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 24,459 | +287 | 🔥 2天 |
| 9 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | Go | 26,067 | +1,123 | NEW |
| 10 | [abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) | Swift | 5,974 | +738 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-09-17.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
