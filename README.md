# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-20）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 59,470 | +3,890 | 🔥 4天 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 33,330 | +849 | NEW |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 99,224 | +1,559 | 🔥 4天 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 168,927 | +1,007 | NEW |
| 5 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 140,446 | +1,201 | 🔥 2天 |
| 6 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 77,585 | +683 | 🔥 3天 |
| 7 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 129,708 | +751 | NEW |
| 8 | [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) | JavaScript | 10,744 | +1,168 | NEW |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 218,505 | +1,256 | 🔥 3天 |
| 10 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 162,050 | +590 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-20.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
