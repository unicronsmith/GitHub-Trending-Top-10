# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-31）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Python | 11,222 | +4,232 | 🔥 2天 |
| 2 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Python | 32,149 | +2,492 | 🔥 2天 |
| 3 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | TypeScript | 18,007 | +1,791 | 🔥 2天 |
| 4 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | HTML | 27,274 | +1,108 | 🔥 2天 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 19,436 | +1,851 | NEW |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 127,012 | +2,846 | NEW |
| 7 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | Python | 16,062 | +251 | NEW |
| 8 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Python | 73,789 | +440 | NEW |
| 9 | [Dimillian/Skills](https://github.com/Dimillian/Skills) | Shell | 2,641 | +173 | NEW |
| 10 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | Python | 75,102 | +76 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-03-31.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
