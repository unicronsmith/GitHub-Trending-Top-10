# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-30）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | Python | 27,567 | +395 | NEW |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 119,962 | +1,425 | 🔥 2天 |
| 3 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | Swift | 4,691 | +830 | 🔥 3天 |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | TypeScript | 8,091 | +617 | NEW |
| 5 | [browser-use/video-use](https://github.com/browser-use/video-use) | Python | 12,305 | +967 | 🔥 2天 |
| 6 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | Python | 7,264 | +1,386 | 🔥 6天 |
| 7 | [Mebus/cupp](https://github.com/Mebus/cupp) | Python | 6,010 | +18 | NEW |
| 8 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | HTML | 127,110 | +1,935 | 🔥 5天 |
| 9 | [google/agents-cli](https://github.com/google/agents-cli) | Python | 3,808 | +433 | NEW |
| 10 | [roboflow/supervision](https://github.com/roboflow/supervision) | Python | 45,723 | +336 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-30.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
