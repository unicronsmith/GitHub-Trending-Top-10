# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-24）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [block/buzz](https://github.com/block/buzz) | Rust | 8,318 | +2,162 | 🔥 2天 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | 72,661 | +3,175 | 🔥 4天 |
| 3 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Python | 69,752 | +636 | 🔥 3天 |
| 4 | [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | Rust | 9,131 | +565 | 🔥 2天 |
| 5 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 33,317 | +401 | 🔥 3天 |
| 6 | [Automattic/harper](https://github.com/Automattic/harper) | Rust | 12,675 | +624 | NEW |
| 7 | [likec4/likec4](https://github.com/likec4/likec4) | TypeScript | 4,859 | +472 | NEW |
| 8 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | JavaScript | 2,099 | +247 | 🔥 2天 |
| 9 | [yorukot/superfile](https://github.com/yorukot/superfile) | Go | 19,102 | +312 | NEW |
| 10 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 85,570 | +1,708 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-24.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
