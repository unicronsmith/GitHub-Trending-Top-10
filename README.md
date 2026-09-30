# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-30）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Rust | 11,828 | +1,280 | 🔥 2天 |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 49,980 | +3,481 | 🔥 4天 |
| 3 | [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | TypeScript | 2,811 | +622 | 🔥 4天 |
| 4 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 24,366 | +88 | NEW |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 148,819 | +675 | NEW |
| 6 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 127,374 | +464 | NEW |
| 7 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | TypeScript | 390,880 | +136 | NEW |
| 8 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Python | 76,020 | +118 | NEW |
| 9 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 272,754 | +736 | NEW |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | TypeScript | 54,527 | +352 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-30.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
