# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-11）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | TypeScript | 32,693 | +956 | 🔥 3天 |
| 2 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Python | 5,498 | +1,325 | 🔥 2天 |
| 3 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | TypeScript | 10,263 | +397 | NEW |
| 4 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | TypeScript | 7,075 | +533 | 🔥 3天 |
| 5 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | JavaScript | 9,634 | +808 | 🔥 3天 |
| 6 | [decolua/9router](https://github.com/decolua/9router) | JavaScript | 7,841 | +942 | NEW |
| 7 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 978 | +154 | NEW |
| 8 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | TypeScript | 7,660 | +312 | NEW |
| 9 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | Jupyter Notebook | 37,141 | +373 | NEW |
| 10 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Python | 162,823 | +29 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-11.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
