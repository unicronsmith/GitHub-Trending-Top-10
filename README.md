# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-26）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 8,765 | +1,341 | 🔥 2天 |
| 2 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | TypeScript | 11,896 | +576 | NEW |
| 3 | [virattt/dexter](https://github.com/virattt/dexter) | TypeScript | 18,651 | +274 | NEW |
| 4 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 42,719 | +1,082 | NEW |
| 5 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Python | 47,464 | +3,787 | 🔥 3天 |
| 6 | [Vaibhavs10/insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper) | Jupyter Notebook | 10,528 | +1,381 | NEW |
| 7 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | Python | 20,018 | +439 | NEW |
| 8 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 40,952 | +264 | NEW |
| 9 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | Python | 5,653 | +546 | NEW |

📄 [查看完整 PDF 报告](reports/2026-03-26.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
