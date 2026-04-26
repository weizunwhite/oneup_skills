# Research Log Entry Styles Reference (按版式配方组织)

本文件按 5 套版式配方（A-E）组织，每套配方下定义 5 种条目风格的渲染方式。

配方选择方法和整体版式规范见 [layout_recipes.md](layout_recipes.md)。

---

## Quick Overview: 5 Entry Styles

| Style | Use Case | 数据结构 |
|-------|----------|---------|
| **table** | 标准结构化笔记 | objective, tools, procedure, observations, problems, solutions, analysis, nextStep |
| **narrative** | 日记/反思 | narrative (多段落文本), objective?, tools?, procedure? |
| **compact** | 快速笔记 | quickNotes (数组), objective?, tools? |
| **debug** | 排障记录 | debugPairs [{problem, process, solution}], objective?, tools? |
| **experiment** | 数据/测试 | dataHeaders, dataRows, observations, analysis, objective?, tools? |

## Style Distribution Guidelines

不变，所有配方共用：
- `narrative` (25-30%): 发现时刻、反思、用户测试、总结
- `table` (20-25%): 结构化工作、设计、里程碑
- `compact` (15-20%): 日常任务、快速设置
- `debug` (10-15%): 排障，明确的问题→解决流程
- `experiment` (15-20%): 测试、测量、数据收集

按项目阶段分布：
```
Phase 1 (调研): Narrative 60% + Table 40%
Phase 2 (学习): Table 40% + Compact 40% + Debug 20%
Phase 3 (开发): Debug 50% + Table 30% + Compact 20%
Phase 4 (测试): Experiment 70% + Table 30%
Phase 5 (论文): Narrative 70% + Compact 30%
```

## Photo Placeholder (所有配方通用内容)

占位符文本统一：`[待补充照片: 描述需要拍摄什么内容]`

占位符**样式**随配方变化（见各配方定义）。

---

# 配方 A：工程笔记本

**特征**: 深色横幅表头 + 二列有框表格 + 分页符分隔 + 一页一条

### 通用组件

```javascript
// === 表头（所有条目共用） ===
function buildHeaderA(idx, entry) {
  return new Table({
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: 65, type: WidthType.PERCENTAGE },
          shading: { fill: "1F4E79" },
          children: [new Paragraph({
            children: [new TextRun({ text: `${idx}. ${entry.title}`, bold: true, color: "FFFFFF", font: "黑体", size: 24 })]
          })]
        }),
        new TableCell({
          width: { size: 35, type: WidthType.PERCENTAGE },
          shading: { fill: "1F4E79" },
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ text: entry.date, color: "FFFFFF", font: "仿宋", size: 21 })]
          })]
        })
      ]
    })],
    width: { size: 100, type: WidthType.PERCENTAGE }
  });
}

// === 字段行 ===
function buildFieldRowA(label, content) {
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
        children: buildContentParagraphs(content, { font: "宋体", size: 21 })
      })
    ]
  });
}

// === 照片占位符 ===
function buildPlaceholderA(desc) {
  return new Paragraph({
    children: [new TextRun({ text: `[待补充照片: ${desc}]`, font: "宋体", size: 21 })],
    shading: { fill: "F2F2F2" },
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 80 }
  });
}

// === 分隔 ===
// 分页符
new Paragraph({ children: [new PageBreak()] })
```

### A-Table 条目
```javascript
function buildEntryA_Table(idx, entry) {
  const rows = [];
  if (entry.objective) rows.push(buildFieldRowA("研究目标", entry.objective));
  if (entry.tools) rows.push(buildFieldRowA("工具材料", entry.tools));
  if (entry.procedure) rows.push(buildFieldRowA("实施过程", entry.procedure));
  if (entry.observations) rows.push(buildFieldRowA("观察记录", entry.observations));
  if (entry.problems) rows.push(buildFieldRowA("遇到问题", entry.problems));
  if (entry.solutions) rows.push(buildFieldRowA("解决方法", entry.solutions));
  // photos row
  if (entry.analysis) rows.push(buildFieldRowA("分析总结", entry.analysis));
  if (entry.nextStep) rows.push(buildFieldRowA("下一步", entry.nextStep));
  // nextStep 行背景 F2F2F2

  return [
    buildHeaderA(idx, entry),
    new Table({ rows, width: { size: 100, type: WidthType.PERCENTAGE }, borders: FULL_BORDERS }),
    // photos or placeholders,
    new Paragraph({ children: [new PageBreak()] })
  ];
}
```

### A-Narrative 条目
```javascript
function buildEntryA_Narrative(idx, entry) {
  return [
    buildHeaderA(idx, entry),
    // narrative 段落（每段 spacing after 120pt）
    ...entry.narrative.split('\n').filter(l => l.trim()).map(p =>
      new Paragraph({ children: [new TextRun({ text: p, font: "宋体", size: 21 })], spacing: { after: 120 } })
    ),
    // photos or placeholders,
    new Paragraph({ children: [new PageBreak()] })
  ];
}
```

### A-Compact 条目
```javascript
function buildEntryA_Compact(idx, entry) {
  return [
    buildHeaderA(idx, entry),
    // bullet points
    ...entry.quickNotes.map(note =>
      new Paragraph({
        children: [new TextRun({ text: `• ${note}`, font: "宋体", size: 21 })],
        indent: { left: 400, hanging: 240 },
        spacing: { after: 60 }
      })
    ),
    // photos or placeholders,
    new Paragraph({ children: [new PageBreak()] })
  ];
}
```

### A-Debug 条目
```javascript
function buildEntryA_Debug(idx, entry) {
  const elements = [buildHeaderA(idx, entry)];
  entry.debugPairs.forEach((pair, i) => {
    elements.push(
      new Paragraph({
        children: [new TextRun({ text: `问题 ${i+1}: ${pair.problem}`, bold: true, font: "黑体", size: 21, color: "C00000" })],
        spacing: { before: 100, after: 60 }
      }),
      new Paragraph({
        children: [new TextRun({ text: `排查: ${pair.process}`, italics: true, font: "宋体", size: 21 })],
        indent: { left: 400 }, spacing: { after: 60 }
      }),
      new Paragraph({
        children: [new TextRun({ text: `解决: ${pair.solution}`, bold: true, font: "宋体", size: 21, color: "1F4E79" })],
        indent: { left: 400 }, spacing: { after: 100 }
      })
    );
  });
  // photos or placeholders
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

### A-Experiment 条目
```javascript
function buildEntryA_Experiment(idx, entry) {
  // 数据表格：深蓝表头 + 交替行
  const headerRow = new TableRow({
    children: entry.dataHeaders.map(h => new TableCell({
      shading: { fill: "1F4E79" },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: h, bold: true, font: "黑体", size: 21, color: "FFFFFF" })]
      })]
    }))
  });
  const dataRows = entry.dataRows.map((row, ri) => new TableRow({
    children: row.map(val => new TableCell({
      shading: { fill: ri % 2 === 0 ? "FFFFFF" : "F2F2F2" },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: val, font: "宋体", size: 21 })]
      })]
    }))
  }));

  return [
    buildHeaderA(idx, entry),
    new Table({ rows: [headerRow, ...dataRows], width: { size: 100, type: WidthType.PERCENTAGE } }),
    // "观察与发现" section
    new Paragraph({ children: [new TextRun({ text: "观察与发现", bold: true, font: "黑体", size: 21 })], spacing: { before: 120, after: 60 } }),
    ...buildBulletParagraphs(entry.observations),
    // "分析" section
    new Paragraph({ children: [new TextRun({ text: "分析", bold: true, font: "黑体", size: 21 })], spacing: { before: 120, after: 60 } }),
    new Paragraph({ children: [new TextRun({ text: entry.analysis, font: "宋体", size: 21 })], spacing: { after: 120 } }),
    // photos or placeholders,
    new Paragraph({ children: [new PageBreak()] })
  ];
}
```

---

# 配方 B：手写日记风

**特征**: 粗体标题+细线 + 纯段落流式 + 居中圆点分隔 + 紧凑一页1-2条

### 通用组件

```javascript
// === 表头 ===
function buildHeaderB(idx, entry) {
  return [
    new Paragraph({
      children: [new TextRun({ text: `${idx}. ${entry.title}`, bold: true, font: "黑体", size: 24 })],
      spacing: { after: 40 }
    }),
    new Paragraph({
      alignment: AlignmentType.RIGHT,
      children: [new TextRun({ text: entry.date, font: "仿宋", size: 20, color: "666666" })],
      spacing: { after: 40 }
    }),
    new Paragraph({
      border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "999999" } },
      spacing: { after: 120 }
    })
  ];
}

// === 字段段落（label + content 同段） ===
function buildFieldParaB(label, content) {
  return new Paragraph({
    children: [
      new TextRun({ text: `${label}：`, bold: true, font: "黑体", size: 21 }),
      new TextRun({ text: content, font: "宋体", size: 21 }),
    ],
    spacing: { after: 100 }
  });
}

// === 多行字段（label 单独一段，内容缩进） ===
function buildMultilineB(label, content) {
  const lines = content.split('\n').filter(l => l.trim());
  return [
    new Paragraph({
      children: [new TextRun({ text: `${label}：`, bold: true, font: "黑体", size: 21 })],
      spacing: { after: 60 }
    }),
    ...lines.map(line => new Paragraph({
      children: [new TextRun({ text: line.replace(/^[-•]\s*/, ''), font: "宋体", size: 21 })],
      spacing: { after: 60 },
      indent: { left: 240 }
    }))
  ];
}

// === 照片占位符 ===
function buildPlaceholderB(desc) {
  return new Paragraph({
    children: [new TextRun({ text: `[待补充照片: ${desc}]`, italics: true, font: "宋体", size: 21, color: "999999" })],
    spacing: { before: 60, after: 60 }
  });
}

// === 分隔 ===
function buildSeparatorB() {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "· · ·", color: "999999", size: 21 })],
    spacing: { before: 200, after: 200 }
  });
}
```

### B-Table 条目
不用表格，用加粗字段名 + 冒号 + 内容，一行一个字段。
```javascript
function buildEntryB_Table(idx, entry) {
  const elements = [...buildHeaderB(idx, entry)];
  if (entry.objective) elements.push(buildFieldParaB("研究目标", entry.objective));
  if (entry.tools) elements.push(buildFieldParaB("工具材料", entry.tools));
  if (entry.procedure) elements.push(...buildMultilineB("实施过程", entry.procedure));
  if (entry.observations) elements.push(...buildMultilineB("观察记录", entry.observations));
  if (entry.problems) elements.push(buildFieldParaB("遇到问题", entry.problems));
  if (entry.solutions) elements.push(buildFieldParaB("解决方法", entry.solutions));
  // photos or placeholders (穿插在相关内容后)
  if (entry.analysis) elements.push(buildFieldParaB("分析总结", entry.analysis));
  if (entry.nextStep) elements.push(buildFieldParaB("下一步", entry.nextStep));
  elements.push(buildSeparatorB());
  return elements;
}
```

### B-Narrative 条目
纯段落，无任何装饰，就像写作文。
```javascript
function buildEntryB_Narrative(idx, entry) {
  return [
    ...buildHeaderB(idx, entry),
    ...entry.narrative.split('\n').filter(l => l.trim()).map(p =>
      new Paragraph({
        children: [new TextRun({ text: p, font: "宋体", size: 21 })],
        spacing: { after: 120 }
      })
    ),
    // photos (穿插在段落间)
    buildSeparatorB()
  ];
}
```

### B-Compact 条目
短横线列表，紧凑排列。
```javascript
function buildEntryB_Compact(idx, entry) {
  return [
    ...buildHeaderB(idx, entry),
    ...entry.quickNotes.map(note =>
      new Paragraph({
        children: [new TextRun({ text: `- ${note}`, font: "宋体", size: 21 })],
        indent: { left: 240, hanging: 160 },
        spacing: { after: 40 }
      })
    ),
    // photos or placeholders
    buildSeparatorB()
  ];
}
```

### B-Debug 条目
问题用粗体，解决用缩进斜体，像在本子上的批注。
```javascript
function buildEntryB_Debug(idx, entry) {
  const elements = [...buildHeaderB(idx, entry)];
  entry.debugPairs.forEach((pair, i) => {
    elements.push(
      new Paragraph({
        children: [new TextRun({ text: `问题${i+1}：${pair.problem}`, bold: true, font: "宋体", size: 21 })],
        spacing: { before: 80, after: 40 }
      }),
      new Paragraph({
        children: [new TextRun({ text: `→ 排查：${pair.process}`, font: "宋体", size: 21 })],
        indent: { left: 360 }, spacing: { after: 40 }
      }),
      new Paragraph({
        children: [new TextRun({ text: `→ 解决：${pair.solution}`, italics: true, font: "宋体", size: 21 })],
        indent: { left: 360 }, spacing: { after: 80 }
      })
    );
  });
  elements.push(buildSeparatorB());
  return elements;
}
```

### B-Experiment 条目
简单数据表格（极简边框），表格前后是普通段落。
```javascript
function buildEntryB_Experiment(idx, entry) {
  // 极简边框数据表
  const headerRow = new TableRow({
    children: entry.dataHeaders.map(h => new TableCell({
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: h, bold: true, font: "黑体", size: 21 })]
      })],
      borders: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "999999" } }
    }))
  });
  const dataRows = entry.dataRows.map(row => new TableRow({
    children: row.map(val => new TableCell({
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: val, font: "宋体", size: 21 })]
      })],
      borders: { bottom: { style: BorderStyle.SINGLE, size: 2, color: "CCCCCC" } }
    }))
  }));

  return [
    ...buildHeaderB(idx, entry),
    // 段落引入
    new Paragraph({
      children: [new TextRun({ text: `测试数据：`, bold: true, font: "黑体", size: 21 })],
      spacing: { after: 60 }
    }),
    new Table({ rows: [headerRow, ...dataRows], width: { size: 100, type: WidthType.PERCENTAGE } }),
    // 观察
    new Paragraph({
      children: [new TextRun({ text: `观察：`, bold: true, font: "黑体", size: 21 })],
      spacing: { before: 100, after: 60 }
    }),
    ...buildPlainLines(entry.observations),
    // 分析
    new Paragraph({
      children: [new TextRun({ text: `分析：`, bold: true, font: "黑体", size: 21 })],
      spacing: { before: 80, after: 60 }
    }),
    new Paragraph({ children: [new TextRun({ text: entry.analysis, font: "宋体", size: 21 })], spacing: { after: 100 } }),
    buildSeparatorB()
  ];
}
```

---

# 配方 C：项目管理风

**特征**: 左侧竖条色块 + 方括号字段名 + 无边框缩进排版 + 分页符

### 通用组件

```javascript
// === 表头 ===
function buildHeaderC(idx, entry) {
  return [
    // 日期小字在上
    new Paragraph({
      children: [new TextRun({ text: entry.date, font: "仿宋", size: 18, color: "666666" })],
      spacing: { after: 40 }
    }),
    // 左侧竖条 + 标题
    new Table({
      rows: [new TableRow({
        children: [
          new TableCell({
            width: { size: 120, type: WidthType.DXA },
            shading: { fill: "1F4E79" },
            borders: ALL_NONE,
            children: [new Paragraph({ text: "" })]
          }),
          new TableCell({
            borders: ALL_NONE,
            children: [new Paragraph({
              children: [new TextRun({ text: `  ${idx}. ${entry.title}`, bold: true, font: "黑体", size: 24 })],
              indent: { left: 120 }
            })]
          })
        ]
      })],
      width: { size: 100, type: WidthType.PERCENTAGE },
      borders: ALL_NONE
    })
  ];
}

// === 方括号字段 ===
function buildBracketFieldC(label, content) {
  const lines = content.split('\n').filter(l => l.trim());
  if (lines.length <= 1) {
    return [new Paragraph({
      children: [
        new TextRun({ text: `【${label}】`, bold: true, font: "黑体", size: 21 }),
        new TextRun({ text: ` ${content}`, font: "宋体", size: 21 }),
      ],
      spacing: { before: 80, after: 60 }
    })];
  }
  return [
    new Paragraph({
      children: [new TextRun({ text: `【${label}】`, bold: true, font: "黑体", size: 21 })],
      spacing: { before: 80, after: 40 }
    }),
    ...lines.map(line => new Paragraph({
      children: [new TextRun({ text: line.replace(/^[-•]\s*/, ''), font: "宋体", size: 21 })],
      indent: { left: 360 },
      spacing: { after: 40 }
    }))
  ];
}

// === 照片占位符 ===
function buildPlaceholderC(desc) {
  // 左侧竖条 + 灰色背景
  return new Table({
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: 80, type: WidthType.DXA },
          shading: { fill: "CCCCCC" },
          borders: ALL_NONE,
          children: [new Paragraph({ text: "" })]
        }),
        new TableCell({
          shading: { fill: "F2F2F2" },
          borders: ALL_NONE,
          children: [new Paragraph({
            children: [new TextRun({ text: `[待补充照片: ${desc}]`, font: "宋体", size: 21 })],
            indent: { left: 120 }
          })]
        })
      ]
    })],
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: ALL_NONE
  });
}

// === 分隔 ===
new Paragraph({ children: [new PageBreak()] })
```

### C-Table 条目
```javascript
function buildEntryC_Table(idx, entry) {
  const elements = [...buildHeaderC(idx, entry)];
  if (entry.objective) elements.push(...buildBracketFieldC("目标", entry.objective));
  if (entry.tools) elements.push(...buildBracketFieldC("工具", entry.tools));
  if (entry.procedure) elements.push(...buildBracketFieldC("过程", entry.procedure));
  if (entry.observations) elements.push(...buildBracketFieldC("观察", entry.observations));
  if (entry.problems) elements.push(...buildBracketFieldC("问题", entry.problems));
  if (entry.solutions) elements.push(...buildBracketFieldC("解决", entry.solutions));
  if (entry.analysis) elements.push(...buildBracketFieldC("分析", entry.analysis));
  if (entry.nextStep) elements.push(...buildBracketFieldC("下一步", entry.nextStep));
  // photos or placeholders
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

### C-Narrative 条目
```javascript
function buildEntryC_Narrative(idx, entry) {
  return [
    ...buildHeaderC(idx, entry),
    // 方括号标记 + 段落内容
    ...buildBracketFieldC("记录", ""),
    ...entry.narrative.split('\n').filter(l => l.trim()).map(p =>
      new Paragraph({
        children: [new TextRun({ text: p, font: "宋体", size: 21 })],
        indent: { left: 360 },
        spacing: { after: 100 }
      })
    ),
    // photos
    new Paragraph({ children: [new PageBreak()] })
  ];
}
```

### C-Compact 条目
```javascript
function buildEntryC_Compact(idx, entry) {
  return [
    ...buildHeaderC(idx, entry),
    new Paragraph({
      children: [new TextRun({ text: "【快速记录】", bold: true, font: "黑体", size: 21 })],
      spacing: { before: 80, after: 40 }
    }),
    ...entry.quickNotes.map(note =>
      new Paragraph({
        children: [new TextRun({ text: `▸ ${note}`, font: "宋体", size: 21 })],
        indent: { left: 360 },
        spacing: { after: 40 }
      })
    ),
    // photos
    new Paragraph({ children: [new PageBreak()] })
  ];
}
```

### C-Debug 条目
```javascript
function buildEntryC_Debug(idx, entry) {
  const elements = [...buildHeaderC(idx, entry)];
  entry.debugPairs.forEach((pair, i) => {
    elements.push(
      ...buildBracketFieldC(`问题${i+1}`, pair.problem),
      new Paragraph({
        children: [
          new TextRun({ text: "排查：", bold: true, font: "黑体", size: 20 }),
          new TextRun({ text: pair.process, font: "宋体", size: 21 })
        ],
        indent: { left: 600 }, spacing: { after: 40 }
      }),
      new Paragraph({
        children: [
          new TextRun({ text: "解决：", bold: true, font: "黑体", size: 20 }),
          new TextRun({ text: pair.solution, font: "宋体", size: 21 })
        ],
        indent: { left: 600 }, spacing: { after: 80 }
      })
    );
  });
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

### C-Experiment 条目
```javascript
function buildEntryC_Experiment(idx, entry) {
  // 表格无深色表头，用粗体行 + 轻度底纹
  const headerRow = new TableRow({
    children: entry.dataHeaders.map(h => new TableCell({
      shading: { fill: "E8E8E8" },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: h, bold: true, font: "黑体", size: 21 })]
      })]
    }))
  });
  const dataRows = entry.dataRows.map(row => new TableRow({
    children: row.map(val => new TableCell({
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: val, font: "宋体", size: 21 })]
      })]
    }))
  }));

  return [
    ...buildHeaderC(idx, entry),
    ...buildBracketFieldC("数据", ""),
    new Table({ rows: [headerRow, ...dataRows], width: { size: 100, type: WidthType.PERCENTAGE } }),
    ...buildBracketFieldC("观察", entry.observations),
    ...buildBracketFieldC("分析", entry.analysis),
    new Paragraph({ children: [new PageBreak()] })
  ];
}
```

---

# 配方 D：极简条目风

**特征**: 编号+粗体+灰日期 + 短横线引导 + 留白分隔 + 紧凑一页2-3条

### 通用组件

```javascript
// === 表头 ===
function buildHeaderD(idx, entry) {
  return new Paragraph({
    children: [
      new TextRun({ text: `(${idx}) `, bold: true, font: "黑体", size: 24 }),
      new TextRun({ text: `${entry.title}  `, bold: true, font: "黑体", size: 24 }),
      new TextRun({ text: entry.date, font: "仿宋", size: 18, color: "999999" }),
    ],
    spacing: { after: 80 }
  });
}

// === 短横线字段（label + content 同行） ===
function buildDashFieldD(label, content) {
  return new Paragraph({
    children: [
      new TextRun({ text: `— ${label}：`, bold: true, font: "黑体", size: 21, color: "444444" }),
      new TextRun({ text: content, font: "宋体", size: 21 }),
    ],
    spacing: { after: 60 },
    indent: { left: 240 }
  });
}

// === 短横线列表 ===
function buildDashListD(items) {
  return items.map(item => new Paragraph({
    children: [new TextRun({ text: `— ${item}`, font: "宋体", size: 21 })],
    spacing: { after: 40 },
    indent: { left: 240 }
  }));
}

// === 照片占位符 ===
function buildPlaceholderD(desc) {
  return new Paragraph({
    children: [
      new TextRun({ text: `— `, font: "宋体", size: 21, color: "999999" }),
      new TextRun({ text: `[待补充照片: ${desc}]`, font: "宋体", size: 21, color: "999999" })
    ],
    indent: { left: 240 },
    spacing: { before: 40, after: 40 }
  });
}

// === 分隔（留白，不分页） ===
function buildSeparatorD() {
  return new Paragraph({ spacing: { after: 300 }, children: [] });
}
```

### D-Table 条目
```javascript
function buildEntryD_Table(idx, entry) {
  const elements = [buildHeaderD(idx, entry)];
  if (entry.objective) elements.push(buildDashFieldD("目标", entry.objective));
  if (entry.tools) elements.push(buildDashFieldD("工具", entry.tools));
  if (entry.procedure) elements.push(...buildMultilineDashD("过程", entry.procedure));
  if (entry.observations) elements.push(...buildMultilineDashD("观察", entry.observations));
  if (entry.problems) elements.push(buildDashFieldD("问题", entry.problems));
  if (entry.solutions) elements.push(buildDashFieldD("解决", entry.solutions));
  if (entry.analysis) elements.push(buildDashFieldD("分析", entry.analysis));
  if (entry.nextStep) elements.push(buildDashFieldD("下一步", entry.nextStep));
  // photos or placeholders
  elements.push(buildSeparatorD());
  return elements;
}

// 多行内容拆分
function buildMultilineDashD(label, content) {
  const lines = content.split('\n').filter(l => l.trim());
  return [
    new Paragraph({
      children: [new TextRun({ text: `— ${label}：`, bold: true, font: "黑体", size: 21, color: "444444" })],
      indent: { left: 240 }, spacing: { after: 40 }
    }),
    ...lines.map(line => new Paragraph({
      children: [new TextRun({ text: line.replace(/^[-•]\s*/, ''), font: "宋体", size: 21 })],
      indent: { left: 480 }, spacing: { after: 40 }
    }))
  ];
}
```

### D-Narrative 条目
```javascript
function buildEntryD_Narrative(idx, entry) {
  return [
    buildHeaderD(idx, entry),
    ...entry.narrative.split('\n').filter(l => l.trim()).map(p =>
      new Paragraph({
        children: [new TextRun({ text: p, font: "宋体", size: 21 })],
        indent: { left: 240 },
        spacing: { after: 100 }
      })
    ),
    // photos
    buildSeparatorD()
  ];
}
```

### D-Compact 条目
```javascript
function buildEntryD_Compact(idx, entry) {
  return [
    buildHeaderD(idx, entry),
    ...buildDashListD(entry.quickNotes),
    // photos
    buildSeparatorD()
  ];
}
```

### D-Debug 条目
```javascript
function buildEntryD_Debug(idx, entry) {
  const elements = [buildHeaderD(idx, entry)];
  entry.debugPairs.forEach((pair, i) => {
    elements.push(
      new Paragraph({
        children: [new TextRun({ text: `— 问题${i+1}：${pair.problem}`, bold: true, font: "宋体", size: 21 })],
        indent: { left: 240 }, spacing: { after: 40 }
      }),
      new Paragraph({
        children: [new TextRun({ text: `  排查：${pair.process}`, font: "宋体", size: 21 })],
        indent: { left: 480 }, spacing: { after: 40 }
      }),
      new Paragraph({
        children: [new TextRun({ text: `  解决：${pair.solution}`, font: "宋体", size: 21 })],
        indent: { left: 480 }, spacing: { after: 60 }
      })
    );
  });
  elements.push(buildSeparatorD());
  return elements;
}
```

### D-Experiment 条目
```javascript
function buildEntryD_Experiment(idx, entry) {
  // 极简数据表（无色表头，细线边框）
  const headerRow = new TableRow({
    children: entry.dataHeaders.map(h => new TableCell({
      borders: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "444444" } },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: h, bold: true, font: "黑体", size: 20 })]
      })]
    }))
  });
  const dataRows = entry.dataRows.map(row => new TableRow({
    children: row.map(val => new TableCell({
      borders: { bottom: { style: BorderStyle.SINGLE, size: 2, color: "DDDDDD" } },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: val, font: "宋体", size: 20 })]
      })]
    }))
  }));

  return [
    buildHeaderD(idx, entry),
    new Table({ rows: [headerRow, ...dataRows], width: { size: 100, type: WidthType.PERCENTAGE } }),
    buildDashFieldD("观察", entry.observations.split('\n')[0] || ""),
    buildDashFieldD("分析", entry.analysis),
    buildSeparatorD()
  ];
}
```

---

# 配方 E：研究报告风

**特征**: 大号标题+下划线 + 目的/工具水平并排 + 灰底区块 + 分页符

### 通用组件

```javascript
// === 表头 ===
function buildHeaderE(idx, entry) {
  return [
    new Paragraph({
      children: [new TextRun({ text: `${idx}. ${entry.title}`, bold: true, font: "黑体", size: 28 })],
      spacing: { after: 40 }
    }),
    new Paragraph({
      children: [new TextRun({ text: entry.date, font: "仿宋", size: 21, color: "666666" })],
      spacing: { after: 40 }
    }),
    new Paragraph({
      border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "333333" } },
      spacing: { after: 160 }
    })
  ];
}

// === 水平并排字段（无边框二列表格） ===
function buildHorizontalPairE(label1, content1, label2, content2) {
  return new Table({
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: 50, type: WidthType.PERCENTAGE },
          borders: ALL_NONE,
          children: [
            new Paragraph({ children: [new TextRun({ text: label1, bold: true, font: "黑体", size: 21, color: "333333" })] }),
            new Paragraph({ children: [new TextRun({ text: content1, font: "宋体", size: 21 })], spacing: { after: 60 } })
          ]
        }),
        new TableCell({
          width: { size: 50, type: WidthType.PERCENTAGE },
          borders: ALL_NONE,
          children: [
            new Paragraph({ children: [new TextRun({ text: label2, bold: true, font: "黑体", size: 21, color: "333333" })] }),
            new Paragraph({ children: [new TextRun({ text: content2, font: "宋体", size: 21 })], spacing: { after: 60 } })
          ]
        })
      ]
    })],
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: ALL_NONE
  });
}

// === 灰底区块 ===
function buildShadedBlockE(label, content) {
  const lines = content.split('\n').filter(l => l.trim());
  return [
    new Paragraph({
      children: [new TextRun({ text: label, bold: true, font: "黑体", size: 21, color: "333333" })],
      spacing: { before: 120, after: 60 }
    }),
    ...lines.map(line => new Paragraph({
      children: [new TextRun({ text: line.replace(/^[-•]\s*/, ''), font: "宋体", size: 21 })],
      shading: { fill: "F5F5F5" },
      spacing: { after: 40 },
      indent: { left: 120, right: 120 }
    }))
  ];
}

// === 照片占位符 ===
function buildPlaceholderE(desc) {
  return new Paragraph({
    children: [new TextRun({ text: `[待补充照片: ${desc}]`, font: "宋体", size: 21 })],
    shading: { fill: "F5F5F5" },
    indent: { left: 120, right: 120 },
    spacing: { before: 60, after: 60 }
  });
}

// === 分隔 ===
new Paragraph({ children: [new PageBreak()] })
```

### E-Table 条目
```javascript
function buildEntryE_Table(idx, entry) {
  const elements = [...buildHeaderE(idx, entry)];
  // 目的 + 工具 水平并排
  if (entry.objective && entry.tools) {
    elements.push(buildHorizontalPairE("目的", entry.objective, "工具/材料", entry.tools));
  }
  // 过程 灰底区块
  if (entry.procedure) elements.push(...buildShadedBlockE("实施过程", entry.procedure));
  if (entry.observations) elements.push(...buildShadedBlockE("观察记录", entry.observations));
  if (entry.problems && entry.solutions) {
    elements.push(buildHorizontalPairE("遇到问题", entry.problems, "解决方法", entry.solutions));
  }
  if (entry.analysis) elements.push(...buildShadedBlockE("分析总结", entry.analysis));
  if (entry.nextStep) {
    elements.push(new Paragraph({
      children: [
        new TextRun({ text: "下一步：", bold: true, font: "黑体", size: 21, color: "333333" }),
        new TextRun({ text: entry.nextStep, font: "宋体", size: 21 })
      ],
      spacing: { before: 80, after: 80 }
    }));
  }
  // photos
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

### E-Narrative 条目
```javascript
function buildEntryE_Narrative(idx, entry) {
  const elements = [...buildHeaderE(idx, entry)];
  // 目的 + 工具 水平并排（如果有）
  if (entry.objective && entry.tools) {
    elements.push(buildHorizontalPairE("目的", entry.objective, "参考资料", entry.tools));
  }
  // narrative 段落
  elements.push(
    ...entry.narrative.split('\n').filter(l => l.trim()).map(p =>
      new Paragraph({
        children: [new TextRun({ text: p, font: "宋体", size: 21 })],
        spacing: { after: 120 }
      })
    )
  );
  // photos
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

### E-Compact 条目
```javascript
function buildEntryE_Compact(idx, entry) {
  const elements = [...buildHeaderE(idx, entry)];
  if (entry.objective && entry.tools) {
    elements.push(buildHorizontalPairE("目的", entry.objective, "工具", entry.tools));
  }
  // quickNotes 用灰底区块
  elements.push(
    new Paragraph({
      children: [new TextRun({ text: "工作记录", bold: true, font: "黑体", size: 21, color: "333333" })],
      spacing: { before: 100, after: 60 }
    }),
    ...entry.quickNotes.map(note => new Paragraph({
      children: [new TextRun({ text: `• ${note}`, font: "宋体", size: 21 })],
      shading: { fill: "F5F5F5" },
      indent: { left: 120, right: 120, hanging: 200 },
      spacing: { after: 40 }
    }))
  );
  // photos
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

### E-Debug 条目
```javascript
function buildEntryE_Debug(idx, entry) {
  const elements = [...buildHeaderE(idx, entry)];
  entry.debugPairs.forEach((pair, i) => {
    // 问题标题
    elements.push(new Paragraph({
      children: [new TextRun({ text: `问题 ${i+1}: ${pair.problem}`, bold: true, font: "黑体", size: 22 })],
      spacing: { before: 120, after: 60 }
    }));
    // 排查 + 解决 水平并排
    elements.push(buildHorizontalPairE("排查过程", pair.process, "解决方案", pair.solution));
  });
  // photos
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

### E-Experiment 条目
```javascript
function buildEntryE_Experiment(idx, entry) {
  // 数据表格：灰色表头（不用深蓝），细边框
  const headerRow = new TableRow({
    children: entry.dataHeaders.map(h => new TableCell({
      shading: { fill: "E0E0E0" },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: h, bold: true, font: "黑体", size: 21 })]
      })]
    }))
  });
  const dataRows = entry.dataRows.map((row, ri) => new TableRow({
    children: row.map(val => new TableCell({
      shading: { fill: ri % 2 === 0 ? "FFFFFF" : "F5F5F5" },
      children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: val, font: "宋体", size: 21 })]
      })]
    }))
  }));

  const elements = [...buildHeaderE(idx, entry)];
  if (entry.objective && entry.tools) {
    elements.push(buildHorizontalPairE("目的", entry.objective, "工具/材料", entry.tools));
  }
  elements.push(
    new Table({ rows: [headerRow, ...dataRows], width: { size: 100, type: WidthType.PERCENTAGE } }),
    ...buildShadedBlockE("观察与发现", entry.observations),
    ...buildShadedBlockE("分析", entry.analysis)
  );
  // photos
  elements.push(new Paragraph({ children: [new PageBreak()] }));
  return elements;
}
```

---

# 通用工具函数

以下函数在所有配方中都可能用到：

```javascript
// 将多行文本拆分为段落数组
function buildContentParagraphs(content, opts = {}) {
  const lines = content.split('\n').filter(l => l.trim());
  return lines.map(line => new Paragraph({
    children: [new TextRun({ text: line.replace(/^[-•]\s*/, ''), font: opts.font || "宋体", size: opts.size || 21 })],
    spacing: { after: opts.spacing?.after || 60 },
    indent: opts.indent,
    shading: opts.shading
  }));
}

// 将多行文本拆分为 bullet 段落
function buildBulletParagraphs(content) {
  const lines = content.split('\n').filter(l => l.trim());
  return lines.map(line => new Paragraph({
    children: [new TextRun({ text: `• ${line.replace(/^[-•]\s*/, '')}`, font: "宋体", size: 21 })],
    spacing: { after: 60 },
    indent: { left: 400, hanging: 240 }
  }));
}

// 纯文本段落（无 bullet）
function buildPlainLines(content) {
  const lines = content.split('\n').filter(l => l.trim());
  return lines.map(line => new Paragraph({
    children: [new TextRun({ text: line.replace(/^[-•]\s*/, ''), font: "宋体", size: 21 })],
    spacing: { after: 60 },
    indent: { left: 240 }
  }));
}
```

---

# 配方选择 → 条目构建的调度

```javascript
// 根据配方和条目风格选择构建函数
function buildEntry(recipe, idx, entry) {
  const style = entry.style || "table";
  const builders = {
    A: { table: buildEntryA_Table, narrative: buildEntryA_Narrative, compact: buildEntryA_Compact, debug: buildEntryA_Debug, experiment: buildEntryA_Experiment },
    B: { table: buildEntryB_Table, narrative: buildEntryB_Narrative, compact: buildEntryB_Compact, debug: buildEntryB_Debug, experiment: buildEntryB_Experiment },
    C: { table: buildEntryC_Table, narrative: buildEntryC_Narrative, compact: buildEntryC_Compact, debug: buildEntryC_Debug, experiment: buildEntryC_Experiment },
    D: { table: buildEntryD_Table, narrative: buildEntryD_Narrative, compact: buildEntryD_Compact, debug: buildEntryD_Debug, experiment: buildEntryD_Experiment },
    E: { table: buildEntryE_Table, narrative: buildEntryE_Narrative, compact: buildEntryE_Compact, debug: buildEntryE_Debug, experiment: buildEntryE_Experiment },
  };
  return builders[recipe][style](idx, entry);
}
```

---

# Implementation Tips

1. **Entry Validation**: Before rendering, verify `date`, `title`, `style` exist; default to "table" if style missing
2. **Multi-line Fields**: Use `.split('\n').filter(l => l.trim())` for clean paragraph breaks
3. **Photo Integration**: Always call photo builder at the end of content; returns empty array if no photos
4. **Font Constants**: `FONT_SONGTI` (宋体) body, `FONT_HEITI` (黑体) headers, `SZ_BODY` (21pt)
5. **紧凑配方注意**: 配方 B/D 不分页，需在脚本中判断：如果下一条目加上当前条目可能超过一页，则在当前条目后插入分页符（可简单按条目长度估算）
