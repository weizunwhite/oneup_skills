# Handwrite Content Specs & Code Patterns (Mode B)

This file contains the complete Node.js `docx` code patterns for generating handwrite
content reference documents. When generating Mode B output, use these patterns.

## Table of Contents

1. [Common Setup & Helpers](#common-setup--helpers)
2. [Chapter Type 1: 问题发现与思考](#chapter-1-问题发现与思考)
3. [Chapter Type 2: 方案对比笔记](#chapter-2-方案对比笔记)
4. [Chapter Type 3: 系统设计草图说明](#chapter-3-系统设计草图说明)
5. [Chapter Type 4: 技术学习笔记](#chapter-4-技术学习笔记)
6. [Chapter Type 5: 调研问卷原件](#chapter-5-调研问卷原件)
7. [Chapter Type 6: 实验/测试记录](#chapter-6-实验测试记录)
8. [Chapter Type 7: 观察日志](#chapter-7-观察日志)
9. [Chapter Type 8: 文献阅读笔记](#chapter-8-文献阅读笔记)
10. [Chapter Type 9: 访谈记录](#chapter-9-访谈记录)
11. [Chapter Type 10: 研究心得/制作感想](#chapter-10-研究心得制作感想)
12. [Document Assembly](#document-assembly)

---

## Common Setup & Helpers

All Mode B generation scripts use these constants and helpers. This is a unified
pattern derived from both hardware-project and research-project implementations.

```javascript
import fs from "fs";
import {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle,
  WidthType, ShadingType, PageBreak, PageNumber, LevelFormat,
} from "docx";

// ── Style constants ──
const FONT_SONG = "宋体";
const FONT_HEI = "黑体";
const SZ_BODY = 24;       // 小四 12pt
const SZ_H1 = 32;         // 小二 18pt
const SZ_H2 = 28;         // 三号 16pt
const SZ_TITLE = 36;      // subtitle on cover
const SZ_COVER = 44;      // cover title
const SZ_TABLE = 22;
const SZ_NOTE = 22;       // note/instruction text (italics)
const SZ_HEADER = 18;     // page header/footer

// ── Color constants ──
const BLUE = "2E5090";
const LIGHT_BLUE = "D6E4F0";
const LIGHT_GRAY = "F2F2F2";
const BORDER_COLOR = "BBBBBB";
const NOTE_BG = "FFF8E1";     // yellow note box
const NOTE_BORDER = "FFB300";  // amber
const TIP_BG = "E8F5E9";      // green tip box
const TIP_BORDER = "43A047";   // green

const LINE_SPACING = 360; // 1.5x

// ── Borders ──
const border = { style: BorderStyle.SINGLE, size: 1, color: BORDER_COLOR };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 60, bottom: 60, left: 100, right: 100 };

// ── Numbering configuration ──
// Create one numbering reference per chapter to keep counters independent.
// Generate refs "n1" through "n10" plus "bullets" and "dash".
const numberingConfig = [
  {
    reference: "bullets",
    levels: [{
      level: 0, format: LevelFormat.BULLET, text: "\u2022",
      alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } },
    }],
  },
  {
    reference: "dash",
    levels: [{
      level: 0, format: LevelFormat.BULLET, text: "-",
      alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } },
    }],
  },
  ...Array.from({ length: 10 }, (_, i) => ({
    reference: `n${i + 1}`,
    levels: [{
      level: 0, format: LevelFormat.DECIMAL, text: "%1.",
      alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } },
    }],
  })),
];
```

### Helper Functions

```javascript
// ── h1: Chapter title (H1, blue, 黑体) ──
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text, bold: true, font: FONT_HEI, size: SZ_H1, color: BLUE })],
    spacing: { before: 360, after: 240 },
  });
}

// ── h2: Sub-section title (H2, blue, 黑体) ──
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun({ text, bold: true, font: FONT_HEI, size: SZ_H2, color: BLUE })],
    spacing: { before: 240, after: 160 },
  });
}

// ── para: Body paragraph ──
// text can be a string or an array of TextRun instances.
// opts: { bold, indent, alignment, spacing, font, size, color }
function para(text, opts = {}) {
  const { bold, indent, alignment, spacing: sp, font, size, color } = opts;
  const runs = typeof text === "string"
    ? [new TextRun({ text, font: font || FONT_SONG, size: size || SZ_BODY, bold, color })]
    : Array.isArray(text) ? text : [];
  return new Paragraph({
    children: runs,
    alignment: alignment || AlignmentType.LEFT,
    spacing: { after: sp !== undefined ? sp : 120, line: LINE_SPACING },
    indent: indent ? { firstLine: 480 } : undefined,
  });
}

// ── bullet: Dash-prefixed list item ──
function bullet(text, ref) {
  const r = typeof text === "string"
    ? [new TextRun({ text, font: FONT_SONG, size: SZ_BODY })] : text;
  return new Paragraph({
    numbering: { reference: ref || "dash", level: 0 },
    children: r,
    spacing: { after: 60, line: LINE_SPACING },
  });
}

// ── numbered: Numbered list item ──
// Use a unique ref per chapter (e.g., "n1" for chapter 1) to keep counters separate.
function numbered(text, ref) {
  const r = typeof text === "string"
    ? [new TextRun({ text, font: FONT_SONG, size: SZ_BODY })] : text;
  return new Paragraph({
    numbering: { reference: ref || "n1", level: 0 },
    children: r,
    spacing: { after: 80, line: LINE_SPACING },
  });
}

// ── noteBox: Colored callout box (single-cell table with shading) ──
// bgColor/borderColor are hex strings without "#".
// Use NOTE_BG + NOTE_BORDER for info/instructions.
// Use TIP_BG + TIP_BORDER for tips/conclusions.
function noteBox(title, lines, bgColor, borderColor) {
  const bdr = { style: BorderStyle.SINGLE, size: 6, color: borderColor };
  const bdrs = { top: bdr, bottom: bdr, left: bdr, right: bdr };
  const children = [
    new Paragraph({
      children: [new TextRun({ text: title, bold: true, font: FONT_HEI, size: SZ_BODY, color: borderColor })],
      spacing: { after: 80 },
    }),
  ];
  lines.forEach(l => {
    children.push(new Paragraph({
      children: [new TextRun({ text: l, font: FONT_SONG, size: SZ_NOTE })],
      spacing: { after: 60, line: 312 },
    }));
  });
  return new Table({
    width: { size: 9026, type: WidthType.DXA },
    columnWidths: [9026],
    rows: [new TableRow({
      children: [new TableCell({
        borders: bdrs,
        width: { size: 9026, type: WidthType.DXA },
        shading: { fill: bgColor, type: ShadingType.CLEAR },
        margins: { top: 120, bottom: 120, left: 200, right: 200 },
        children,
      })],
    })],
  });
}

// ── makeTable: Data table with header row ──
function makeTable(headers, rows, colWidths) {
  const tw = colWidths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: tw, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [
      new TableRow({
        children: headers.map((h, i) => cell(h, {
          bold: true, shading: LIGHT_BLUE, width: colWidths[i],
          font: FONT_HEI, size: SZ_TABLE,
        })),
      }),
      ...rows.map(row => new TableRow({
        children: row.map((c, i) => cell(c, { width: colWidths[i] })),
      })),
    ],
  });
}

// ── cell: Generic table cell ──
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
      spacing: { after: 0, line: 276 },
    })],
  };
  if (shading) co.shading = { fill: shading, type: ShadingType.CLEAR };
  if (width) co.width = { size: width, type: WidthType.DXA };
  if (colspan) co.columnSpan = colspan;
  return new TableCell(co);
}

// ── labelLine: "Label：Value" line (for interview/observation records) ──
function labelLine(label, value) {
  return new Paragraph({
    spacing: { line: LINE_SPACING },
    children: [
      new TextRun({ text: label, bold: true, font: FONT_SONG, size: SZ_BODY }),
      new TextRun({ text: value, font: FONT_SONG, size: SZ_BODY }),
    ],
  });
}

// ── qaPair: Q&A pair (for interviews) ──
function qaPair(q, a) {
  return [
    new Paragraph({
      spacing: { line: LINE_SPACING },
      children: [
        new TextRun({ text: "问：", bold: true, font: FONT_SONG, size: SZ_BODY }),
        new TextRun({ text: q, font: FONT_SONG, size: SZ_BODY }),
      ],
    }),
    new Paragraph({
      spacing: { line: LINE_SPACING },
      children: [
        new TextRun({ text: "答：", bold: true, font: FONT_SONG, size: SZ_BODY }),
        new TextRun({ text: a, font: FONT_SONG, size: SZ_BODY }),
      ],
    }),
    para(""),
  ];
}

// ── divider: Horizontal line ──
function divider() {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: "CCCCCC", space: 4 } },
    children: [],
  });
}

// ── copyToLine: "抄写到：" instruction at the top of each chapter ──
function copyToLine(destination) {
  return para([
    new TextRun({ text: "抄写到：", bold: true, font: FONT_HEI, size: SZ_BODY }),
    new TextRun({ text: destination, font: FONT_SONG, size: SZ_BODY }),
  ]);
}
```

---

## Chapter 1: 问题发现与思考

**Use for**: All project types. First-person account of how the student discovered
the problem and started thinking about solutions.

**Content structure**:
- A short story or anecdote about noticing the problem
- Why this problem matters
- Initial ideas for solving it
- What the student decided to research/build

**Code pattern**:

```javascript
// Example for a hardware project (smart desk lamp for posture)
function chapter_problemDiscovery(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("一、问题发现与思考"));
  C.push(copyToLine("空白纸上，标题写"我的发现"，右上角写日期 YYYY年M月"));
  C.push(para(""));

  // Personal anecdote
  C.push(para("【具体的个人经历或观察，描述发现问题的过程】", { indent: true }));
  C.push(para(""));

  // Why it matters
  C.push(h2("这个问题有多严重？"));
  C.push(bullet("【统计数据或普遍现象描述】"));
  C.push(bullet("【身边的具体例子】"));
  C.push(bullet("【问题造成的影响】"));
  C.push(para(""));

  // Initial thinking
  C.push(h2("我的想法"));
  C.push(para("【学生对解决方案的初步设想，包括为什么选择这个方向】", { indent: true }));
}
```

**Writing guidelines**:
- Start with a concrete personal experience (e.g., "有一天我写作业的时候...")
- Include specific details that tie to the project
- End with a clear connection to what the student decided to build/research

---

## Chapter 2: 方案对比笔记

**Use for**: Hardware and software projects. Compares 2-3 alternative approaches
and explains why the chosen approach is best.

**Content structure**:
- 2-3 alternative solutions, each with: sensor/method, capabilities, pros, cons
- A conclusion box explaining the final choice

**Code pattern**:

```javascript
function chapter_schemeComparison(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("二、三种方案对比笔记"));
  C.push(copyToLine("空白纸上，标题写"XX方案对比"，右上角写日期 YYYY年M月D日"));
  C.push(para(""));

  C.push(para("【引出对比的背景句】", { indent: true }));
  C.push(para(""));

  // Scheme A
  C.push(h2("方案一：【方案名称】"));
  C.push(bullet("传感器/方法：【具体型号或技术】"));
  C.push(bullet("能做什么：【功能描述】"));
  C.push(bullet("优点：【具体优势】"));
  C.push(bullet("缺点：【具体劣势】"));
  C.push(para(""));

  // Scheme B
  C.push(h2("方案二：【方案名称】"));
  // ... same bullet pattern ...
  C.push(para(""));

  // Scheme C (chosen)
  C.push(h2("方案三：【方案名称】  ★ 我选这个！"));
  // ... same bullet pattern ...
  C.push(para(""));

  // Conclusion
  C.push(noteBox(
    "结论",
    [
      "【为什么选方案三的理由，1-2句话】",
      "【额外优势补充】",
    ],
    TIP_BG, TIP_BORDER
  ));
}
```

**Writing guidelines**:
- Use actual sensor models/technology names from the project's technical proposal
- Pros/cons should be specific, not generic
- The "chosen" scheme should clearly align with what was actually built

---

## Chapter 3: 系统设计草图说明

**Use for**: Hardware projects (always), software/IoT projects (if relevant).
Describes the system architecture in a way students can hand-draw.

**Content structure**:
- Drawing instructions (note box)
- Input section: sensors/inputs → main controller
- Output section: main controller → actuators/displays
- Network section (if applicable): controller → cloud → app

**Code pattern**:

```javascript
function chapter_systemDesign(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("三、系统架构图手绘稿"));
  C.push(copyToLine("空白纸上，标题写"XX系统设计图"，右上角写日期 YYYY年M月D日"));
  C.push(para(""));

  C.push(noteBox(
    "画图说明",
    [
      "在纸中间画一个大方框，写上"【主控名称】"",
      "然后在周围画小方框，用箭头连线到中间",
      "建议先用铅笔画，画好后再用黑笔描",
    ],
    NOTE_BG, NOTE_BORDER
  ));

  C.push(para(""));
  C.push(h2("左边（输入部分）"));
  // Use text art to show connections:
  C.push(para("[传感器1]  ——→  主控        用途：XXX"));
  C.push(para("[传感器2]  ——→  主控        用途：XXX"));
  C.push(para(""));

  C.push(h2("右边（输出部分）"));
  C.push(para("主控  ——→  [输出设备1]     用途：XXX"));
  C.push(para("主控  ——→  [输出设备2]     用途：XXX"));
  C.push(para(""));

  // Optional: networking
  C.push(h2("下面（联网部分）"));
  C.push(para("主控  ——→  [WiFi]  ——→  [云平台]  ——→  [手机端]"));
}
```

**Writing guidelines**:
- Use the exact component names from the technical proposal
- Describe connections in plain text with arrows (→)
- Keep it simple enough for a student to hand-draw

---

## Chapter 4: 技术学习笔记

**Use for**: Hardware and software projects. Documents specific technical details
the student learned — pin assignments, algorithms, protocols, etc.

**Content structure varies by project type**:

### Sub-type A: Pin Assignment Table (hardware)

```javascript
function chapter_pinTable(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("四、引脚分配表"));
  C.push(copyToLine("空白纸上，标题写"引脚连接表"，可以接在系统设计图的下面"));
  C.push(para(""));

  C.push(para("【主控芯片】引脚分配：", { bold: true }));
  C.push(para(""));

  // Generate from actual source code pin definitions
  C.push(makeTable(
    ["模块", "引脚", "说明"],
    [
      ["【模块1】", "GPIO XX", "【功能说明】"],
      ["【模块2】", "GPIO XX", "【功能说明】"],
      // ... more rows from actual pin assignments
    ],
    [2600, 2200, 4226]
  ));
}
```

### Sub-type B: Algorithm Description (software/hardware)

```javascript
function chapter_algorithm(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("五、【算法名称】思路"));
  C.push(copyToLine("空白纸上，标题写"XX的思路"，右上角写日期 YYYY年M月"));
  C.push(para(""));

  C.push(para([
    new TextRun({ text: "【算法名称】原理：", bold: true, font: FONT_HEI, size: SZ_BODY }),
  ]));
  C.push(para(""));

  // Step-by-step explanation in student language
  C.push(para([
    new TextRun({ text: "1. 【步骤名】", bold: true, font: FONT_SONG, size: SZ_BODY }),
  ], { spacing: 60 }));
  C.push(para("【用学生能理解的语言解释这一步做什么】", { spacing: 160 }));

  C.push(para([
    new TextRun({ text: "2. 【步骤名】", bold: true, font: FONT_SONG, size: SZ_BODY }),
  ], { spacing: 60 }));
  // ... bullets with specific thresholds/parameters from code ...

  // Decision rules table (if applicable)
  C.push(makeTable(
    ["情况", "判断条件", "含义"],
    [
      ["【情况1】", "【具体条件，含数值】", "【通俗解释】"],
      // ... more rows
    ],
    [2200, 3426, 3400]
  ));
}
```

**Writing guidelines**:
- Extract EXACT pin numbers, threshold values, algorithm parameters from source code
- Explain in student-appropriate language, not engineer-speak
- Use tables for structured data (pin tables, decision rules)

---

## Chapter 5: 调研问卷原件

**Use for**: Research projects (always), hardware/software (if a user survey was part of the project).

**Content structure**:
- Questionnaire title (centered)
- Brief greeting to respondents
- 4-8 multiple-choice or short-answer questions relevant to the research topic
- Date line at bottom

**Code pattern**:

```javascript
function chapter_questionnaire(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("一、问卷调查原件"));
  C.push(copyToLine("空白纸上，手写整份问卷题目"));
  C.push(para(""));

  // Centered questionnaire title
  C.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 300 },
    children: [new TextRun({ text: "关于XX的小调查", font: FONT_HEI, size: SZ_H2, bold: true })],
  }));

  C.push(para("亲爱的同学：", { spacing: 80 }));
  C.push(para("【简短说明问卷目的】", { indent: true }));
  C.push(para(""));

  // Questions with checkbox options
  C.push(para([
    new TextRun({ text: "1. 【问题内容】", bold: true, font: FONT_SONG, size: SZ_BODY }),
  ]));
  C.push(para("    □ 选项A    □ 选项B    □ 选项C    □ 选项D", { spacing: 160 }));

  // ... more questions ...

  C.push(para(""));
  C.push(para("填写日期：____年____月____日"));
}
```

**Writing guidelines**:
- Questions should directly relate to the project's research problem
- Use □ (U+25A1) for checkboxes
- 4-6 questions for elementary, 6-8 for middle school
- Language should be age-appropriate for both the surveyor and respondents

---

## Chapter 6: 实验/测试记录

**Use for**: Hardware projects (always — testing the device), research projects
(experiments/field tests), software projects (if applicable).

**Content structure**:

### For hardware/testing projects:
- Test explanation note box
- Data table with actual test results (from technical proposal or source code)
- Statistical summary
- Brief analysis paragraph

### For research/observation experiments:
- Experiment setup description (steps with labelLine format)
- Results description
- "我的发现" conclusion

**Code pattern (testing with data table)**:

```javascript
function chapter_testData(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("六、测试数据记录表"));
  C.push(copyToLine("原始资料模板中的"数据采集表（XX测试）"，日期写 YYYY年M月"));
  C.push(para(""));

  C.push(noteBox(
    "测试说明",
    [
      "【测试方法简述】",
      "【测试次数和条件】",
      "把下面的数据抄到数据采集表的空格里。",
    ],
    NOTE_BG, NOTE_BORDER
  ));

  C.push(para(""));

  // Data table — populate with realistic test data
  C.push(makeTable(
    ["序号", "测试条件", "参数1", "参数2", "结果", "正确"],
    [
      ["1", "【条件】", "【值】", "【值】", "【结果】", "✓"],
      // ... 15-20 rows of realistic test data
    ],
    [700, 1600, 1200, 1400, 1600, 700]
  ));

  C.push(para(""));
  C.push(h2("统计（抄到表格底部）"));
  C.push(para("总测试次数：XX次"));
  C.push(para("正确检测次数：XX次"));
  C.push(para("准确率：XX%"));
  C.push(para(""));

  C.push(h2("数据分析与结论（抄到表格下方空白处）"));
  C.push(para("【2-3句总结测试结果，指出哪些情况表现好，哪些有待改进】", { indent: true }));
}
```

**Code pattern (research experiment with labeled sections)**:

```javascript
function chapter_experimentRecord(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("X、实验记录：【实验名称】"));
  C.push(copyToLine("空白纸上，标题写"【实验名称】""));
  C.push(para(""));

  C.push(labelLine("实验日期：", "YYYY年M月XX日"));
  C.push(labelLine("实验目的：", "【用一句话说明实验要验证什么】"));
  C.push(para(""));

  C.push(para("实验步骤：", { bold: true }));
  C.push(numbered("【步骤1】", "nX"));
  C.push(numbered("【步骤2】", "nX"));
  C.push(numbered("【步骤3】", "nX"));
  C.push(para(""));

  C.push(para("实验结果：", { bold: true }));
  C.push(para("【详细描述观察到的现象，包含具体数据】"));
  C.push(para(""));

  C.push(para("我的发现：", { bold: true }));
  C.push(para("【一句话总结学到了什么】"));
}
```

**Writing guidelines**:
- Test data should be realistic — use actual values from the technical proposal or
  generate plausible data that matches the project's specifications
- Include some "incorrect" results (✗) to make data look authentic (85-95% accuracy)
- Statistics should match the data in the table
- For research experiments, the labeled section format (日期、目的、步骤、结果、发现) is preferred

---

## Chapter 7: 观察日志

**Use for**: Research projects (always), hardware projects (if observation was part of the process).

**Content structure**:
- Date and time observations in chronological order
- Descriptive paragraphs with specific times and activities
- Summary/conclusion

**Code pattern**:

```javascript
function chapter_observationLog(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("X、观察日志：【观察主题】"));
  C.push(copyToLine("空白纸上，标题写"【观察主题】""));
  C.push(para(""));

  C.push(labelLine("观察日期：", "YYYY年M月XX日（星期X）"));
  C.push(labelLine("观察对象：", "【观察对象描述】"));
  C.push(para(""));

  // Time-stamped observations
  C.push(para("早上 7:00 — 【观察内容，具体活动和持续时间】"));
  C.push(para("上午 10:00 — 【观察内容】"));
  C.push(para("中午 11:30 — 【观察内容】"));
  // ... more time entries ...
  C.push(para(""));

  C.push(para("总结：", { bold: true }));
  C.push(para("【对观察结果的归纳，引出对项目设计的启发】"));
}
```

**Writing guidelines**:
- Observations should be specific and time-stamped
- Include quantitative details where possible
- Connect observations to the project's design decisions

---

## Chapter 8: 文献阅读笔记

**Use for**: All project types. Documents what the student learned from reading
related materials.

**Content structure**:
- Source information (title, author/source)
- Key excerpted content
- Connection to the project ("对我项目的启发")

**Code pattern**:

```javascript
function chapter_literatureNotes(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("X、文献阅读笔记"));
  C.push(copyToLine("空白纸上，标题写"阅读笔记""));
  C.push(para(""));

  // Literature entry 1
  C.push(h2("文献摘录1"));
  C.push(labelLine("资料来源：", "《【文献名称】》"));
  C.push(para(""));
  C.push(para("摘录内容：", { bold: true }));
  C.push(para("【从技术方案或论文中提取的相关文献内容摘要】"));
  C.push(para(""));
  C.push(para("对我项目的启发：", { bold: true }));
  C.push(para("【1-2句话说明这个文献对项目有什么帮助】"));

  C.push(divider());

  // Literature entry 2
  C.push(h2("文献摘录2"));
  // ... same pattern ...
}
```

**Writing guidelines**:
- 2-3 literature entries is typical
- Sources should be plausible (government reports, technical documentation, textbooks)
- The "启发" section should clearly connect to the project's design choices

---

## Chapter 9: 访谈记录

**Use for**: Research projects (always), hardware/software (if user interviews were conducted).

**Content structure**:
- Interview metadata (date, interviewee, method)
- Q&A pairs using `qaPair()` helper
- "我的感受" reflection

**Code pattern**:

```javascript
function chapter_interview(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("X、访谈记录"));
  C.push(copyToLine("空白纸上，标题写"访谈记录""));
  C.push(para(""));

  C.push(labelLine("访谈日期：", "YYYY年M月XX日"));
  C.push(labelLine("访谈对象：", "【受访者身份，如"外婆""同学""老师"】"));
  C.push(labelLine("访谈方式：", "面对面交谈"));
  C.push(para(""));

  // Q&A pairs
  ...qaPair(
    "【问题1：与项目主题相关的问题】",
    "【回答：口语化，有个人特色】"
  ).forEach(p => C.push(p));

  ...qaPair(
    "【问题2】",
    "【回答】"
  ).forEach(p => C.push(p));

  // ... more Q&A pairs (3-5 total) ...

  C.push(para("我的感受：", { bold: true }));
  C.push(para("【对访谈结果的反思，如何影响了项目方向】"));
}
```

**Writing guidelines**:
- Questions should be natural and conversational
- Answers should sound like real spoken language, not formal writing
- 3-5 Q&A pairs is typical
- The reflection should connect interview insights to project decisions

---

## Chapter 10: 研究心得/制作感想

**Use for**: All project types. Personal reflection on the entire project experience.

**Content structure**:
- What was learned (technical skills)
- What was learned (broader understanding)
- Difficulties encountered and how they were overcome
- Personal feelings and future hopes

**Code pattern**:

```javascript
function chapter_reflection(C) {
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("X、制作感想"));
  C.push(copyToLine("空白纸上，标题写"我的感想""));
  C.push(para(""));

  C.push(para("通过做这个项目，我学到了很多东西。", { indent: false }));
  C.push(para(""));

  // Technical learning
  C.push(para("【描述学到的具体技术技能，提及实际使用的工具/语言/平台】", { indent: false }));
  C.push(para(""));

  // Broader understanding
  C.push(para("【描述对更大主题的理解，如物联网、环保、健康等】", { indent: false }));
  C.push(para(""));

  // Difficulties
  C.push(para("【描述遇到的具体困难（2-3个），以及怎么解决的】", { indent: false }));
  C.push(para(""));

  // Future hopes
  C.push(para("【对项目未来的展望和个人感受】", { indent: false }));
}
```

**Writing guidelines**:
- This is the most personal chapter — voice and tone matter most here
- Reference specific technical details learned (actual tools, methods, components)
- Difficulties should be real and specific (e.g., "传感器信号不稳定")
- Elementary: simpler emotions, shorter paragraphs
- Middle school: more analytical reflection, longer paragraphs

---

## Document Assembly

Combine all selected chapters into a single document with cover page, table of
contents, chapter content, instructions, and mapping table.

```javascript
function buildDocument(projectName, chapters, chapterTitles) {
  // chapters: array of functions, each takes C (array) and pushes paragraphs
  // chapterTitles: array of { num: "一", title: "问卷调查原件", copyTo: "空白纸上" }

  const C = [];

  // ===== COVER PAGE =====
  C.push(new Paragraph({ spacing: { before: 2400 } }));
  C.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 200 },
    children: [new TextRun({ text: projectName, font: FONT_HEI, size: SZ_COVER, bold: true, color: BLUE })],
  }));
  C.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 600 },
    children: [new TextRun({ text: "手抄内容汇总", font: FONT_HEI, size: SZ_COVER, bold: true, color: BLUE })],
  }));
  C.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 200 },
    children: [new TextRun({ text: "打印后对照手抄到空白模板上", font: FONT_SONG, size: SZ_BODY, color: "888888" })],
  }));

  C.push(new Paragraph({ spacing: { before: 800 } }));

  // Usage instructions
  C.push(noteBox(
    "使用说明",
    [
      `本文档包含${chapterTitles.length}份需要手写的材料内容。`,
      "请打印本文档，然后对照着把内容抄到对应的空白模板（原始资料模板）上。",
      "手写时注意：用自己平时的字迹，不用太工整，可以有涂改。",
    ],
    NOTE_BG, NOTE_BORDER
  ));

  // Table of contents
  C.push(new Paragraph({ spacing: { before: 400 } }));
  C.push(para("目录：", { bold: true }));
  chapterTitles.forEach(ch => {
    C.push(numbered(`${ch.title}`, "n1"));
  });

  // ===== CHAPTER CONTENT =====
  chapters.forEach(fn => fn(C));

  // ===== 手抄注意事项 =====
  C.push(new Paragraph({ children: [new PageBreak()] }));
  C.push(h1("手抄注意事项"));

  C.push(noteBox(
    "重要提醒",
    [
      "1. 用自己平时写作业的笔和纸写，不要太工整也不要太潦草",
      "2. 可以有涂改，看起来更真实自然",
      "3. 画图时用铅笔先画，再用黑笔描",
      "4. 数据表格可以用尺子画格子",
      "5. 写完后拍照保存电子版",
    ],
    TIP_BG, TIP_BORDER
  ));

  C.push(para(""));
  C.push(h2("手抄对应关系"));

  C.push(makeTable(
    ["手抄内容", "抄到哪里", "注意事项"],
    chapterTitles.map(ch => [ch.title, ch.copyTo, ch.note || ""]),
    [2000, 3526, 3500]
  ));

  // ===== BUILD DOCUMENT =====
  const doc = new Document({
    styles: {
      default: { document: { run: { font: FONT_SONG, size: SZ_BODY } } },
      paragraphStyles: [
        {
          id: "Heading1", name: "Heading 1",
          basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: SZ_H1, bold: true, font: FONT_HEI, color: BLUE },
          paragraph: { spacing: { before: 360, after: 240 }, outlineLevel: 0 },
        },
        {
          id: "Heading2", name: "Heading 2",
          basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: SZ_H2, bold: true, font: FONT_HEI, color: BLUE },
          paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 1 },
        },
      ],
    },
    numbering: { config: numberingConfig },
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838 },  // A4
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({
              text: `${projectName} — 手抄内容汇总（打印用）`,
              font: FONT_SONG, size: SZ_HEADER, color: "999999",
            })],
            border: {
              bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 4 },
            },
          })],
        }),
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: "— ", font: FONT_SONG, size: SZ_HEADER, color: "999999" }),
              new TextRun({ children: [PageNumber.CURRENT], font: FONT_SONG, size: SZ_HEADER, color: "999999" }),
              new TextRun({ text: " —", font: FONT_SONG, size: SZ_HEADER, color: "999999" }),
            ],
          })],
        }),
      },
      children: C,
    }],
  });

  return doc;
}

// ── Save ──
async function save(doc, outPath) {
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(outPath, buf);
  console.log("DONE:", outPath);
}
```

---

## Full Example: Assembly for a Hardware Project

This shows how to wire everything together for a hardware invention project
(e.g., a smart lamp with posture detection).

```javascript
// Define chapter metadata for TOC and mapping table
const chapterTitles = [
  { title: "问卷调查原件", copyTo: "空白纸上（手写问卷原件）", note: "写完后复印给同学填" },
  { title: "三种方案对比笔记", copyTo: "空白纸上", note: "右上角写日期" },
  { title: "系统架构图手绘稿", copyTo: "空白纸上（手绘框图）", note: "右上角写日期" },
  { title: "引脚分配表", copyTo: "空白纸上或接在架构图后", note: "用尺子画表格" },
  { title: "坐姿检测算法思路", copyTo: "空白纸上", note: "写日期" },
  { title: "测试数据记录表", copyTo: "原始资料模板的数据采集表", note: "写日期" },
];

// Define chapter functions (each pushes content to C array)
const chapters = [
  chapter_questionnaire,     // chapter 5 type
  chapter_schemeComparison,  // chapter 2 type
  chapter_systemDesign,      // chapter 3 type
  chapter_pinTable,          // chapter 4 sub-type A
  chapter_algorithm,         // chapter 4 sub-type B
  chapter_testData,          // chapter 6 type
];

const doc = buildDocument("智能坐姿台灯", chapters, chapterTitles);
save(doc, "输出/智能坐姿台灯_手抄内容汇总.docx");
```

## Full Example: Assembly for a Research Project

For a research/observation project (e.g., elderly care water monitoring).

```javascript
const chapterTitles = [
  { title: "实验记录（共3份）", copyTo: "空白纸上", note: "日期按老师指定" },
  { title: "观察日志（共2份）", copyTo: "空白纸上", note: "日期按老师指定" },
  { title: "文献摘录（共2份）", copyTo: "空白纸上", note: "" },
  { title: "访谈记录", copyTo: "空白纸上", note: "" },
  { title: "制作心得", copyTo: "空白纸上", note: "" },
];

const chapters = [
  chapter_experiments,       // chapter 6 type (multiple experiments)
  chapter_observations,      // chapter 7 type
  chapter_literatureNotes,   // chapter 8 type
  chapter_interview,         // chapter 9 type
  chapter_reflection,        // chapter 10 type
];

const doc = buildDocument("以水知安——独居老人用水监测系统", chapters, chapterTitles);
save(doc, "输出/以水知安_手抄内容汇总.docx");
```

---

## Content Generation Guidelines

When generating actual content (not template placeholders), follow these rules:

### Voice & Tone by Grade Level

| Grade | Vocabulary | Sentence Length | Technical Detail | Example |
|-------|-----------|-----------------|-----------------|---------|
| 小学低(1-3) | Very simple, daily words | Short (5-15 chars) | Minimal, describe what they see | "灯变红了，说明坐姿不对" |
| 小学高(4-6) | Simple but includes tech terms | Medium (10-25 chars) | Moderate, name components and values | "ESP32检测到faceWidth超过140像素" |
| 初中(7-9) | Uses technical terminology | Longer, compound sentences | Detailed, includes formulas and analysis | "通过滑动平均算法对最近5帧数据取均值，有效降低了误报率" |

### Data Authenticity

- Test data should include ~10-15% "wrong" results to look realistic
- Avoid perfect round numbers — use values like 98, 7658, 99.3
- Include realistic measurement units and precision
- Statistics should be mathematically consistent with the data table

### Date Timeline

- Assign dates that span the project's research period (typically 3-6 months)
- Earlier chapters (problem discovery, literature review) get earlier dates
- Testing and reflection get later dates
- Use "XX日" for specific days that the teacher will assign
