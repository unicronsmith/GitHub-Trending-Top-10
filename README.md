# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-03）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [fmtlib/fmt](https://github.com/fmtlib/fmt) | C++ | 24,786 | +955 | 🔥 2天 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 246,383 | +1,576 | NEW |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 240,574 | +778 | 🔥 2天 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 122,881 | +2,138 | 🔥 2天 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | Python | 173,460 | +277 | NEW |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 246,763 | +749 | NEW |
| 7 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Go | 102,920 | +545 | NEW |
| 8 | [blader/humanizer](https://github.com/blader/humanizer) | Python | 41,123 | +1,214 | NEW |
| 9 | [google-research/timesfm](https://github.com/google-research/timesfm) | Python | 30,579 | +1,626 | 🔥 2天 |
| 10 | [averygan/reclip](https://github.com/averygan/reclip) | HTML | 8,199 | +673 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-03.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
