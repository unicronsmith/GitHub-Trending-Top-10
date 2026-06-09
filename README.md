# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-09）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 36,169 | +3,177 | 🔥 5天 |
| 2 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | Python | 9,759 | +1,800 | 🔥 2天 |
| 3 | [roboflow/supervision](https://github.com/roboflow/supervision) | Python | 42,687 | +735 | NEW |
| 4 | [opencv/opencv](https://github.com/opencv/opencv) | C++ | 88,430 | +395 | NEW |
| 5 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | TypeScript | 14,046 | +821 | 🔥 2天 |
| 6 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | 48,318 | +490 | NEW |
| 7 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | Python | 3,806 | +631 | 🔥 2天 |
| 8 | [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | Roff | 73,349 | +517 | NEW |
| 9 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Unknown | 139,010 | +66 | NEW |
| 10 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | TypeScript | 19,667 | +786 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-09.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
