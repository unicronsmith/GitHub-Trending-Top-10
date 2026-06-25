# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-25）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | TypeScript | 18,057 | +619 | 🔥 2天 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 21,265 | +3,719 | 🔥 7天 |
| 3 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | Python | 1,525 | +201 | NEW |
| 4 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | TypeScript | 6,168 | +112 | NEW |
| 5 | [apple/container](https://github.com/apple/container) | Swift | 42,819 | +1,838 | 🔥 2天 |
| 6 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | TypeScript | 19,921 | +692 | 🔥 2天 |
| 7 | [garrytan/gstack](https://github.com/garrytan/gstack) | TypeScript | 115,334 | +922 | NEW |
| 8 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | Python | 1,011 | +15 | NEW |
| 9 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 20,832 | +1,031 | NEW |
| 10 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | TypeScript | 19,597 | +280 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-25.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
