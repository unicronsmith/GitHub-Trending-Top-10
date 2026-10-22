# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [php/php-src](https://github.com/php/php-src) | C | 40,901 | +110 | NEW |
| 2 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 31,364 | +303 | NEW |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 172,822 | +1,949 | 🔥 3天 |
| 4 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 38,457 | +2,979 | 🔥 3天 |
| 5 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 132,475 | +1,407 | NEW |
| 6 | [supabase/supabase](https://github.com/supabase/supabase) | TypeScript | 113,322 | +683 | 🔥 2天 |
| 7 | [fastapi/fastapi](https://github.com/fastapi/fastapi) | Python | 103,511 | +96 | NEW |
| 8 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Python | 42,760 | +428 | NEW |
| 9 | [Meloong-Git/PCL](https://github.com/Meloong-Git/PCL) | Visual Basic .NET | 8,598 | +115 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
