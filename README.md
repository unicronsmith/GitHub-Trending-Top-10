# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-04）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 249,111 | +2,757 | 🔥 2天 |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 124,594 | +1,683 | 🔥 3天 |
| 3 | [fmtlib/fmt](https://github.com/fmtlib/fmt) | C++ | 25,410 | +681 | 🔥 3天 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 247,899 | +1,139 | 🔥 2天 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | Python | 173,940 | +512 | 🔥 2天 |
| 6 | [blader/humanizer](https://github.com/blader/humanizer) | Python | 42,212 | +1,132 | 🔥 2天 |
| 7 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 241,247 | +721 | 🔥 3天 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Go | 103,393 | +503 | 🔥 2天 |
| 9 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | TypeScript | 2,186 | +395 | NEW |
| 10 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | Python | 4,411 | +68 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-04.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
