# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-25）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | TypeScript | 29,357 | +5,625 | 🔥 4天 |
| 2 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 14,649 | +1,448 | 🔥 2天 |
| 3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 17,818 | +3,167 | 🔥 6天 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 191,731 | +2,052 | NEW |
| 5 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 8,850 | +999 | NEW |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 24,113 | +3,171 | 🔥 7天 |
| 7 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | Swift | 19,311 | +598 | NEW |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Unknown | 153,592 | +2,753 | 🔥 3天 |
| 9 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | Python | 23,662 | +462 | NEW |
| 10 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | Python | 41,125 | +151 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-25.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
