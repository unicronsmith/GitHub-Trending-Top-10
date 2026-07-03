# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-03）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | Python | 33,574 | +2,137 | 🔥 4天 |
| 2 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | JavaScript | 22,917 | +352 | NEW |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | JavaScript | 82,368 | +926 | 🔥 2天 |
| 4 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | Java | 77,232 | +77 | NEW |
| 5 | [actions/checkout](https://github.com/actions/checkout) | TypeScript | 8,216 | +26 | 🔥 2天 |
| 6 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 45,320 | +104 | 🔥 2天 |
| 7 | [ansible/ansible](https://github.com/ansible/ansible) | Python | 69,088 | +50 | NEW |
| 8 | [facebook/astryx](https://github.com/facebook/astryx) | TypeScript | 4,081 | +1,108 | NEW |
| 9 | [rommapp/romm](https://github.com/rommapp/romm) | Python | 9,561 | +236 | NEW |
| 10 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | Python | 25,944 | +68 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-03.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
