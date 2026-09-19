# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-19）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 15,234 | +3,162 | 🔥 4天 |
| 2 | [trycua/cua](https://github.com/trycua/cua) | HTML | 23,934 | +383 | NEW |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 96,724 | +547 | 🔥 3天 |
| 4 | [coder/coder](https://github.com/coder/coder) | Go | 15,461 | +406 | NEW |
| 5 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | TypeScript | 146,545 | +482 | 🔥 3天 |
| 6 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | TypeScript | 15,751 | +477 | NEW |
| 7 | [higgsfield-ai/higgsfield](https://github.com/higgsfield-ai/higgsfield) | Jupyter Notebook | 4,725 | +325 | NEW |
| 8 | [docling-project/docling](https://github.com/docling-project/docling) | Python | 66,776 | +94 | NEW |
| 9 | [cloudflare/quiche](https://github.com/cloudflare/quiche) | Rust | 11,883 | +5 | NEW |
| 10 | [asciimoo/hister](https://github.com/asciimoo/hister) | Go | 5,110 | +430 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-19.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
