# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-06-10）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 50,361 | +781 | NEW |
| 2 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | Unknown | 13,993 | +775 | NEW |
| 3 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | TypeScript | 14,650 | +618 | 🔥 3天 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 38,661 | +2,561 | 🔥 6天 |
| 5 | [soxoj/maigret](https://github.com/soxoj/maigret) | Python | 31,710 | +261 | NEW |
| 6 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Unknown | 139,386 | +397 | 🔥 2天 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 223,112 | +1,011 | NEW |
| 8 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | Go | 4,984 | +92 | NEW |
| 9 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 84,446 | +1,471 | NEW |
| 10 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | Python | 2,115 | +535 | NEW |

📄 [查看完整 PDF 报告](reports/2026-06-10.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
