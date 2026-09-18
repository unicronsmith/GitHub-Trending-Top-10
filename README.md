# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-18）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 12,220 | +3,019 | 🔥 3天 |
| 2 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | TypeScript | 146,095 | +442 | 🔥 2天 |
| 3 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Go | 36,246 | +2,724 | 🔥 5天 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 261,622 | +965 | NEW |
| 5 | [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) | TypeScript | 4,941 | +1,319 | 🔥 2天 |
| 6 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 96,177 | +677 | 🔥 2天 |
| 7 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | Python | 3,809 | +571 | NEW |
| 8 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | TypeScript | 69,123 | +298 | NEW |
| 9 | [ankitects/anki](https://github.com/ankitects/anki) | Rust | 31,091 | +430 | NEW |
| 10 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 24,734 | +300 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-09-18.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
