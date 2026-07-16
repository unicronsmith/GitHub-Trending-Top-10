# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-16）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [apache/ossie](https://github.com/apache/ossie) | Python | 730 | +34 | NEW |
| 2 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | CSS | 10,087 | +1,277 | 🔥 4天 |
| 3 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | TypeScript | 73,440 | +1,664 | 🔥 4天 |
| 4 | [PostHog/posthog](https://github.com/PostHog/posthog) | Python | 35,595 | +58 | NEW |
| 5 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | Rust | 65,772 | +299 | 🔥 2天 |
| 6 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | Shell | 1,362 | +323 | NEW |
| 7 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | HTML | 14,694 | +949 | NEW |
| 8 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 122,387 | +1,236 | NEW |
| 9 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | TypeScript | 79,919 | +51 | NEW |
| 10 | [YimMenu/YimMenuV2](https://github.com/YimMenu/YimMenuV2) | C++ | 1,479 | +38 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-16.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
