# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-02）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | Python | 30,797 | +1,211 | 🔥 3天 |
| 2 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | JavaScript | 79,523 | +866 | NEW |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 124,953 | +2,114 | 🔥 4天 |
| 4 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | HTML | 8,882 | +2,470 | 🔥 2天 |
| 5 | [santifer/career-ops](https://github.com/santifer/career-ops) | JavaScript | 57,315 | +322 | NEW |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 243,958 | +1,047 | NEW |
| 7 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 44,925 | +92 | NEW |
| 8 | [browser-use/video-use](https://github.com/browser-use/video-use) | Python | 13,508 | +693 | NEW |
| 9 | [actions/checkout](https://github.com/actions/checkout) | TypeScript | 8,087 | +5 | NEW |
| 10 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 224,869 | +721 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-02.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
