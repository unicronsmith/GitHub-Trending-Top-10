# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-08）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Python | 28,490 | +422 | NEW |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 33,943 | +1,070 | NEW |
| 3 | [openai/skills](https://github.com/openai/skills) | Python | 26,326 | +490 | NEW |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 253,779 | +1,426 | 🔥 6天 |
| 5 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | TypeScript | 47,410 | +2,628 | 🔥 2天 |
| 6 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | JavaScript | 48,535 | +666 | 🔥 2天 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 283,129 | +446 | NEW |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Unknown | 211,149 | +325 | NEW |
| 9 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 181,344 | +2,045 | 🔥 2天 |
| 10 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | JavaScript | 10,237 | +872 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-09-08.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
