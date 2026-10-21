# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-21）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 62,455 | +3,131 | 🔥 5天 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 35,280 | +1,997 | 🔥 2天 |
| 3 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | Python | 94,724 | +439 | NEW |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 100,708 | +1,543 | 🔥 5天 |
| 5 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Python | 77,050 | +477 | NEW |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 170,897 | +2,051 | 🔥 2天 |
| 7 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 141,272 | +914 | 🔥 3天 |
| 8 | [supabase/supabase](https://github.com/supabase/supabase) | TypeScript | 112,703 | +509 | NEW |
| 9 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | TypeScript | 58,876 | +105 | NEW |
| 10 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 42,645 | +570 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-21.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
