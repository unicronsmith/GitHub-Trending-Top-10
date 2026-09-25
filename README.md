# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-25）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | TypeScript | 83,810 | +1,853 | NEW |
| 2 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 36,783 | +62 | NEW |
| 3 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Python | 28,738 | +1,652 | 🔥 2天 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 291,483 | +465 | 🔥 3天 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 269,492 | +671 | NEW |
| 6 | [dream-num/univer](https://github.com/dream-num/univer) | TypeScript | 18,186 | +1,048 | 🔥 4天 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills) | Python | 178,120 | +155 | NEW |
| 8 | [androoAGI/starnet](https://github.com/androoAGI/starnet) | JavaScript | 330 | +113 | NEW |
| 9 | [derv82/wifit3](https://github.com/derv82/wifit3) | Python | 743 | +168 | NEW |
| 10 | [kelseyhightower/kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way) | Unknown | 50,040 | +105 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-25.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
