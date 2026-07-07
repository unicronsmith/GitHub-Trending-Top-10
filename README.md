# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-07）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | TypeScript | 8,398 | +2,402 | NEW |
| 2 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | 20,087 | +1,781 | 🔥 4天 |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 71,573 | +1,311 | 🔥 2天 |
| 4 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 78,081 | +1,122 | 🔥 2天 |
| 5 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 52,421 | +1,704 | 🔥 4天 |
| 6 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | Rust | 8,165 | +665 | NEW |
| 7 | [AhmadIbrahiim/Website-downloader](https://github.com/AhmadIbrahiim/Website-downloader) | HTML | 3,611 | +173 | NEW |
| 8 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | Swift | 16,915 | +377 | NEW |
| 9 | [dotnet/skills](https://github.com/dotnet/skills) | C# | 4,213 | +200 | NEW |
| 10 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | C# | 9,279 | +802 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-07.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
