# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-29）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | TypeScript | 3,697 | +607 | 🔥 2天 |
| 2 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | TypeScript | 45,135 | +797 | 🔥 3天 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 235,229 | +636 | 🔥 2天 |
| 4 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | Python | 7,596 | +227 | 🔥 2天 |
| 5 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust | 13,093 | +652 | NEW |
| 6 | [grokability/snipe-it](https://github.com/grokability/snipe-it) | PHP | 14,261 | +6 | NEW |
| 7 | [deepfakes/faceswap](https://github.com/deepfakes/faceswap) | Python | 55,982 | +135 | NEW |
| 8 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Python | 51,054 | +332 | NEW |
| 9 | [different-ai/openwork](https://github.com/different-ai/openwork) | TypeScript | 17,428 | +58 | NEW |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 263,031 | +634 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-29.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
