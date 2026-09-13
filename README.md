# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-13）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | C | 29,043 | +652 | NEW |
| 2 | [ever-co/ever-gauzy](https://github.com/ever-co/ever-gauzy) | TypeScript | 4,642 | +58 | NEW |
| 3 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | JavaScript | 31,104 | +2,898 | 🔥 4天 |
| 4 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | TypeScript | 5,423 | +215 | NEW |
| 5 | [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | TypeScript | 2,032 | +444 | 🔥 3天 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 58,134 | +383 | NEW |
| 7 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 65,760 | +727 | 🔥 2天 |
| 8 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | Go | 23,718 | +613 | NEW |
| 9 | [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | Python | 7,558 | +500 | NEW |
| 10 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | Java | 33,325 | +238 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-09-13.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
