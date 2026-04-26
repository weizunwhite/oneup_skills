---
name: competition-paper-generator
description: >
  Generate competition papers (研究报告/论文) for youth science and technology innovation projects.
  Outputs Word (.docx) with embedded diagrams and photos. Supports 4 grade levels.
  Trigger on: 论文, 研究报告, 竞赛论文, 研究方案, 开题报告.
---

# Competition Paper Generator (竞赛论文生成器)

## Overview

Generate complete, high-quality competition papers for youth science and technology innovation projects. The paper serves two purposes simultaneously:

1. **Complete project record** — a thorough documentation of the entire invention/research process from start to finish
2. **Competition submission** — strategically structured so evaluators can quickly grasp the project's value, especially through the abstract

**Output**: Word (.docx) with photos embedded + diagram placeholders, plus separate .drawio source files for user review and editing.

**Also supports**: Research proposals (研究方案/开题报告) as a condensed version

## Critical Rules

### Content Rules

**NEVER use metaphors, analogies, or personification for technical components (ALL grades, including 小低).** Do not compare MCUs to "brains", cameras to "eyes", sensors to "noses", batteries to "hearts", etc. Even for the youngest students, use simple but accurate language: "ESP32负责处理数据" ✅, not "ESP32就像大脑" ❌. See `references/writing-guidelines.md` → "Forbidden Patterns" for comprehensive examples.

**ALL grade levels MUST include these two sections:**
1. **心得体会** — personal reflections and growth from the project (near the end)
2. **致谢** — acknowledgments to teachers, parents, school, etc. (final section before references)

**Do NOT create a standalone「个人贡献」section.** Instead, demonstrate student authenticity through writing details throughout the paper — real debugging struggles, specific failure-and-fix stories, personal observations in background sections, and concrete growth reflections in 心得体会. See `references/writing-guidelines.md` → "Authenticity Through Writing" for grade-specific techniques.

**NEVER fabricate references.** All references MUST be verified via WebSearch before inclusion. AI-generated Chinese academic journal citations are especially prone to hallucination — verify every journal name, volume, issue, and page number.

**Do NOT treat cost/price as a research objective or innovation point.** Cost may appear naturally in background research (e.g., "现有产品价格较高") as context for why existing solutions are unsuitable, but should NOT be listed as a quantified research target (e.g., ~~"成本控制：<X元"~~) or highlighted as an innovation. Research objectives should focus on technical performance metrics: accuracy, speed, success rate, range, battery life, weight, etc.

### Figure & Table Numbering Rules

**Every figure and every table MUST have a number and caption. No exceptions.**

**Numbering modes** (set `NUMBERING_MODE` in docx code, confirm with user which to use):
- `"sequential"` — 图1, 图2, ... 图N / 表1, 表2, ... 表N (simpler, for shorter papers)
- `"chapter"` — 图1.1, 图1.2, 图2.1 / 表1.1, 表2.1 (formal, for longer papers with many figures)

**Caption placement — this is mandatory and must not be confused:**
- **图注** (figure caption): **Below** the image, centered, 五号宋体
- **表注** (table caption): **Above** the table, centered, 五号宋体

**Code helpers** (see `references/docx-generation.md`):
- `figImg()` / `figPng()` — embed image + auto-numbered caption below
- `figDiagramPlaceholder()` — gray placeholder + auto-numbered caption below (for .drawio diagrams)
- `placeholder()` — dashed box + auto-numbered caption below (for missing photos)
- `makeTableWithCaption()` — auto-numbered caption above + table body
- Do NOT use `makeTable()` directly — always use `makeTableWithCaption()` for proper numbering

**In-text references**: Every figure and table must be referenced in the body text (e.g., "如图3所示", "表2.1列出了...")

### Diagram Strategy: Placeholder + Editable Source

Competition papers are final submissions — diagrams need human review before inclusion. Therefore:

1. **Generate .drawio XML files** with clear Chinese filenames (e.g., `图1_系统架构图.drawio`)
2. **Insert placeholders in the .docx** at correct locations (e.g., `【此处插入 图1 系统架构图】`)
3. **User reviews and edits** .drawio files in Draw.io (app.diagrams.net)
4. **User exports PNG** and manually replaces placeholders in Word

This approach saves tokens (no PNG conversion code), ensures diagram quality through human review, and gives users editable source files.

**IMPORTANT: Read the `project-drawio-generator` skill** before generating any .drawio file for XML rules and templates.

### Architecture Diagram Rules

**Use scenario-based (场景式) architecture diagrams, NOT layered software architecture diagrams.**

A good architecture diagram for competition papers should show:
- Physical deployment scene (spatial layout of devices)
- Device appearance with key components labeled
- Communication links between devices (UWB, WiFi, BLE, etc.)
- System composition box listing key modules
- System workflow box with numbered steps
- Data flow legend and key technical specs

Do NOT create abstract layered diagrams (应用层→通信层→驱动层→硬件层) — these are too academic and hard for evaluators to quickly understand.

## Workflow

### Step 1: Gather Project Information

Ask targeted questions to understand the project:

**Essential:**
- Project name and brief description
- Student grade level → determines which of the 4 tiers to use:
  - 小学低 (grades 1-3)
  - 小学高 (grades 4-6)
  - 初中 (grades 7-9) ← most common
  - 高中 (grades 10-12)
- Competition target (科创大赛, 金鹏论坛, etc.)
- What problem does it solve?
- How does it work? (technical overview)
- What materials/technologies are used?

**User-provided materials (expect these):**
- **Technical documentation** — detailed technical proposal/design document
- **Design photos** — 3D renders, CAD screenshots, design sketches (may be in PPTX)
- **Process photos** — hardware assembly, coding, debugging, testing
- **Product photos** — finished device from multiple angles

### Step 2: Process User-Provided Photos

**Photo classification and processing pipeline:**

1. **Scan the project folder** for all image files and PPTX files
2. **Extract images from PPTX** if present (use python-pptx)
3. **Classify photos** into categories:
   - Design photos (3D renders, CAD views, sketches)
   - Process photos (assembly, coding, testing)
   - Product photos (finished device)
   - Documentation photos (research notes, datasheets)
4. **Resize all photos** to max 600px on longest side for Word embedding
5. **Convert RGBA → RGB** (JPEG compatibility)
6. **Save processed photos** to a `photos_resized/` directory

```python
# Photo extraction from PPTX
from pptx import Presentation
from PIL import Image
import os, io

prs = Presentation("path/to/file.pptx")
for i, slide in enumerate(prs.slides):
    for shape in slide.shapes:
        if shape.shape_type == 13:  # Picture type
            blob = shape.image.blob
            img = Image.open(io.BytesIO(blob))
            img.save(f"ppt_images/slide{i+1:02d}.png")

# Resize for Word embedding
def resize_photo(path, out_path, max_size=600):
    img = Image.open(path)
    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    ratio = min(max_size / img.width, max_size / img.height)
    if ratio < 1:
        img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)
    img.save(out_path, quality=95)
```

### Step 3: Determine Paper Structure, Visual Style, and Transition Set

Based on grade level and project characteristics, **automatically** select three things (no user confirmation needed):

1. **Structure variant** — Follow the "自动选择算法" in `references/paper-structures.md`:
   - 初中/高中: Analyze project for independent technical problems (→B), iteration evidence (→C), separable modules (→D, 初中 only), otherwise default (→A)
   - 小学: Use `hash(项目名称) % 3` to select variant A/B/C

2. **Visual style preset** — Use `hash(项目名称) % 3` to select from 3 presets in `references/docx-generation.md`: 学术蓝 / 稳重灰 / 科技青

3. **Transition expression set** — Use `projectName.charCodeAt(0) % 3` to select transition set 0/1/2 from `references/writing-guidelines.md`

Key structural differences by grade:
- **小学低**: ~3000 words, story-like, simple structure, colloquial language (3 variants)
- **小学高**: ~5000 words, structured invention report, natural student voice with data (3 variants)
- **初中**: ~8000-10000 words, systematic technical paper, formal language, detailed data analysis (4 variants)
- **高中**: ~12000-15000 words, academic paper, literature review, statistical analysis (3 variants)

### Step 4: Write the Abstract (摘要)

**The abstract is the single most important section.** Evaluators will read it completely, even if they skim everything else.

The abstract MUST contain:
- What problem the project solves (1-2 sentences)
- Core technical approach (1-2 sentences)
- **Specific quantitative results** (not "效果良好" but "测距精度±10cm，成功率96%")
- Key innovation points (1-2 sentences)
- Practical value (1 sentence)

Refer to `references/writing-guidelines.md` for grade-specific abstract templates.

### Step 5: Write the Paper Body

Generate sections progressively. Follow the structure variant selected in Step 3, using `references/paper-structures.md` for section details.

**Transition language:** Use the transition expression set selected in Step 3. Refer to `references/writing-guidelines.md` → "过渡语料库" for the specific expressions. Also vary paragraph opening structures (直述式/背景先行式/数据先行式/问题先行式) across the paper.

**Writing principles across all grades:**
- Complete project documentation from start to finish — never skip steps
- Every claim backed by data or evidence
- Innovation points reinforced throughout (first in abstract, then in design rationale, then in test results, finally summarized)
- Honest about failures and iterations — this proves authenticity
- Student authenticity shown through writing details (debugging stories, personal observations), NOT through a standalone declaration section
- No metaphors or analogies for technical components (all grades, including 小低)

**Grade-specific language:**
- 小学 (both tiers): Colloquial, first person "我", natural student expressions
- 初中: Formal, mix of "我" and "本系统/本装置/本项目", technically precise
- 高中: Academic, "本研究/本文", with proper terminology and citations

Refer to `references/writing-guidelines.md` for detailed style guidance per grade.

### Step 6: Generate Background Illustrations (.drawio)

For the 项目背景 chapter, generate 3-5 background illustration .drawio files.

**IMPORTANT: Read `project-drawio-generator` SKILL.md first for XML rules and templates.**

Typical illustrations:
- **统计图表** — bar chart showing relevant data (e.g., myopia rates, pollution levels)
- **对比图** — side-by-side traditional vs. project solution
- **问题概述** — card-style layout showing pain points

**Naming convention**: Use sequential figure numbers with Chinese descriptions:
- `图3_宠物粪便处理方式统计.drawio`
- `图4_传统方案与本项目对比.drawio`

In the .docx, insert a placeholder at the correct location:
```
【此处插入 图3 宠物粪便处理方式统计】
```

### Step 7: Generate System Architecture Diagram (.drawio)

For 小学高 and above, generate a scenario-based architecture diagram .drawio file.

**IMPORTANT: Read `project-drawio-generator` SKILL.md first.**

The diagram should show:
- Physical deployment of devices in their usage scene
- Key components labeled on each device
- Communication links with dashed arrows and protocol labels
- System composition info box (right side)
- Workflow steps info box (right side)
- Data flow legend (bottom)
- Key technical specs bar (bottom)

**Filename**: `图5_系统架构图.drawio` (number follows previous figures)

**In .docx**: Insert placeholder `【此处插入 图5 系统架构图】`

For 小学低, diagrams are optional.

### Step 8: Generate Flow Chart (.drawio)

For 初中 and above, generate a flow chart .drawio file.

The flow chart should show the usage workflow with:
- Start/end rounded rectangles
- Process step boxes (color-coded by module)
- Decision diamonds with Yes/No branches
- Exception handling paths (side branches)
- Loop-back arrows for retry logic

**Filename**: `图6_工作流程图.drawio`

**In .docx**: Insert placeholder `【此处插入 图6 工作流程图】`

### Step 9: Generate Word Document (.docx)

Use Node.js `docx` package to generate the final Word document with all content embedded.

**Apply the visual style preset selected in Step 3.** Initialize `STYLE_PRESET` with `selectPreset(项目名称)` at the top of the generation code. This determines:
- Title/heading colors (`ACCENT`)
- Table header rendering mode (`hcell()` behavior)
- Section dividers between major chapters (`sectionDivider()`)

Refer to `references/docx-generation.md` for the complete code template including:
- **Style presets** (PRESETS object, selectPreset function, ACCENT/ACCENT_LIGHT/BORDER_COLOR)
- Helper functions (cell, hcell with 3 modes, makeTable, h1, h2, para, bullet, numbered)
- **sectionDivider()** — use between major sections instead of hardcoded PageBreak
- Image embedding helpers (figImg for JPG, figPng for PNG, placeholder for missing photos)
- Document structure with headers, footers, page numbers
- Proper numbering configs for bullets and numbered lists

**Diagram placeholders in .docx:**

For each .drawio diagram, insert a visible gray placeholder + figure caption:

```javascript
// Placeholder for diagram — user will replace after review
new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 200, after: 100 },
    children: [
        new TextRun({
            text: "【此处插入 图5 系统架构图】",
            font: FONT_SONG,
            size: 24,
            color: "999999",
        }),
    ],
}),
new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [
        new TextRun({
            text: "图5 系统架构图",
            font: FONT_SONG,
            size: 21,
        }),
    ],
}),
```

**User-provided photos** (process photos, product photos, 3D renders) are still directly embedded as before using figImg/figPng helpers.

**Photo embedding guidelines:**
- Process/product photos: 280-400px wide depending on orientation
- 3D design images: 300-320px wide
- Always add figure number and caption below each image

### Step 10: Verify References

**CRITICAL: Verify ALL references before finalizing.**

1. Use WebSearch to verify each reference exists
2. For Chinese journal papers: verify journal name, year, volume, issue, page numbers
3. For standards: verify standard number and title
4. For online resources: verify URL is accessible
5. Replace any fabricated references with real, verified ones

Common verified reference types:
- GB national standards (e.g., GB 11533-2011)
- Government reports (e.g., 国家卫健委 reports)
- IC datasheets (e.g., ESP32, DW1000)
- GitHub libraries (verify repo exists)
- Real academic papers (verify via web search)

### Step 11: Generate Research Proposal (if requested)

Research proposals (研究方案/开题报告) are a condensed pre-project document. Extract from the paper:

- 项目背景 (condensed)
- 研究目标 (with quantified indicators)
- 研究思路与技术路线
- 研究方法
- 创新点
- 研究计划 (timeline with milestones)
- 预期成果

Approximately 1/3 the length of the full paper. Save as a separate .docx file.

### Step 12: Finalize and Output

**Output structure:**
```
project_folder/
├── 项目名称_研究报告.docx              # Paper (photos embedded, diagram placeholders)
├── 项目名称_研究方案.docx              # Research proposal (if requested)
├── 图3_背景统计图表.drawio             # Background illustration (editable)
├── 图4_传统方案对比.drawio             # Comparison diagram (editable)
├── 图5_系统架构图.drawio               # Architecture diagram (editable)
├── 图6_工作流程图.drawio               # Flow chart (editable)
└── photos_resized/                     # Processed photos (intermediate)
```

**Inform the user** that:
1. All .drawio files can be opened at app.diagrams.net for review and editing
2. After review, export each diagram as PNG (File → Export as → PNG, 2x zoom recommended)
3. Open the .docx, find `【此处插入 图X ...】` placeholders, replace with exported PNGs
4. Recommended sizes in Word: architecture ~14cm wide, flowchart ~10cm wide

Copy all files to the output folder and present to user.

## Evaluator Context

Understanding how evaluators review projects helps write better papers:

**Evaluator review order:**
1. 项目介绍视频 / 演示视频 (first impression)
2. 项目方案 (technical overview)
3. 项目日志 (process authenticity)
4. 项目报告/论文 (deep dive)
5. 其他补充材料

**Implications for paper writing:**
- The paper is a **complete project record** — it documents everything from start to finish
- The abstract is the **one section evaluators definitely read fully** — make every word count
- Authenticity comes from writing details (debugging struggles, iteration stories), not standalone declarations
- Specific data and quantified results throughout demonstrate rigor
- Honest discussion of failures and iterations proves authenticity

## Resources

### references/paper-structures.md
Detailed paper structures for all four grade levels, with section descriptions and word count guidance.

### references/writing-guidelines.md
Grade-specific writing style, language rules, abstract templates, and common pitfalls to avoid.

### references/docx-generation.md
Complete Word document generation template using Node.js `docx` package. Includes helper functions, image embedding patterns, document structure, and photo processing pipeline.

### references/examples.md
Example sections from real competition papers showing best practices at each grade level.

### External: project-drawio-generator skill
All diagram generation uses the `project-drawio-generator` skill for XML rules and templates. Diagrams are generated as .drawio files for user review — no automatic PNG conversion needed.
