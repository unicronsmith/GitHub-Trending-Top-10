# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-11）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | TypeScript | 7,646 | +328 | 🔥 3天 |
| 2 | [oven-sh/bun](https://github.com/oven-sh/bun) | Rust | 94,480 | +209 | 🔥 2天 |
| 3 | [abseil/abseil-cpp](https://github.com/abseil/abseil-cpp) | C++ | 17,562 | +89 | 🔥 2天 |
| 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 77,105 | +1,116 | 🔥 6天 |
| 5 | [jbeder/yaml-cpp](https://github.com/jbeder/yaml-cpp) | C++ | 6,115 | +69 | 🔥 2天 |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 165,177 | +1,712 | 🔥 2天 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 252,103 | +1,013 | 🔥 2天 |
| 8 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | TypeScript | 109,850 | +177 | 🔥 2天 |
| 9 | [catchorg/Catch2](https://github.com/catchorg/Catch2) | C++ | 20,649 | +76 | 🔥 2天 |
| 10 | [chriskohlhoff/asio](https://github.com/chriskohlhoff/asio) | C++ | 6,104 | +92 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-07-11.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
