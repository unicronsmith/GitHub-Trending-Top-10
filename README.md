# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-07-30）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | Python | 8,207 | +827 | 🔥 3天 |
| 2 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | Jupyter Notebook | 53,286 | +115 | NEW |
| 3 | [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | Python | 10,699 | +945 | NEW |
| 4 | [different-ai/openwork](https://github.com/different-ai/openwork) | TypeScript | 18,327 | +97 | 🔥 2天 |
| 5 | [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | JavaScript | 10,323 | +12 | NEW |
| 6 | [pascalorg/editor](https://github.com/pascalorg/editor) | TypeScript | 19,860 | +1,022 | NEW |
| 7 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 55,216 | +377 | NEW |
| 8 | [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore) | C# | 38,248 | +5 | NEW |
| 9 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | C | 136,916 | +68 | NEW |
| 10 | [ansible/ansible](https://github.com/ansible/ansible) | Python | 69,749 | +20 | NEW |

📄 [查看完整 PDF 报告](reports/2026-07-30.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
