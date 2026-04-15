# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-15）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 38,437 | +9,263 | 🔥 8天 |
| 2 | [pascalorg/editor](https://github.com/pascalorg/editor) | TypeScript | 12,142 | +820 | 🔥 2天 |
| 3 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 56,764 | +2,997 | 🔥 3天 |
| 4 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | Jupyter Notebook | 28,859 | +1,068 | NEW |
| 5 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | Python | 54,627 | +1,007 | 🔥 3天 |
| 6 | [chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11) | Assembly | 66,576 | +472 | 🔥 2天 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 153,334 | +1,919 | 🔥 2天 |
| 8 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 17,812 | +1,162 | 🔥 2天 |
| 9 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Python | 422,455 | +839 | NEW |
| 10 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | TypeScript | 2,178 | +1,020 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-15.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
