# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-14）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | C | 31,466 | +2,233 | 🔥 2天 |
| 2 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Go | 24,985 | +1,796 | NEW |
| 3 | [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | Python | 8,176 | +578 | 🔥 2天 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 28,633 | +2,774 | NEW |
| 5 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | Python | 72,960 | +524 | NEW |
| 6 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 80,973 | +640 | NEW |
| 7 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 66,581 | +770 | 🔥 3天 |
| 8 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | Python | 1,888 | +52 | NEW |
| 9 | [localsend/localsend](https://github.com/localsend/localsend) | Dart | 91,105 | +213 | NEW |
| 10 | [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | Rust | 67,451 | +110 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-14.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
