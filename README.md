# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | TypeScript | 19,495 | +1,393 | 🔥 2天 |
| 2 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 25,795 | +2,549 | 🔥 5天 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 17,805 | +3,684 | 🔥 5天 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 12,688 | +988 | 🔥 4天 |
| 5 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | Python | 22,853 | +367 | NEW |
| 6 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Unknown | 148,206 | +3,152 | NEW |
| 7 | [dotnet/skills](https://github.com/dotnet/skills) | C# | 2,650 | +389 | 🔥 3天 |
| 8 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 41,157 | +501 | 🔥 3天 |
| 9 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 6,861 | +238 | NEW |
| 10 | [presenton/presenton](https://github.com/presenton/presenton) | JavaScript | 6,007 | +302 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
