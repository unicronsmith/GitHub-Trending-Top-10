# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-05）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | 15,783 | +718 | 🔥 2天 |
| 2 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | JavaScript | 25,090 | +718 | 🔥 3天 |
| 3 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 49,343 | +471 | 🔥 2天 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | JavaScript | 56,842 | +850 | NEW |
| 5 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Python | 20,299 | +136 | NEW |
| 6 | [rommapp/romm](https://github.com/rommapp/romm) | Python | 10,351 | +398 | 🔥 3天 |
| 7 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | Rust | 11,704 | +707 | 🔥 2天 |
| 8 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | TypeScript | 23,472 | +742 | 🔥 2天 |
| 9 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | Python | 26,695 | +443 | 🔥 3天 |
| 10 | [usestrix/strix](https://github.com/usestrix/strix) | Python | 36,541 | +1,904 | 🔥 6天 |

📄 [查看完整 PDF 报告](reports/2026-07-05.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
