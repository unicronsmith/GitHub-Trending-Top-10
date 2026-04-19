# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-19）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | TypeScript | 1,841 | +447 | NEW |
| 2 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | Dart | 10,715 | +609 | 🔥 3天 |
| 3 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Python | 22,717 | +470 | NEW |
| 4 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | JavaScript | 5,217 | +1,131 | 🔥 3天 |
| 5 | [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | Cuda | 6,614 | +31 | NEW |
| 6 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | Jupyter Notebook | 32,262 | +547 | 🔥 5天 |
| 7 | [aaddrick/claude-desktop-debian](https://github.com/aaddrick/claude-desktop-debian) | Shell | 3,535 | +44 | NEW |
| 8 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | Rust | 112,252 | +393 | NEW |
| 9 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Shell | 3,363 | +403 | 🔥 3天 |
| 10 | [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | HTML | 834 | +135 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-19.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
