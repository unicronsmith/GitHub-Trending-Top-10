# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-10）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | TypeScript | 6,793 | +185 | 🔥 2天 |
| 2 | [oven-sh/bun](https://github.com/oven-sh/bun) | Rust | 93,894 | +82 | NEW |
| 3 | [abseil/abseil-cpp](https://github.com/abseil/abseil-cpp) | C++ | 17,469 | +3 | NEW |
| 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 76,463 | +2,554 | 🔥 5天 |
| 5 | [jbeder/yaml-cpp](https://github.com/jbeder/yaml-cpp) | C++ | 6,044 | +65 | NEW |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 163,957 | +1,728 | NEW |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 251,444 | +1,096 | NEW |
| 8 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | TypeScript | 109,720 | +166 | NEW |
| 9 | [catchorg/Catch2](https://github.com/catchorg/Catch2) | C++ | 20,568 | +69 | NEW |
| 10 | [chriskohlhoff/asio](https://github.com/chriskohlhoff/asio) | C++ | 6,032 | +87 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-10.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
