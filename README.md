# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-04）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | JavaScript | 23,551 | +634 | 🔥 2天 |
| 2 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | JavaScript | 83,392 | +2,863 | 🔥 3天 |
| 3 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | TypeScript | 22,677 | +1,110 | NEW |
| 4 | [usestrix/strix](https://github.com/usestrix/strix) | Python | 35,427 | +2,803 | 🔥 5天 |
| 5 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 45,609 | +405 | 🔥 3天 |
| 6 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | 14,404 | +607 | NEW |
| 7 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 48,391 | +432 | NEW |
| 8 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | Python | 26,372 | +793 | 🔥 2天 |
| 9 | [rommapp/romm](https://github.com/rommapp/romm) | Python | 9,951 | +239 | 🔥 2天 |
| 10 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | Rust | 11,065 | +478 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-04.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
