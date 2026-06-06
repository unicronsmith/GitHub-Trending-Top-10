# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-06）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 184,141 | +1,845 | 🔥 3天 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | Python | 15,095 | +2,473 | 🔥 5天 |
| 3 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | TypeScript | 32,936 | +366 | 🔥 2天 |
| 4 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | TypeScript | 26,308 | +1,152 | 🔥 3天 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 208,714 | +1,361 | 🔥 5天 |
| 6 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 21,914 | +148 | 🔥 2天 |
| 7 | [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) | Jupyter Notebook | 9,543 | +479 | 🔥 3天 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | Python | 64,926 | +320 | 🔥 2天 |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 28,402 | +731 | 🔥 2天 |
| 10 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Python | 80,717 | +747 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-06-06.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
