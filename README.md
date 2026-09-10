# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-10）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Python | 36,896 | +3,854 | 🔥 3天 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | JavaScript | 22,572 | +1,588 | NEW |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 284,443 | +731 | 🔥 3天 |
| 4 | [alsk1992/CloddsBot](https://github.com/alsk1992/CloddsBot) | TypeScript | 1,373 | +299 | NEW |
| 5 | [Tencent/teamai-cli](https://github.com/Tencent/teamai-cli) | TypeScript | 3,552 | +837 | 🔥 2天 |
| 6 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | Rust | 35,547 | +247 | NEW |
| 7 | [liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes) | Unknown | 18,489 | +891 | 🔥 2天 |
| 8 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 37,358 | +1,287 | 🔥 3天 |
| 9 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | JavaScript | 30,649 | +957 | 🔥 2天 |
| 10 | [armory3d/armorpaint](https://github.com/armory3d/armorpaint) | C | 4,268 | +73 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-10.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
