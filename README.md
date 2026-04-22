# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | TypeScript | 7,018 | +169 | 🔥 2天 |
| 2 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | Python | 12,484 | +2,548 | 🔥 3天 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 51,014 | +1,187 | NEW |
| 4 | [langfuse/langfuse](https://github.com/langfuse/langfuse) | TypeScript | 25,345 | +67 | NEW |
| 5 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | TypeScript | 39,212 | +346 | NEW |
| 6 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | TypeScript | 11,847 | +609 | NEW |
| 7 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 49,147 | +824 | 🔥 3天 |
| 8 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | Python | 17,252 | +162 | 🔥 2天 |
| 9 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | Python | 54,142 | +534 | 🔥 2天 |
| 10 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | Python | 5,127 | +237 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
