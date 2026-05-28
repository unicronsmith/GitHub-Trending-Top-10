# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-28）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 65,191 | +1,742 | NEW |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 196,815 | +1,388 | 🔥 4天 |
| 3 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Shell | 25,579 | +2,235 | 🔥 3天 |
| 4 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | Unknown | 6,146 | +755 | 🔥 3天 |
| 5 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 47,621 | +495 | 🔥 2天 |
| 6 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | HTML | 170,161 | +1,769 | NEW |
| 7 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | Unknown | 47,915 | +2,015 | NEW |
| 8 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 126,933 | +1,263 | NEW |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 210,627 | +1,726 | NEW |
| 10 | [revfactory/harness](https://github.com/revfactory/harness) | HTML | 3,720 | +68 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-28.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
