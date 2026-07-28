# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-28）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [pascalorg/editor](https://github.com/pascalorg/editor) | TypeScript | 18,240 | +412 | NEW |
| 2 | [jenkinsci/jenkins](https://github.com/jenkinsci/jenkins) | Java | 25,973 | +180 | 🔥 2天 |
| 3 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | TypeScript | 44,474 | +572 | 🔥 2天 |
| 4 | [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | Python | 15,563 | +185 | NEW |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 234,424 | +458 | NEW |
| 6 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | Python | 6,765 | +177 | NEW |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | Python | 10,720 | +366 | NEW |
| 8 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | TypeScript | 3,040 | +420 | NEW |
| 9 | [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | Python | 9,153 | +113 | NEW |
| 10 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | Python | 4,975 | +17 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-28.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
