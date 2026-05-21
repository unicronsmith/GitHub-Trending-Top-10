# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-21）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 21,236 | +674 | 🔥 3天 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 11,961 | +2,123 | 🔥 3天 |
| 3 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Unknown | 142,278 | +2,679 | 🔥 2天 |
| 4 | [dotnet/skills](https://github.com/dotnet/skills) | C# | 2,016 | +96 | NEW |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 200,989 | +1,743 | 🔥 3天 |
| 6 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 38,867 | +890 | 🔥 5天 |
| 7 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | TypeScript | 5,155 | +741 | NEW |
| 8 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 40,278 | +132 | NEW |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 10,303 | +765 | 🔥 2天 |
| 10 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Python | 14,210 | +182 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-21.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
