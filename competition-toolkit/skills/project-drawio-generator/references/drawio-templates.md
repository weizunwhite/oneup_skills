# Draw.io XML Templates (图表模板大全)

## Overview

Complete, parameterized Draw.io XML templates for all supported diagram types. When generating diagrams, copy the relevant template, replace `{{PLACEHOLDER}}` values with project-specific content, and adjust element count/positions as needed.

**Critical XML rules:**
- Every `<mxCell>` needs a unique `id` (incrementing integers starting from 2)
- IDs 0 and 1 are reserved for root cells (always include them)
- Use `parent="1"` for top-level elements
- Do NOT use double hyphens inside XML comments
- Encode special characters: `&amp;` for &, `&lt;` for <, `&gt;` for >
- Use `&#xa;` for line breaks in `value` attributes

---

## Template 1: System Architecture (系统架构图)

**Canvas: 1200×820, Background: #F8FAFE**

```xml
<mxfile host="app.diagrams.net" agent="Claude">
  <diagram id="arch" name="系统架构图">
    <mxGraphModel dx="1200" dy="820" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="1200" pageHeight="820"
                  math="0" shadow="0" background="#F8FAFE">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- TITLE BAR -->
        <mxCell id="2" value="{{PROJECT_NAME}} — 系统架构图"
          style="rounded=0;whiteSpace=wrap;html=1;fillColor=#1A237E;strokeColor=none;fontColor=#FFFFFF;fontSize=18;fontStyle=1;verticalAlign=middle;"
          vertex="1" parent="1">
          <mxGeometry x="0" y="0" width="1200" height="50" as="geometry"/>
        </mxCell>

        <!-- SCENE AREA (white box, left 65%) -->
        <mxCell id="3" value=""
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=5;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1;"
          vertex="1" parent="1">
          <mxGeometry x="30" y="65" width="750" height="480" as="geometry"/>
        </mxCell>

        <!-- DEVICE A -->
        <mxCell id="10" value="{{DEVICE_A_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=5;"
          vertex="1" parent="1">
          <mxGeometry x="80" y="120" width="240" height="320" as="geometry"/>
        </mxCell>
        <mxCell id="11" value="{{DEVICE_A_COMPONENTS}}"
          style="text;html=1;align=left;verticalAlign=top;spacingLeft=5;fontSize=12;fontColor=#1A237E;"
          vertex="1" parent="1">
          <mxGeometry x="95" y="155" width="210" height="150" as="geometry"/>
        </mxCell>
        <!-- Device A submodule (optional) -->
        <mxCell id="12" value="{{SUBMODULE_A}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#E3F2FD;strokeColor=#2962FF;strokeWidth=1;fontColor=#2962FF;fontSize=11;dashed=1;"
          vertex="1" parent="1">
          <mxGeometry x="100" y="330" width="200" height="80" as="geometry"/>
        </mxCell>

        <!-- PERSON (optional, between devices) -->
        <mxCell id="15" value=""
          style="shape=mxgraph.basic.person;fillColor=#90A4AE;strokeColor=#546E7A;strokeWidth=1;"
          vertex="1" parent="1">
          <mxGeometry x="395" y="200" width="50" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="16" value="用户"
          style="text;html=1;fontSize=12;fontColor=#546E7A;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="385" y="275" width="70" height="20" as="geometry"/>
        </mxCell>

        <!-- DEVICE B -->
        <mxCell id="20" value="{{DEVICE_B_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=5;"
          vertex="1" parent="1">
          <mxGeometry x="510" y="160" width="230" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="21" value="{{DEVICE_B_COMPONENTS}}"
          style="text;html=1;align=left;verticalAlign=top;spacingLeft=5;fontSize=12;fontColor=#1B5E20;"
          vertex="1" parent="1">
          <mxGeometry x="525" y="195" width="200" height="130" as="geometry"/>
        </mxCell>

        <!-- COMMUNICATION LINK (dashed, bidirectional) -->
        <mxCell id="30" value=""
          style="endArrow=classic;startArrow=classic;html=1;strokeColor=#AA00FF;strokeWidth=2;dashed=1;dashPattern=8 4;curved=1;"
          edge="1" parent="1" source="10" target="20">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <!-- Link label pill -->
        <mxCell id="31" value="{{COMM_PROTOCOL_1}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=50;fillColor=#E8D5F5;strokeColor=#AA00FF;strokeWidth=1;fontColor=#4A148C;fontSize=12;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="340" y="145" width="120" height="30" as="geometry"/>
        </mxCell>

        <!-- INFO BOX: System Composition -->
        <mxCell id="40" value=""
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2962FF;strokeWidth=2;"
          vertex="1" parent="1">
          <mxGeometry x="810" y="65" width="360" height="230" as="geometry"/>
        </mxCell>
        <mxCell id="41" value="系统组成"
          style="rounded=0;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=#2962FF;fontColor=#FFFFFF;fontSize=14;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="810" y="65" width="360" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="42" value="&lt;table style='font-size:12px;color:#1A1A1A;line-height:2.0'&gt;&lt;tr&gt;&lt;td style='color:#2962FF;font-weight:bold'&gt;●&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{MODULE_1}}&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='color:#00C853;font-weight:bold'&gt;●&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{MODULE_2}}&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='color:#FF6D00;font-weight:bold'&gt;●&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{MODULE_3}}&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='color:#AA00FF;font-weight:bold'&gt;●&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{MODULE_4}}&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;"
          style="text;html=1;align=left;verticalAlign=top;spacingLeft=10;spacingTop=5;"
          vertex="1" parent="1">
          <mxGeometry x="815" y="105" width="350" height="180" as="geometry"/>
        </mxCell>

        <!-- INFO BOX: Workflow Steps -->
        <mxCell id="50" value=""
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#FF6D00;strokeWidth=2;"
          vertex="1" parent="1">
          <mxGeometry x="810" y="310" width="360" height="235" as="geometry"/>
        </mxCell>
        <mxCell id="51" value="工作流程"
          style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FF6D00;strokeColor=#FF6D00;fontColor=#FFFFFF;fontSize=14;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="810" y="310" width="360" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="52" value="&lt;table style='font-size:12px;color:#1A1A1A;line-height:2.2'&gt;&lt;tr&gt;&lt;td style='background:#FF6D00;color:white;border-radius:50%;width:22px;height:22px;text-align:center;font-weight:bold'&gt;1&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{STEP_1}}&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='background:#FF6D00;color:white;border-radius:50%;width:22px;height:22px;text-align:center;font-weight:bold'&gt;2&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{STEP_2}}&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='background:#FF6D00;color:white;border-radius:50%;width:22px;height:22px;text-align:center;font-weight:bold'&gt;3&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{STEP_3}}&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='background:#FF6D00;color:white;border-radius:50%;width:22px;height:22px;text-align:center;font-weight:bold'&gt;4&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{STEP_4}}&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;"
          style="text;html=1;align=left;verticalAlign=top;spacingLeft=10;spacingTop=5;"
          vertex="1" parent="1">
          <mxGeometry x="815" y="350" width="350" height="185" as="geometry"/>
        </mxCell>

        <!-- LEGEND BAR -->
        <mxCell id="60" value=""
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=1;"
          vertex="1" parent="1">
          <mxGeometry x="30" y="560" width="750" height="45" as="geometry"/>
        </mxCell>
        <mxCell id="61" value="数据流图例"
          style="text;html=1;fontSize=12;fontStyle=1;fontColor=#546E7A;"
          vertex="1" parent="1">
          <mxGeometry x="45" y="568" width="75" height="25" as="geometry"/>
        </mxCell>
        <!-- Add legend entries as small dashed lines + labels -->

        <!-- SPECS BAR -->
        <mxCell id="70" value=""
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8EAF6;strokeColor=#3F51B5;strokeWidth=1;"
          vertex="1" parent="1">
          <mxGeometry x="30" y="620" width="1140" height="45" as="geometry"/>
        </mxCell>
        <mxCell id="71" value="&lt;b style='color:#1A237E'&gt;核心技术指标：&lt;/b&gt;&lt;span style='color:#1A1A1A'&gt;{{SPEC_1}} &amp;nbsp;│&amp;nbsp; {{SPEC_2}} &amp;nbsp;│&amp;nbsp; {{SPEC_3}} &amp;nbsp;│&amp;nbsp; {{SPEC_4}}&lt;/span&gt;"
          style="text;html=1;fontSize=13;verticalAlign=middle;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="628" width="1100" height="30" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

### Architecture Adaptation Notes

**Single-device project:** Remove Device B, add cloud/phone/environment on the other side.
**Multi-device (3+):** Triangular or horizontal layout, wider canvas (1400×800).
**Software/IoT project:** Phone ↔ Cloud ↔ Sensor device, use MQTT/HTTP links.

---

## Template 2: Flow Chart (流程图)

**Canvas: 620×900, Background: #FFFFFF**

```xml
<mxfile host="app.diagrams.net" agent="Claude">
  <diagram id="flow" name="流程图">
    <mxGraphModel dx="620" dy="900" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="620" pageHeight="900"
                  math="0" shadow="0" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Title -->
        <mxCell id="2" value="{{PROJECT_NAME}} — 使用流程图"
          style="text;html=1;fontSize=16;fontStyle=1;fontColor=#1A237E;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="60" y="15" width="500" height="30" as="geometry"/>
        </mxCell>

        <!-- START -->
        <mxCell id="10" value="开始"
          style="ellipse;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=#1A237E;strokeWidth=2;fontColor=#FFFFFF;fontSize=14;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="220" y="60" width="160" height="50" as="geometry"/>
        </mxCell>

        <!-- Arrow -->
        <mxCell id="11" value=""
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;"
          edge="1" parent="1" source="10" target="20">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- STEP 1 (yellow - init) -->
        <mxCell id="20" value="{{STEP_1}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFF8E1;strokeColor=#F9A825;strokeWidth=2;fontColor=#1A1A1A;fontSize=13;"
          vertex="1" parent="1">
          <mxGeometry x="190" y="140" width="220" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="21" value=""
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;"
          edge="1" parent="1" source="20" target="30">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- STEP 2 (blue - processing) -->
        <mxCell id="30" value="{{STEP_2}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A1A1A;fontSize=13;"
          vertex="1" parent="1">
          <mxGeometry x="190" y="220" width="220" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="31" value=""
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;"
          edge="1" parent="1" source="30" target="40">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- DECISION (red diamond) -->
        <mxCell id="40" value="{{DECISION}}"
          style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFCDD2;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=12;"
          vertex="1" parent="1">
          <mxGeometry x="210" y="305" width="180" height="80" as="geometry"/>
        </mxCell>

        <!-- YES path (down, green label) -->
        <mxCell id="41" value="是"
          style="endArrow=classic;html=1;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=12;fontStyle=1;"
          edge="1" parent="1" source="40" target="50">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- NO path (right, red label, loops back) -->
        <mxCell id="42" value="否"
          style="endArrow=classic;html=1;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=12;fontStyle=1;edgeStyle=orthogonalEdgeStyle;"
          edge="1" parent="1" source="40" target="45">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- NO branch box -->
        <mxCell id="45" value="{{NO_ACTION}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFCDD2;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=12;"
          vertex="1" parent="1">
          <mxGeometry x="440" y="315" width="140" height="50" as="geometry"/>
        </mxCell>

        <!-- Loop back arrow -->
        <mxCell id="46" value=""
          style="endArrow=classic;html=1;strokeColor=#FF1744;strokeWidth=1;dashed=1;edgeStyle=orthogonalEdgeStyle;"
          edge="1" parent="1" source="45" target="30">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="540" y="340"/>
              <mxPoint x="540" y="245"/>
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- STEP 3 (green - success) -->
        <mxCell id="50" value="{{STEP_3}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1A1A1A;fontSize=13;"
          vertex="1" parent="1">
          <mxGeometry x="190" y="425" width="220" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="51" value=""
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;"
          edge="1" parent="1" source="50" target="60">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- STEP 4 (orange - action) -->
        <mxCell id="60" value="{{STEP_4}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFE0B2;strokeColor=#FF6D00;strokeWidth=2;fontColor=#1A1A1A;fontSize=13;"
          vertex="1" parent="1">
          <mxGeometry x="190" y="510" width="220" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="61" value=""
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;"
          edge="1" parent="1" source="60" target="70">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- END -->
        <mxCell id="70" value="结束"
          style="ellipse;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=#1A237E;strokeWidth=2;fontColor=#FFFFFF;fontSize=14;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="220" y="595" width="160" height="50" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Template 3: Hardware Wiring Diagram (硬件接线图)

**Canvas: 1100×750, Background: #FFFFFF**

```xml
<mxfile host="app.diagrams.net" agent="Claude">
  <diagram id="wiring" name="硬件接线图">
    <mxGraphModel dx="1100" dy="750" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="1100" pageHeight="750"
                  math="0" shadow="0" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Title -->
        <mxCell id="2" value="{{PROJECT_NAME}} — 硬件接线图"
          style="text;html=1;fontSize=16;fontStyle=1;fontColor=#1A237E;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="200" y="10" width="700" height="30" as="geometry"/>
        </mxCell>

        <!-- MCU Main Board (center) -->
        <mxCell id="10" value="{{MCU_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=3;fontColor=#1A237E;fontSize=16;fontStyle=1;verticalAlign=top;spacingTop=8;"
          vertex="1" parent="1">
          <mxGeometry x="380" y="120" width="300" height="420" as="geometry"/>
        </mxCell>

        <!-- MCU Pin labels (left side) -->
        <mxCell id="11" value="&lt;div style='font-size:11px;font-family:monospace;line-height:2.0;color:#1A237E;text-align:right'&gt;{{LEFT_PIN_1}}&lt;br&gt;{{LEFT_PIN_2}}&lt;br&gt;{{LEFT_PIN_3}}&lt;br&gt;{{LEFT_PIN_4}}&lt;br&gt;{{LEFT_PIN_5}}&lt;br&gt;{{LEFT_PIN_6}}&lt;br&gt;{{LEFT_PIN_7}}&lt;br&gt;{{LEFT_PIN_8}}&lt;/div&gt;"
          style="text;html=1;align=right;verticalAlign=top;spacingTop=5;"
          vertex="1" parent="1">
          <mxGeometry x="390" y="160" width="120" height="350" as="geometry"/>
        </mxCell>

        <!-- MCU Pin labels (right side) -->
        <mxCell id="12" value="&lt;div style='font-size:11px;font-family:monospace;line-height:2.0;color:#1A237E;text-align:left'&gt;{{RIGHT_PIN_1}}&lt;br&gt;{{RIGHT_PIN_2}}&lt;br&gt;{{RIGHT_PIN_3}}&lt;br&gt;{{RIGHT_PIN_4}}&lt;br&gt;{{RIGHT_PIN_5}}&lt;br&gt;{{RIGHT_PIN_6}}&lt;br&gt;{{RIGHT_PIN_7}}&lt;br&gt;{{RIGHT_PIN_8}}&lt;/div&gt;"
          style="text;html=1;align=left;verticalAlign=top;spacingTop=5;"
          vertex="1" parent="1">
          <mxGeometry x="550" y="160" width="120" height="350" as="geometry"/>
        </mxCell>

        <!-- Peripheral Module (left, e.g., Sensor) -->
        <mxCell id="20" value="{{PERIPHERAL_1_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="150" width="200" height="100" as="geometry"/>
        </mxCell>
        <mxCell id="21" value="{{PERIPHERAL_1_PINS}}"
          style="text;html=1;align=left;fontSize=11;fontColor=#1B5E20;fontFamily=monospace;"
          vertex="1" parent="1">
          <mxGeometry x="60" y="190" width="180" height="50" as="geometry"/>
        </mxCell>

        <!-- Wire: Peripheral 1 → MCU (color-coded) -->
        <mxCell id="22" value="{{WIRE_1_LABEL}}"
          style="endArrow=none;html=1;strokeColor=#2962FF;strokeWidth=2;fontColor=#2962FF;fontSize=10;fontStyle=1;edgeStyle=orthogonalEdgeStyle;"
          edge="1" parent="1" source="20" target="10">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Peripheral Module (left, e.g., Motor Driver) -->
        <mxCell id="25" value="{{PERIPHERAL_2_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#FFE0B2;strokeColor=#FF6D00;strokeWidth=2;fontColor=#E65100;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="300" width="200" height="100" as="geometry"/>
        </mxCell>

        <!-- Peripheral Module (right, e.g., Display) -->
        <mxCell id="30" value="{{PERIPHERAL_3_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#E8D5F5;strokeColor=#AA00FF;strokeWidth=2;fontColor=#4A148C;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="820" y="150" width="200" height="100" as="geometry"/>
        </mxCell>

        <!-- Peripheral Module (right, e.g., Communication) -->
        <mxCell id="35" value="{{PERIPHERAL_4_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#B2DFDB;strokeColor=#00BFA5;strokeWidth=2;fontColor=#004D40;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="820" y="300" width="200" height="100" as="geometry"/>
        </mxCell>

        <!-- Power Supply (bottom) -->
        <mxCell id="40" value="{{POWER_NAME}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#FFCDD2;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="430" y="580" width="200" height="60" as="geometry"/>
        </mxCell>
        <!-- Power wires (red=VCC, black=GND) -->
        <mxCell id="41" value="VCC"
          style="endArrow=none;html=1;strokeColor=#FF1744;strokeWidth=3;fontColor=#FF1744;fontSize=10;fontStyle=1;"
          edge="1" parent="1" source="40" target="10">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- PIN LEGEND (bottom) -->
        <mxCell id="90" value=""
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#E0E0E0;strokeWidth=1;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="670" width="1000" height="55" as="geometry"/>
        </mxCell>
        <mxCell id="91" value="&lt;span style='font-size:12px'&gt;&lt;b style='color:#1A237E'&gt;接线图例：&lt;/b&gt;&lt;span style='color:#FF1744'&gt;━━ VCC/电源&lt;/span&gt; &amp;nbsp;│&amp;nbsp; &lt;span style='color:#1A1A1A'&gt;━━ GND/地线&lt;/span&gt; &amp;nbsp;│&amp;nbsp; &lt;span style='color:#2962FF'&gt;━━ I2C (SDA/SCL)&lt;/span&gt; &amp;nbsp;│&amp;nbsp; &lt;span style='color:#00C853'&gt;━━ SPI&lt;/span&gt; &amp;nbsp;│&amp;nbsp; &lt;span style='color:#FF6D00'&gt;━━ UART (TX/RX)&lt;/span&gt; &amp;nbsp;│&amp;nbsp; &lt;span style='color:#AA00FF'&gt;━━ PWM/GPIO&lt;/span&gt;&lt;/span&gt;"
          style="text;html=1;verticalAlign=middle;"
          vertex="1" parent="1">
          <mxGeometry x="60" y="678" width="980" height="38" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Template 4: Software Module Diagram (软件模块关系图)

**Canvas: 1000×700, Background: #F8FAFE**

```xml
<mxfile host="app.diagrams.net" agent="Claude">
  <diagram id="swmod" name="软件模块关系图">
    <mxGraphModel dx="1000" dy="700" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="1000" pageHeight="700"
                  math="0" shadow="0" background="#F8FAFE">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Title -->
        <mxCell id="2" value="{{PROJECT_NAME}} — 软件模块关系图"
          style="text;html=1;fontSize=16;fontStyle=1;fontColor=#1A237E;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="200" y="10" width="600" height="30" as="geometry"/>
        </mxCell>

        <!-- APPLICATION LAYER -->
        <mxCell id="10" value="应用层"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#FF4081;strokeWidth=2;fontColor=#880E4F;fontSize=13;fontStyle=1;verticalAlign=top;spacingTop=5;dashed=1;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="55" width="900" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="11" value="{{APP_MODULE_1}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FCE4EC;strokeColor=#FF4081;strokeWidth=2;fontColor=#880E4F;fontSize=12;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="80" y="90" width="170" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="12" value="{{APP_MODULE_2}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FCE4EC;strokeColor=#FF4081;strokeWidth=2;fontColor=#880E4F;fontSize=12;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="280" y="90" width="170" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="13" value="{{APP_MODULE_3}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FCE4EC;strokeColor=#FF4081;strokeWidth=2;fontColor=#880E4F;fontSize=12;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="480" y="90" width="170" height="60" as="geometry"/>
        </mxCell>

        <!-- SERVICE/LOGIC LAYER -->
        <mxCell id="20" value="逻辑层"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=13;fontStyle=1;verticalAlign=top;spacingTop=5;dashed=1;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="210" width="900" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="21" value="{{LOGIC_MODULE_1}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=12;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="120" y="245" width="200" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="22" value="{{LOGIC_MODULE_2}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=12;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="380" y="245" width="200" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="23" value="{{LOGIC_MODULE_3}}"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=12;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="640" y="245" width="200" height="60" as="geometry"/>
        </mxCell>

        <!-- DRIVER/HAL LAYER -->
        <mxCell id="30" value="驱动层"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=13;fontStyle=1;verticalAlign=top;spacingTop=5;dashed=1;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="365" width="900" height="120" as="geometry"/>
        </mxCell>
        <!-- Add driver modules similarly -->

        <!-- HARDWARE LAYER -->
        <mxCell id="40" value="硬件层"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE0B2;strokeColor=#FF6D00;strokeWidth=2;fontColor=#E65100;fontSize=13;fontStyle=1;verticalAlign=top;spacingTop=5;dashed=1;"
          vertex="1" parent="1">
          <mxGeometry x="50" y="520" width="900" height="120" as="geometry"/>
        </mxCell>
        <!-- Add hardware components similarly -->

        <!-- Arrows between layers (use source/target for auto-routing) -->
        <mxCell id="50" value=""
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=1;dashed=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;"
          edge="1" parent="1" source="11" target="21">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <!-- Add more inter-layer arrows as needed -->

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Template 5: Sequence Diagram (时序图)

**Canvas: 900×700, Background: #FFFFFF**

```xml
<mxfile host="app.diagrams.net" agent="Claude">
  <diagram id="seq" name="时序图">
    <mxGraphModel dx="900" dy="700" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="900" pageHeight="700"
                  math="0" shadow="0" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Title -->
        <mxCell id="2" value="{{PROJECT_NAME}} — 通信时序图"
          style="text;html=1;fontSize=16;fontStyle=1;fontColor=#1A237E;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="200" y="10" width="500" height="30" as="geometry"/>
        </mxCell>

        <!-- Participant A (lifeline header) -->
        <mxCell id="10" value="{{PARTICIPANT_A}}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="80" y="55" width="150" height="40" as="geometry"/>
        </mxCell>
        <!-- Lifeline A (dashed vertical) -->
        <mxCell id="11" value=""
          style="endArrow=none;html=1;strokeColor=#2962FF;strokeWidth=1;dashed=1;dashPattern=4 4;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="155" y="95" as="sourcePoint"/>
            <mxPoint x="155" y="650" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <!-- Participant B -->
        <mxCell id="15" value="{{PARTICIPANT_B}}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="370" y="55" width="150" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="16" value=""
          style="endArrow=none;html=1;strokeColor=#00C853;strokeWidth=1;dashed=1;dashPattern=4 4;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="445" y="95" as="sourcePoint"/>
            <mxPoint x="445" y="650" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <!-- Participant C -->
        <mxCell id="18" value="{{PARTICIPANT_C}}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8D5F5;strokeColor=#AA00FF;strokeWidth=2;fontColor=#4A148C;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="660" y="55" width="150" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="19" value=""
          style="endArrow=none;html=1;strokeColor=#AA00FF;strokeWidth=1;dashed=1;dashPattern=4 4;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="735" y="95" as="sourcePoint"/>
            <mxPoint x="735" y="650" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <!-- Message 1: A → B -->
        <mxCell id="30" value="{{MSG_1}}"
          style="endArrow=classic;html=1;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=11;fontStyle=1;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="155" y="140" as="sourcePoint"/>
            <mxPoint x="445" y="140" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <!-- Message 2: B → C -->
        <mxCell id="31" value="{{MSG_2}}"
          style="endArrow=classic;html=1;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=11;fontStyle=1;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="445" y="200" as="sourcePoint"/>
            <mxPoint x="735" y="200" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <!-- Message 3: C → B (response, dashed) -->
        <mxCell id="32" value="{{MSG_3}}"
          style="endArrow=classic;html=1;strokeColor=#AA00FF;strokeWidth=2;dashed=1;fontColor=#4A148C;fontSize=11;fontStyle=1;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="735" y="260" as="sourcePoint"/>
            <mxPoint x="445" y="260" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <!-- Add more messages at y increments of ~60px -->

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Template 6: State Machine (状态机图)

**Canvas: 900×600, Background: #FFFFFF**

```xml
<mxfile host="app.diagrams.net" agent="Claude">
  <diagram id="state" name="状态机图">
    <mxGraphModel dx="900" dy="600" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="900" pageHeight="600"
                  math="0" shadow="0" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Title -->
        <mxCell id="2" value="{{PROJECT_NAME}} — 系统状态机"
          style="text;html=1;fontSize=16;fontStyle=1;fontColor=#1A237E;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="200" y="10" width="500" height="30" as="geometry"/>
        </mxCell>

        <!-- Initial state (filled circle) -->
        <mxCell id="5" value=""
          style="ellipse;whiteSpace=wrap;html=1;fillColor=#1A237E;strokeColor=#1A237E;"
          vertex="1" parent="1">
          <mxGeometry x="60" y="250" width="25" height="25" as="geometry"/>
        </mxCell>

        <!-- State: Idle -->
        <mxCell id="10" value="空闲状态&#xa;(Idle)"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=30;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="130" y="225" width="140" height="70" as="geometry"/>
        </mxCell>

        <!-- Arrow: Initial → Idle -->
        <mxCell id="6" value=""
          style="endArrow=classic;html=1;strokeColor=#1A237E;strokeWidth=2;"
          edge="1" parent="1" source="5" target="10">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- State: Running -->
        <mxCell id="20" value="运行状态&#xa;(Running)"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=30;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="380" y="120" width="140" height="70" as="geometry"/>
        </mxCell>

        <!-- Transition: Idle → Running -->
        <mxCell id="30" value="{{EVENT_1}}"
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;fontColor=#1A1A1A;fontSize=11;curved=1;"
          edge="1" parent="1" source="10" target="20">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- State: Error -->
        <mxCell id="25" value="错误状态&#xa;(Error)"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=30;fillColor=#FFCDD2;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="380" y="320" width="140" height="70" as="geometry"/>
        </mxCell>

        <!-- State: Complete -->
        <mxCell id="28" value="完成状态&#xa;(Complete)"
          style="rounded=1;whiteSpace=wrap;html=1;arcSize=30;fillColor=#FFE0B2;strokeColor=#FF6D00;strokeWidth=2;fontColor=#E65100;fontSize=13;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="650" y="225" width="140" height="70" as="geometry"/>
        </mxCell>

        <!-- Transitions between states -->
        <mxCell id="31" value="{{EVENT_2}}"
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;fontColor=#1A1A1A;fontSize=11;curved=1;"
          edge="1" parent="1" source="20" target="28">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="32" value="{{EVENT_3}}"
          style="endArrow=classic;html=1;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=11;curved=1;"
          edge="1" parent="1" source="20" target="25">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="33" value="{{EVENT_4}}"
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;fontColor=#1A1A1A;fontSize=11;curved=1;"
          edge="1" parent="1" source="25" target="10">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="34" value="{{EVENT_5}}"
          style="endArrow=classic;html=1;strokeColor=#546E7A;strokeWidth=2;fontColor=#1A1A1A;fontSize=11;curved=1;"
          edge="1" parent="1" source="28" target="10">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Template 7: Statistics Bar Chart (统计柱状图)

**Canvas: 900×560, Background: #FFFFFF**

```xml
<mxfile host="app.diagrams.net" agent="Claude">
  <diagram id="stats" name="统计图表">
    <mxGraphModel dx="900" dy="560" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1" page="1"
                  pageScale="1" pageWidth="900" pageHeight="560"
                  math="0" shadow="0" background="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Title -->
        <mxCell id="2" value="{{CHART_TITLE}}"
          style="text;html=1;fontSize=18;fontStyle=1;fontColor=#1A237E;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="100" y="15" width="700" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="3" value="（数据来源：{{SOURCE}}）"
          style="text;html=1;fontSize=12;fontColor=#546E7A;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="100" y="45" width="700" height="20" as="geometry"/>
        </mxCell>

        <!-- Axes -->
        <mxCell id="5" value=""
          style="endArrow=none;html=1;strokeColor=#BDBDBD;strokeWidth=1;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="120" y="80" as="sourcePoint"/>
            <mxPoint x="120" y="440" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="6" value=""
          style="endArrow=none;html=1;strokeColor=#BDBDBD;strokeWidth=1;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="120" y="440" as="sourcePoint"/>
            <mxPoint x="850" y="440" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <!-- Grid lines + Y labels (at 20% intervals) -->
        <!-- Chart area: y=80 (100%) to y=440 (0%), height=360px -->
        <!-- For value V%: bar_height=V/100*360, bar_y=440-bar_height, label_y=bar_y-25 -->

        <!-- BAR 1 -->
        <mxCell id="20" value=""
          style="rounded=0;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=none;"
          vertex="1" parent="1">
          <mxGeometry x="170" y="{{BAR1_Y}}" width="100" height="{{BAR1_H}}" as="geometry"/>
        </mxCell>
        <mxCell id="21" value="{{BAR1_VAL}}"
          style="text;html=1;fontSize=14;fontStyle=1;fontColor=#2962FF;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="170" y="{{BAR1_LABEL_Y}}" width="100" height="25" as="geometry"/>
        </mxCell>
        <mxCell id="22" value="{{BAR1_CAT}}"
          style="text;html=1;fontSize=13;fontColor=#1A1A1A;align=center;"
          vertex="1" parent="1">
          <mxGeometry x="170" y="450" width="100" height="25" as="geometry"/>
        </mxCell>

        <!-- BAR 2, 3, 4... same pattern at x+150 increments -->

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Template 8: Pie Chart (饼图)

**Canvas: 700×550, Background: #FFFFFF**

For pie charts in Draw.io, use labeled sectors with a central summary. Since Draw.io doesn't have native pie charts, use arc shapes or simulate with colored sectors:

```xml
<!-- Approach: Use a combination of partial ellipses and a legend -->
<!-- Central circle with total -->
<mxCell id="10" value="{{TOTAL_LABEL}}"
  style="ellipse;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#E0E0E0;strokeWidth=2;fontColor=#1A237E;fontSize=14;fontStyle=1;"
  vertex="1" parent="1">
  <mxGeometry x="200" y="120" width="250" height="250" as="geometry"/>
</mxCell>

<!-- Legend (right side) with colored squares + labels + percentages -->
<mxCell id="50" value="&lt;table style='font-size:13px;color:#1A1A1A;line-height:2.0'&gt;&lt;tr&gt;&lt;td style='background:#2962FF;width:16px;height:16px'&gt;&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{CAT_1}} ({{PCT_1}}%)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='background:#00C853;width:16px;height:16px'&gt;&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{CAT_2}} ({{PCT_2}}%)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='background:#FF6D00;width:16px;height:16px'&gt;&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{CAT_3}} ({{PCT_3}}%)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td style='background:#FF1744;width:16px;height:16px'&gt;&lt;/td&gt;&lt;td&gt;&amp;nbsp;{{CAT_4}} ({{PCT_4}}%)&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;"
  style="text;html=1;align=left;verticalAlign=middle;"
  vertex="1" parent="1">
  <mxGeometry x="490" y="170" width="180" height="150" as="geometry"/>
</mxCell>
```

**Alternative:** Generate pie chart as SVG via Python and embed, or use Draw.io's built-in chart shapes from `mxgraph.chart` library.

---

## Template 9: Comparison Diagram (对比图)

**Canvas: 1000×560, Background: #FFFFFF**

```xml
<!-- VS circle center -->
<mxCell id="3" value="VS"
  style="ellipse;whiteSpace=wrap;html=1;fillColor=#546E7A;strokeColor=none;fontColor=#FFFFFF;fontSize=16;fontStyle=1;"
  vertex="1" parent="1">
  <mxGeometry x="468" y="55" width="64" height="40" as="geometry"/>
</mxCell>

<!-- LEFT: Traditional (red theme) -->
<mxCell id="10" value="传统方式"
  style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFCDD2;strokeColor=#FF1744;strokeWidth=2;fontColor=#B71C1C;fontSize=16;fontStyle=1;"
  vertex="1" parent="1">
  <mxGeometry x="150" y="55" width="180" height="40" as="geometry"/>
</mxCell>
<!-- Disadvantages with ✗ marks in red -->

<!-- RIGHT: Project solution (green theme) -->
<mxCell id="20" value="本项目方案"
  style="rounded=1;whiteSpace=wrap;html=1;fillColor=#C8F7C5;strokeColor=#00C853;strokeWidth=2;fontColor=#1B5E20;fontSize=16;fontStyle=1;"
  vertex="1" parent="1">
  <mxGeometry x="670" y="55" width="180" height="40" as="geometry"/>
</mxCell>
<!-- Advantages with ✓ marks in green -->
```

---

## Template 10: Problem Overview (问题概览图)

**Canvas: 1000×520, Background: #FFFFFF**

4 colored cards in a row, each with:
- Colored number circle
- Bold title
- Description text

Arrow down to solution box.

See full template in original jinpeng skill templates.

---

## Template 11: Line Chart (折线图)

**Canvas: 900×560, Background: #FFFFFF**

```xml
<!-- Same axes structure as bar chart -->
<!-- Data points as small circles -->
<mxCell id="30" value=""
  style="ellipse;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=#FFFFFF;strokeWidth=2;"
  vertex="1" parent="1">
  <mxGeometry x="{{X}}" y="{{Y}}" width="10" height="10" as="geometry"/>
</mxCell>

<!-- Lines connecting data points -->
<mxCell id="40" value=""
  style="endArrow=none;html=1;strokeColor=#2962FF;strokeWidth=2;curved=1;"
  edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="{{X1}}" y="{{Y1}}" as="sourcePoint"/>
    <mxPoint x="{{X2}}" y="{{Y2}}" as="targetPoint"/>
  </mxGeometry>
</mxCell>

<!-- Legend for multiple series -->
<mxCell id="80" value="&lt;span style='color:#2962FF'&gt;━━&lt;/span&gt; {{SERIES_1}} &amp;nbsp;&amp;nbsp; &lt;span style='color:#FF6D00'&gt;━━&lt;/span&gt; {{SERIES_2}}"
  style="text;html=1;fontSize=12;align=center;"
  vertex="1" parent="1">
  <mxGeometry x="300" y="480" width="300" height="25" as="geometry"/>
</mxCell>
```

---

## Template 12: Timeline (时间线)

**Canvas: 1200×500, Background: #FFFFFF**

```xml
<!-- Horizontal timeline bar -->
<mxCell id="5" value=""
  style="endArrow=classic;html=1;strokeColor=#2962FF;strokeWidth=3;"
  edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="80" y="250" as="sourcePoint"/>
    <mxPoint x="1120" y="250" as="targetPoint"/>
  </mxGeometry>
</mxCell>

<!-- Milestone 1 (above the line) -->
<mxCell id="10" value=""
  style="rhombus;whiteSpace=wrap;html=1;fillColor=#2962FF;strokeColor=#1A237E;strokeWidth=2;"
  vertex="1" parent="1">
  <mxGeometry x="145" y="238" width="24" height="24" as="geometry"/>
</mxCell>
<mxCell id="11" value="{{DATE_1}}"
  style="text;html=1;fontSize=11;fontStyle=1;fontColor=#2962FF;align=center;"
  vertex="1" parent="1">
  <mxGeometry x="107" y="268" width="100" height="20" as="geometry"/>
</mxCell>
<mxCell id="12" value="{{MILESTONE_1}}"
  style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=1;fontColor=#1A237E;fontSize=12;"
  vertex="1" parent="1">
  <mxGeometry x="87" y="130" width="140" height="60" as="geometry"/>
</mxCell>
<!-- Connector line from milestone box to timeline -->
<mxCell id="13" value=""
  style="endArrow=none;html=1;strokeColor=#2962FF;strokeWidth=1;dashed=1;"
  edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="157" y="190" as="sourcePoint"/>
    <mxPoint x="157" y="238" as="targetPoint"/>
  </mxGeometry>
</mxCell>

<!-- Milestone 2 (below the line, alternating) -->
<!-- Same pattern but milestone box at y=310 -->
```

---

## Template 13: Mind Map (思维导图)

**Canvas: 1200×800, Background: #FFFFFF**

```xml
<!-- Center node -->
<mxCell id="10" value="{{CENTER_TOPIC}}"
  style="ellipse;whiteSpace=wrap;html=1;fillColor=#1A237E;strokeColor=none;fontColor=#FFFFFF;fontSize=16;fontStyle=1;"
  vertex="1" parent="1">
  <mxGeometry x="500" y="340" width="200" height="80" as="geometry"/>
</mxCell>

<!-- Branch 1 (top-right, blue) -->
<mxCell id="20" value="{{BRANCH_1}}"
  style="rounded=1;whiteSpace=wrap;html=1;arcSize=50;fillColor=#D6E4FF;strokeColor=#2962FF;strokeWidth=2;fontColor=#1A237E;fontSize=14;fontStyle=1;"
  vertex="1" parent="1">
  <mxGeometry x="780" y="150" width="170" height="45" as="geometry"/>
</mxCell>
<mxCell id="21" value=""
  style="endArrow=none;html=1;strokeColor=#2962FF;strokeWidth=2;curved=1;"
  edge="1" parent="1" source="10" target="20">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- Sub-branches of Branch 1 -->
<mxCell id="22" value="{{SUB_1A}}"
  style="rounded=1;whiteSpace=wrap;html=1;arcSize=50;fillColor=#E3F2FD;strokeColor=#2962FF;strokeWidth=1;fontColor=#1A237E;fontSize=12;"
  vertex="1" parent="1">
  <mxGeometry x="1000" y="110" width="140" height="35" as="geometry"/>
</mxCell>
<mxCell id="23" value=""
  style="endArrow=none;html=1;strokeColor=#2962FF;strokeWidth=1;curved=1;"
  edge="1" parent="1" source="20" target="22">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- Branch 2 (top-left, green), Branch 3 (bottom-right, orange), etc. -->
<!-- Each branch uses a different color from the palette -->
```

---

## XML Generation Best Practices

### ID Scheme
- `0, 1`: Reserved root cells
- `2-4`: Title, subtitle, background shapes
- `5-9`: Axes, dividers, global elements
- `10-19`: Group A elements (Device A / State 1 / Branch 1)
- `20-29`: Group B elements
- `30-39`: Group C elements / Connections
- `40-49`: Info boxes
- `50-59`: Info boxes continued
- `60-69`: Legend
- `70-79`: Specs / footer
- `80-89`: Additional elements
- `90-99`: Extra elements

### Position Calculation Helpers

**Bar chart:**
```
Chart area: y_top=80 (100%), y_bottom=440 (0%), height=360px
bar_height = value / max_value * 360
bar_y = 440 - bar_height
label_y = bar_y - 25
Bars at x: 170, 320, 470, 620 (150px spacing for 4 bars)
```

**Line chart:**
```
Same chart area as bar chart
point_y = 440 - (value / max_value * 360)
point_x = 120 + (index / (n-1)) * 730
```

**Timeline:**
```
Timeline y=250, total width 80 to 1120 = 1040px
milestone_x = 80 + (index / (n-1)) * 1040
Alternate boxes above (y=130) and below (y=310) the line
```
