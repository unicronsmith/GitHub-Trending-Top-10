# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-01）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 150,084 | +1,179 | 🔥 2天 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 273,618 | +888 | 🔥 2天 |
| 3 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Rust | 13,826 | +2,503 | 🔥 3天 |
| 4 | [firebase/firebase-ios-sdk](https://github.com/firebase/firebase-ios-sdk) | C++ | 6,833 | +112 | NEW |
| 5 | [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | TypeScript | 3,494 | +640 | 🔥 5天 |
| 6 | [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 9,279 | +157 | NEW |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 293,808 | +476 | NEW |
| 8 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 24,707 | +357 | 🔥 2天 |
| 9 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | TypeScript | 55,170 | +624 | 🔥 2天 |
| 10 | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 111,035 | +294 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-01.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
