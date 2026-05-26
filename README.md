# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-05-26）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | TypeScript | 34,216 | +4,721 | 🔥 5天 |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 193,620 | +1,912 | 🔥 2天 |
| 3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 20,060 | +2,169 | 🔥 7天 |
| 4 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 16,362 | +1,698 | 🔥 3天 |
| 5 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 9,743 | +871 | 🔥 2天 |
| 6 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | Unknown | 4,744 | +547 | NEW |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Shell | 20,675 | +1,440 | NEW |
| 8 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | HTML | 166,420 | +1,127 | NEW |
| 9 | [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | C# | 52,264 | +91 | NEW |
| 10 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | JavaScript | 4,972 | +738 | NEW |

📄 [查看完整 PDF 报告](reports/2026-05-26.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
