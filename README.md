# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-02）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | Jupyter Notebook | 58,364 | +949 | 🔥 4天 |
| 2 | [usekaneo/kaneo](https://github.com/usekaneo/kaneo) | TypeScript | 5,874 | +760 | 🔥 3天 |
| 3 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 25,151 | +242 | NEW |
| 4 | [iv-org/invidious](https://github.com/iv-org/invidious) | Crystal | 21,732 | +435 | NEW |
| 5 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 534,372 | +710 | NEW |
| 6 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | PowerShell | 12,410 | +1,320 | 🔥 3天 |
| 7 | [different-ai/openwork](https://github.com/different-ai/openwork) | TypeScript | 20,061 | +585 | 🔥 5天 |
| 8 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Jupyter Notebook | 114,461 | +108 | NEW |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 64,259 | +645 | NEW |
| 10 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TypeScript | 10,565 | +227 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-02.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
