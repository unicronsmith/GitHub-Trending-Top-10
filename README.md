# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-18）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust | 15,688 | +3,945 | 🔥 8天 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Python | 10,448 | +1,302 | NEW |
| 3 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 36,303 | +1,047 | 🔥 2天 |
| 4 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 24,158 | +610 | 🔥 6天 |
| 5 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Swift | 8,010 | +827 | NEW |
| 6 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | C++ | 110,770 | +179 | NEW |
| 7 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 59,554 | +963 | NEW |
| 8 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Python | 14,586 | +1,391 | NEW |
| 9 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | TypeScript | 3,826 | +1,244 | 🔥 2天 |
| 10 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | Python | 7,492 | +768 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-05-18.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
