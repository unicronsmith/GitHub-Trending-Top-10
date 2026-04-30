# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-30）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | Rust | 47,160 | +12,822 | 🔥 2天 |
| 2 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 56,507 | +386 | NEW |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 47,351 | +7,280 | 🔥 5天 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 173,983 | +1,653 | 🔥 2天 |
| 5 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | TypeScript | 5,470 | +393 | NEW |
| 6 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Python | 429,024 | +307 | NEW |
| 7 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust | 1,675 | +411 | 🔥 2天 |
| 8 | [soxoj/maigret](https://github.com/soxoj/maigret) | Python | 20,541 | +79 | NEW |
| 9 | [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack) | Python | 11,920 | +1,033 | 🔥 3天 |
| 10 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | Kotlin | 12,692 | +799 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-30.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
