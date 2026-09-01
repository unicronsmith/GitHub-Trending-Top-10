# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-09-01）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | TypeScript | 31,067 | +37 | NEW |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Python | 44,657 | +161 | NEW |
| 3 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | TypeScript | 29,025 | +3,122 | 🔥 3天 |
| 4 | [iv-org/invidious](https://github.com/iv-org/invidious) | Crystal | 23,663 | +583 | NEW |
| 5 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | Python | 56,813 | +1,005 | 🔥 2天 |
| 6 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 13,247 | +509 | NEW |
| 7 | [3b1b/manim](https://github.com/3b1b/manim) | Python | 92,420 | +74 | NEW |
| 8 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | Rust | 17,725 | +545 | NEW |
| 9 | [browser-use/video-use](https://github.com/browser-use/video-use) | Python | 22,666 | +591 | NEW |
| 10 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | 41,313 | +914 | 🔥 6天 |

📄 [查看完整 PDF 报告](reports/2026-09-01.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
