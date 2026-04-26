# Draw.io Diagram Templates

## Color Scheme

Use consistent colors across all diagrams. Each module type gets a unique color pair (fill + border):

```
MCU/主控:       fill=#D6E4FF  stroke=#2962FF  fontColor=#1A237E
视觉/AI:        fill=#C8F7C5  stroke=#00C853  fontColor=#1B5E20
机械/执行:      fill=#FFE0B2  stroke=#FF6D00  fontColor=#E65100
底盘/移动:      fill=#E8D5F5  stroke=#AA00FF  fontColor=#4A148C
传感/安全:      fill=#FFCDD2  stroke=#FF1744  fontColor=#B71C1C
通信/蓝牙:      fill=#E3F2FD  stroke=#1565C0  fontColor=#0D47A1
用户交互:       fill=#FCE4EC  stroke=#FF4081  fontColor=#880E4F
电源:           fill=#FFF8E1  stroke=#F9A825  fontColor=#F57F17
收纳/存储:      fill=#B2DFDB  stroke=#00BFA5  fontColor=#004D40
标题栏(深蓝):   fill=#1A237E  fontColor=#FFFFFF
信息面板边框:   stroke=#2962FF or #FF6D00
决策菱形(是):   fill=#C8F7C5  stroke=#00C853
决策菱形(否):   fill=#FFCDD2  stroke=#FF1744
流程步骤(常规): fill=#D6E4FF  stroke=#2962FF
异常处理:       fill=#FFCDD2  stroke=#FF1744
```

## Common Patterns

### Title Bar
```xml
<mxCell id="title" value="项目名称 — 图表类型" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#1A237E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;verticalAlign=middle;" vertex="1" parent="1">
<mxGeometry x="0" y="0" width="1200" height="48" as="geometry"/>
</mxCell>
```

### Module Box with Description
```xml
<mxCell id="mod1" value="模块名称&lt;br&gt;副标题" style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=13;fontStyle=1;" vertex="1" parent="1">
<mxGeometry x="100" y="100" width="160" height="55" as="geometry"/>
</mxCell>
<mxCell id="mod1_desc" value="描述文字第一行&lt;br&gt;描述文字第二行" style="text;html=1;align=center;fontSize=10;fontColor=#546E7A;" vertex="1" parent="1">
<mxGeometry x="100" y="156" width="160" height="26" as="geometry"/>
</mxCell>
```

### Communication Label (pill-shaped)
```xml
<mxCell id="label1" value="UART2" style="rounded=1;whiteSpace=wrap;html=1;arcSize=50;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=1;fontColor=#1B5E20;fontSize=10;fontStyle=1;" vertex="1" parent="1">
<mxGeometry x="200" y="200" width="55" height="22" as="geometry"/>
</mxCell>
```

### Arrow Styles
```
Solid arrow:     endArrow=classic;html=1;strokeColor=#COLOR;strokeWidth=2;
Bidirectional:   endArrow=classic;startArrow=classic;html=1;strokeColor=#COLOR;strokeWidth=2;
Dashed wireless: endArrow=classic;startArrow=classic;html=1;strokeColor=#COLOR;strokeWidth=2;dashed=1;dashPattern=5 3;
Orthogonal:      edgeStyle=orthogonalEdgeStyle; (add to any arrow style)
```

### Info Panel (right-side box with list)
```xml
<mxCell id="panel_bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2962FF;strokeWidth=2;" vertex="1" parent="1">
<mxGeometry x="800" y="60" width="375" height="250" as="geometry"/>
</mxCell>
<mxCell id="panel_title" value="面板标题" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=#2962FF;fontColor=#FFFFFF;fontSize=14;fontStyle=1;" vertex="1" parent="1">
<mxGeometry x="800" y="60" width="375" height="32" as="geometry"/>
</mxCell>
<mxCell id="panel_content" value="&lt;table style='font-size:12px;color:#1A1A1A;line-height:2.0'&gt;&lt;tr&gt;&lt;td style='color:#2962FF;font-weight:bold'&gt;●&lt;/td&gt;&lt;td&gt;&amp;nbsp;第一项描述&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='color:#00C853;font-weight:bold'&gt;●&lt;/td&gt;&lt;td&gt;&amp;nbsp;第二项描述&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="text;html=1;align=left;verticalAlign=top;spacingLeft=8;spacingTop=4;" vertex="1" parent="1">
<mxGeometry x="805" y="95" width="365" height="210" as="geometry"/>
</mxCell>
```

### Legend Bar (bottom)
```xml
<mxCell id="legend_bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1;" vertex="1" parent="1">
<mxGeometry x="30" y="570" width="740" height="36" as="geometry"/>
</mxCell>
<mxCell id="legend_text" value="&lt;span style='font-size:11px'&gt;&lt;b style='color:#546E7A'&gt;通信：&lt;/b&gt;&lt;span style='color:#00C853'&gt;━ UART&lt;/span&gt; &amp;nbsp;│&amp;nbsp; &lt;span style='color:#FF6D00'&gt;━ PWM&lt;/span&gt; &amp;nbsp;│&amp;nbsp; &lt;span style='color:#1565C0'&gt;┅ BLE&lt;/span&gt;&lt;/span&gt;" style="text;html=1;verticalAlign=middle;" vertex="1" parent="1">
<mxGeometry x="38" y="575" width="720" height="26" as="geometry"/>
</mxCell>
```

### Specs Bar (bottom, below legend)
```xml
<mxCell id="specs_bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8EAF6;strokeColor=#3F51B5;strokeWidth=1;" vertex="1" parent="1">
<mxGeometry x="30" y="615" width="1140" height="38" as="geometry"/>
</mxCell>
<mxCell id="specs_text" value="&lt;b style='color:#1A237E'&gt;核心技术指标：&lt;/b&gt;指标1 &amp;nbsp;│&amp;nbsp; 指标2 &amp;nbsp;│&amp;nbsp; 指标3" style="text;html=1;fontSize=12;verticalAlign=middle;" vertex="1" parent="1">
<mxGeometry x="45" y="621" width="1110" height="26" as="geometry"/>
</mxCell>
```

---

## Template 1: System Architecture Diagram (系统架构图)

**Typical size**: 1200×760 px
**Layout**: Left half = robot/device body (dashed outline) with modules around a central MCU. Right half = info panels. Bottom = legend + specs.

```
Layout sketch:
┌──────────────────────────────────────────────────────────────┐
│ Title Bar (full width, dark blue)                            │
├──────────────────────────────────┬───────────────────────────┤
│                                  │  ┌─────────────────────┐  │
│   ┌──────┐    ┌──────┐         │  │  系统组成 (info box) │  │
│   │Vision│←──→│ Arm  │ Eye-in  │  │  ● Module 1          │  │
│   └──────┘    └──────┘  Hand   │  │  ● Module 2          │  │
│       ↕ UART     ↑ UART TX     │  │  ...                 │  │
│   ┌──────────────────┐         │  └─────────────────────┘  │
│   │  ESP32 主控芯片   │←BLE──→ │  ┌─────────────────────┐  │
│   └──────────────────┘  蓝牙交互│  │  工作流程 (info box) │  │
│     ↕ PWM       ↕ GPIO         │  │  ① Step 1            │  │
│   ┌──────┐    ┌──────┐ 垃圾桶  │  │  ② Step 2            │  │
│   │Chassis│   │Sensor│         │  │  ...                 │  │
│   └──────┘    └──────┘         │  └─────────────────────┘  │
│ (dashed outline: robot body)   │                            │
├──────────────────────────────────┴───────────────────────────┤
│ Legend: ━ UART  ━ PWM  ┅ BLE                                │
│ Specs: metric1 │ metric2 │ metric3 │ budget                 │
└──────────────────────────────────────────────────────────────┘
```

**Key elements to include:**
- Central MCU box (largest, thickest border)
- Module boxes around MCU with colored arrows
- Communication protocol labels on each arrow
- Dashed outline around physical robot body
- External elements (phone, cloud) outside the outline
- Two info panels on right: System Composition + Workflow
- Legend + specs at bottom

---

## Template 2: Workflow / Flowchart (工作流程图)

**Typical size**: 780×1280 px (portrait, tall)
**Layout**: Top-down flow with decision diamonds and exception branches on sides.

**Element styles:**
```xml
<!-- Start/End: rounded rectangle, colored -->
<mxCell value="开始" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#E8EAF6;strokeColor=#3F51B5;strokeWidth=2;fontColor=#1A237E;fontSize=12;fontStyle=1;" .../>

<!-- Process step -->
<mxCell value="步骤描述" style="rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A1A1A;fontSize=12;" .../>

<!-- Decision diamond -->
<mxCell value="条件&lt;br&gt;判断？" style="rhombus;whiteSpace=wrap;html=1;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=12;fontStyle=1;" .../>

<!-- Exception handler (side branch) -->
<mxCell value="异常处理" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFCDD2;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=11;" .../>

<!-- Emergency stop indicator -->
<mxCell value="⚠ 急停" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FF1744;strokeColor=#B71C1C;strokeWidth=2;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" .../>
```

**Flow pattern:**
- Main flow goes top→bottom in center column
- "Yes" branches continue downward (green arrows)
- "No" branches go right to exception handlers (red arrows)
- Exception handlers loop back to main flow via orthogonal dashed arrows
- Use `edgeStyle=orthogonalEdgeStyle` with `<Array as="points">` for routing

**For two-layer state machines** (e.g., work mode + task state machine):
- Top section: mode layer (IDLE ↔ TEACH, timer → PATROL)
- Dashed box around the task state machine section
- Label the dashed box with the sub-state machine name

---

## Template 3: Statistics / Bar Chart (统计图表)

**Typical size**: 800×500 px
**Use for**: Background data, comparison numbers, survey results

Draw bars as filled rectangles with values on top:
```xml
<!-- Bar -->
<mxCell value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=none;" vertex="1" parent="1">
<mxGeometry x="120" y="200" width="60" height="150" as="geometry"/>
</mxCell>
<!-- Bar label -->
<mxCell value="67%" style="text;html=1;align=center;fontSize=12;fontStyle=1;fontColor=#2962FF;" vertex="1" parent="1">
<mxGeometry x="120" y="180" width="60" height="20" as="geometry"/>
</mxCell>
<!-- X-axis label -->
<mxCell value="类别A" style="text;html=1;align=center;fontSize=11;fontColor=#546E7A;" vertex="1" parent="1">
<mxGeometry x="120" y="355" width="60" height="20" as="geometry"/>
</mxCell>
```

**Layout**: Title at top → Y-axis label (rotated) → bars in a row → X-axis labels → data source citation at bottom.

---

## Template 4: Comparison Diagram (对比图)

**Typical size**: 900×450 px
**Use for**: Traditional approach vs. project solution

Layout as two side-by-side cards:
```
┌─────────────────┐  VS  ┌─────────────────┐
│   传统方式       │      │   本项目方案     │
│   (red-tinted)  │      │   (green-tinted) │
│                 │      │                  │
│  ✗ Problem 1   │      │  ✓ Solution 1    │
│  ✗ Problem 2   │      │  ✓ Solution 2    │
│  ✗ Problem 3   │      │  ✓ Solution 3    │
└─────────────────┘      └─────────────────┘
```

Use `✗` (red) for problems and `✓` (green) for solutions in HTML table format.

---

## Template 5: Timeline / Development Plan (时间线)

**Typical size**: 1000×400 px
**Use for**: Development phases, project milestones

Horizontal timeline with phase blocks:
```xml
<!-- Timeline axis -->
<mxCell value="" style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;" edge="1" parent="1">
<mxGeometry relative="1" as="geometry">
<mxPoint x="50" y="200" as="sourcePoint"/>
<mxPoint x="950" y="200" as="targetPoint"/>
</mxGeometry>
</mxCell>

<!-- Phase block above timeline -->
<mxCell value="阶段1&lt;br&gt;底盘调试" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
<mxGeometry x="80" y="120" width="150" height="60" as="geometry"/>
</mxCell>
<!-- Week label below timeline -->
<mxCell value="第1-2周" style="text;html=1;fontSize=10;fontColor=#546E7A;align=center;" vertex="1" parent="1">
<mxGeometry x="80" y="210" width="150" height="20" as="geometry"/>
</mxCell>
```

Alternate phases above/below timeline for visual variety.

---

## Template 6: State Machine Diagram (状态机图)

**Typical size**: 900×600 px
**Use for**: System state definitions, mode transitions

```xml
<!-- State node -->
<mxCell value="IDLE&lt;br&gt;待机状态" style="ellipse;whiteSpace=wrap;html=1;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=12;" vertex="1" parent="1">
<mxGeometry x="100" y="200" width="120" height="60" as="geometry"/>
</mxCell>

<!-- Transition arrow with condition -->
<mxCell value="定时器到期" style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;fontColor=#1A1A1A;fontSize=10;fontStyle=1;" edge="1" parent="1" source="idle" target="patrol">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Use ellipses for states, labeled arrows for transitions, and group related states with dashed rectangles.

---

## Dimension Guidelines

| Diagram Type | Width | Height | Orientation |
|-------------|-------|--------|-------------|
| System Architecture | 1200 | 700-800 | Landscape |
| Workflow (simple) | 720 | 900-1100 | Portrait |
| Workflow (complex) | 780 | 1200-1400 | Portrait |
| Statistics Chart | 800 | 450-550 | Landscape |
| Comparison | 900 | 400-500 | Landscape |
| Timeline | 1000 | 350-450 | Landscape |
| State Machine | 900 | 500-650 | Landscape |
| Mind Map | 1000 | 700 | Landscape |

Set `pageWidth` and `pageHeight` in `<mxGraphModel>` to match these dimensions.
