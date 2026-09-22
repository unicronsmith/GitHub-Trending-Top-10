# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 36,118 | +436 | 🔥 3天 |
| 2 | [agent-substrate/substrate](https://github.com/agent-substrate/substrate) | Go | 2,771 | +498 | NEW |
| 3 | [dream-num/univer](https://github.com/dream-num/univer) | TypeScript | 15,030 | +202 | NEW |
| 4 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Python | 30,962 | +33 | NEW |
| 5 | [google/ax](https://github.com/google/ax) | Go | 7,007 | +2,324 | NEW |
| 6 | [mvt-project/mvt](https://github.com/mvt-project/mvt) | Python | 13,832 | +441 | 🔥 2天 |
| 7 | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | 2,032 | +197 | NEW |
| 8 | [browser-use/video-use](https://github.com/browser-use/video-use) | Python | 25,593 | +155 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
