# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-16）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cordiverse/cordis](https://github.com/cordiverse/cordis) | TypeScript | 4,373 | +599 | NEW |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 19,064 | +1,607 | 🔥 5天 |
| 3 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 3,016 | +149 | NEW |
| 4 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | Python | 6,232 | +547 | 🔥 3天 |
| 5 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | Python | 72,226 | +434 | NEW |
| 6 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Python | 460,706 | +2,260 | NEW |
| 7 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | Python | 1,857 | +297 | NEW |
| 8 | [github/spec-kit](https://github.com/github/spec-kit) | Python | 129,368 | +892 | 🔥 2天 |
| 9 | [megadose/holehe](https://github.com/megadose/holehe) | Python | 13,206 | +382 | 🔥 3天 |
| 10 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | Swift | 10,430 | +104 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-16.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
