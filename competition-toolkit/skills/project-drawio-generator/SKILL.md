---
name: project-drawio-generator
description: >
  Generate all types of professional diagrams for youth science and technology innovation
  projects using Draw.io XML format. Covers system architecture, flow charts, statistics
  charts, comparison diagrams, wiring diagrams, software module diagrams, sequence diagrams,
  state machines, test result charts (line/radar/pie), timelines, mind maps, and more.
  Outputs editable .drawio files and PNG exports. Used across all competition papers,
  technical proposals, presentations, research logs, and proposals.
  Trigger on: 架构图, 流程图, 系统图, 图表, drawio, 接线图, 模块图, 时序图, 状态机,
  折线图, 雷达图, 饼图, 时间线, 甘特图, 思维导图, 对比图, 统计图, 原理图, 数据流图,
  生成图表, 画图, 制图, diagram, chart, draw.
  Also trigger when competition-paper-generator or tech-proposal-generator needs diagrams.
---

# Project Draw.io Diagram Generator (项目图表生成器)

## Overview

Generate professional, editable diagrams in Draw.io XML format for student science and technology innovation projects. All diagrams can be:
- Opened and edited in Draw.io (app.diagrams.net)
- Automatically converted to high-resolution PNG for embedding in Word documents or Markdown
- Customized by the user after generation

## Supported Diagram Types

| Type | Chinese | When to Use |
|------|---------|-------------|
| System Architecture | 系统架构图 | Show physical devices, modules, communication links |
| Workflow / Flowchart | 工作流程图 | Show step-by-step process with decision branches |
| State Machine | 状态机图 | Show system states and transitions |
| Statistics Chart | 统计图表 | Bar charts, data comparisons for background section |
| Comparison Diagram | 对比图 | Side-by-side traditional vs. project solution |
| Timeline | 时间线/甘特图 | Development phases, project milestones |
| Mind Map | 思维导图 | Brainstorming, feature overview |
| Wiring Diagram | 接线图 | Pin connections, hardware wiring |
| Software Module | 模块图 | Software layers, class relationships |
| Test Results | 测试结果图 | Line charts, radar charts for test data |

## Critical XML Rules

Draw.io uses an XML parser that is strict about certain things. **ALWAYS follow these rules** to avoid parsing errors:

### Rule 1: NO XML Comments
```xml
<!-- This will BREAK Draw.io -->
```
Draw.io's parser cannot handle XML comments. Never include `<!-- -->` in generated XML.

### Rule 2: Escape Chinese Quotation Marks
When Chinese text contains ASCII quotation marks `"` inside an XML attribute value, they MUST be escaped as `&quot;`:
```xml
<!-- WRONG: breaks XML parsing -->
<mxCell value="进入"扫描模式"" .../>

<!-- CORRECT: escaped quotes -->
<mxCell value="进入&quot;扫描模式&quot;" .../>
```

### Rule 3: Single-Line Attributes
Keep each `<mxCell>` element's attributes on a single line. Multi-line attributes can cause parsing issues.

### Rule 4: Validate Before Output
Always validate the generated XML with Python's `xml.etree.ElementTree` before saving:
```python
import xml.etree.ElementTree as ET
try:
    ET.parse(filepath)
    print("XML valid")
except ET.ParseError as e:
    print(f"XML error: {e}")
```

### Rule 5: XML Structure Template
Every .drawio file must follow this structure:
```xml
<mxfile host="app.diagrams.net" agent="Claude">
<diagram id="unique-id" name="Diagram Name">
<mxGraphModel dx="WIDTH" dy="HEIGHT" grid="1" gridSize="10" guides="1"
  tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1"
  pageWidth="WIDTH" pageHeight="HEIGHT" math="0" shadow="0" background="#FFFFFF">
<root>
<mxCell id="0"/>
<mxCell id="1" parent="0"/>
<!-- diagram elements here -->
</root>
</mxGraphModel>
</diagram>
</mxfile>
```

## Workflow

### Step 1: Determine Diagram Type and Content

Based on user request and project context, determine:
- Which diagram type(s) to generate
- What content to include (modules, steps, data, etc.)
- Appropriate dimensions (see templates)

### Step 2: Generate Draw.io XML

Refer to `references/diagram-templates.md` for templates of each diagram type.

**Design principles for all diagrams:**
- Use scenario-based (场景式) architecture diagrams, NOT abstract layered diagrams
- Color-code modules consistently (see color scheme in templates)
- Include legends and technical specs where appropriate
- Label all communication links with protocol names
- Use HTML formatting in `value` attributes for rich text (line breaks, bold, tables)

### Step 3: Validate XML

```python
import xml.etree.ElementTree as ET
ET.parse("output.drawio")  # Will throw if invalid
```

### Step 4: Convert to PNG (if needed)

When the diagram needs to be embedded in a Word document or Markdown file, convert to high-resolution PNG. Refer to `references/drawio-to-png.md` for the conversion script.

**Quick conversion command:**
```python
# Ensure mxgraph is installed
import subprocess, os
if not os.path.exists('/home/claude/node_modules/mxgraph'):
    subprocess.run(['npm', 'install', 'mxgraph'], cwd='/home/claude')

# Convert
exec(open('/home/claude/skills/project-drawio-generator/scripts/render_drawio.py').read())
render_drawio('input.drawio', 'output.png', scale=2)
```

Or copy the script and call directly:
```bash
python3 /path/to/render_drawio.py input.drawio output.png 2
```

### Step 5: Output

**Standalone diagram request:**
- Save .drawio to `/mnt/user-data/outputs/`
- Optionally also save .png
- Use `present_files` to share

**Called from another skill (paper/proposal):**
- Save .drawio to working directory
- Convert to PNG at specified scale (2x for Word, 1x for Markdown)
- Return PNG path for embedding

## Architecture Diagram Guidelines

Architecture diagrams for competition projects should be **scenario-based** (场景式), showing:

1. **Physical layout** — where devices are deployed in space
2. **Device modules** — key components labeled on each device
3. **Communication links** — dashed arrows with protocol labels (UART, I2C, WiFi, BLE, etc.)
4. **System composition box** — right-side panel listing all modules with color dots
5. **Workflow summary box** — right-side panel with numbered steps
6. **Legend bar** — bottom bar showing communication line colors/styles
7. **Technical specs bar** — bottom bar with key metrics

**Do NOT create abstract layered diagrams** (应用层→通信层→驱动层→硬件层). These are too academic and hard for evaluators to quickly understand.

## Resources

### references/diagram-templates.md
Complete Draw.io XML templates for all diagram types. Includes color schemes, layout patterns, and example code for each type.

### references/drawio-to-png.md
PNG conversion solution using Playwright + mxGraph. Includes the render script, installation instructions, and troubleshooting.

### scripts/render_drawio.py
Standalone Python script for converting .drawio files to high-resolution PNG images.
