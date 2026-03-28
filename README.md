# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-28）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 13,297 | +2,821 | 🔥 4天 |
| 2 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | Python | 83,612 | +1,616 | NEW |
| 3 | [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | Python | 3,078 | +143 | NEW |
| 4 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Python | 24,894 | +337 | NEW |
| 5 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 42,162 | +668 | 🔥 3天 |
| 6 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | Python | 7,237 | +912 | 🔥 3天 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 119,495 | +2,752 | NEW |
| 8 | [virattt/dexter](https://github.com/virattt/dexter) | TypeScript | 19,883 | +672 | 🔥 3天 |
| 9 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | TypeScript | 14,324 | +1,411 | 🔥 3天 |
| 10 | [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | C++ | 29,796 | +79 | NEW |

📄 [查看完整 PDF 报告](reports/2026-03-28.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
