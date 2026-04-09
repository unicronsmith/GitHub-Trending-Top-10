# GitHub Trending Top 10

每天自动获取 GitHub Trending 前 10 热门项目，使用 AI 生成中文深度解读，输出精美 PDF 报告。

## 工作原理

1. 每天美东 6:00 AM 由 GitHub Actions 自动触发
2. 爬取 [github.com/trending](https://github.com/trending) 前 10 个项目
3. 获取每个项目的 README，调用 DeepSeek AI 生成中文分析
4. 生成精美杂志风格 PDF 报告，自动提交到 `reports/` 目录

## 今日榜单（2026-04-09）

| 排名 | 项目 | 语言 | Stars | 今日增长 | 状态 |
| :---: | --- | :---: | ---: | ---: | :---: |
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 41,012 | +5,794 | NEW |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Unknown | 9,703 | +702 | 🔥 2天 |
| 3 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Python | 14,013 | +1,306 | NEW |
| 4 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Python | 7,260 | +460 | NEW |
| 5 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | Java | 13,028 | +1,012 | NEW |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | Shell | 142,716 | +2,028 | 🔥 2天 |
| 7 | [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | Python | 4,905 | +649 | 🔥 2天 |
| 8 | [coleam00/Archon](https://github.com/coleam00/Archon) | TypeScript | 14,028 | +138 | NEW |
| 9 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 11,854 | +223 | NEW |
| 10 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | TypeScript | 6,495 | +174 | NEW |

📄 [查看完整 PDF 报告](reports/2026-04-09.pdf)

## 历史报告

所有历史报告保存在 [`reports/`](reports/) 目录中。

---

*由 GitHub Actions + DeepSeek AI 自动生成*
