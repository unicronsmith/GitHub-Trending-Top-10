# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-02）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 88,137 | +683 | NEW |
| 2 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Go | 108,936 | +271 | NEW |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 294,276 | +561 | 🔥 2天 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 151,329 | +1,429 | 🔥 3天 |
| 5 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | JavaScript | 74,071 | +717 | NEW |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 274,483 | +955 | 🔥 3天 |
| 7 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Rust | 14,303 | +584 | 🔥 4天 |
| 8 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | JavaScript | 52,293 | +139 | NEW |
| 9 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | TypeScript | 55,703 | +584 | 🔥 3天 |
| 10 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 24,951 | +276 | 🔥 3天 |

📄 [查看完整 PDF 报告](reports/2026-10-02.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
