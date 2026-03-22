# 报告索引页设计文档

**日期**：2026-03-22
**状态**：已确认

## 概述

为 GitHub Trending Top 10 项目添加一个 HTML 索引页（`reports/index.html`），以卡片网格形式展示所有历史报告，方便用户浏览和下载。

## 设计决策

| 决策 | 选项 | 理由 |
|------|------|------|
| 更新方式 | 静态生成 | 与现有架构一致（main.py 已生成 JSON/PDF/README），无前端 JS 依赖，GitHub Pages 开箱即用 |
| 布局风格 | 卡片网格 | 紧凑美观，报告积累后浏览体验好 |
| 视觉主题 | GitHub 暗色 | 与 PDF 封面/卡片头部的 `#0d1117` 暗色调统一 |
| 卡片信息量 | 丰富 | 日期 + 星期 + Top 3 项目 + 新上榜数 + Stars 总增长 + 语言标签 + PDF/JSON 链接 |

## 架构

### 新增文件

- `templates/index.html` — Jinja2 模板，渲染索引页 HTML
- `reports/index.html` — 生成的静态索引页（每次运行覆盖）

### 修改文件

- `src/main.py` — 新增 `generate_index()` 函数，在流程末尾调用

### 不需要修改的文件

- `.github/workflows/daily.yml` — `git add reports/` 已覆盖新文件
- `src/scraper.py`、`src/analyzer.py`、`src/pdf_generator.py` — 无关

## 数据流

```
reports/*.json  →  main.py:generate_index()  →  Jinja2 渲染  →  reports/index.html
```

1. `generate_index()` 扫描 `reports/` 目录下匹配 `YYYY-MM-DD.json` 模式的文件（正则：`\d{4}-\d{2}-\d{2}\.json`），忽略其他 JSON 文件
2. 读取每个 JSON，提取：日期、项目列表（名称、语言、stars、is_new）
3. 按日期倒序排列
4. 计算每日聚合数据：Top 3 项目名、新上榜数量、今日 Stars 总增长（`sum(project['today_stars'])`）、语言分布（去重后的唯一语言列表）
5. 使用 `autoescape=True` 的 Jinja2 Environment 渲染 `templates/index.html` 模板（防止项目描述中的 HTML/XSS 注入）
6. 输出为 `reports/index.html`

## 页面结构

### 页头
- 圆形渐变图标（与 PDF 封面一致）
- 标题："GitHub Trending Top 10"
- 副标题："每日热门开源项目深度解读 · 历史报告归档"
- 统计行："共 N 份报告 · 最新：YYYY-MM-DD"

### 卡片网格
- 3 列网格布局，响应式（≤768px 2 列，≤480px 1 列）
- 需要 `<meta name="viewport" content="width=device-width, initial-scale=1">` 使响应式生效
- 按日期倒序排列，最新在左上
- 最新报告卡片：蓝色边框（`#58a6ff`）+ "最新" 标签

### 每张卡片内容
- **日期**：YYYY-MM-DD，最新报告蓝色加粗，其余白色
- **星期**：中文星期几，灰色小字
- **Top 3 项目**：排名序号（橙色）+ 项目名
- **统计标签**：新上榜数（绿色底）+ 今日 Stars 总增长（蓝色底，`sum(today_stars)`，显示为 "今日 +N"）
- **语言标签**：去重后的唯一语言 pill，背景色半透明取语言色，文字取语言色（不显示出现次数）
- **星期**：使用 Python `datetime.weekday()` + 中文映射（`{0: '周一', ..., 6: '周日'}`），`strftime('%A')` 返回英文不可直接用
- **下载链接**：📄 PDF 报告 + 📊 JSON 数据，相对路径链接

### 页脚
- "数据来源：github.com/trending · 由 DeepSeek AI 提供智能分析 · 自动生成"

## 样式规范

- 背景色：`#0d1117`
- 卡片背景：`#161b22`
- 卡片边框：`#30363d`（普通）/ `#58a6ff`（最新）
- 主文字色：`#c9d1d9`
- 次文字色：`#8b949e`
- 强调蓝：`#58a6ff`
- 强调绿：`#3fb950`
- 强调橙：`#f78166`
- 字体栈：`"Noto Sans CJK SC", "Noto Sans SC", "Microsoft YaHei", "PingFang SC", sans-serif`

## 集成点

### main.py 调用位置

在现有步骤 5（更新 README）之后新增步骤 6。需更新所有现有 `print()` 中的 `[N/5]` 为 `[N/6]`：

```
[1/6] 爬取 GitHub Trending
[2/6] 对比历史数据
[3/6] 获取 README + AI 分析
[4/6] 保存数据 + 生成 PDF
[5/6] 更新 README
[6/6] 生成索引页          ← 新增
```

`generate_index()` 的调用必须用 `try/except` 包裹，失败时打印警告但不中断整个流程。索引页是便利功能，不应影响核心报告生成管线。

### generate_index() 函数签名

```python
def generate_index():
    """扫描 reports/ 目录的 JSON 文件，生成历史报告索引页。"""
```

- 无参数，直接读取 REPORTS_DIR
- 读取所有 `*.json`，解析后按日期倒序
- 渲染 `templates/index.html` 模板
- 输出到 `reports/index.html`

## 边界情况

- 只有 1 份报告时正常显示（无需特殊处理）
- JSON 文件损坏或格式异常时跳过，打印警告
- 语言为 "Unknown" 时使用灰色默认色
- 语言色缺失或为空字符串时使用 `#666` 作为 fallback
- 模板需包含 `<html lang="zh-CN">` 和 `<title>` 标签，与现有 `report.html` 保持一致
