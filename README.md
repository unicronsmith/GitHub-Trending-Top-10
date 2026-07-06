# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-06）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 50,836 | +1,386 | 🔥 3天 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 70,355 | +1,114 | NEW |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | 18,463 | +2,493 | 🔥 3天 |
| 4 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 77,052 | +471 | NEW |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | JavaScript | 58,394 | +1,453 | 🔥 2天 |
| 6 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Python | 20,944 | +611 | 🔥 2天 |
| 7 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | JavaScript | 26,050 | +910 | 🔥 4天 |
| 8 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 49,526 | +237 | NEW |
| 9 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | Rust | 12,564 | +783 | 🔥 3天 |
| 10 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | Python | 3,845 | +368 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-06.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
