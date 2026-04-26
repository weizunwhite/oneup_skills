# Layout Recipes (版式配方)

## Overview

5 套版式配方，每个项目基于项目名 hash 选择一套。不同配方改变**页面结构和排版方式**，使不同项目的研究日志在视觉上有明显差异。

## Recipe Selection Algorithm

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

---

## Recipe A: 工程笔记本

**整体风格**: 最正式，像实验室笔记本。

| 维度 | 规范 |
|------|------|
| 表头样式 | 深色横幅（全宽，白字），背景色 `1F4E79` |
| 内容区版式 | 二列表格（左标签 1.6cm + 右内容），有完整边框 |
| 页面密度 | 一页一条（宽松） |
| 条目间分隔 | 分页符（PageBreak） |
| 字段排列 | 垂直（逐行展开，每个字段占一行） |
| 照片位置 | 条目末尾，"照片记录"小标题后 |

### 表头渲染
```javascript
// 全宽深色横幅
new Table({
  rows: [new TableRow({
    children: [
      new TableCell({
        shading: { fill: "1F4E79" },
        children: [new Paragraph({
          children: [
            new TextRun({ text: `${idx}. ${entry.title}`, bold: true, color: "FFFFFF", font: "黑体", size: 24 }),
          ]
        })]
      }),
      new TableCell({
        shading: { fill: "1F4E79" },
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [
            new TextRun({ text: entry.date, color: "FFFFFF", font: "仿宋", size: 21 }),
          ]
        })]
      })
    ]
  })],
  width: { size: 100, type: WidthType.PERCENTAGE }
})
```

### 内容区渲染
```javascript
// 每个字段一行，左标签右内容，有边框
function buildFieldRow(label, content) {
  return new TableRow({
    children: [
      new TableCell({
        width: { size: 1600, type: WidthType.DXA },
        shading: { fill: "D6E4F0" },
        children: [new Paragraph({
          children: [new TextRun({ text: label, bold: true, font: "黑体", size: 21 })]
        })]
      }),
      new TableCell({
        children: [new Paragraph({
          children: [new TextRun({ text: content, font: "宋体", size: 21 })]
        })]
      })
    ]
  });
}

// 字段表格
new Table({
  rows: fieldRows, // objective, tools, procedure, observations, etc.
  width: { size: 100, type: WidthType.PERCENTAGE },
  borders: { /* 完整边框 */ }
})
```

### 分隔方式
```javascript
// 每个条目后加分页符
new Paragraph({ children: [new PageBreak()] })
```

---

## Recipe B: 手写日记风

**整体风格**: 像学生手写的日记本，无表格，纯段落流式排版。

| 维度 | 规范 |
|------|------|
| 表头样式 | 粗体标题 + 日期右对齐，下方一条细线（0.5pt，颜色 `999999`） |
| 内容区版式 | 纯段落流式排版，无表格，字段名用加粗引导 |
| 页面密度 | 紧凑，一页可放 1-2 条短条目 |
| 条目间分隔 | 三个居中圆点 `· · ·`（间距前后各 200pt） |
| 字段排列 | 垂直，但融入段落（不用表格） |
| 照片位置 | 文字间穿插（紧跟相关内容段落后） |

### 表头渲染
```javascript
// 标题行：粗体标题 + 日期右对齐
new Paragraph({
  children: [
    new TextRun({ text: `${idx}. ${entry.title}`, bold: true, font: "黑体", size: 24 }),
  ],
  spacing: { after: 40 }
}),
// 日期行
new Paragraph({
  alignment: AlignmentType.RIGHT,
  children: [
    new TextRun({ text: entry.date, font: "仿宋", size: 20, color: "666666" }),
  ],
  spacing: { after: 40 }
}),
// 细线分隔
new Paragraph({
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "999999" } },
  spacing: { after: 120 }
})
```

### 内容区渲染
```javascript
// 纯段落，字段名加粗引导
function buildFieldParagraph(label, content) {
  return new Paragraph({
    children: [
      new TextRun({ text: `${label}：`, bold: true, font: "黑体", size: 21 }),
      new TextRun({ text: content, font: "宋体", size: 21 }),
    ],
    spacing: { after: 100 }
  });
}

// 多行内容（如 procedure）分段渲染
function buildMultilineParagraphs(label, content) {
  const lines = content.split('\n').filter(l => l.trim());
  return [
    new Paragraph({
      children: [new TextRun({ text: `${label}：`, bold: true, font: "黑体", size: 21 })],
      spacing: { after: 60 }
    }),
    ...lines.map(line => new Paragraph({
      children: [new TextRun({ text: line.trim(), font: "宋体", size: 21 })],
      spacing: { after: 60 },
      indent: { left: 240 }
    }))
  ];
}
```

### 分隔方式
```javascript
// 三个居中圆点
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "· · ·", color: "999999", size: 21 }),
  ],
  spacing: { before: 200, after: 200 }
})
```

---

## Recipe C: 项目管理风

**整体风格**: 像项目进度报告，左侧竖条色块标识。

| 维度 | 规范 |
|------|------|
| 表头样式 | 左侧 4px 竖条色块（`1F4E79`）+ 标题，日期在竖条上方小字 |
| 内容区版式 | 无边框缩进排版，字段名用方括号 `【目标】` `【过程】` |
| 页面密度 | 一页一条 |
| 条目间分隔 | 分页符（PageBreak） |
| 字段排列 | 垂直（逐行展开） |
| 照片位置 | 条目末尾 |

### 表头渲染
```javascript
// 日期小字在上
new Paragraph({
  children: [
    new TextRun({ text: entry.date, font: "仿宋", size: 18, color: "666666" }),
  ],
  spacing: { after: 40 }
}),
// 左侧竖条 + 标题（用单列表格模拟竖条）
new Table({
  rows: [new TableRow({
    children: [
      // 竖条色块（窄列）
      new TableCell({
        width: { size: 120, type: WidthType.DXA },
        shading: { fill: "1F4E79" },
        borders: { top: {style: BorderStyle.NONE}, bottom: {style: BorderStyle.NONE}, right: {style: BorderStyle.NONE} },
        children: [new Paragraph({ text: "" })]
      }),
      // 标题
      new TableCell({
        borders: { top: {style: BorderStyle.NONE}, bottom: {style: BorderStyle.NONE}, left: {style: BorderStyle.NONE} },
        children: [new Paragraph({
          children: [
            new TextRun({ text: `  ${idx}. ${entry.title}`, bold: true, font: "黑体", size: 24 }),
          ],
          indent: { left: 120 }
        })]
      })
    ]
  })],
  width: { size: 100, type: WidthType.PERCENTAGE },
  borders: { /* 全部 NONE */ }
})
```

### 内容区渲染
```javascript
// 方括号字段名 + 缩进内容
function buildBracketField(label, content) {
  return [
    new Paragraph({
      children: [
        new TextRun({ text: `【${label}】`, bold: true, font: "黑体", size: 21 }),
      ],
      spacing: { before: 100, after: 40 }
    }),
    ...contentToParagraphs(content, { indent: { left: 360 }, font: "宋体", size: 21, spacing: { after: 60 } })
  ];
}
// contentToParagraphs: 将多行文本拆分为段落数组
```

### 分隔方式
```javascript
new Paragraph({ children: [new PageBreak()] })
```

---

## Recipe D: 极简条目风

**整体风格**: 像简洁的工作备忘录，紧凑排列。

| 维度 | 规范 |
|------|------|
| 表头样式 | 编号圆圈 + 标题粗体 + 日期灰色小字（同一行） |
| 内容区版式 | 全宽段落，无表格无边框，要点用短横线 `—` 引导 |
| 页面密度 | 紧凑，一页 2-3 条 |
| 条目间分隔 | 留白间距（spacing after 300pt） |
| 字段排列 | 垂直，但极简（字段名与内容同行） |
| 照片位置 | 条目末尾，紧凑排列 |

### 表头渲染
```javascript
// 编号圆圈 + 标题 + 日期（同一行）
new Paragraph({
  children: [
    // 编号用粗体圆圈样式
    new TextRun({ text: `❶❷❸❹❺❻❼❽❾❿⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴`[idx-1] || `${idx}`, font: "黑体", size: 24 }),
    // 如果超过20条或字体不支持，fallback 到纯数字
    new TextRun({ text: ` ${entry.title}  `, bold: true, font: "黑体", size: 24 }),
    new TextRun({ text: entry.date, font: "仿宋", size: 18, color: "999999" }),
  ],
  spacing: { after: 80 }
})
// 注意：circled numbers 在 Word 中可能不显示，实际实现用加粗数字 + 圆括号 fallback：
// `(${idx})` 或 `${idx}.`
```

**Fallback 表头（推荐）**:
```javascript
new Paragraph({
  children: [
    new TextRun({ text: `(${idx}) `, bold: true, font: "黑体", size: 24 }),
    new TextRun({ text: `${entry.title}  `, bold: true, font: "黑体", size: 24 }),
    new TextRun({ text: entry.date, font: "仿宋", size: 18, color: "999999" }),
  ],
  spacing: { after: 80 }
})
```

### 内容区渲染
```javascript
// 字段名与内容同行，用短横线引导
function buildDashField(label, content) {
  return new Paragraph({
    children: [
      new TextRun({ text: `— ${label}：`, bold: true, font: "黑体", size: 21, color: "444444" }),
      new TextRun({ text: content, font: "宋体", size: 21 }),
    ],
    spacing: { after: 60 },
    indent: { left: 240 }
  });
}

// 多行内容（如 quickNotes）
function buildDashList(items) {
  return items.map(item => new Paragraph({
    children: [
      new TextRun({ text: `— ${item}`, font: "宋体", size: 21 }),
    ],
    spacing: { after: 40 },
    indent: { left: 240 }
  }));
}
```

### 分隔方式
```javascript
// 留白间距（不分页）
new Paragraph({
  spacing: { after: 300 },
  children: []
})
```

---

## Recipe E: 研究报告风

**整体风格**: 像正式的研究记录表，大号标题 + 下划线。

| 维度 | 规范 |
|------|------|
| 表头样式 | 无背景色，标题用大号黑体（28pt）+ 日期，下划线分隔（1pt，`333333`） |
| 内容区版式 | 目的/工具一行水平并排（二列无边框表格），过程和观察垂直展开，有淡灰底色区块 |
| 页面密度 | 一页一条 |
| 条目间分隔 | 分页符（PageBreak） |
| 字段排列 | 混合（目的+工具水平并排，其余垂直） |
| 照片位置 | 条目末尾 |

### 表头渲染
```javascript
// 大号标题
new Paragraph({
  children: [
    new TextRun({ text: `${idx}. ${entry.title}`, bold: true, font: "黑体", size: 28 }),
  ],
  spacing: { after: 40 }
}),
// 日期
new Paragraph({
  children: [
    new TextRun({ text: entry.date, font: "仿宋", size: 21, color: "666666" }),
  ],
  spacing: { after: 40 }
}),
// 下划线
new Paragraph({
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "333333" } },
  spacing: { after: 160 }
})
```

### 内容区渲染
```javascript
// 目的 + 工具 水平并排（无边框二列表格）
new Table({
  rows: [new TableRow({
    children: [
      new TableCell({
        width: { size: 50, type: WidthType.PERCENTAGE },
        borders: { /* 全部 NONE */ },
        children: [
          new Paragraph({ children: [
            new TextRun({ text: "目的", bold: true, font: "黑体", size: 21, color: "333333" })
          ]}),
          new Paragraph({ children: [
            new TextRun({ text: entry.objective, font: "宋体", size: 21 })
          ], spacing: { after: 60 }})
        ]
      }),
      new TableCell({
        width: { size: 50, type: WidthType.PERCENTAGE },
        borders: { /* 全部 NONE */ },
        children: [
          new Paragraph({ children: [
            new TextRun({ text: "工具/材料", bold: true, font: "黑体", size: 21, color: "333333" })
          ]}),
          new Paragraph({ children: [
            new TextRun({ text: entry.tools, font: "宋体", size: 21 })
          ], spacing: { after: 60 }})
        ]
      })
    ]
  })],
  width: { size: 100, type: WidthType.PERCENTAGE },
  borders: { /* 全部 NONE */ }
}),

// 过程/观察 垂直展开，带淡灰底色区块
function buildShadedBlock(label, content) {
  return [
    new Paragraph({
      children: [new TextRun({ text: label, bold: true, font: "黑体", size: 21, color: "333333" })],
      spacing: { before: 120, after: 60 }
    }),
    ...contentToParagraphs(content, {
      shading: { fill: "F5F5F5" },
      font: "宋体", size: 21,
      spacing: { after: 60 },
      indent: { left: 120, right: 120 }
    })
  ];
}
// 用于 procedure, observations, analysis 等
```

### 分隔方式
```javascript
new Paragraph({ children: [new PageBreak()] })
```

---

## Cover Page & TOC by Recipe

封面和目录也按配方微调：

| 配方 | 封面风格 | 目录风格 |
|------|----------|----------|
| A | 居中大标题 + 横线上下框 | 带编号的正式目录 |
| B | 左对齐手写感标题，右下角日期 | 简单条目列表，无前导点 |
| C | 左侧竖条 + 标题，项目管理风格 | 缩进分级目录 |
| D | 居中小号标题，极简 | 紧凑单列目录 |
| E | 大号粗体标题 + 下划线，研究报告风 | 带页码的正式目录 |

---

## Photo Placeholder by Recipe

所有配方的照片占位符内容相同（`[待补充照片: 描述]`），但样式随配方变化：

| 配方 | 占位符样式 |
|------|-----------|
| A | 灰色背景框（`F2F2F2`），居中显示 |
| B | 斜体灰色文字，无背景，左对齐 |
| C | 左侧竖条 + 灰色背景 |
| D | 短横线引导 + 灰色文字 |
| E | 淡灰底色区块（`F5F5F5`），与内容区块同风格 |

---

## Quick Reference Table

| 维度 | A 工程笔记本 | B 手写日记风 | C 项目管理风 | D 极简条目风 | E 研究报告风 |
|------|-------------|-------------|-------------|-------------|-------------|
| 表头 | 深色横幅白字 | 粗体+细线 | 左侧竖条 | 编号+粗体+灰日期 | 大号标题+下划线 |
| 内容 | 二列有框表格 | 纯段落 | 方括号无框缩进 | 短横线引导 | 水平并排+灰底区块 |
| 密度 | 一页一条 | 一页1-2条 | 一页一条 | 一页2-3条 | 一页一条 |
| 分隔 | 分页符 | 居中圆点 | 分页符 | 留白300pt | 分页符 |
| 照片 | 末尾 | 穿插 | 末尾 | 末尾紧凑 | 末尾 |
