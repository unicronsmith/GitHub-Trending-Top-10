# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-08-14）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 16,209 | +4,475 | 🔥 3天 |
| 2 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Python | 7,212 | +713 | 🔥 5天 |
| 3 | [anthropics/skills](https://github.com/anthropics/skills) | Python | 169,338 | +312 | NEW |
| 4 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | Python | 5,244 | +769 | NEW |
| 5 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | Swift | 10,054 | +76 | NEW |
| 6 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | Python | 71,274 | +328 | NEW |
| 7 | [macro-inc/macro](https://github.com/macro-inc/macro) | Rust | 2,804 | +1,239 | 🔥 3天 |
| 8 | [megadose/holehe](https://github.com/megadose/holehe) | Python | 12,578 | +195 | NEW |
| 9 | [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) | Python | 20,769 | +283 | NEW |
| 10 | [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | Rust | 1,371 | +408 | NEW |

📄 [查看完整 PDF 报告](reports/2026-08-14.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
