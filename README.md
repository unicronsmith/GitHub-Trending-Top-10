# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-15）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 17,855 | +3,646 | 🔥 4天 |
| 2 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | Python | 5,795 | +662 | 🔥 2天 |
| 3 | [megadose/holehe](https://github.com/megadose/holehe) | Python | 12,962 | +427 | 🔥 2天 |
| 4 | [macro-inc/macro](https://github.com/macro-inc/macro) | Rust | 3,158 | +436 | 🔥 4天 |
| 5 | [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) | Python | 21,038 | +293 | 🔥 2天 |
| 6 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | JavaScript | 10,560 | +165 | NEW |
| 7 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | TypeScript | 7,495 | +769 | NEW |
| 8 | [github/spec-kit](https://github.com/github/spec-kit) | Python | 128,766 | +1,160 | NEW |
| 9 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | TypeScript | 6,081 | +579 | NEW |
| 10 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Go | 88,509 | +473 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-15.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
