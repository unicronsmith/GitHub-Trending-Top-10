# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-08）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | TypeScript | 7,379 | +2,293 | NEW |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 84,149 | +1,131 | 🔥 4天 |
| 3 | [cloudflare/computer](https://github.com/cloudflare/computer) | TypeScript | 6,148 | +872 | 🔥 3天 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 209,342 | +2,152 | 🔥 3天 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 268,996 | +782 | NEW |
| 6 | [goauthentik/authentik](https://github.com/goauthentik/authentik) | Python | 23,787 | +530 | 🔥 3天 |
| 7 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Python | 2,459 | +122 | NEW |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | Python | 70,683 | +141 | NEW |
| 9 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | Go | 7,189 | +55 | NEW |
| 10 | [jdx/mise](https://github.com/jdx/mise) | Rust | 32,137 | +135 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-08.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
