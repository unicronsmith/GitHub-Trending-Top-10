# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-08）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 8,370 | +51 | NEW |
| 2 | [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | Python | 4,184 | +215 | NEW |
| 3 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | Kotlin | 19,174 | +897 | 🔥 3天 |
| 4 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | Python | 8,206 | +662 | NEW |
| 5 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | C++ | 2,771 | +528 | 🔥 3天 |
| 6 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | Python | 10,252 | +636 | NEW |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 140,447 | +1,926 | NEW |
| 8 | [newton-physics/newton](https://github.com/newton-physics/newton) | Python | 3,885 | +67 | NEW |
| 9 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 24,987 | +1,195 | 🔥 3天 |
| 10 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | Python | 50,428 | +123 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-08.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
