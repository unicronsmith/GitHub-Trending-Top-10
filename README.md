# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-07）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 9,787 | +641 | 🔥 2天 |
| 2 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | Rust | 17,217 | +6,175 | 🔥 5天 |
| 3 | [z-lab/dflash](https://github.com/z-lab/dflash) | Python | 3,250 | +654 | NEW |
| 4 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | TypeScript | 8,674 | +230 | 🔥 2天 |
| 5 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | Python | 5,962 | +532 | 🔥 2天 |
| 6 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 32,158 | +800 | 🔥 2天 |
| 7 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Python | 29,172 | +953 | NEW |
| 8 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | TypeScript | 4,881 | +406 | NEW |
| 9 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | Ruby | 15,264 | +774 | 🔥 3天 |
| 10 | [decolua/9router](https://github.com/decolua/9router) | JavaScript | 4,086 | +130 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-07.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
