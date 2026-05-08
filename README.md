# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-08）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 13,347 | +1,343 | 🔥 3天 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 33,815 | +3,062 | 🔥 3天 |
| 3 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | Rust | 20,989 | +5,799 | 🔥 6天 |
| 4 | [z-lab/dflash](https://github.com/z-lab/dflash) | Python | 3,635 | +671 | 🔥 2天 |
| 5 | [decolua/9router](https://github.com/decolua/9router) | JavaScript | 5,079 | +149 | 🔥 2天 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Python | 2,375 | +482 | NEW |
| 7 | [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | Python | 1,602 | +31 | NEW |
| 8 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | Python | 14,284 | +189 | NEW |
| 9 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | Python | 6,523 | +559 | 🔥 3天 |
| 10 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | TypeScript | 76,225 | +74 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-08.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
