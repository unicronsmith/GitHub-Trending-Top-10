# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-01）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 122,010 | +1,791 | 🔥 3天 |
| 2 | [usestrix/strix](https://github.com/usestrix/strix) | Python | 28,734 | +515 | 🔥 2天 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Python | 16,186 | +721 | NEW |
| 4 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | HTML | 7,971 | +1,343 | NEW |
| 5 | [facebook/astryx](https://github.com/facebook/astryx) | TypeScript | 2,132 | +364 | NEW |
| 6 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | TypeScript | 9,106 | +387 | 🔥 2天 |
| 7 | [allenai/olmocr](https://github.com/allenai/olmocr) | Python | 18,074 | +295 | NEW |
| 8 | [logto-io/logto](https://github.com/logto-io/logto) | TypeScript | 13,075 | +561 | NEW |
| 9 | [togatoga/karukan](https://github.com/togatoga/karukan) | Rust | 526 | +29 | NEW |
| 10 | [Mebus/cupp](https://github.com/Mebus/cupp) | Python | 6,195 | +32 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-07-01.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
