# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-15）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | TypeScript | 69,866 | +4,276 | 🔥 3天 |
| 2 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | CSS | 6,635 | +1,015 | 🔥 3天 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 171,419 | +1,679 | 🔥 2天 |
| 4 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | TypeScript | 42,308 | +537 | NEW |
| 5 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Rust | 4,554 | +473 | 🔥 4天 |
| 6 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Python | 23,299 | +1,256 | 🔥 4天 |
| 7 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | Rust | 65,124 | +607 | NEW |
| 8 | [par274/sharpemu](https://github.com/par274/sharpemu) | C# | 2,388 | +332 | NEW |
| 9 | [1c7/chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) | Python | 55,697 | +1,196 | NEW |
| 10 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Python | 26,004 | +128 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-15.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
