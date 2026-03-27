# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-27）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 11,568 | +2,685 | 🔥 3天 |
| 2 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | TypeScript | 13,291 | +598 | 🔥 2天 |
| 3 | [virattt/dexter](https://github.com/virattt/dexter) | TypeScript | 19,302 | +210 | 🔥 2天 |
| 4 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 43,582 | +1,002 | 🔥 2天 |
| 5 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Python | 49,562 | +2,394 | 🔥 4天 |
| 6 | [Vaibhavs10/insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper) | Jupyter Notebook | 11,603 | +1,370 | 🔥 2天 |
| 7 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | Python | 20,921 | +437 | 🔥 2天 |
| 8 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 41,593 | +117 | 🔥 2天 |
| 9 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | Python | 6,557 | +557 | 🔥 2天 |
| 10 | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | JavaScript | 687 | +33 | NEW |

📄 [查看完整 PDF 报告](reports/2026-03-27.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
