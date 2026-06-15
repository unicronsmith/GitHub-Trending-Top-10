# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-15）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | TypeScript | 122,575 | +2,650 | 🔥 3天 |
| 2 | [teslamate-org/teslamate](https://github.com/teslamate-org/teslamate) | Elixir | 8,171 | +35 | NEW |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 29,686 | +1,045 | NEW |
| 4 | [meshery/meshery](https://github.com/meshery/meshery) | TypeScript | 10,561 | +227 | 🔥 2天 |
| 5 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | Ruby | 31,533 | +431 | 🔥 3天 |
| 6 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | Java | 126,803 | +95 | NEW |
| 7 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | TypeScript | 447,700 | +738 | 🔥 2天 |
| 8 | [trycua/cua](https://github.com/trycua/cua) | HTML | 18,060 | +57 | NEW |
| 9 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | Unknown | 352,136 | +516 | NEW |
| 10 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 32,849 | +538 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-15.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
