# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-17）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cordiverse/cordis](https://github.com/cordiverse/cordis) | TypeScript | 5,318 | +720 | 🔥 2天 |
| 2 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | Shell | 25,781 | +270 | NEW |
| 3 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | Python | 72,981 | +572 | 🔥 2天 |
| 4 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | TypeScript | 84,285 | +150 | NEW |
| 5 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Python | 462,644 | +1,588 | 🔥 2天 |
| 6 | [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) | JavaScript | 40,345 | +452 | NEW |
| 7 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | Python | 6,947 | +443 | 🔥 4天 |

📄 [查看完整 PDF 报告](reports/2026-08-17.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
