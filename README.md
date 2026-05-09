# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-09）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 16,550 | +3,660 | 🔥 4天 |
| 2 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | TypeScript | 31,052 | +850 | NEW |
| 3 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | TypeScript | 3,015 | +400 | NEW |
| 4 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | Python | 45,320 | +667 | NEW |
| 5 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | JavaScript | 8,165 | +294 | NEW |
| 6 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | TypeScript | 13,524 | +144 | NEW |
| 7 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 38,590 | +145 | NEW |
| 8 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | Go | 2,067 | +595 | NEW |
| 9 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | TypeScript | 5,927 | +513 | NEW |
| 10 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | Jupyter Notebook | 36,362 | +189 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-09.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
