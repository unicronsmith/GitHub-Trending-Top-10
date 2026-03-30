# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-03-30）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Python | 28,343 | +1,056 | NEW |
| 2 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Python | 8,873 | +1,165 | NEW |
| 3 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | TypeScript | 16,896 | +835 | NEW |
| 4 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | HTML | 24,905 | +1,050 | NEW |
| 5 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | Python | 85,846 | +1,132 | 🔥 3天 |
| 6 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Python | 64,249 | +137 | NEW |
| 7 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | TypeScript | 439,322 | +122 | NEW |
| 8 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | Python | 74,254 | +68 | NEW |
| 9 | [apache/superset](https://github.com/apache/superset) | TypeScript | 71,661 | +430 | 🔥 2天 |
| 10 | [fastfetch-cli/fastfetch](https://github.com/fastfetch-cli/fastfetch) | C | 21,278 | +37 | NEW |

📄 [查看完整 PDF 报告](reports/2026-03-30.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
