# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-06）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | Rust | 11,450 | +2,434 | 🔥 4天 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 29,089 | +629 | NEW |
| 3 | [PriorLabs/TabPFN](https://github.com/PriorLabs/TabPFN) | Python | 6,470 | +57 | NEW |
| 4 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | Ruby | 14,371 | +927 | 🔥 2天 |
| 5 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | Python | 5,412 | +197 | NEW |
| 6 | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | C++ | 62,824 | +87 | NEW |
| 7 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | TypeScript | 8,229 | +213 | NEW |
| 8 | [virattt/dexter](https://github.com/virattt/dexter) | TypeScript | 24,116 | +659 | 🔥 3天 |
| 9 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 8,507 | +540 | NEW |
| 10 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 44,657 | +2,432 | 🔥 4天 |

📄 [查看完整 PDF 报告](reports/2026-05-06.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
