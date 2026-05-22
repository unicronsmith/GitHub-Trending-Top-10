# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 23,703 | +682 | 🔥 4天 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 15,539 | +4,294 | 🔥 4天 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 63,484 | +1,269 | NEW |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 11,260 | +1,333 | 🔥 3天 |
| 5 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 40,756 | +151 | 🔥 2天 |
| 6 | [dotnet/skills](https://github.com/dotnet/skills) | C# | 2,391 | +129 | 🔥 2天 |
| 7 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | TypeScript | 17,387 | +666 | NEW |
| 8 | [odoo/odoo](https://github.com/odoo/odoo) | Python | 50,918 | +48 | NEW |
| 9 | [byJoey/cfnew](https://github.com/byJoey/cfnew) | Unknown | 13,213 | +85 | NEW |
| 10 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | Unknown | 222,893 | +756 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
