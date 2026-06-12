# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-12）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [apple/container](https://github.com/apple/container) | Swift | 34,371 | +3,513 | 🔥 2天 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 56,197 | +2,660 | 🔥 3天 |
| 3 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | Python | 3,047 | +517 | 🔥 3天 |
| 4 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | Unknown | 16,706 | +823 | 🔥 3天 |
| 5 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | 3,102 | +811 | 🔥 2天 |
| 6 | [soxoj/maigret](https://github.com/soxoj/maigret) | Python | 32,902 | +559 | 🔥 3天 |
| 7 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Unknown | 140,074 | +355 | 🔥 4天 |
| 8 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | TypeScript | 15,580 | +369 | 🔥 5天 |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 225,609 | +1,276 | 🔥 3天 |
| 10 | [restic/restic](https://github.com/restic/restic) | Go | 34,316 | +307 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-12.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
