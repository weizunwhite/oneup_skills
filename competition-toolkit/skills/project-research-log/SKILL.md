---
name: project-research-log
description: >
  Generate research logs (研究日志) and supplementary checklists (补充文档) for youth science and technology
  innovation competition projects. Produces two Word outputs: (1) a professionally formatted research log
  with varied entry styles (narrative/table/compact/debug/experiment), embedded process photos, and photo
  placeholders; (2) a supplementary document listing handwritten materials, photos, and other items the
  student needs to prepare. Use this skill whenever users mention 研究日志, 工作日志, 研究记录, 项目日志,
  日志生成, or need research process documentation for competitions like 全国青少年科技创新大赛 (青创赛)
  or 北京金鹏科技论坛 (金鹏). Also trigger when users want to convert a project paper/technical document
  into daily log entries, or when they ask about documenting their research process.
---

# Research Log & Supplement Generator

## What This Skill Produces

Two Word documents (.docx):

1. **研究日志** — A complete research log with:
   - Cover page (project name + timeline, NO personal info)
   - Table of contents organized by phases
   - 15-30 daily entries using **5 different recording styles** (not uniform!)
   - Embedded process photos where available
   - Photo placeholders (marked with `[待补充照片]`) where photos are missing
   - Entry separation per layout recipe (page breaks, spacing, or decorative dividers)

2. **补充文档** — A checklist telling the student what to prepare:
   - Photos that need to be taken/found
   - Handwritten materials to create (sketches, calculations, notes)
   - Data sheets to fill out
   - Other supporting evidence

## Critical Rules

### No Personal Information
Competition rules prohibit school names, student names, and teacher names in submitted materials.
- Cover page: only project name and timeline
- Entry content: use passive voice (not "老师建议" but "经过讨论确定")
- Photo descriptions: no identifying info
- Headers/footers: only "研究日志 | [project name]"

### Photos Are Essential
Process photos are critical evidence of student participation. The skill must:
- **Embed existing photos** when the user provides a photo directory
- **Add placeholders** for missing photos with clear descriptions of what to shoot
- Aim for at least 2-3 photos per entry with photos, spread across the project timeline
- Photo types should vary: hardware work, coding screens, testing, handwritten notes, measurements

### Entry Style Variety
Real research logs are NOT uniform. A student might write detailed notes one day and quick bullet
points the next. The log must use **at least 3 different styles** across entries.

Additionally, different projects use different **layout recipes** (版式配方) — selected automatically
based on project name hash — so two projects will have visually distinct page structures (different
header styles, content layouts, density, and separators). See [references/layout_recipes.md](references/layout_recipes.md)
for recipe definitions and [references/entry_styles.md](references/entry_styles.md) for per-recipe rendering code.

## Workflow

### Step 1: Gather Project Information

The user typically provides one or more of:
- A project paper / technical report (研究报告 / 论文)
- A technical proposal (技术方案)
- Verbal description of the project
- A photo directory with process photos

Extract from the source material:
1. **Project name** and brief description
2. **Timeline** (start month → end month)
3. **Grade level** (小学/初中/高中) — affects writing style and complexity
4. **Major phases** and what happened in each
5. **Technical components** (hardware, software, algorithms)
6. **Problems encountered and solutions**
7. **Test results and data**

For detailed extraction strategies, see [references/paper_analysis.md](references/paper_analysis.md).

### Step 2: Scan for Photos

If the user provides a photo directory:
1. List all image files (jpg, jpeg, png)
2. Read a sample from each date group to identify content
3. Build a `photoMap` mapping entry indices to relevant photos
4. Photos with dates in filenames (e.g., `IMG_20260121_180037.jpg`) help with timeline alignment

If no photos are provided:
- Use `[待补充照片: description]` placeholders throughout
- The supplement document will list all needed photos

### Step 3: Plan Log Structure

#### 3a. Select Layout Recipe

Based on the project name, select a layout recipe using the hash algorithm. This determines the overall visual style of the entire research log (header style, content layout, density, separators, etc.).

```javascript
function selectRecipe(projectName) {
  let hash = 0;
  for (const ch of projectName) {
    hash = ((hash << 5) - hash + ch.charCodeAt(0)) | 0;
  }
  const recipes = ["A", "B", "C", "D", "E"];
  return recipes[Math.abs(hash) % recipes.length];
}
```

| Recipe | Style | Key Visual Features |
|--------|-------|-------------------|
| A | 工程笔记本 | 深色横幅表头 + 二列有框表格 + 一页一条 |
| B | 手写日记风 | 粗体标题+细线 + 纯段落 + 紧凑一页1-2条 + 圆点分隔 |
| C | 项目管理风 | 左侧竖条色块 + 方括号字段 + 无框缩进 |
| D | 极简条目风 | 编号+粗体+灰日期 + 短横线引导 + 一页2-3条 |
| E | 研究报告风 | 大号标题+下划线 + 水平并排字段 + 灰底区块 |

**Output the selected recipe** at the start of the planning phase, e.g.: "选定配方: B（手写日记风）"

See [references/layout_recipes.md](references/layout_recipes.md) for full recipe definitions.

#### 3b. Design Entry List

Design the entry list as a JSON array. Each entry needs:

```javascript
{
  date: "YYYY.MM.DD（周X）",   // realistic date with weekday
  title: "entry title",        // concise, descriptive
  style: "narrative|table|compact|debug|experiment",
  // ... style-specific fields (see references/entry_styles.md)
}
```

**Style distribution guidelines:**
- `narrative` (25-30%): Discovery moments, reflections, user testing, final summary
- `table` (20-25%): Structured work like design, implementation milestones
- `compact` (15-20%): Routine tasks, quick setup sessions
- `debug` (10-15%): Troubleshooting sessions with clear problem→solution flow
- `experiment` (15-20%): Testing, measurements, data collection

These percentages apply regardless of which recipe is selected. The recipe changes **how** each style renders, not **which** styles are used.

**Phase structure** (adapt to project):
- 调研选题 (15-20% of entries)
- 学习准备 (15-20%)
- 硬件/软件开发 (30-40%)
- 测试验证 (15-20%)
- 论文撰写与材料准备 (5-10%)

**Date pattern tips:**
- Work mostly on weekends (周六/周日) for school students
- Occasional weekday evenings during intensive phases
- Leave gaps (not every week) — realistic pacing
- Cluster entries during development phases

### Step 4: Generate the Research Log

Write a Node.js script using the `docx` and `sharp` libraries to generate the Word document.

```bash
# Install dependencies if needed
npm install docx sharp 2>/dev/null

# The generation script should be written by Claude based on the project data
node gen_log.js
```

**Document structure the script must produce:**

1. **Cover page**: "研究日志" title + project name + timeline (NO names/schools) — styled per recipe
2. **Table of contents**: Phase names → entry titles with dates — styled per recipe
3. **Phase sections**: Phase header → entries — density and separation per recipe
4. **Header**: "研究日志 | {project name}" on every page
5. **Footer**: Page numbers centered

**Key technical requirements:**
- Use `docx` npm package (not python-docx)
- Use `sharp` for photo resizing (500px max, JPEG 72% quality)
- Chinese fonts: 宋体 (body), 黑体 (headings), 仿宋 (cover info)
- A4 page size with standard margins
- **Entry separation follows the selected recipe**: Recipes A/C/E use PageBreak; Recipe B uses centered dots `· · ·`; Recipe D uses spacing (300pt)
- Photos displayed at ~180px width with gray caption text
- **Photo placeholder style follows the selected recipe** (see layout_recipes.md)

**Recipe-aware rendering:**

The script must implement the selected recipe's rendering for all components:
1. Use `selectRecipe(projectName)` to determine the recipe (A-E)
2. For each entry, call the recipe-specific builder: `buildEntry{Recipe}_{Style}(idx, entry)`
3. Cover page and TOC should also follow the recipe's visual style
4. See [references/layout_recipes.md](references/layout_recipes.md) for recipe definitions (header, content, density, separators)
5. See [references/entry_styles.md](references/entry_styles.md) for per-recipe entry rendering code

### Step 5: Generate the Supplement Document

Create a second Word document listing everything the student needs to prepare. Organize by category:

**A. 需要拍摄/补充的照片**
For each photo placeholder in the log, list:
- Which log entry it belongs to (date + title)
- What the photo should show
- Shooting tips (角度、光线、构图建议)

**B. 需要手写的材料**
- 实验记录表 (with specific data fields to fill in)
- 电路草图 / 系统架构图 (hand-drawn versions)
- 计算过程 (specific formulas and numbers to work through)
- 问卷原件 (if surveys were done)
- 测试数据记录表

**C. 需要补充的电子资料**
- Screenshots of code/debugging (specify which code sections)
- Screen recordings of software testing
- Data exports (CSV files, serial monitor logs)

**D. 注意事项**
- All handwritten materials must be by the student (not adult handwriting)
- Photos should show the student actively working (not posed)
- No school uniforms with visible school name
- No name tags or badges visible in photos
- Date stamps on photos should roughly match log dates
- Handwritten notes should look natural, not too neat

Generate this as a clean Word document with checkboxes (☐) for tracking completion.

### Step 6: Output and Verify

Save both files to the project output directory:
- `研究日志_{project_short_name}.docx`
- `补充材料清单_{project_short_name}.docx`

Verify:
- No personal information (school/student/teacher names) anywhere
- Photo placeholders are clearly marked with `[待补充照片]`
- Entry styles are varied (not all the same format)
- Entry separation follows the selected recipe (page breaks for A/C/E; centered dots for B; spacing for D)
- Total entry count is reasonable for the timeline and grade level

## Grade Level Adaptation

| Aspect | 小学 (1-5年级) | 初中 (6-9年级) | 高中 (10-12年级) |
|--------|----------------|----------------|------------------|
| Timeline | 2-4 months | 3-6 months | 4-8 months |
| Entries | 12-18 | 18-25 | 25-35 |
| Language | 简单直白，口语化 | 有一定术语，较通顺 | 可用专业术语 |
| Problems | 接线错误、安装问题 | 通信协议、数据处理 | 算法优化、边界条件 |
| Narrative voice | "今天好开心，终于把灯点亮了！" | "今天尝试了...发现..." | "对XX进行了系统性测试" |
| Compact notes | 3-4 bullet points | 4-6 bullet points | 5-8 bullet points |

## Reference Files

- **[references/layout_recipes.md](references/layout_recipes.md)** — 5 layout recipes (版式配方) defining page structure, headers, content layout, density, and separators
- **[references/entry_styles.md](references/entry_styles.md)** — Per-recipe rendering code for all 5 entry styles (table/narrative/compact/debug/experiment)
- **[references/paper_analysis.md](references/paper_analysis.md)** — How to extract log content from project papers
