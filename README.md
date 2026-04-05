# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-05）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | Python | 3,749 | +343 | NEW |
| 2 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | Python | 24,573 | +1,197 | 🔥 2天 |
| 3 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | TypeScript | 16,128 | +1,789 | 🔥 3天 |
| 4 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | TypeScript | 21,273 | +1,591 | 🔥 3天 |
| 5 | [telegramdesktop/tdesktop](https://github.com/telegramdesktop/tdesktop) | C++ | 30,915 | +249 | NEW |
| 6 | [block/goose](https://github.com/block/goose) | Rust | 35,961 | +935 | NEW |
| 7 | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | 8,838 | +72 | NEW |
| 8 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | Python | 79,697 | +994 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-04-05.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
