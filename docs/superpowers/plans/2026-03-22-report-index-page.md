# 报告索引页实施计划

> **For agentic workers:** REQUIRED: Use superpowers:team-driven-development (max efficiency, Agent Teams), superpowers:subagent-driven-development (simpler), or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 添加静态 HTML 索引页，以 GitHub 暗色风格卡片网格展示所有历史报告

**Architecture:** 新增 Jinja2 模板 `templates/index.html`，在 `src/main.py` 添加 `generate_index()` 函数扫描 `reports/*.json` 并渲染索引页到 `reports/index.html`。使用 `autoescape=True` 防 XSS，`try/except` 包裹防止索引生成失败影响核心管线。

**Tech Stack:** Python, Jinja2 (已有依赖), HTML/CSS

**Spec:** `docs/superpowers/specs/2026-03-22-report-index-page-design.md`

---

## File Structure

| 操作 | 文件 | 职责 |
|------|------|------|
| 新增 | `templates/index.html` | Jinja2 模板：暗色卡片网格索引页 |
| 修改 | `src/main.py` | 新增 `generate_index()`，集成到 `main()` 末尾 |
| 生成 | `reports/index.html` | 静态输出（不入版本库模板，但入 git） |

---

## Chunk 1: Implementation

### Task 1: 创建索引页 Jinja2 模板

**Files:**
- Create: `templates/index.html`

**Depends on:** nothing

- [ ] **Step 1: 创建 `templates/index.html`**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GitHub Trending Top 10 — 历史报告</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: "Noto Sans CJK SC", "Noto Sans SC", "Microsoft YaHei", "PingFang SC", sans-serif;
    background: #0d1117;
    color: #c9d1d9;
    line-height: 1.6;
    min-height: 100vh;
  }

  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 40px 20px;
  }

  /* ── 页头 ── */
  .header {
    text-align: center;
    margin-bottom: 40px;
  }

  .header-icon {
    width: 56px;
    height: 56px;
    background: linear-gradient(135deg, #f78166, #f0883e, #d29922);
    border-radius: 50%;
    margin: 0 auto 16px auto;
  }

  .header h1 {
    font-size: 28px;
    font-weight: 700;
    color: #58a6ff;
    margin-bottom: 6px;
  }

  .header .subtitle {
    color: #8b949e;
    font-size: 14px;
  }

  .header .stats {
    color: #484f58;
    font-size: 12px;
    margin-top: 8px;
  }

  /* ── 卡片网格 ── */
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }

  @media (max-width: 768px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 480px) {
    .grid { grid-template-columns: 1fr; }
  }

  /* ── 卡片 ── */
  .card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 16px;
    transition: border-color 0.2s;
  }

  .card:hover {
    border-color: #58a6ff;
  }

  .card.latest {
    border-color: #58a6ff;
    position: relative;
  }

  .badge-latest {
    position: absolute;
    top: 10px;
    right: 10px;
    background: #58a6ff;
    color: #0d1117;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 8px;
    font-weight: bold;
  }

  .card-date {
    font-weight: bold;
    font-size: 16px;
    color: #c9d1d9;
  }

  .card.latest .card-date {
    color: #58a6ff;
  }

  .card-weekday {
    color: #484f58;
    font-size: 11px;
    margin: 2px 0 10px 0;
  }

  /* Top 3 */
  .card-top3-label {
    font-size: 11px;
    color: #8b949e;
    margin-bottom: 4px;
  }

  .card-top3 {
    font-size: 11px;
    color: #c9d1d9;
    line-height: 1.7;
    margin-bottom: 10px;
  }

  .card-top3 .rank {
    color: #f78166;
  }

  /* 统计标签 */
  .card-stats {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 10px;
  }

  .stat-new {
    background: rgba(63, 185, 80, 0.12);
    color: #3fb950;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 8px;
  }

  .stat-stars {
    background: rgba(88, 166, 255, 0.12);
    color: #58a6ff;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 8px;
  }

  /* 语言标签 */
  .card-langs {
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
    margin-bottom: 12px;
  }

  .lang-pill {
    font-size: 9px;
    padding: 2px 7px;
    border-radius: 8px;
  }

  /* 下载链接 */
  .card-links {
    font-size: 11px;
  }

  .card-links a {
    text-decoration: none;
    margin-right: 10px;
  }

  .card-links a.pdf { color: #3fb950; }
  .card-links a.json { color: #58a6ff; }
  .card-links a:hover { text-decoration: underline; }

  /* ── 页脚 ── */
  .footer {
    text-align: center;
    margin-top: 40px;
    color: #484f58;
    font-size: 11px;
  }
</style>
</head>
<body>
<div class="container">

  <!-- 页头 -->
  <div class="header">
    <div class="header-icon"></div>
    <h1>GitHub Trending Top 10</h1>
    <p class="subtitle">每日热门开源项目深度解读 · 历史报告归档</p>
    <p class="stats">共 {{ days|length }} 份报告{% if days %} · 最新：{{ days[0].date }}{% endif %}</p>
  </div>

  <!-- 卡片网格 -->
  <div class="grid">
    {% for day in days %}
    <div class="card{% if loop.first %} latest{% endif %}">
      {% if loop.first %}<span class="badge-latest">最新</span>{% endif %}

      <div class="card-date">{{ day.date }}</div>
      <div class="card-weekday">{{ day.weekday }}</div>

      <div class="card-top3-label">Top 3</div>
      <div class="card-top3">
        {% for name in day.top3 %}
        <span class="rank">{{ loop.index }}.</span> {{ name }}<br>
        {% endfor %}
      </div>

      <div class="card-stats">
        <span class="stat-new">{{ day.new_count }} 个新上榜</span>
        <span class="stat-stars">今日 +{{ "{:,}".format(day.total_today_stars) }}</span>
      </div>

      <div class="card-langs">
        {% for lang in day.languages %}
        <span class="lang-pill" style="background:{{ lang.bg }};color:{{ lang.fg }};">{{ lang.name }}</span>
        {% endfor %}
      </div>

      <div class="card-links">
        <a class="pdf" href="{{ day.date }}.pdf">📄 PDF 报告</a>
        <a class="json" href="{{ day.date }}.json">📊 JSON 数据</a>
      </div>
    </div>
    {% endfor %}
  </div>

  <!-- 页脚 -->
  <div class="footer">
    数据来源：github.com/trending · 由 DeepSeek AI 提供智能分析 · 自动生成
  </div>

</div>
</body>
</html>
```

- [ ] **Step 2: 提交模板**

```bash
git add templates/index.html
git commit -m "feat: 添加报告索引页 Jinja2 模板"
```

---

### Task 2: 添加 generate_index() 并集成到 main()

**Files:**
- Modify: `src/main.py:1-147`

**Depends on:** Task 1

- [ ] **Step 1: 在 `main.py` 顶部添加 `import re`**

在第 4 行 `from pathlib import Path` 之后添加：

```python
import re
```

- [ ] **Step 2: 在 `update_readme()` 函数之后添加 `generate_index()` 函数**

在 `src/main.py` 第 99 行（`update_readme` 函数末尾）之后插入：

```python
WEEKDAY_CN = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"


def generate_index():
    """扫描 reports/ 目录的 JSON 文件，生成历史报告索引页。"""
    json_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}\.json$")
    json_files = sorted(
        [f for f in REPORTS_DIR.iterdir() if json_pattern.match(f.name)],
        key=lambda f: f.stem,
        reverse=True,
    )

    days = []
    for jf in json_files:
        try:
            with open(jf, encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"  警告：跳过损坏的 JSON 文件 {jf.name}：{e}")
            continue

        projects = data.get("projects", [])
        date_str = data.get("date", jf.stem)
        dt = datetime.strptime(date_str, "%Y-%m-%d")

        # Top 3 项目名
        top3 = [p.get("name", "unknown") for p in projects[:3]]

        # 新上榜数量
        new_count = sum(1 for p in projects if p.get("is_new"))

        # 今日 Stars 总增长
        total_today_stars = sum(p.get("today_stars", 0) for p in projects)

        # 去重语言列表（保留顺序）
        seen_langs = {}
        for p in projects:
            lang = p.get("language", "Unknown")
            if lang not in seen_langs:
                color = p.get("language_color") or "#666"
                if not color:
                    color = "#666"
                seen_langs[lang] = color

        languages = []
        for name, color in seen_langs.items():
            languages.append({
                "name": name,
                "fg": color,
                "bg": f"{color}30",
            })

        days.append({
            "date": date_str,
            "weekday": WEEKDAY_CN[dt.weekday()],
            "top3": top3,
            "new_count": new_count,
            "total_today_stars": total_today_stars,
            "languages": languages,
        })

    # 渲染模板（autoescape=True 防 XSS）
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=True,
    )
    template = env.get_template("index.html")
    html = template.render(days=days)

    output_path = REPORTS_DIR / "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  索引页已生成：{output_path}")
```

- [ ] **Step 3: 在 `main.py` 顶部添加 Jinja2 导入**

在 `from pdf_generator import generate_pdf` 之后添加：

```python
from jinja2 import Environment, FileSystemLoader
```

- [ ] **Step 4: 更新 `main()` 中的步骤编号 `[N/5]` → `[N/6]`**

将 `main()` 函数中所有 `[1/5]` 到 `[5/5]` 替换为 `[1/6]` 到 `[5/6]`。

- [ ] **Step 5: 在 `main()` 末尾添加步骤 6 调用**

在 `update_readme(projects, today)` 之后，`print(f"\n完成！...")` 之前，插入：

```python
    # 6. 生成索引页
    print("\n[6/6] 正在生成索引页...")
    try:
        generate_index()
    except Exception as e:
        print(f"  警告：索引页生成失败（不影响报告）：{e}")
```

- [ ] **Step 6: 提交**

```bash
git add src/main.py
git commit -m "feat: 添加 generate_index() 生成历史报告索引页"
```

---

### Task 3: 验证

**Files:** (只读验证)

**Depends on:** Task 1, Task 2

- [ ] **Step 1: 在本地运行 `generate_index()` 验证输出**

```bash
cd src && python -c "
from main import generate_index
generate_index()
"
```

Expected: 打印 `索引页已生成：...reports/index.html`

- [ ] **Step 2: 检查生成的 HTML 文件**

确认 `reports/index.html` 存在且包含：
- `<html lang="zh-CN">`
- `2026-03-22` 日期
- `MoneyPrinterV2` 项目名
- PDF 和 JSON 链接
- 响应式 viewport meta 标签

- [ ] **Step 3: 在浏览器中打开确认视觉效果**

```bash
start reports/index.html  # Windows
```

确认暗色主题、卡片布局、信息完整性。

- [ ] **Step 4: 提交生成的索引页**

```bash
git add reports/index.html
git commit -m "feat: 生成首份报告索引页"
```
