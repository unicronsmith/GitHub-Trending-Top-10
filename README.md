# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-04）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | Python | 11,439 | +3,139 | 🔥 3天 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 180,193 | +1,735 | NEW |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 206,583 | +1,736 | 🔥 3天 |
| 4 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Python | 79,583 | +105 | NEW |
| 5 | [github/spec-kit](https://github.com/github/spec-kit) | Python | 108,270 | +311 | NEW |
| 6 | [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) | Jupyter Notebook | 8,785 | +138 | NEW |
| 7 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | TypeScript | 24,430 | +227 | NEW |
| 8 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | Python | 9,295 | +583 | NEW |
| 9 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | Unknown | 349,451 | +330 | NEW |
| 10 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | Java | 8,821 | +25 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-04.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
