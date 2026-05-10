# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-10）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | TypeScript | 31,695 | +656 | 🔥 2天 |
| 2 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 18,008 | +1,479 | 🔥 5天 |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Shell | 37,838 | +1,092 | NEW |
| 4 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Python | 4,102 | +1,167 | NEW |
| 5 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | Python | 15,138 | +646 | NEW |
| 6 | [jundot/omlx](https://github.com/jundot/omlx) | Python | 13,065 | +187 | NEW |
| 7 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | JavaScript | 8,802 | +642 | 🔥 2天 |
| 8 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | TypeScript | 6,524 | +604 | 🔥 2天 |
| 9 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | Go | 2,756 | +694 | 🔥 2天 |
| 10 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | Python | 10,365 | +538 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-10.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
