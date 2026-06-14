# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-14）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | TypeScript | 119,769 | +530 | 🔥 2天 |
| 2 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | TypeScript | 446,887 | +114 | NEW |
| 3 | [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | Python | 13,934 | +8 | NEW |
| 4 | [swc-project/swc](https://github.com/swc-project/swc) | Rust | 33,704 | +20 | NEW |
| 5 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | Ruby | 31,030 | +83 | 🔥 2天 |
| 6 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | 4,824 | +804 | NEW |
| 7 | [meshery/meshery](https://github.com/meshery/meshery) | TypeScript | 10,290 | +3 | NEW |
| 8 | [cypress-io/cypress](https://github.com/cypress-io/cypress) | TypeScript | 49,762 | +7 | NEW |
| 9 | [GorvGoyl/Clone-Wars](https://github.com/GorvGoyl/Clone-Wars) | Unknown | 35,067 | +337 | NEW |
| 10 | [Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots](https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots) | TeX | 2,448 | +276 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-14.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
