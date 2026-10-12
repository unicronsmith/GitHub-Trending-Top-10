# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-12）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 147,911 | +45,495 | 🔥 7天 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | JavaScript | 53,291 | +1,903 | 🔥 2天 |
| 3 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 27,129 | +394 | NEW |
| 4 | [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 21,154 | +4,106 | 🔥 5天 |
| 5 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | Python | 154,791 | +142 | NEW |
| 6 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 52,307 | +2,100 | 🔥 6天 |
| 7 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 37,361 | +886 | 🔥 2天 |
| 8 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | C++ | 40,839 | +134 | NEW |
| 9 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 58,825 | +705 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-12.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
