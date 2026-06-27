# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-27）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | Haskell | 13,135 | +432 | 🔥 2天 |
| 2 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | Python | 3,428 | +1,274 | 🔥 3天 |
| 3 | [commaai/openpilot](https://github.com/commaai/openpilot) | Python | 61,927 | +80 | 🔥 2天 |
| 4 | [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | Go | 35,575 | +619 | NEW |
| 5 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | HTML | 123,929 | +90 | 🔥 2天 |
| 6 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | TypeScript | 21,918 | +2,407 | 🔥 4天 |
| 7 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | C | 135,578 | +67 | NEW |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Python | 32,613 | +589 | NEW |
| 9 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | TypeScript | 21,699 | +1,088 | NEW |
| 10 | [garrytan/gstack](https://github.com/garrytan/gstack) | TypeScript | 116,879 | +950 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-27.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
