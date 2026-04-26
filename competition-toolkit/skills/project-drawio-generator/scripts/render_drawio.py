#!/usr/bin/env python3
"""
render_drawio.py — Convert .drawio XML files to high-resolution PNG images.

Usage:
    python3 render_drawio.py input.drawio output.png [scale]

    scale: Device scale factor (default: 2)
           1 = screen preview, 2 = Word documents, 3 = print quality

Dependencies:
    - playwright (pre-installed in Anthropic environments)
    - mxgraph npm package: run `cd /home/claude && npm install mxgraph`

Can also be used programmatically:
    exec(open('render_drawio.py').read())
    render_drawio('input.drawio', 'output.png', scale=2)
"""

import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET


def ensure_mxgraph():
    """Install mxgraph npm package if not present."""
    mxclient = "/home/claude/node_modules/mxgraph/javascript/mxClient.js"
    if not os.path.exists(mxclient):
        print("Installing mxgraph npm package...")
        subprocess.run(["npm", "install", "mxgraph"], cwd="/home/claude", check=True,
                       capture_output=True)
    return mxclient


def render_drawio(input_path, output_path, scale=2, timeout_ms=3000):
    """
    Convert a .drawio file to PNG.

    Args:
        input_path: Path to .drawio XML file
        output_path: Path for output PNG
        scale: Device scale factor (1, 2, or 3)
        timeout_ms: Milliseconds to wait for rendering (default 3000)

    Returns:
        output_path on success, raises Exception on failure
    """
    mxclient_path = ensure_mxgraph()
    mxbase_path = os.path.dirname(mxclient_path)

    # Validate and parse XML
    tree = ET.parse(input_path)
    model = tree.find(".//mxGraphModel")
    if model is None:
        raise ValueError(f"No <mxGraphModel> found in {input_path}")

    pw = int(model.get("pageWidth", 1200))
    ph = int(model.get("pageHeight", 800))

    with open(input_path, "r", encoding="utf-8") as f:
        xml_content = f.read()

    xml_escaped = json.dumps(xml_content)

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>body{{margin:0;padding:0;background:white;}}#container{{overflow:hidden;}}</style>
</head><body>
<div id="container"></div>
<script>
window.mxBasePath='{mxbase_path}/src';
window.mxLoadResources=false;
window.mxLoadStylesheets=false;
</script>
<script src="file://{os.path.abspath(mxclient_path)}"></script>
<script>
try{{
var xmlStr={xml_escaped};
var xmlDoc=new DOMParser().parseFromString(xmlStr,'text/xml');
var container=document.getElementById('container');
container.style.width='{pw}px';
container.style.height='{ph}px';
var graph=new mxGraph(container);
graph.setEnabled(false);
graph.htmlLabels=true;
var doc=mxUtils.createXmlDocument();
var importedNode=doc.importNode(xmlDoc.querySelector('mxGraphModel'),true);
doc.appendChild(importedNode);
var codec=new mxCodec(doc);
codec.decode(doc.documentElement,graph.getModel());
document.title='OK:'+{pw}+':'+{ph};
}}catch(e){{document.title='ERROR:'+e.message;console.error(e);}}
</script></body></html>"""

    html_path = os.path.join(os.path.dirname(output_path) or "/home/claude", "_render_tmp.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(
                viewport={"width": pw, "height": ph},
                device_scale_factor=scale,
            )
            page.goto(f"file://{os.path.abspath(html_path)}")
            page.wait_for_timeout(timeout_ms)

            title = page.title()
            if title.startswith("ERROR:"):
                browser.close()
                raise RuntimeError(f"mxGraph render failed: {title}")

            page.screenshot(path=output_path, full_page=True)
            browser.close()

        actual_w = pw * scale
        actual_h = ph * scale
        print(f"Rendered: {output_path} ({actual_w}x{actual_h}px, {scale}x scale)")
        return output_path

    finally:
        if os.path.exists(html_path):
            os.remove(html_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 render_drawio.py input.drawio output.png [scale]")
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    sc = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    render_drawio(in_file, out_file, scale=sc)
