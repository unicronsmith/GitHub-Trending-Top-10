# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-21）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | TypeScript | 5,698 | +607 | 🔥 2天 |
| 2 | [trycua/cua](https://github.com/trycua/cua) | HTML | 25,562 | +609 | 🔥 3天 |
| 3 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | TypeScript | 17,449 | +843 | 🔥 3天 |
| 4 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 7,512 | +217 | NEW |
| 5 | [coder/coder](https://github.com/coder/coder) | Go | 16,318 | +461 | NEW |
| 6 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 35,686 | +425 | 🔥 2天 |
| 7 | [cloudflare/quiche](https://github.com/cloudflare/quiche) | Rust | 12,234 | +69 | NEW |
| 8 | [mvt-project/mvt](https://github.com/mvt-project/mvt) | Python | 13,437 | +177 | NEW |
| 9 | [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | Python | 8,080 | +266 | NEW |
| 10 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | Unknown | 103,848 | +221 | NEW |

📄 [查看完整 PDF 报告](reports/2026-09-21.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
