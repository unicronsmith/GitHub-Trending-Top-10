# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-05）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 181,970 | +1,821 | 🔥 2天 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | Python | 13,902 | +2,503 | 🔥 4天 |
| 3 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | TypeScript | 32,347 | +350 | NEW |
| 4 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | TypeScript | 25,560 | +1,142 | 🔥 2天 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 207,900 | +1,368 | 🔥 4天 |
| 6 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 21,267 | +127 | NEW |
| 7 | [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) | Jupyter Notebook | 9,268 | +494 | 🔥 2天 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | Python | 64,470 | +324 | NEW |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 27,994 | +738 | NEW |
| 10 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Python | 80,308 | +755 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-05.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
