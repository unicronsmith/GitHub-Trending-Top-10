# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-10-10）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 64,596 | +25,784 | 🔥 5天 |
| 2 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | C++ | 25,269 | +5,831 | 🔥 6天 |
| 3 | [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 13,380 | +3,217 | 🔥 3天 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 48,601 | +1,189 | 🔥 4天 |
| 5 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 26,113 | +178 | NEW |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 283,910 | +1,737 | 🔥 5天 |
| 7 | [flutter/flutter](https://github.com/flutter/flutter) | Dart | 179,344 | +39 | NEW |
| 8 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | C++ | 200,628 | +24 | NEW |
| 9 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Python | 59,130 | +372 | NEW |
| 10 | [pytorch/pytorch](https://github.com/pytorch/pytorch) | Python | 104,060 | +81 | NEW |

📄 [查看完整 PDF 报告](reports/2026-10-10.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
