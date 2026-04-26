# Word Document (.docx) Generation Template

## Overview

Use Node.js `docx` package to generate professionally formatted Word documents with embedded images, tables, headers, footers, and page numbers.

**Install**: `npm install docx` (should already be available in the VM)

**CRITICAL FORMAT RULES:**
- Every figure MUST have a numbered caption **below** the image, centered (图注在下)
- Every table MUST have a numbered caption **above** the table, centered (表注在上)
- Use `figImg`/`figPng`/`figDiagramPlaceholder` for figures (auto-numbered caption below)
- Use `makeTableWithCaption` for tables (auto-numbered caption above)
- Never use `makeTable` directly — it produces tables without captions

---

## Font Specification (中文竞赛论文标准)

| 元素 | 字号 | 字体 | docx size值 | docx font值 |
|------|------|------|-------------|-------------|
| 封面标题 | 二号(22pt) | 黑体 | 44 | "黑体" |
| 封面副标题 | 三号(16pt) | 黑体 | 32 | "黑体" |
| 一级标题 | 三号(16pt) | 黑体 | 32 | "黑体" |
| 二级标题 | 四号(14pt) | 黑体 | 28 | "黑体" |
| **正文** | **小四(12pt)** | **宋体** | **24** | **"宋体"** |
| 表格内容 | 五号(10.5pt) | 宋体 | 21 | "宋体" |
| 表头 | 五号(10.5pt) | 黑体 | 21 | "黑体" |
| 图注 | 五号(10.5pt) | 宋体 | 21 | "宋体" |
| 页眉/页脚 | 小五(9pt) | 宋体 | 18 | "宋体" |

> **为什么用宋体/黑体？** 这两个字体是 Windows 系统自带的，评委电脑一定能正确显示。Arial 等西文字体在中文环境下可能导致显示异常。

---

## Complete Code Template

### Imports and Setup

```javascript
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, Header, Footer, AlignmentType, HeadingLevel, BorderStyle,
  WidthType, ShadingType, PageBreak, PageNumber, LevelFormat,
} = require("docx");

// Paths
const PHOTO = "photos_resized/";          // Processed photos directory
const PROJ = "project_folder/";           // Output directory

// Load pre-generated diagrams
const archImg = fs.readFileSync(PROJ + "system_arch_v2.png");
const flowImg = fs.readFileSync(PROJ + "flow_diagram.png");

function loadPhoto(name) { return fs.readFileSync(PHOTO + name); }
```

### Style Presets & Constants

```javascript
// ============================================================
// Style Presets — 3 套视觉风格，用 hash(项目名称) % 3 自动选择
// ============================================================
const PRESETS = {
  academic_blue: {
    name: "学术蓝",
    ACCENT: "2E5090",        // 深蓝标题色
    ACCENT_LIGHT: "D6E4F0",  // 浅蓝表头背景
    BORDER: "BBBBBB",
    headerMode: "colored_bg", // 表头：蓝色背景填充
    sectionDivider: "page_break", // 章节分隔：分页符
  },
  steady_gray: {
    name: "稳重灰",
    ACCENT: "333333",        // 深灰标题色
    ACCENT_LIGHT: "F2F2F2",  // 极浅灰（仅备用，headerMode 不使用背景）
    BORDER: "AAAAAA",
    headerMode: "bold_only",  // 表头：仅加粗无背景
    sectionDivider: "none",   // 无分隔，连续排版
  },
  tech_teal: {
    name: "科技青",
    ACCENT: "1A7A6D",        // 青色标题色
    ACCENT_LIGHT: "E0F2EF",  // 浅青背景（备用）
    BORDER: "CCCCCC",
    headerMode: "bottom_border", // 表头：无背景+粗底线
    sectionDivider: "hr_line",   // 细水平线
  },
};

// ---- 自动选择预设 ----
function selectPreset(projectName) {
  const hash = [...projectName].reduce((sum, c) => sum + c.charCodeAt(0), 0);
  const keys = Object.keys(PRESETS);
  return PRESETS[keys[hash % keys.length]];
}

// 使用方式：const STYLE = selectPreset("医院自动取药系统");
const STYLE_PRESET = selectPreset("项目名称");  // ← 替换为实际项目名称

// ---- 从预设导出颜色常量 ----
const ACCENT = STYLE_PRESET.ACCENT;
const ACCENT_LIGHT = STYLE_PRESET.ACCENT_LIGHT;
const BORDER_COLOR = STYLE_PRESET.BORDER;

// Font constants — 宋体/黑体 are Windows built-in, guaranteed to display correctly
const FONT_SONG = "宋体";     // 正文、表格、图注、表注
const FONT_HEI = "黑体";      // 标题、表头
const SZ_BODY = 24;           // 小四 = 12pt = 24 half-points
const SZ_TABLE = 21;          // 五号 = 10.5pt
const SZ_CAPTION = 21;        // 五号 = 10.5pt (图注、表注)
const SZ_H1 = 32;             // 三号 = 16pt
const SZ_H2 = 28;             // 四号 = 14pt
const SZ_TITLE = 44;          // 二号 = 22pt
const SZ_SUBTITLE = 32;       // 三号 = 16pt
const SZ_HEADER = 18;         // 小五 = 9pt

// ============================================================
// Figure & Table Numbering Configuration
// ============================================================
// Two numbering modes:
//   "sequential"  — 图1, 图2, ... 图55 / 表1, 表2, ... 表20
//   "chapter"     — 图1.1, 图1.2, 图2.1 / 表1.1, 表2.1
// Set this based on user preference or competition requirements.
const NUMBERING_MODE = "sequential";  // or "chapter"
let currentChapter = 0;               // updated by h1() when mode is "chapter"
let figNum = 0;                       // global figure counter (sequential mode)
let tabNum = 0;                       // global table counter (sequential mode)
let chapterFigNum = 0;                // per-chapter figure counter (chapter mode)
let chapterTabNum = 0;                // per-chapter table counter (chapter mode)

function nextFigLabel() {
  if (NUMBERING_MODE === "chapter") {
    chapterFigNum++;
    return `图${currentChapter}.${chapterFigNum}`;
  }
  figNum++;
  return `图${figNum}`;
}

function nextTabLabel() {
  if (NUMBERING_MODE === "chapter") {
    chapterTabNum++;
    return `表${currentChapter}.${chapterTabNum}`;
  }
  tabNum++;
  return `表${tabNum}`;
}

// Table borders
const border = { style: BorderStyle.SINGLE, size: 1, color: BORDER_COLOR };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 60, bottom: 60, left: 100, right: 100 };
```

### Helper Functions

```javascript
// ---- Table cell helper ----
function cell(text, opts = {}) {
  const { bold, shading, width, alignment, font, size, colspan } = opts;
  const runs = typeof text === "string"
    ? [new TextRun({ text, bold: bold || false, font: font || FONT_SONG, size: size || SZ_TABLE })]
    : Array.isArray(text) ? text : [];
  const co = {
    borders, margins: cellMargins,
    children: [new Paragraph({
      children: runs,
      alignment: alignment || AlignmentType.LEFT,
      spacing: { after: 0, line: 276 }
    })]
  };
  if (shading) co.shading = { fill: shading, type: ShadingType.CLEAR };
  if (width) co.width = { size: width, type: WidthType.DXA };
  if (colspan) co.columnSpan = colspan;
  return new TableCell(co);
}

// ---- Header cell (3 rendering modes based on style preset) ----
function hcell(text, width) {
  const mode = STYLE_PRESET.headerMode;
  if (mode === "bold_only") {
    // 稳重灰：仅加粗，无背景色
    return cell(text, { bold: true, width, font: FONT_HEI, size: SZ_TABLE });
  } else if (mode === "bottom_border") {
    // 科技青：无背景色，粗底线
    const thickBottom = { style: BorderStyle.SINGLE, size: 3, color: ACCENT };
    const co = {
      borders: { ...borders, bottom: thickBottom },
      margins: cellMargins,
      children: [new Paragraph({
        children: [new TextRun({ text, bold: true, font: FONT_HEI, size: SZ_TABLE })],
        alignment: AlignmentType.LEFT,
        spacing: { after: 0, line: 276 }
      })]
    };
    if (width) co.width = { size: width, type: WidthType.DXA };
    return new TableCell(co);
  } else {
    // 学术蓝（默认）：蓝色背景填充
    return cell(text, { bold: true, shading: ACCENT_LIGHT, width, font: FONT_HEI, size: SZ_TABLE });
  }
}

// ---- Section divider (based on style preset) ----
function sectionDivider() {
  const mode = STYLE_PRESET.sectionDivider;
  if (mode === "page_break") {
    return new Paragraph({ children: [new PageBreak()] });
  } else if (mode === "hr_line") {
    return new Paragraph({
      spacing: { before: 300, after: 300 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: BORDER_COLOR, space: 8 } },
      children: [],
    });
  } else {
    // "none"：纯间距，无分隔符
    return new Paragraph({ spacing: { before: 400, after: 200 }, children: [] });
  }
}

// ---- Quick table builder ----
function makeTable(headers, rows, colWidths) {
  const tw = colWidths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: tw, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [
      new TableRow({ children: headers.map((h, i) => hcell(h, colWidths[i])) }),
      ...rows.map(row => new TableRow({
        children: row.map((c, i) => cell(c, { width: colWidths[i] }))
      }))
    ]
  });
}

// ---- Heading 1 (三号 黑体) ----
function h1(text) {
  // In chapter numbering mode, reset per-chapter counters
  if (NUMBERING_MODE === "chapter") {
    currentChapter++;
    chapterFigNum = 0;
    chapterTabNum = 0;
  }
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text, bold: true, font: FONT_HEI, size: SZ_H1, color: ACCENT })],
    spacing: { before: 360, after: 200 }
  });
}

// ---- Heading 2 (四号 黑体) ----
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun({ text, bold: true, font: FONT_HEI, size: SZ_H2, color: ACCENT })],
    spacing: { before: 240, after: 160 }
  });
}

// ---- Body paragraph (小四 宋体) ----
function para(text, opts = {}) {
  const { bold, indent, alignment, spacing } = opts;
  const runs = typeof text === "string"
    ? [new TextRun({ text, font: FONT_SONG, size: SZ_BODY, bold })]
    : Array.isArray(text) ? text : [];
  return new Paragraph({
    children: runs,
    alignment: alignment || AlignmentType.JUSTIFIED,
    spacing: { after: spacing !== undefined ? spacing : 120, line: 360 },
    indent: indent ? { firstLine: 480 } : undefined
  });
}
```

### Image Embedding Helpers

```javascript
// ============================================================
// Figure Helpers — 图注在图片底部，居中，五号宋体
// ============================================================

// ---- Embed JPG image with caption ----
function figImg(photoName, caption, w, h) {
  const label = nextFigLabel();
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 60 },
      children: [new ImageRun({
        type: "jpg",
        data: loadPhoto(photoName),
        transformation: { width: w, height: h },
        altText: { title: caption, description: caption, name: photoName }
      })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
      children: [new TextRun({
        text: `${label} ${caption}`,
        font: FONT_SONG, size: SZ_CAPTION,
      })]
    }),
  ];
}

// ---- Embed PNG image with caption ----
function figPng(data, caption, w, h) {
  const label = nextFigLabel();
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 60 },
      children: [new ImageRun({
        type: "png",
        data,
        transformation: { width: w, height: h },
        altText: { title: caption, description: caption, name: caption }
      })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
      children: [new TextRun({
        text: `${label} ${caption}`,
        font: FONT_SONG, size: SZ_CAPTION,
      })]
    }),
  ];
}

// ---- Placeholder for missing photos ----
function placeholder(caption) {
  const label = nextFigLabel();
  const borderPH = { style: BorderStyle.DASHED, size: 2, color: "999999" };
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 0 },
      border: { top: borderPH, bottom: borderPH, left: borderPH, right: borderPH },
      children: [new TextRun({ text: "\n", font: FONT_SONG, size: SZ_BODY })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      border: {
        left: { style: BorderStyle.DASHED, size: 2, color: "999999" },
        right: { style: BorderStyle.DASHED, size: 2, color: "999999" }
      },
      children: [new TextRun({
        text: `【占位符】请补充照片：${caption}`,
        font: FONT_SONG, size: SZ_BODY, color: "CC0000",
      })],
      spacing: { before: 200, after: 200 },
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 60 },
      border: {
        bottom: borderPH,
        left: { style: BorderStyle.DASHED, size: 2, color: "999999" },
        right: { style: BorderStyle.DASHED, size: 2, color: "999999" }
      },
      children: [new TextRun({ text: "\n", font: FONT_SONG, size: SZ_BODY })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
      children: [new TextRun({
        text: `${label} ${caption}`,
        font: FONT_SONG, size: SZ_CAPTION,
      })]
    }),
  ];
}

// ---- Diagram placeholder (for .drawio diagrams, user will replace later) ----
function figDiagramPlaceholder(caption) {
  const label = nextFigLabel();
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 100 },
      children: [new TextRun({
        text: `【此处插入 ${label} ${caption}】`,
        font: FONT_SONG, size: SZ_BODY, color: "999999",
      })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
      children: [new TextRun({
        text: `${label} ${caption}`,
        font: FONT_SONG, size: SZ_CAPTION,
      })]
    }),
  ];
}

// ============================================================
// Table Helpers — 表注在表格顶部，居中，五号宋体
// ============================================================

// ---- Table with caption (表注在上方居中) ----
function makeTableWithCaption(caption, headers, rows, colWidths) {
  const label = nextTabLabel();
  const tw = colWidths.reduce((a, b) => a + b, 0);
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 100 },
      children: [new TextRun({
        text: `${label} ${caption}`,
        font: FONT_SONG, size: SZ_CAPTION,
      })]
    }),
    new Table({
      width: { size: tw, type: WidthType.DXA },
      columnWidths: colWidths,
      rows: [
        new TableRow({ children: headers.map((h, i) => hcell(h, colWidths[i])) }),
        ...rows.map(row => new TableRow({
          children: row.map((c, i) => cell(c, { width: colWidths[i] }))
        }))
      ]
    }),
    new Paragraph({ spacing: { after: 200 }, children: [] }),
  ];
}
```

### Numbering Configuration

```javascript
const numberingConfig = [
  {
    reference: "bullets",
    levels: [{
      level: 0, format: LevelFormat.BULLET, text: "\u2022",
      alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } }
    }]
  },
  // Create multiple numbered list references (n1, n2, n3, n4)
  // to allow independent numbering for different sections
  ...["n1", "n2", "n3", "n4"].map(ref => ({
    reference: ref,
    levels: [{
      level: 0, format: LevelFormat.DECIMAL, text: "%1.",
      alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } }
    }]
  })),
];

function bullet(text) {
  const r = typeof text === "string"
    ? [new TextRun({ text, font: FONT_SONG, size: SZ_BODY })] : text;
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    children: r,
    spacing: { after: 60, line: 312 }
  });
}

function numbered(text, ref) {
  const r = typeof text === "string"
    ? [new TextRun({ text, font: FONT_SONG, size: SZ_BODY })] : text;
  return new Paragraph({
    numbering: { reference: ref || "n1", level: 0 },
    children: r,
    spacing: { after: 80, line: 312 }
  });
}
```

### Document Assembly

```javascript
const C = [];  // Array to collect all paragraphs

// ===== TITLE PAGE (二号 黑体) =====
C.push(new Paragraph({ spacing: { before: 3600 } }));
C.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 100 },
  children: [new TextRun({ text: "项目名称第一行", font: FONT_HEI, size: SZ_TITLE, bold: true, color: ACCENT })]
}));
C.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 600 },
  children: [new TextRun({ text: "项目名称第二行", font: FONT_HEI, size: SZ_TITLE, bold: true, color: ACCENT })]
}));
C.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 1200 },
  children: [new TextRun({ text: "研究报告", font: FONT_HEI, size: SZ_SUBTITLE, color: "666666" })]
}));
C.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 200 },
  children: [new TextRun({ text: "竞赛名称", font: FONT_SONG, size: SZ_BODY, color: "888888" })]
}));
C.push(new Paragraph({ children: [new PageBreak()] }));

// ===== ABSTRACT (小四 宋体) =====
C.push(h1("摘要"));
C.push(para("摘要正文...", { indent: true }));
C.push(para([
  new TextRun({ text: "关键词：", font: FONT_HEI, size: SZ_BODY, bold: true }),
  new TextRun({ text: "关键词1；关键词2；关键词3", font: FONT_SONG, size: SZ_BODY }),
]));

// ===== 项目背景 =====
// Use sectionDivider() between major sections (respects style preset)
C.push(sectionDivider());
C.push(h1("一、项目背景"));
C.push(h2("1.1 问题现状分析"));
C.push(para("背景描述...", { indent: true }));
// Insert background illustrations here:
C.push(...figImg("statistics_chart.jpg", "图表标题", 480, 300));
C.push(...figImg("problems_overview.jpg", "问题概览标题", 500, 280));

// ===== Continue with remaining sections =====
// Use the same pattern: h1/h2 for headings, para for text,
// makeTableWithCaption for data tables (caption on top),
// figImg/figPng for images (caption on bottom),
// placeholder for missing photos

// ===== REFERENCES =====
C.push(h1("参考文献"));
const refs = [
  "参考文献1...",
  "参考文献2...",
];
refs.forEach((r, i) => C.push(para(`[${i + 1}] ${r}`, { spacing: 80 })));
```

### Build and Save

```javascript
const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT_SONG, size: SZ_BODY } } },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1",
        basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: SZ_H1, bold: true, font: FONT_HEI, color: ACCENT },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2",
        basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: SZ_H2, bold: true, font: FONT_HEI, color: ACCENT },
        paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 1 }
      },
    ]
  },
  numbering: { config: numberingConfig },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },  // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({
            text: "项目名称 — 研究报告",
            font: FONT_SONG, size: SZ_HEADER, color: "999999"
          })],
          border: {
            bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 4 }
          }
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "— ", font: FONT_SONG, size: SZ_HEADER, color: "999999" }),
            new TextRun({ children: [PageNumber.CURRENT], font: FONT_SONG, size: SZ_HEADER, color: "999999" }),
            new TextRun({ text: " —", font: FONT_SONG, size: SZ_HEADER, color: "999999" }),
          ]
        })]
      })
    },
    children: C,
  }],
});

const OUT_PATH = PROJ + "项目名称_研究报告.docx";
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT_PATH, buf);
  console.log("DOCX created: " + OUT_PATH);
  if (NUMBERING_MODE === "sequential") {
    console.log("Total figures: " + figNum);
    console.log("Total tables: " + tabNum);
  } else {
    console.log("Numbering mode: chapter-based");
    console.log("Total chapters: " + currentChapter);
  }
});
```

---

## Image Size Guidelines

| Image Type | Width (px) | Notes |
|------------|-----------|-------|
| Background illustrations (statistics, comparison) | 480-520 | Match page width nicely |
| Architecture diagram | 560 | Wider to show full scene |
| Flow chart | 400 | Narrower, taller |
| Process photos (landscape) | 400 | Standard process shots |
| Process photos (portrait) | 280 | Taller photos |
| 3D design renders | 300-320 | Usually square-ish |
| Product photos | 280-400 | Depends on orientation |

**Height calculation**: Maintain original aspect ratio. Calculate from original image dimensions:
```javascript
// Calculate height preserving aspect ratio
const targetWidth = 400;
const ratio = originalHeight / originalWidth;
const targetHeight = Math.round(targetWidth * ratio);
```

---

## Rich Text Patterns

### Bold label + normal description (for contributions, debug problems)
```javascript
C.push(para([
  new TextRun({ text: "问题1：标题。", bold: true, font: FONT_SONG, size: SZ_BODY }),
  new TextRun({ text: "详细描述...", font: FONT_SONG, size: SZ_BODY }),
], { indent: true }));
```

### Numbered list with bold label
```javascript
C.push(numbered([
  new TextRun({ text: "调研阶段：", bold: true, font: FONT_HEI, size: SZ_BODY }),
  new TextRun({ text: "具体工作描述...", font: FONT_SONG, size: SZ_BODY }),
], "n1"));
```

### Section divider before major section
```javascript
// Use sectionDivider() — automatically applies the correct divider for the current style preset
// (page break for 学术蓝, horizontal line for 科技青, spacing only for 稳重灰)
C.push(sectionDivider());
C.push(h1("章节标题"));
```

---

## Photo Processing Pipeline

### Step 1: Extract from PPTX (if applicable)

```bash
pip install python-pptx Pillow --break-system-packages
```

```python
from pptx import Presentation
from PIL import Image
import os, io

def extract_pptx_images(pptx_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    prs = Presentation(pptx_path)
    count = 0
    for i, slide in enumerate(prs.slides):
        for shape in slide.shapes:
            if shape.shape_type == 13:  # Picture
                blob = shape.image.blob
                img = Image.open(io.BytesIO(blob))
                out_path = os.path.join(out_dir, f"slide{i+1:02d}.png")
                img.save(out_path)
                count += 1
                print(f"  Extracted: slide{i+1:02d}.png ({img.size[0]}x{img.size[1]})")
    print(f"Total: {count} images extracted")
```

### Step 2: Resize and Convert

```python
def resize_for_docx(input_path, output_path, max_size=600):
    """Resize image to max dimension, convert RGBA to RGB."""
    img = Image.open(input_path)

    # Convert RGBA to RGB (white background)
    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')

    # Resize if needed
    ratio = min(max_size / img.width, max_size / img.height)
    if ratio < 1:
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    img.save(output_path, quality=95)
    print(f"  {os.path.basename(output_path)}: {img.size[0]}x{img.size[1]}")
```

### Step 3: Classify Photos

Based on filename patterns and content, classify into:
- `bg_*.jpg` — Background/reference photos (from web or stock)
- `3d_*.png` — 3D design renders (from PPTX or CAD exports)
- `design_*.jpg` — Design process photos
- `coding*.jpg` — Programming/debugging photos
- `test_*.jpg` — Testing process photos
- `wiring*.jpg` — Hardware assembly photos
- Other descriptive names based on content

---

## Common Issues

**Images not appearing in Word:**
- Ensure the image file exists and is readable with `fs.readFileSync()`
- Check that `type` matches actual format: "jpg" for JPEG, "png" for PNG
- Verify transformation dimensions are reasonable (not too small or too large)

**Tables too wide:**
- Total column widths should sum to ~9360 DXA (A4 width minus margins)
- Use DXA units: 1 inch = 1440 DXA

**Numbering resets unexpectedly:**
- Each `reference` string creates an independent counter
- Use different references ("n1", "n2", "n3") for different sections that need independent numbering
- Same reference continues numbering from where it left off

**Chinese font in Word:**
- 使用"宋体"（正文）和"黑体"（标题）确保评委电脑能正确显示
- 宋体和黑体是 Windows 系统自带字体，无需额外安装
- docx 包中直接使用中文字体名即可：`font: "宋体"`、`font: "黑体"`
