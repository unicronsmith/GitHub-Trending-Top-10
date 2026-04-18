# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-18）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | JavaScript | 4,685 | +737 | 🔥 2天 |
| 2 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | Python | 3,996 | +845 | 🔥 3天 |
| 3 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Shell | 2,917 | +538 | 🔥 2天 |
| 4 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | Dart | 10,054 | +824 | 🔥 2天 |
| 5 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | Jupyter Notebook | 31,781 | +944 | 🔥 4天 |
| 6 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | 12,177 | +311 | 🔥 2天 |
| 7 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 20,141 | +797 | 🔥 5天 |
| 8 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | TypeScript | 4,355 | +110 | 🔥 2天 |
| 9 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | Python | 1,639 | +184 | 🔥 2天 |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 158,293 | +1,713 | 🔥 2天 |

📄 [查看完整 PDF 报告](reports/2026-04-18.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
