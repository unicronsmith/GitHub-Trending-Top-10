# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-26）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | Haskell | 11,761 | +191 | NEW |
| 2 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | TypeScript | 20,430 | +1,475 | 🔥 3天 |
| 3 | [commaai/openpilot](https://github.com/commaai/openpilot) | Python | 61,621 | +67 | NEW |
| 4 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | Go | 3,134 | +996 | NEW |
| 5 | [grafana/grafana](https://github.com/grafana/grafana) | TypeScript | 74,713 | +17 | NEW |
| 6 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | HTML | 123,507 | +48 | NEW |
| 7 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Python | 70,053 | +644 | NEW |
| 8 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | Unknown | 9,147 | +220 | NEW |
| 9 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | TypeScript | 7,222 | +241 | 🔥 2天 |
| 10 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | Python | 2,792 | +309 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-26.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
