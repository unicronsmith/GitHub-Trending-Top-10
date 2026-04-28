# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-28）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 33,934 | +5,645 | 🔥 3天 |
| 2 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 32,265 | +1,102 | 🔥 2天 |
| 3 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | Python | 3,300 | +638 | 🔥 2天 |
| 4 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Python | 43,703 | +757 | 🔥 2天 |
| 5 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Python | 25,963 | +154 | 🔥 3天 |
| 6 | [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack) | Python | 10,073 | +348 | NEW |
| 7 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | JavaScript | 1,363 | +200 | NEW |
| 8 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Python | 427,475 | +600 | NEW |
| 9 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | Go | 2,104 | +138 | NEW |
| 10 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 16,866 | +2,949 | 🔥 6天 |

📄 [查看完整 PDF 报告](reports/2026-04-28.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
