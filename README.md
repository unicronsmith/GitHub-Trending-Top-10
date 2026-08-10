# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-10）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Python | 3,619 | +967 | NEW |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 141,325 | +858 | NEW |
| 3 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Python | 60,680 | +215 | NEW |
| 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 85,438 | +680 | 🔥 6天 |
| 5 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | TypeScript | 76,144 | +167 | NEW |
| 6 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | TypeScript | 12,442 | +2,356 | 🔥 3天 |
| 7 | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | C++ | 65,130 | +190 | 🔥 2天 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 89,145 | +156 | NEW |
| 9 | [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | TypeScript | 17,601 | +143 | NEW |
| 10 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | TypeScript | 164,531 | +815 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-10.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
