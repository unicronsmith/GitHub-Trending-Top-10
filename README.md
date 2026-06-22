# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 10,946 | +2,935 | 🔥 4天 |
| 2 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | Swift | 6,798 | +2,462 | 🔥 4天 |
| 3 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 31,930 | +614 | NEW |
| 4 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 18,313 | +957 | 🔥 2天 |
| 5 | [penpot/penpot](https://github.com/penpot/penpot) | Clojure | 52,672 | +730 | 🔥 3天 |
| 6 | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | TypeScript | 82,547 | +394 | NEW |
| 7 | [garrytan/gstack](https://github.com/garrytan/gstack) | TypeScript | 112,803 | +454 | NEW |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | TypeScript | 29,753 | +369 | NEW |
| 9 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | Rust | 21,137 | +538 | 🔥 3天 |
| 10 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Python | 73,030 | +736 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
