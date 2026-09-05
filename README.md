# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-05）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 251,550 | +2,666 | 🔥 3天 |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 249,152 | +1,325 | 🔥 3天 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 127,210 | +2,813 | 🔥 4天 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 241,759 | +573 | 🔥 4天 |
| 5 | [fmtlib/fmt](https://github.com/fmtlib/fmt) | C++ | 25,533 | +133 | 🔥 4天 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | Python | 174,372 | +472 | 🔥 3天 |
| 7 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 31,383 | +852 | NEW |
| 8 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 204,441 | +725 | NEW |
| 9 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 70,562 | +127 | NEW |
| 10 | [humanlayer/skills](https://github.com/humanlayer/skills) | TypeScript | 2,491 | +1,141 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-05.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
