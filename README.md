# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-23）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 41,142 | +2,706 | 🔥 4天 |
| 2 | [php/php-src](https://github.com/php/php-src) | C | 41,480 | +722 | 🔥 2天 |
| 3 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 31,999 | +643 | 🔥 2天 |
| 4 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Rust | 18,401 | +1,240 | NEW |
| 5 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | TypeScript | 6,671 | +547 | NEW |
| 6 | [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) | Python | 8,133 | +209 | NEW |
| 7 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Python | 40,069 | +144 | NEW |
| 8 | [nodejs/node](https://github.com/nodejs/node) | JavaScript | 122,651 | +93 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-23.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
