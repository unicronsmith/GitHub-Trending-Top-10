# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-18）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [google-research/timesfm](https://github.com/google-research/timesfm) | Python | 22,384 | +858 | 🔥 2天 |
| 2 | [n0-computer/iroh](https://github.com/n0-computer/iroh) | Rust | 9,850 | +369 | 🔥 2天 |
| 3 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | TypeScript | 449,355 | +417 | NEW |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 231,896 | +1,435 | 🔥 2天 |
| 5 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | Unknown | 3,884 | +286 | NEW |
| 6 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | C | 6,516 | +2,308 | 🔥 2天 |
| 7 | [alibaba/zvec](https://github.com/alibaba/zvec) | C++ | 11,027 | +435 | NEW |
| 8 | [withastro/flue](https://github.com/withastro/flue) | TypeScript | 5,342 | +164 | NEW |
| 9 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | TypeScript | 21,449 | +1,339 | NEW |
| 10 | [makeplane/plane](https://github.com/makeplane/plane) | TypeScript | 51,610 | +610 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-18.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
