# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-31）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | PowerShell | 10,021 | +612 | NEW |
| 2 | [different-ai/openwork](https://github.com/different-ai/openwork) | TypeScript | 19,119 | +915 | 🔥 3天 |
| 3 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 55,857 | +378 | 🔥 2天 |
| 4 | [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | Python | 11,459 | +621 | 🔥 2天 |
| 5 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | Jupyter Notebook | 54,871 | +155 | 🔥 2天 |
| 6 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | Java | 10,065 | +7 | NEW |
| 7 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | Ruby | 34,955 | +53 | NEW |
| 8 | [agavra/tuicr](https://github.com/agavra/tuicr) | Rust | 2,019 | +190 | NEW |
| 9 | [usekaneo/kaneo](https://github.com/usekaneo/kaneo) | TypeScript | 4,629 | +188 | NEW |
| 10 | [geo-tp/ESP32-Bit-Pirate](https://github.com/geo-tp/ESP32-Bit-Pirate) | C++ | 4,685 | +152 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-31.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
