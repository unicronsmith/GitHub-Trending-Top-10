# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-12）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 1,978 | +366 | 🔥 2天 |
| 2 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | TypeScript | 5,252 | +430 | NEW |
| 3 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Python | 7,037 | +1,320 | 🔥 3天 |
| 4 | [apernet/hysteria](https://github.com/apernet/hysteria) | Go | 19,991 | +28 | NEW |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 74,472 | +3,886 | NEW |
| 6 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | Java | 2,055 | +111 | NEW |
| 7 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | TypeScript | 8,436 | +212 | 🔥 2天 |
| 8 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Jupyter Notebook | 93,375 | +337 | NEW |
| 9 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | Python | 47,925 | +1,248 | NEW |
| 10 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | TypeScript | 11,497 | +427 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-05-12.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
