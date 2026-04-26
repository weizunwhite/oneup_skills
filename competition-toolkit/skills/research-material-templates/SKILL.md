---
name: research-material-templates
description: >
  Generate standardized research material templates (原始研究资料模板) for youth science
  and technology innovation competition projects. Two modes: Mode A outputs blank Word
  (.docx) templates for students to print and fill in by hand; Mode B generates a
  handwrite content reference document with project-specific content that students copy
  onto paper as original research evidence. Template types include: experiment records,
  data collection sheets, observation logs, interview records, literature excerpts,
  and survey questionnaires. Use this skill whenever users mention 原始资料, 研究资料模板,
  实验记录表, 数据采集表, 观察日志, 访谈记录, 文献摘录, 问卷调查, 手抄内容, 手抄参考,
  手抄稿, 带内容的原始资料, 手写内容, or need standardized documentation templates for
  competition projects.
---

# Research Material Templates Generator

This skill has two modes:

| Mode | Name | Output | Use Case |
|------|------|--------|----------|
| **A** | 空白模板 | Multiple .docx files (blank tables) | Students print and fill in during research |
| **B** | 手抄内容参考 | Single .docx file (with content) | Students read and hand-copy onto paper as original evidence |

---

## Mode A: Blank Templates (空白模板)

### Purpose

Competition projects (青创赛、金鹏科技论坛) require original research documentation
as supporting evidence. Judges want to see that students conducted real research with
proper records. This mode generates printable Word templates that students fill in
by hand during their research process, making their work look organized and professional.

### When to Use

The user wants blank templates for documenting their research process. They might say:
- "帮我生成一些原始研究资料的模板"
- "我需要实验记录表"
- "做一些数据采集表格"
- "帮我准备研究资料模板"
- "需要一些访谈记录的模板"

### Available Template Types

| Type | Chinese | Use Case |
|------|---------|----------|
| Experiment Record | 实验记录表 | Recording experiment steps, conditions, results, observations |
| Data Collection | 数据采集表 | Systematic data recording with units, timestamps |
| Observation Log | 观察日志 | Daily/periodic observation records |
| Interview Record | 访谈记录表 | Expert interviews, user interviews |
| Literature Excerpt | 文献摘录表 | Key findings from papers, books, websites |
| Survey Questionnaire | 问卷调查表 | User surveys with various question types |

### Workflow

#### Step 1: Determine Project Context

Ask the user (if not already clear from context):
1. What is the project about? (topic/title)
2. Which templates do they need? (default: all six types)
3. What grade level? (小学/初中/高中 — affects complexity)
4. How many blank rows per template? (default: 10 for most types)

If the user has a technical proposal (技术方案) or paper (论文) already, read it first
to extract project-specific details (variable names, equipment, data types) and
pre-fill template headers/columns accordingly.

#### Step 2: Generate Templates

Read `references/template-specs.md` for the complete template specifications and
code patterns for each template type.

Key principles:
- **Output format**: One .docx file per template type
- **Font**: 宋体 for body text, 黑体 for headers — same as competition paper standard
- **Layout**: Tables with clear borders, enough blank rows for hand-writing
- **Row height**: At least 400 DXA (~0.7cm) per row so students can write comfortably
- **Header info**: Every template should have project name, student name, date fields at top
- **Use Node.js `docx` package**: `npm install docx` then generate via script

#### Step 3: Customize for Project

Based on the project topic, customize:
- Column headers in data collection sheets (specific variables being measured)
- Observation categories in observation logs
- Interview question prompts relevant to the research
- Survey questions tailored to the research topic
- Experiment record fields matching the actual experiments

#### Step 4: Output

Save all templates to the workspace folder. Name files clearly:
- `实验记录表_[项目简称].docx`
- `数据采集表_[项目简称].docx`
- `观察日志_[项目简称].docx`
- `访谈记录表_[项目简称].docx`
- `文献摘录表_[项目简称].docx`
- `问卷调查表_[项目简称].docx`

### Font Standard (Mode A)

Same as competition papers — this ensures consistency across all project documents:

| Element | Size | Font | docx size | docx font |
|---------|------|------|-----------|-----------|
| Template title | 三号(16pt) | 黑体 | 32 | "黑体" |
| Section headers | 四号(14pt) | 黑体 | 28 | "黑体" |
| Table headers | 五号(10.5pt) | 黑体 | 21 | "黑体" |
| Table content/blanks | 五号(10.5pt) | 宋体 | 21 | "宋体" |
| Instructions/tips | 小五(9pt) | 宋体 | 18 | "宋体" |

### Grade Level Adaptations (Mode A)

- **小学 (Elementary)**: Simpler tables, fewer columns, larger cells for bigger handwriting, add guiding prompts in cells (e.g., "在这里写下你观察到的现象")
- **初中 (Middle School)**: Standard complexity, clear structure, some guiding prompts
- **高中 (High School)**: More detailed fields, space for analysis/reflection, professional layout

---

## Mode B: Handwrite Content Reference (手抄内容参考)

### Purpose

Competition judges review "original research materials" as evidence of authenticity. Hand-written materials (especially reflections, experiment notes, observation logs) are a key component. Mode B generates a single Word document containing **project-specific content** written in the student's first-person voice. Students print this document and use it as a reference to hand-copy the content onto paper, producing authentic-looking original research materials.

### When to Use

The user wants content that students will hand-copy. They might say:
- "生成手抄内容"
- "手抄参考"
- "手抄稿"
- "带内容的原始资料"
- "手写内容"
- "需要手抄的材料"

### Prerequisites

Before generating Mode B content, you MUST read:
1. **Project's `原始资料/`** — technical proposal, source code, photos, all documents
2. **Already-generated competition paper** (if available) — for accurate technical details
3. **Project info** — grade level, project type (hardware/software/research)

Without reading the original materials first, the generated content will be generic and useless.

### Workflow

#### Step 1: Deep-read all project materials

Read everything in `原始资料/`:
- Technical proposal (`*技术方案*`, `*技术文档*`) — full text
- Source code (`原始资料/source/`) — extract pin assignments, protocols, algorithms
- Photos (`原始资料/photos/`) — note what's documented
- Any other documents (drafts, wiring diagrams, etc.)
- Already-generated paper in `输出/` if available

Form a complete understanding of the project's technical details, research process, and timeline.

#### Step 2: Select chapters based on project type

Use the Chapter Selection Matrix below to determine which chapters to include.

**Chapter Selection Matrix** (10 possible chapter types):

| # | Chapter Type | 硬件发明 | 软件/IoT | 调研类 |
|---|-------------|---------|---------|-------|
| 1 | 问题发现与思考 | ✓ | ✓ | ✓ |
| 2 | 方案对比笔记 | ✓ | ✓ | - |
| 3 | 系统设计草图说明 | ✓ | △ | - |
| 4 | 技术学习笔记（引脚/算法等） | ✓ | ✓ | - |
| 5 | 调研问卷原件 | △ | △ | ✓ |
| 6 | 实验/测试记录 | ✓ | △ | ✓ |
| 7 | 观察日志 | △ | - | ✓ |
| 8 | 文献阅读笔记 | ✓ | ✓ | ✓ |
| 9 | 访谈记录 | △ | △ | ✓ |
| 10 | 研究心得/制作感想 | ✓ | ✓ | ✓ |

Legend: ✓ = always include, △ = include if relevant materials exist, - = skip

**Grade-level chapter count**:
- 小学低年级 (1-3年级): 4-5 chapters, short simple sentences, basic vocabulary
- 小学高年级 (4-6年级): 6-8 chapters, paragraph-style, includes specific technical details
- 初中 (7-9年级): 7-10 chapters, deeper analysis, reflective writing

#### Step 3: Generate content in student voice

For each selected chapter, write content that:
- Uses **first person** ("我发现..." / "我想到...")
- Matches the student's **grade level** in vocabulary and sentence complexity
- Contains **specific technical details** from the original materials (pin numbers, sensor models, algorithm parameters, test data)
- Feels like a real student's notes — not too polished, slightly informal
- Includes realistic dates that align with the project timeline

#### Step 4: Assemble and output

Read `references/handwrite-content-specs.md` for the complete code patterns, helpers, and chapter templates.

Generate a single .docx file with this structure:

1. **Cover page**: Project name + "手抄内容汇总"
2. **Usage instructions** (yellow note box): Brief explanation of how to use this document
3. **Numbered table of contents**: List all chapters
4. **Chapter content** (each on a new page):
   - Chapter title (H1, blue, 黑体)
   - "抄写到：" instruction line (where to copy this content)
   - Actual content (paragraphs, bullet lists, tables, note boxes as appropriate)
5. **手抄注意事项 page**: Tips for hand-copying (use own handwriting, OK to have corrections, etc.)
6. **手抄对应关系表**: Table mapping each chapter → where to copy → notes

Output file: `{项目名称}_手抄内容汇总.docx`

### Font Standard (Mode B)

| Element | Size | Font | docx size | docx font |
|---------|------|------|-----------|-----------|
| Cover title | 二号(22pt) | 黑体 | 44 | "黑体" |
| H1 chapter title | 小二(18pt) | 黑体 | 32 | "黑体" |
| H2 sub-section | 三号(16pt) | 黑体 | 28 | "黑体" |
| Body text | 小四(12pt) | 宋体 | 24 | "宋体" |
| Table text | — | 宋体 | 22 | "宋体" |
| Note/instruction | — | 宋体 | 22 | "宋体" (italics) |
| Header/footer | — | 宋体 | 18 | "宋体" |
| Line spacing | 1.5x | — | 360 (half-points) | — |

### Color Scheme (Mode B)

| Element | Color Code |
|---------|-----------|
| Title/heading text | #2E5090 (blue) |
| Table header bg | #D6E4F0 (light blue) |
| Note box bg (info) | #FFF8E1 (light yellow) |
| Note box border (info) | #FFB300 (amber) |
| Tip box bg | #E8F5E9 (light green) |
| Tip box border | #43A047 (green) |
| General border | #BBBBBB (gray) |
