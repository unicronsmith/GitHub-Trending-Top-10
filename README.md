# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-22）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 67,378 | +1,295 | 🔥 2天 |
| 2 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 82,939 | +1,114 | NEW |
| 3 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Python | 7,586 | +1,866 | 🔥 2天 |
| 4 | [schollz/croc](https://github.com/schollz/croc) | Go | 37,151 | +361 | NEW |
| 5 | [likec4/likec4](https://github.com/likec4/likec4) | TypeScript | 4,061 | +58 | NEW |
| 6 | [chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11) | Assembly | 70,271 | +1,235 | NEW |
| 7 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 45,378 | +565 | NEW |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | TypeScript | 24,322 | +2,034 | NEW |
| 9 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 32,427 | +134 | NEW |
| 10 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Python | 68,484 | +155 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-22.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
