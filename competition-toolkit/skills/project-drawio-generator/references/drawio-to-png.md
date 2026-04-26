# Draw.io to PNG Conversion

## Overview

Convert .drawio XML files to high-resolution PNG images using **Playwright** (headless Chromium) + **mxGraph** (npm package, local rendering, no network required).

This approach works in all Anthropic environments (claude.ai, Claude Code, Cowork) because:
- Playwright + Chromium are pre-installed
- mxGraph npm package can be installed locally
- No external network access needed for rendering (only for initial npm install)

## Prerequisites

### First-time Setup
```bash
cd /home/claude
npm install mxgraph
```

This installs `mxgraph` to `/home/claude/node_modules/mxgraph/`. The key file is `javascript/mxClient.js` (~92K lines) which contains the full mxGraph rendering engine.

### Verify Setup
```python
import os
assert os.path.exists('/home/claude/node_modules/mxgraph/javascript/mxClient.js')
```

## Conversion Script

Use `scripts/render_drawio.py` for conversion. It can be called as a standalone script or imported as a function.

### Standalone Usage
```bash
python3 render_drawio.py input.drawio output.png [scale]
```
- `input.drawio` — path to the .drawio XML file
- `output.png` — path for the output PNG
- `scale` — optional device scale factor (default: 2, use 3 for Word documents)

### Programmatic Usage
```python
exec(open('render_drawio.py').read())
render_drawio('input.drawio', 'output.png', scale=2)
```

## How It Works

1. Read the .drawio XML file
2. Extract `pageWidth` and `pageHeight` from `<mxGraphModel>` attributes
3. Generate an HTML page that:
   - Loads mxGraph from the local npm package (`file://` protocol)
   - Creates an `mxGraph` instance in a container sized to page dimensions
   - Decodes the XML model using `mxCodec`
4. Open the HTML in headless Chromium via Playwright
5. Set `device_scale_factor` for high-DPI rendering (2x = double resolution)
6. Take a full-page screenshot as PNG

## Scale Factor Guide

| Use Case | Scale | Typical Output Size | Quality |
|----------|-------|-------------------|---------|
| Preview / Markdown | 1 | 1200×760 | Good for screen |
| Word document embedding | 2 | 2400×1520 | Recommended |
| Print / high-quality | 3 | 3600×2280 | Best, large file |

For Word documents (论文, 技术方案), **always use scale=2** as the minimum. The docx image embedding should reference the actual pixel dimensions and set display width to ~560px for architecture diagrams or ~400px for flow charts.

## Troubleshooting

### "mxGraph is not defined"
The mxClient.js file is not loading. Check:
- `/home/claude/node_modules/mxgraph/javascript/mxClient.js` exists
- The HTML uses `file://` protocol for the script src
- `window.mxBasePath` is set before loading mxClient.js

### Blank or white PNG
The XML model failed to decode. Check:
- XML validates with `xml.etree.ElementTree.parse()`
- No XML comments in the file
- No unescaped quotes in attribute values
- Page title shows "OK:WIDTH:HEIGHT" (check via `page.title()`)

### Chinese text not rendering
Chromium in this environment supports CJK text by default. If text is missing:
- Ensure `html=1` is in the cell style (enables HTML label rendering)
- Use `&lt;br&gt;` for line breaks, not `\n`
- Check that `fontFamily` is not set to a non-existent font

### Timeout errors
Increase wait time in the script. Default is 2000ms which is usually sufficient. For very complex diagrams (100+ elements), increase to 4000ms.
