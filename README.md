# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-14）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 120,221 | +996 | 🔥 3天 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 169,321 | +1,559 | NEW |
| 3 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Rust | 4,054 | +1,295 | 🔥 3天 |
| 4 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | TypeScript | 68,511 | +1,229 | 🔥 2天 |
| 5 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | Python | 61,660 | +330 | NEW |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | CSS | 5,685 | +794 | 🔥 2天 |
| 7 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Python | 22,404 | +1,153 | 🔥 3天 |
| 8 | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | PowerShell | 51,247 | +118 | 🔥 2天 |
| 9 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | HTML | 13,058 | +451 | 🔥 2天 |
| 10 | [penpot/penpot](https://github.com/penpot/penpot) | Clojure | 55,892 | +264 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-14.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
