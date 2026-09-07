# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-07）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | TypeScript | 45,116 | +734 | NEW |
| 2 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python | 179,613 | +771 | NEW |
| 3 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 20,627 | +147 | NEW |
| 4 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | JavaScript | 9,426 | +117 | NEW |
| 5 | [MoonTechLab/LunaTV](https://github.com/MoonTechLab/LunaTV) | TypeScript | 9,628 | +171 | NEW |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 252,453 | +1,905 | 🔥 5天 |
| 7 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | JavaScript | 47,920 | +602 | NEW |
| 8 | [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | Python | 5,072 | +541 | NEW |
| 9 | [BraveOPotato/FckSignups](https://github.com/BraveOPotato/FckSignups) | TypeScript | 3,652 | +497 | NEW |
| 10 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Python | 81,724 | +188 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-07.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
