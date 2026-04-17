# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-17）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | JavaScript | 3,511 | +812 | NEW |
| 2 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | Python | 3,199 | +872 | 🔥 2天 |
| 3 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Shell | 2,506 | +375 | NEW |
| 4 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | Dart | 9,463 | +378 | NEW |
| 5 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | Jupyter Notebook | 31,217 | +1,385 | 🔥 3天 |
| 6 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | 11,395 | +1,107 | NEW |
| 7 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | TypeScript | 19,477 | +880 | 🔥 4天 |
| 8 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | TypeScript | 4,174 | +107 | NEW |
| 9 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | Python | 1,102 | +167 | NEW |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 157,028 | +2,058 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-17.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
