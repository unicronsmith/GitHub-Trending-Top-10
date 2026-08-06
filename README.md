# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-06）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TypeScript | 15,668 | +1,892 | 🔥 5天 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 82,321 | +226 | 🔥 2天 |
| 3 | [cloudflare/computer](https://github.com/cloudflare/computer) | TypeScript | 4,330 | +891 | NEW |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 205,975 | +1,695 | NEW |
| 5 | [goauthentik/authentik](https://github.com/goauthentik/authentik) | Python | 22,804 | +123 | NEW |
| 6 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | Python | 2,583 | +326 | 🔥 2天 |
| 7 | [google/guava](https://github.com/google/guava) | Java | 51,550 | +9 | NEW |
| 8 | [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | Roff | 76,913 | +157 | NEW |
| 9 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | Python | 185,852 | +28 | NEW |
| 10 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Python | 28,807 | +232 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-06.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
