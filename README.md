# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-28）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | Haskell | 14,343 | +1,469 | 🔥 3天 |
| 2 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | HTML | 124,386 | +459 | 🔥 3天 |
| 3 | [commaai/openpilot](https://github.com/commaai/openpilot) | Python | 62,189 | +322 | 🔥 3天 |
| 4 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | Python | 4,909 | +685 | 🔥 4天 |
| 5 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | Python | 7,964 | +372 | NEW |
| 6 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | C | 18,526 | +2,162 | NEW |
| 7 | [cupy/cupy](https://github.com/cupy/cupy) | Python | 11,338 | +172 | NEW |
| 8 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | Swift | 3,246 | +264 | NEW |
| 9 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Python | 71,194 | +749 | NEW |
| 10 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Python | 13,951 | +92 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-28.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
