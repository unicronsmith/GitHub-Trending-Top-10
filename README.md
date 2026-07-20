# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-20）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Python | 22,305 | +663 | 🔥 4天 |
| 2 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust | 9,225 | +235 | NEW |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | TypeScript | 20,709 | +1,343 | NEW |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 40,170 | +501 | 🔥 3天 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 134,366 | +949 | NEW |
| 6 | [kvcache-ai/ktransformers](https://github.com/kvcache-ai/ktransformers) | Python | 18,604 | +360 | 🔥 2天 |
| 7 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 43,810 | +610 | 🔥 2天 |
| 8 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | Python | 28,577 | +303 | NEW |
| 9 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | Python | 13,918 | +865 | NEW |
| 10 | [every-app/open-seo](https://github.com/every-app/open-seo) | TypeScript | 5,403 | +222 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-20.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
