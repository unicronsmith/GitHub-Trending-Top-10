# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [huggingface/ml-intern](https://github.com/huggingface/ml-intern) | Python | 1,483 | +530 | NEW |
| 2 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | TypeScript | 8,034 | +1,023 | 🔥 3天 |
| 3 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | Python | 17,828 | +574 | 🔥 3天 |
| 4 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | Python | 60,327 | +518 | NEW |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 49,549 | +427 | 🔥 4天 |
| 6 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | JavaScript | 6,501 | +677 | NEW |
| 7 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 3,899 | +181 | NEW |
| 8 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | TypeScript | 12,613 | +521 | 🔥 2天 |
| 9 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | Jupyter Notebook | 58,451 | +177 | NEW |
| 10 | [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | C# | 52,642 | +70 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
