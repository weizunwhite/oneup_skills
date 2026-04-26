# Template Specifications & Code Patterns

This file contains the complete Node.js `docx` code patterns for generating each
template type. When generating templates, use these patterns as the foundation.

## Table of Contents

1. [Common Setup](#common-setup)
2. [Experiment Record (实验记录表)](#experiment-record)
3. [Data Collection Sheet (数据采集表)](#data-collection-sheet)
4. [Observation Log (观察日志)](#observation-log)
5. [Interview Record (访谈记录表)](#interview-record)
6. [Literature Excerpt (文献摘录表)](#literature-excerpt)
7. [Survey Questionnaire (问卷调查表)](#survey-questionnaire)

---

## Common Setup

All templates share these constants and helpers. Put this at the top of every
generation script.

```javascript
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageBreak, LevelFormat,
} = require("docx");

// ── Font constants (中文竞赛标准) ──
const FONT_SONG = "宋体";
const FONT_HEI  = "黑体";
const SZ_TITLE  = 32;  // 三号 16pt
const SZ_H2     = 28;  // 四号 14pt
const SZ_TH     = 21;  // 五号 10.5pt (table header)
const SZ_TD     = 21;  // 五号 10.5pt (table content)
const SZ_NOTE   = 18;  // 小五 9pt (instructions)

// ── Page setup (A4) ──
const PAGE_W = 11906;  // A4 width in DXA
const PAGE_H = 16838;  // A4 height in DXA
const MARGIN = 1440;   // 1 inch = 2.54cm
const CONTENT_W = PAGE_W - MARGIN * 2;  // usable width

// ── Borders ──
const border = { style: BorderStyle.SINGLE, size: 1, color: "000000" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0 };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

// ── Row height for handwriting ──
const ROW_H = 600;  // ~1cm, comfortable for handwriting

// ── Helper: table header cell ──
function thCell(text, width) {
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: "E8E8E8", type: ShadingType.CLEAR },
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    verticalAlign: "center",
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, font: FONT_HEI, size: SZ_TH, bold: true })],
    })],
  });
}

// ── Helper: table data cell (blank for filling in) ──
function tdCell(text, width) {
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    children: [new Paragraph({
      children: text
        ? [new TextRun({ text, font: FONT_SONG, size: SZ_TD })]
        : [],
    })],
  });
}

// ── Helper: blank rows ──
function blankRows(colWidths, count = 10) {
  const rows = [];
  for (let i = 0; i < count; i++) {
    rows.push(new TableRow({
      height: { value: ROW_H, rule: "atLeast" },
      children: colWidths.map(w => tdCell("", w)),
    }));
  }
  return rows;
}

// ── Helper: title paragraph ──
function title(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [new TextRun({ text, font: FONT_HEI, size: SZ_TITLE, bold: true })],
  });
}

// ── Helper: info header (项目名称 / 姓名 / 日期) ──
function infoHeader(projectName) {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [Math.floor(CONTENT_W/3), Math.floor(CONTENT_W/3), Math.floor(CONTENT_W/3)],
    rows: [new TableRow({
      children: [
        tdCellNoBorder(`项目名称：${projectName}`, Math.floor(CONTENT_W/3)),
        tdCellNoBorder("记录人：________", Math.floor(CONTENT_W/3)),
        tdCellNoBorder("日期：____年____月____日", Math.floor(CONTENT_W/3)),
      ],
    })],
  });
}

function tdCellNoBorder(text, width) {
  return new TableCell({
    borders: noBorders,
    width: { size: width, type: WidthType.DXA },
    margins: { top: 40, bottom: 40, left: 0, right: 0 },
    children: [new Paragraph({
      children: [new TextRun({ text, font: FONT_SONG, size: SZ_TD })],
    })],
  });
}

// ── Helper: instruction note ──
function note(text) {
  return new Paragraph({
    spacing: { before: 100, after: 100 },
    children: [new TextRun({ text: "说明：" + text, font: FONT_SONG, size: SZ_NOTE, italics: true, color: "666666" })],
  });
}

// ── Helper: spacer ──
function spacer(h = 200) {
  return new Paragraph({ spacing: { before: h } });
}

// ── Save document ──
async function saveDoc(doc, filename) {
  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(filename, buffer);
  console.log("Saved:", filename);
}
```

---

## Experiment Record

**实验记录表** — Records each experiment with conditions, steps, results, observations.

### Layout

```
┌─────────────────────────────────────────┐
│           实验记录表                      │
│  项目名称：XXX    记录人：___  日期：___   │
├─────────────────────────────────────────┤
│ 实验编号：___    实验名称：______________ │
├──────┬──────────────────────────────────┤
│ 实验目的 │                               │
├──────┼──────────────────────────────────┤
│ 实验器材 │                               │
├──────┼──────────────────────────────────┤
│ 实验步骤 │ 1.                            │
│          │ 2.                            │
│          │ 3.                            │
├──────┼──────────────────────────────────┤
│ 实验数据 │                               │
├──────┼──────────────────────────────────┤
│ 实验现象 │                               │
├──────┼──────────────────────────────────┤
│ 结果分析 │                               │
├──────┼──────────────────────────────────┤
│ 问题记录 │                               │
└──────┴──────────────────────────────────┘
```

### Code Pattern

```javascript
function experimentRecord(projectName) {
  const labelW = 1800;
  const valueW = CONTENT_W - labelW;

  function labelValueRow(label, heightMultiple = 1) {
    return new TableRow({
      height: { value: ROW_H * heightMultiple, rule: "atLeast" },
      children: [
        new TableCell({
          borders, width: { size: labelW, type: WidthType.DXA },
          shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
          margins: { top: 60, bottom: 60, left: 80, right: 80 },
          verticalAlign: "center",
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: label, font: FONT_HEI, size: SZ_TH, bold: true })],
          })],
        }),
        tdCell("", valueW),
      ],
    });
  }

  const table = new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [labelW, valueW],
    rows: [
      labelValueRow("实验目的", 2),
      labelValueRow("实验器材", 2),
      labelValueRow("实验步骤", 4),
      labelValueRow("实验数据", 3),
      labelValueRow("实验现象", 2),
      labelValueRow("结果分析", 3),
      labelValueRow("问题记录", 2),
    ],
  });

  // Build multiple pages (one experiment per page)
  const children = [];
  for (let i = 0; i < 5; i++) {
    if (i > 0) children.push(new Paragraph({ children: [new PageBreak()] }));
    children.push(title("实验记录表"));
    children.push(infoHeader(projectName));
    children.push(spacer(100));
    // Experiment number row
    children.push(new Paragraph({
      children: [new TextRun({ text: `实验编号：${i+1}    实验名称：`, font: FONT_SONG, size: SZ_TD })],
    }));
    children.push(spacer(100));
    children.push(table);  // Note: reuse same table definition
    children.push(spacer(100));
    children.push(note("请如实记录实验过程，包括失败的实验和意外发现"));
  }

  return children;
}
```

---

## Data Collection Sheet

**数据采集表** — Tabular format for recording measurements with multiple data points.

### Layout

Column headers should be customized based on the project. Common patterns:

**For measurement projects:**
| 序号 | 时间 | 测量对象 | 测量值1 | 测量值2 | 单位 | 备注 |

**For testing projects:**
| 序号 | 测试条件 | 测试项目 | 预期结果 | 实际结果 | 是否通过 | 备注 |

**For survey/counting projects:**
| 序号 | 日期 | 地点 | 统计项1 | 统计项2 | 统计项3 | 合计 |

### Code Pattern

```javascript
function dataCollectionSheet(projectName, columns) {
  // columns = [{ header: "序号", width: 800 }, { header: "时间", width: 1200 }, ...]
  // If not provided, use default columns
  if (!columns) {
    columns = [
      { header: "序号", width: 800 },
      { header: "日期", width: 1200 },
      { header: "测量条件", width: 1800 },
      { header: "数据1", width: 1400 },
      { header: "数据2", width: 1400 },
      { header: "数据3", width: 1400 },
      { header: "备注", width: Math.max(CONTENT_W - 8000, 1000) },
    ];
  }

  // Ensure widths sum to CONTENT_W
  const totalW = columns.reduce((s, c) => s + c.width, 0);
  const scale = CONTENT_W / totalW;
  columns = columns.map(c => ({ ...c, width: Math.round(c.width * scale) }));

  const colWidths = columns.map(c => c.width);

  const headerRow = new TableRow({
    children: columns.map(c => thCell(c.header, c.width)),
  });

  const table = new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [headerRow, ...blankRows(colWidths, 20)],
  });

  return [
    title("数据采集表"),
    infoHeader(projectName),
    spacer(100),
    note("每次测量/采集数据时填写一行，注意记录单位和测量条件"),
    spacer(100),
    table,
    spacer(200),
    // Statistics summary section
    new Paragraph({
      children: [new TextRun({ text: "数据统计", font: FONT_HEI, size: SZ_H2, bold: true })],
    }),
    spacer(100),
    new Paragraph({
      children: [new TextRun({ text: "平均值：________  最大值：________  最小值：________", font: FONT_SONG, size: SZ_TD })],
    }),
    spacer(100),
    new Paragraph({
      children: [new TextRun({ text: "数据分析与结论：", font: FONT_SONG, size: SZ_TD })],
    }),
    spacer(600),
  ];
}
```

---

## Observation Log

**观察日志** — For recording observations over time (daily, weekly, or per-event).

### Layout

```
┌──────────────────────────────────────┐
│            观察日志                    │
│ 项目名称：XXX   观察人：___  第__次   │
├──────┬───────────────────────────────┤
│ 日期时间 │ ____年__月__日  __:__     │
├──────┼───────────────────────────────┤
│ 观察地点 │                           │
├──────┼───────────────────────────────┤
│ 观察对象 │                           │
├──────┼───────────────────────────────┤
│ 观察内容 │                           │
│ 与现象   │                           │
│          │                           │
├──────┼───────────────────────────────┤
│ 数据记录 │                           │
├──────┼───────────────────────────────┤
│ 思考与   │                           │
│ 疑问     │                           │
├──────┼───────────────────────────────┤
│ 草图/示  │                           │
│ 意图     │ (可在此处画图)             │
└──────┴───────────────────────────────┘
```

### Code Pattern

Same label-value pattern as Experiment Record, but with observation-specific fields.
Generate 10 pages (one observation per page) by default.

```javascript
function observationLog(projectName) {
  const labelW = 1800;
  const valueW = CONTENT_W - labelW;

  function lvRow(label, h = 1) {
    return new TableRow({
      height: { value: ROW_H * h, rule: "atLeast" },
      children: [
        new TableCell({
          borders, width: { size: labelW, type: WidthType.DXA },
          shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
          margins: { top: 60, bottom: 60, left: 80, right: 80 },
          verticalAlign: "center",
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: label, font: FONT_HEI, size: SZ_TH, bold: true })],
          })],
        }),
        tdCell("", valueW),
      ],
    });
  }

  const children = [];
  for (let i = 0; i < 10; i++) {
    if (i > 0) children.push(new Paragraph({ children: [new PageBreak()] }));
    children.push(title("观察日志"));
    children.push(infoHeader(projectName));
    children.push(new Paragraph({
      alignment: AlignmentType.RIGHT,
      children: [new TextRun({ text: `第 ${i+1} 次观察`, font: FONT_SONG, size: SZ_TD })],
    }));
    children.push(spacer(100));
    children.push(new Table({
      width: { size: CONTENT_W, type: WidthType.DXA },
      columnWidths: [labelW, valueW],
      rows: [
        lvRow("日期时间"),
        lvRow("观察地点"),
        lvRow("观察对象"),
        lvRow("观察内容与现象", 4),
        lvRow("数据记录", 2),
        lvRow("思考与疑问", 2),
        lvRow("草图/示意图", 4),
      ],
    }));
  }

  return children;
}
```

---

## Interview Record

**访谈记录表** — For recording expert or user interviews.

### Layout

```
┌──────────────────────────────────────┐
│          访谈记录表                   │
│ 项目名称：XXX                        │
├──────┬───────────────────────────────┤
│ 访谈日期 │                           │
├──────┼───────────────────────────────┤
│ 受访者姓名│                          │
├──────┼───────────────────────────────┤
│ 受访者身份│ □专家 □用户 □其他:___    │
├──────┼───────────────────────────────┤
│ 访谈方式 │ □面对面 □电话 □线上       │
├──────┼───────────────────────────────┤
│ 访谈目的 │                           │
├──────┴───────────────────────────────┤
│ 访谈内容记录                          │
│ 问题1：                              │
│ 回答：                               │
│                                      │
│ 问题2：                              │
│ 回答：                               │
│                                      │
│ ...                                  │
├──────────────────────────────────────┤
│ 主要收获与启发                        │
│                                      │
├──────────────────────────────────────┤
│ 访谈人签名：___  受访者签名：___      │
└──────────────────────────────────────┘
```

### Code Pattern

```javascript
function interviewRecord(projectName) {
  const labelW = 1800;
  const valueW = CONTENT_W - labelW;

  function lvRow(label, h = 1) {
    return new TableRow({
      height: { value: ROW_H * h, rule: "atLeast" },
      children: [
        new TableCell({
          borders, width: { size: labelW, type: WidthType.DXA },
          shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
          margins: { top: 60, bottom: 60, left: 80, right: 80 },
          verticalAlign: "center",
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: label, font: FONT_HEI, size: SZ_TH, bold: true })],
          })],
        }),
        tdCell("", valueW),
      ],
    });
  }

  // Full-width row for longer content sections
  function fullRow(label, h = 1) {
    return [
      new TableRow({
        children: [
          new TableCell({
            borders, width: { size: CONTENT_W, type: WidthType.DXA },
            columnSpan: 2,
            shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
            margins: { top: 60, bottom: 60, left: 80, right: 80 },
            children: [new Paragraph({
              children: [new TextRun({ text: label, font: FONT_HEI, size: SZ_TH, bold: true })],
            })],
          }),
        ],
      }),
      new TableRow({
        height: { value: ROW_H * h, rule: "atLeast" },
        children: [
          new TableCell({
            borders, width: { size: CONTENT_W, type: WidthType.DXA },
            columnSpan: 2,
            margins: { top: 60, bottom: 60, left: 80, right: 80 },
            children: [new Paragraph({})],
          }),
        ],
      }),
    ];
  }

  const children = [];
  for (let i = 0; i < 3; i++) {
    if (i > 0) children.push(new Paragraph({ children: [new PageBreak()] }));
    children.push(title("访谈记录表"));
    children.push(infoHeader(projectName));
    children.push(spacer(100));

    children.push(new Table({
      width: { size: CONTENT_W, type: WidthType.DXA },
      columnWidths: [labelW, valueW],
      rows: [
        lvRow("访谈日期"),
        lvRow("受访者姓名"),
        lvRow("受访者身份"),
        lvRow("访谈方式"),
        lvRow("访谈目的", 2),
        ...fullRow("访谈内容记录（请详细记录问答内容）", 12),
        ...fullRow("主要收获与启发", 3),
      ],
    }));

    children.push(spacer(200));
    children.push(new Paragraph({
      children: [new TextRun({
        text: "访谈人签名：____________    受访者签名：____________",
        font: FONT_SONG, size: SZ_TD,
      })],
    }));
  }

  return children;
}
```

---

## Literature Excerpt

**文献摘录表** — For recording key information from research papers, books, and websites.

### Layout

Tabular format, one row per source:

| 序号 | 文献题目 | 作者 | 来源/出处 | 发表时间 | 摘录要点 | 对本项目的启发 |

### Code Pattern

```javascript
function literatureExcerpt(projectName) {
  const cols = [
    { header: "序号", width: 600 },
    { header: "文献题目", width: 1800 },
    { header: "作者", width: 1000 },
    { header: "来源/出处", width: 1400 },
    { header: "发表时间", width: 900 },
    { header: "摘录要点", width: 2000 },
    { header: "对本项目的启发", width: 1326 },
  ];

  // Scale to fit
  const totalW = cols.reduce((s, c) => s + c.width, 0);
  const scale = CONTENT_W / totalW;
  cols.forEach(c => c.width = Math.round(c.width * scale));

  const colWidths = cols.map(c => c.width);
  const headerRow = new TableRow({
    children: cols.map(c => thCell(c.header, c.width)),
  });

  return [
    title("文献摘录表"),
    infoHeader(projectName),
    spacer(100),
    note("阅读相关文献资料时，将重要信息记录在此表中，便于后续引用"),
    spacer(100),
    new Table({
      width: { size: CONTENT_W, type: WidthType.DXA },
      columnWidths: colWidths,
      rows: [headerRow, ...blankRows(colWidths, 15)],
    }),
  ];
}
```

---

## Survey Questionnaire

**问卷调查表** — Generates a structured questionnaire template.

### Layout

The questionnaire has two parts:
1. **基本信息** — respondent demographics (age, gender, etc.)
2. **调查问题** — the actual questions, with checkboxes or rating scales

Questions should be customized based on the project topic.

### Code Pattern

```javascript
function surveyQuestionnaire(projectName, researchTopic) {
  // Generate a questionnaire shell with customizable questions
  const children = [
    title("问卷调查表"),
    spacer(100),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({
        text: `关于"${researchTopic}"的调查问卷`,
        font: FONT_SONG, size: SZ_TD,
      })],
    }),
    spacer(100),
    note("本问卷仅用于学术研究，所有信息将严格保密，感谢您的配合！"),
    spacer(200),

    // Section 1: Basic info
    new Paragraph({
      children: [new TextRun({ text: "一、基本信息", font: FONT_HEI, size: SZ_H2, bold: true })],
    }),
    spacer(100),
    new Paragraph({
      children: [new TextRun({ text: "1. 您的年龄：________", font: FONT_SONG, size: SZ_TD })],
    }),
    spacer(100),
    new Paragraph({
      children: [new TextRun({ text: "2. 您的性别：□ 男  □ 女", font: FONT_SONG, size: SZ_TD })],
    }),
    spacer(100),
    new Paragraph({
      children: [new TextRun({ text: "3. 您的职业/年级：________", font: FONT_SONG, size: SZ_TD })],
    }),
    spacer(200),

    // Section 2: Survey questions (placeholder structure)
    new Paragraph({
      children: [new TextRun({ text: "二、调查问题", font: FONT_HEI, size: SZ_H2, bold: true })],
    }),
    spacer(100),
    note("以下问题请根据项目实际研究内容进行定制"),
    spacer(100),
  ];

  // Generate 10 blank question slots
  for (let i = 1; i <= 10; i++) {
    children.push(new Paragraph({
      spacing: { before: 200 },
      children: [new TextRun({
        text: `${i}. ________________________________________________`,
        font: FONT_SONG, size: SZ_TD,
      })],
    }));
    children.push(new Paragraph({
      spacing: { before: 100 },
      children: [new TextRun({
        text: "   □ A.________  □ B.________  □ C.________  □ D.________",
        font: FONT_SONG, size: SZ_TD,
      })],
    }));
  }

  // Thank you note
  children.push(spacer(300));
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({
      text: "感谢您的参与！",
      font: FONT_HEI, size: SZ_TD, bold: true,
    })],
  }));
  children.push(spacer(100));
  children.push(new Paragraph({
    alignment: AlignmentType.RIGHT,
    children: [new TextRun({
      text: "调查日期：____年____月____日",
      font: FONT_SONG, size: SZ_TD,
    })],
  }));

  return children;
}
```

---

## Document Assembly

Combine all templates into separate documents. Each template type gets its own file.

```javascript
async function generateAll(projectName, outputDir) {
  const pageProps = {
    page: {
      size: { width: PAGE_W, height: PAGE_H },
      margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN },
    },
  };

  const templates = [
    { name: "实验记录表", fn: () => experimentRecord(projectName) },
    { name: "数据采集表", fn: () => dataCollectionSheet(projectName) },
    { name: "观察日志", fn: () => observationLog(projectName) },
    { name: "访谈记录表", fn: () => interviewRecord(projectName) },
    { name: "文献摘录表", fn: () => literatureExcerpt(projectName) },
    { name: "问卷调查表", fn: () => surveyQuestionnaire(projectName, projectName) },
  ];

  for (const t of templates) {
    const doc = new Document({
      styles: {
        default: {
          document: { run: { font: FONT_SONG, size: SZ_TD } },
        },
      },
      sections: [{ properties: pageProps, children: t.fn() }],
    });
    await saveDoc(doc, `${outputDir}/${t.name}_${projectName}.docx`);
  }
}

// Run
generateAll("项目名称", "./output").catch(console.error);
```

---

## Customization Tips

When the project topic is known, customize these elements:

1. **数据采集表 columns**: Replace generic "数据1/2/3" with actual measurement names
   (e.g., "距离(cm)", "时间(s)", "温度(°C)")

2. **观察日志 fields**: Add project-specific observation categories

3. **问卷调查表 questions**: Write actual survey questions related to the research topic

4. **实验记录表 pages**: Adjust the number of pages based on how many experiments
   the project involves

5. **文献摘录表 rows**: Adjust based on expected number of sources (usually 10-20)
