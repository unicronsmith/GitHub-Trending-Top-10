# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-14）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 29,031 | +5,733 | 🔥 7天 |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 54,443 | +3,175 | 🔥 2天 |
| 3 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 16,717 | +512 | NEW |
| 4 | [pascalorg/editor](https://github.com/pascalorg/editor) | TypeScript | 10,704 | +769 | NEW |
| 5 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 107,767 | +2,808 | 🔥 5天 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 151,332 | +1,928 | NEW |
| 7 | [chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11) | Assembly | 65,936 | +390 | NEW |
| 8 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | Python | 53,565 | +783 | 🔥 2天 |
| 9 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 17,483 | +1,554 | 🔥 6天 |
| 10 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 81,912 | +11,289 | 🔥 6天 |

📄 [查看完整 PDF 报告](reports/2026-04-14.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
