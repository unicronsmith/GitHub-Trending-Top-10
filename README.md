# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-02）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | Python | 5,044 | +1,266 | NEW |
| 2 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 140,487 | +3,616 | 🔥 6天 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 202,993 | +1,842 | NEW |
| 4 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Python | 58,780 | +1,196 | 🔥 2天 |
| 5 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | Python | 12,264 | +1,725 | 🔥 2天 |
| 6 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | TypeScript | 4,301 | +319 | NEW |
| 7 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Python | 24,814 | +779 | NEW |
| 8 | [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Jupyter Notebook | 18,194 | +570 | NEW |
| 9 | [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | Python | 6,240 | +31 | NEW |
| 10 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | TypeScript | 24,397 | +677 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-06-02.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
