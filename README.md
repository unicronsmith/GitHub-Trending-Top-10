# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-12）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | JavaScript | 28,311 | +2,265 | 🔥 3天 |
| 2 | [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | TypeScript | 1,586 | +505 | 🔥 2天 |
| 3 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 65,040 | +216 | NEW |
| 4 | [nab138/iloader](https://github.com/nab138/iloader) | TypeScript | 3,000 | +209 | 🔥 2天 |
| 5 | [Flowseal/zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) | Batchfile | 33,167 | +52 | NEW |
| 6 | [jihe520/MathModelAgent](https://github.com/jihe520/MathModelAgent) | Python | 5,019 | +264 | NEW |
| 7 | [Sonarr/Sonarr](https://github.com/Sonarr/Sonarr) | C# | 15,837 | +228 | 🔥 2天 |
| 8 | [alsk1992/CloddsBot](https://github.com/alsk1992/CloddsBot) | TypeScript | 2,322 | +377 | 🔥 3天 |
| 9 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | Java | 33,086 | +247 | NEW |
| 10 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 137,378 | +237 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-12.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
