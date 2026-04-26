# Mixly 2.0 积木 XML 语法参考

完整的 Mixly 2.0 (Blockly) 积木类型及其 XML 写法。每个积木包含所有 field、value、shadow、statement、mutation 细节。

---

## 结构积木

### base_setup — setup/loop 主结构

```xml
<block type="base_setup" x="20" y="20">
  <statement name="DO">
    <!-- setup() 中的语句 -->
  </statement>
  <statement name="DO2">
    <!-- loop() 中的语句 -->
  </statement>
</block>
```

- `DO` = setup() 语句体
- `DO2` = loop() 语句体
- 每个 .mix 文件只有一个 `base_setup`

---

## 变量积木

### variables_declare — 声明变量

```xml
<block type="variables_declare">
  <field name="variables_type">global_variate</field>
  <field name="VAR">sensorValue</field>
  <field name="TYPE">int</field>
  <value name="VALUE">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
</block>
```

**TYPE 可选值**：`int`, `long`, `float`, `boolean`, `byte`, `char`, `String`

**variables_type 可选值**：`global_variate`（全局）, `local_variate`（局部）

**多变量声明串联**（洋葱结构 — 第一个声明包裹后续声明）：

```xml
<block type="variables_declare" x="20" y="20">
  <field name="variables_type">global_variate</field>
  <field name="VAR">varA</field>
  <field name="TYPE">int</field>
  <value name="VALUE">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
  <next>
    <block type="variables_declare">
      <field name="variables_type">global_variate</field>
      <field name="VAR">varB</field>
      <field name="TYPE">boolean</field>
      <value name="VALUE">
        <block type="logic_boolean"><field name="BOOL">FALSE</field></block>
      </value>
      <!-- 更多变量继续 <next> 嵌套 -->
    </block>
  </next>
</block>
```

### variables_set — 设置变量值

```xml
<block type="variables_set">
  <field name="VAR">sensorValue</field>
  <value name="VALUE">
    <block type="math_number"><field name="NUM">100</field></block>
  </value>
</block>
```

### variables_get — 获取变量值

```xml
<block type="variables_get">
  <field name="VAR">sensorValue</field>
</block>
```

输出型积木，用在 `<value>` 内部。

---

## I/O 积木

### inout_digital_write2 — digitalWrite

```xml
<block type="inout_digital_write2">
  <value name="PIN">
    <shadow type="pins_digital"><field name="PIN">13</field></shadow>
  </value>
  <value name="STAT">
    <shadow type="inout_highlow"><field name="BOOL">HIGH</field></shadow>
  </value>
</block>
```

### inout_digital_read2 — digitalRead

```xml
<block type="inout_digital_read2">
  <value name="PIN">
    <shadow type="pins_digital"><field name="PIN">5</field></shadow>
  </value>
</block>
```

输出型积木（返回 HIGH/LOW）。

### inout_analog_write — analogWrite (PWM)

```xml
<block type="inout_analog_write">
  <value name="PIN">
    <shadow type="pins_pwm"><field name="PIN">3</field></shadow>
  </value>
  <value name="NUM">
    <shadow type="math_number"><field name="NUM">128</field></shadow>
  </value>
</block>
```

### inout_analog_read — analogRead

```xml
<block type="inout_analog_read">
  <value name="PIN">
    <shadow type="pins_analog"><field name="PIN">A0</field></shadow>
  </value>
</block>
```

输出型积木（返回 0-1023）。

### inout_pinMode — pinMode

```xml
<block type="inout_pinMode">
  <field name="MODE">OUTPUT</field>
  <value name="PIN">
    <shadow type="pins_digital"><field name="PIN">5</field></shadow>
  </value>
</block>
```

**MODE 可选值**：`INPUT`, `OUTPUT`, `INPUT_PULLUP`

### inout_highlow — HIGH/LOW 常量

```xml
<block type="inout_highlow">
  <field name="BOOL">HIGH</field>
</block>
```

**BOOL 可选值**：`HIGH`, `LOW`

---

## 引脚 Shadow 积木

这些积木只能作为 shadow 出现在 `<value>` 内部。

### pins_digital — 数字引脚

```xml
<shadow type="pins_digital"><field name="PIN">13</field></shadow>
```

AVR 有效值：`0`-`13`

### pins_analog — 模拟引脚

```xml
<shadow type="pins_analog"><field name="PIN">A0</field></shadow>
```

AVR 有效值：`A0`-`A7`

### pins_pwm — PWM 引脚

```xml
<shadow type="pins_pwm"><field name="PIN">3</field></shadow>
```

AVR 有效值：`3`, `5`, `6`, `9`, `10`, `11`

---

## 控制流积木

### controls_if — if/elseif/else

**简单 if**：

```xml
<block type="controls_if">
  <value name="IF0">
    <!-- 条件表达式 -->
  </value>
  <statement name="DO0">
    <!-- if 体 -->
  </statement>
</block>
```

**if + else**：

```xml
<block type="controls_if">
  <mutation else="1"></mutation>
  <value name="IF0"><!-- 条件 --></value>
  <statement name="DO0"><!-- if 体 --></statement>
  <statement name="ELSE"><!-- else 体 --></statement>
</block>
```

**if + elseif + else**：

```xml
<block type="controls_if">
  <mutation elseif="2" else="1"></mutation>
  <value name="IF0"><!-- 条件1 --></value>
  <statement name="DO0"><!-- if 体 --></statement>
  <value name="IF1"><!-- 条件2 --></value>
  <statement name="DO1"><!-- elseif 体1 --></statement>
  <value name="IF2"><!-- 条件3 --></value>
  <statement name="DO2"><!-- elseif 体2 --></statement>
  <statement name="ELSE"><!-- else 体 --></statement>
</block>
```

**mutation 属性**：
- `elseif="N"` — N 个 elseif 分支（IF1..IFN, DO1..DON）
- `else="1"` — 有 else 分支

### controls_for — for 循环

```xml
<block type="controls_for">
  <field name="VAR">i</field>
  <value name="FROM">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
  <value name="TO">
    <block type="math_number"><field name="NUM">9</field></block>
  </value>
  <value name="STEP">
    <block type="math_number"><field name="NUM">1</field></block>
  </value>
  <statement name="DO">
    <!-- 循环体 -->
  </statement>
</block>
```

### controls_whileUntil — while/until 循环

```xml
<block type="controls_whileUntil">
  <field name="MODE">WHILE</field>
  <value name="BOOL">
    <!-- 条件表达式 -->
  </value>
  <statement name="DO">
    <!-- 循环体 -->
  </statement>
</block>
```

**MODE 可选值**：`WHILE`, `UNTIL`

### do_while — do-while 循环

```xml
<block type="do_while">
  <value name="select_data">
    <!-- 条件表达式 -->
  </value>
  <statement name="DO">
    <!-- 循环体 -->
  </statement>
</block>
```

### controls_delay — delay

```xml
<block type="controls_delay">
  <field name="UNIT">delay</field>
  <value name="DELAY_TIME">
    <shadow type="math_number"><field name="NUM">1000</field></shadow>
  </value>
</block>
```

**UNIT 可选值**：`delay`（毫秒）, `delayMicroseconds`（微秒）

### controls_millis — millis/micros

```xml
<block type="controls_millis">
  <field name="UNIT">millis</field>
</block>
```

输出型积木。**UNIT 可选值**：`millis`, `micros`

---

## 逻辑积木

### logic_compare — 比较运算

```xml
<block type="logic_compare">
  <field name="OP">EQ</field>
  <value name="A"><!-- 左操作数 --></value>
  <value name="B"><!-- 右操作数 --></value>
</block>
```

**OP 可选值**：`EQ` (==), `NEQ` (!=), `LT` (<), `LTE` (<=), `GT` (>), `GTE` (>=)

### logic_operation — 逻辑运算

```xml
<block type="logic_operation">
  <field name="OP">AND</field>
  <value name="A"><!-- 左 --></value>
  <value name="B"><!-- 右 --></value>
</block>
```

**OP 可选值**：`AND`, `OR`

### logic_negate — 逻辑非

```xml
<block type="logic_negate">
  <value name="BOOL"><!-- 表达式 --></value>
</block>
```

### logic_boolean — 布尔常量

```xml
<block type="logic_boolean">
  <field name="BOOL">TRUE</field>
</block>
```

**BOOL 可选值**：`TRUE`, `FALSE`

---

## 数学积木

### math_number — 数字字面量

```xml
<block type="math_number">
  <field name="NUM">42</field>
</block>
```

支持整数和浮点数。

### math_arithmetic — 四则运算

```xml
<block type="math_arithmetic">
  <field name="OP">ADD</field>
  <value name="A">
    <shadow type="math_number"><field name="NUM">1</field></shadow>
  </value>
  <value name="B">
    <shadow type="math_number"><field name="NUM">1</field></shadow>
  </value>
</block>
```

**OP 可选值**：`ADD` (+), `MINUS` (-), `MULTIPLY` (*), `DIVIDE` (/), `MODULO` (%), `POWER` (^)

### math_map — map 映射

```xml
<block type="math_map">
  <value name="NUM"><!-- 输入值 --></value>
  <value name="DMIN"><!-- 输入最小值 --></value>
  <value name="DMAX"><!-- 输入最大值 --></value>
  <value name="RMIN"><!-- 输出最小值 --></value>
  <value name="RMAX"><!-- 输出最大值 --></value>
</block>
```

### math_constrain — constrain 限制范围

```xml
<block type="math_constrain">
  <value name="VALUE"><!-- 输入值 --></value>
  <value name="LOW"><!-- 最小值 --></value>
  <value name="HIGH"><!-- 最大值 --></value>
</block>
```

---

## 文本积木

### text — 字符串字面量

```xml
<block type="text">
  <field name="TEXT">Hello</field>
</block>
```

### text_join — 字符串拼接

```xml
<block type="text_join">
  <value name="A">
    <block type="text"><field name="TEXT">Value: </field></block>
  </value>
  <value name="B">
    <block type="number_to_text">
      <value name="VAR">
        <block type="variables_get"><field name="VAR">sensorValue</field></block>
      </value>
    </block>
  </value>
</block>
```

### number_to_text — 数字转字符串

```xml
<block type="number_to_text">
  <value name="VAR">
    <block type="variables_get"><field name="VAR">myNum</field></block>
  </value>
</block>
```

---

## 串口积木

### serial_begin — Serial.begin

```xml
<block type="serial_begin">
  <field name="serial_select">Serial</field>
  <value name="CONTENT">
    <block type="math_number"><field name="NUM">9600</field></block>
  </value>
</block>
```

**serial_select 可选值**：`Serial`, `Serial1`, `Serial2`, `Serial3`

### serial_print — Serial.print / println

```xml
<block type="serial_print">
  <field name="serial_select">Serial</field>
  <field name="new_line">println</field>
  <value name="CONTENT">
    <block type="text"><field name="TEXT">Hello</field></block>
  </value>
</block>
```

**new_line 可选值**：`println`（换行）, `print`（不换行）

数字打印用 `serial_print_num`：

```xml
<block type="serial_print_num">
  <field name="serial_select">Serial</field>
  <field name="new_line">println</field>
  <value name="CONTENT">
    <block type="variables_get"><field name="VAR">sensorValue</field></block>
  </value>
</block>
```

### serial_available — Serial.available

```xml
<block type="serial_available">
  <field name="serial_select">Serial</field>
</block>
```

输出型积木（返回可读字节数）。

---

## EEPROM 积木

### store_eeprom_write_byte — EEPROM.write (单字节)

```xml
<block type="store_eeprom_write_byte">
  <value name="ADDRESS">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
  <value name="DATA">
    <block type="math_number"><field name="NUM">255</field></block>
  </value>
</block>
```

### store_eeprom_read_byte — EEPROM.read (单字节)

```xml
<block type="store_eeprom_read_byte">
  <value name="ADDRESS">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
</block>
```

输出型积木。

### store_eeprom_put — EEPROM.put (任意类型)

```xml
<block type="store_eeprom_put">
  <value name="ADDRESS">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
  <value name="DATA">
    <block type="variables_get"><field name="VAR">myValue</field></block>
  </value>
</block>
```

### store_eeprom_get — EEPROM.get (任意类型)

```xml
<block type="store_eeprom_get">
  <value name="ADDRESS">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
  <value name="DATA">
    <block type="variables_get"><field name="VAR">myValue</field></block>
  </value>
</block>
```

---

## 函数积木

### procedures_defnoreturn — 定义无返回值函数

**无参数**：

```xml
<block type="procedures_defnoreturn" x="20" y="500">
  <field name="NAME">shortBeep</field>
  <statement name="STACK">
    <!-- 函数体 -->
  </statement>
</block>
```

**有参数**：

```xml
<block type="procedures_defnoreturn" x="20" y="500">
  <mutation xmlns="http://www.w3.org/1999/xhtml">
    <arg name="duration" vartype="long"></arg>
    <arg name="pin" vartype="int"></arg>
  </mutation>
  <field name="NAME">fadeLight</field>
  <statement name="STACK">
    <!-- 函数体，可用 variables_get 获取参数 -->
  </statement>
</block>
```

**mutation arg 属性**：
- `name` — 参数名
- `vartype` — 参数类型：`int`, `long`, `float`, `boolean`, `String`

### procedures_defreturn — 定义有返回值函数

```xml
<block type="procedures_defreturn" x="20" y="500">
  <mutation xmlns="http://www.w3.org/1999/xhtml">
    <arg name="x" vartype="int"></arg>
  </mutation>
  <field name="NAME">square</field>
  <statement name="STACK">
    <!-- 函数体 -->
  </statement>
  <value name="RETURN">
    <!-- 返回值表达式 -->
  </value>
</block>
```

### procedures_callnoreturn — 调用无返回值函数

**无参数**：

```xml
<block type="procedures_callnoreturn">
  <mutation xmlns="http://www.w3.org/1999/xhtml" name="shortBeep"></mutation>
</block>
```

**有参数**：

```xml
<block type="procedures_callnoreturn" inline="true">
  <mutation xmlns="http://www.w3.org/1999/xhtml" name="fadeLight">
    <arg name="duration"></arg>
    <arg name="pin"></arg>
  </mutation>
  <value name="ARG0">
    <block type="math_number"><field name="NUM">1000</field></block>
  </value>
  <value name="ARG1">
    <block type="math_number"><field name="NUM">5</field></block>
  </value>
</block>
```

**注意**：参数值按顺序用 `ARG0`, `ARG1`, `ARG2`... 命名。

### procedures_callreturn — 调用有返回值函数

```xml
<block type="procedures_callreturn" inline="true">
  <mutation xmlns="http://www.w3.org/1999/xhtml" name="square">
    <arg name="x"></arg>
  </mutation>
  <value name="ARG0">
    <block type="math_number"><field name="NUM">5</field></block>
  </value>
</block>
```

输出型积木。

---

## DS1302 时钟库积木

需安装第三方库：`fyshi2016/Mixly_DS1302`

### DS1302_init — 初始化

```xml
<block type="DS1302_init">
  <value name="RST">
    <shadow type="pins_digital"><field name="PIN">2</field></shadow>
  </value>
  <value name="DAT">
    <shadow type="pins_digital"><field name="PIN">3</field></shadow>
  </value>
  <value name="CLK">
    <shadow type="pins_digital"><field name="PIN">4</field></shadow>
  </value>
</block>
```

### DS1302_set_date — 设置日期时间

```xml
<block type="DS1302_set_date">
  <value name="YEAR"><block type="math_number"><field name="NUM">2025</field></block></value>
  <value name="MONTH"><block type="math_number"><field name="NUM">1</field></block></value>
  <value name="DAY"><block type="math_number"><field name="NUM">15</field></block></value>
  <value name="HOUR"><block type="math_number"><field name="NUM">8</field></block></value>
  <value name="MINUTE"><block type="math_number"><field name="NUM">30</field></block></value>
  <value name="SECOND"><block type="math_number"><field name="NUM">0</field></block></value>
</block>
```

### DS1302_get_date — 获取日期字符串

```xml
<block type="DS1302_get_date"></block>
```

输出型积木，返回 "YYYY-M-D" 格式字符串。

### DS1302_get_time — 获取时间字符串

```xml
<block type="DS1302_get_time"></block>
```

输出型积木，返回 "HH:MM:SS" 格式字符串。

---

## OLED / U8g2 显示积木

内置积木，无需额外安装。

### oled_init — 初始化 OLED

```xml
<block type="oled_init">
  <value name="ADDRESS">
    <block type="math_number"><field name="NUM">60</field></block>
  </value>
</block>
```

注意：地址 `0x3C` = 十进制 `60`。

### oled_page — 页面渲染循环

```xml
<block type="oled_page">
  <statement name="DO">
    <!-- 所有绘制指令放在这里 -->
  </statement>
</block>
```

对应 U8g2 的 `firstPage()/nextPage()` 循环。

### oled_print — 打印文字

```xml
<block type="oled_print">
  <value name="POS_X">
    <block type="math_number"><field name="NUM">0</field></block>
  </value>
  <value name="POS_Y">
    <block type="math_number"><field name="NUM">16</field></block>
  </value>
  <value name="TEXT">
    <block type="text"><field name="TEXT">Hello</field></block>
  </value>
</block>
```

### oled_clear — 清屏

```xml
<block type="oled_clear"></block>
```

### oled_drawLine — 画线

```xml
<block type="oled_drawLine">
  <value name="START_X"><block type="math_number"><field name="NUM">0</field></block></value>
  <value name="START_Y"><block type="math_number"><field name="NUM">0</field></block></value>
  <value name="END_X"><block type="math_number"><field name="NUM">127</field></block></value>
  <value name="END_Y"><block type="math_number"><field name="NUM">63</field></block></value>
</block>
```

### oled_drawFrame — 画矩形框

```xml
<block type="oled_drawFrame">
  <value name="D0_X"><block type="math_number"><field name="NUM">0</field></block></value>
  <value name="D0_Y"><block type="math_number"><field name="NUM">0</field></block></value>
  <value name="WIDTH"><block type="math_number"><field name="NUM">128</field></block></value>
  <value name="HEIGHT"><block type="math_number"><field name="NUM">64</field></block></value>
</block>
```

### oled_drawCircle — 画圆

```xml
<block type="oled_drawCircle">
  <value name="D0_X"><block type="math_number"><field name="NUM">64</field></block></value>
  <value name="D0_Y"><block type="math_number"><field name="NUM">32</field></block></value>
  <value name="RADIUS"><block type="math_number"><field name="NUM">20</field></block></value>
</block>
```

### oled_drawPixel — 画像素点

```xml
<block type="oled_drawPixel">
  <value name="POS_X"><block type="math_number"><field name="NUM">64</field></block></value>
  <value name="POS_Y"><block type="math_number"><field name="NUM">32</field></block></value>
</block>
```

---

## MAKER17 OLED 扩展积木

来自 17maker 扩展库，提供更丰富的 OLED 功能。

### MAKER17_oled_init2 — 初始化

```xml
<block type="MAKER17_oled_init2">
  <field name="TYPE">SSD1306</field>
  <field name="ADDRESS">0x3C</field>
</block>
```

### MAKER17_oled_page — 页面渲染

```xml
<block type="MAKER17_oled_page">
  <statement name="DO">
    <!-- 绘制指令 -->
  </statement>
</block>
```

### MAKER17_oled_setFont — 设置字体

```xml
<block type="MAKER17_oled_setFont">
  <field name="FONT">u8g2_font_ncenB14_tr</field>
</block>
```

### MAKER17_oled_drawStr — 绘制字符串

```xml
<block type="MAKER17_oled_drawStr">
  <value name="POS_X"><block type="math_number"><field name="NUM">0</field></block></value>
  <value name="POS_Y"><block type="math_number"><field name="NUM">16</field></block></value>
  <value name="TEXT"><block type="text"><field name="TEXT">Hello</field></block></value>
</block>
```

### MAKER17_oled_print — 打印数值

```xml
<block type="MAKER17_oled_print">
  <value name="POS_X"><block type="math_number"><field name="NUM">0</field></block></value>
  <value name="POS_Y"><block type="math_number"><field name="NUM">32</field></block></value>
  <value name="TEXT">
    <block type="variables_get"><field name="VAR">temperature</field></block>
  </value>
</block>
```

---

## 代码块积木

Mixly 支持直接插入 C/C++ 代码，用于无法用积木表达的逻辑。

### inout_custom_code — 插入代码语句

语句型积木，可放在 setup/loop/函数体中，与其他积木用 `<next>` 串联。

```xml
<block type="inout_custom_code">
  <field name="CODE">TCCR1B = TCCR1B &amp; 0b11111000 | 0x01;</field>
</block>
```

**注意**：XML 中特殊字符需转义：
- `&` → `&amp;`
- `<` → `&lt;`
- `>` → `&gt;`
- `"` → `&quot;`

**多行代码**：用 `&#10;` 表示换行：

```xml
<block type="inout_custom_code">
  <field name="CODE">pinMode(A0, INPUT);&#10;pinMode(A1, INPUT);&#10;pinMode(A2, INPUT);</field>
</block>
```

**在 next 链中使用**（与普通积木混合）：

```xml
<block type="serial_begin">
  <field name="serial_select">Serial</field>
  <value name="CONTENT">
    <block type="math_number"><field name="NUM">9600</field></block>
  </value>
  <next>
    <block type="inout_custom_code">
      <field name="CODE">Wire.begin();</field>
      <next>
        <block type="inout_custom_code">
          <field name="CODE">myLib.init(0x50);</field>
        </block>
      </next>
    </block>
  </next>
</block>
```

### inout_custom_code_value — 插入代码表达式（有返回值）

输出型积木，可放在 `<value>` 内部，用于需要返回值的位置。

```xml
<block type="inout_custom_code_value">
  <field name="CODE">analogRead(A3) * 0.0048828125</field>
</block>
```

**在 value 中使用**（如赋值、条件判断）：

```xml
<block type="variables_set">
  <field name="VAR">voltage</field>
  <value name="VALUE">
    <block type="inout_custom_code_value">
      <field name="CODE">analogRead(A3) * 0.0048828125</field>
    </block>
  </value>
</block>
```

**在 if 条件中使用**：

```xml
<block type="controls_if">
  <value name="IF0">
    <block type="inout_custom_code_value">
      <field name="CODE">myLib.isReady()</field>
    </block>
  </value>
  <statement name="DO0">
    <!-- ... -->
  </statement>
</block>
```

### 代码块 + #include 头文件

代码块积木生成的代码会直接插入到 setup/loop 中。如果需要 `#include`，可以在全局区用一个代码块积木（放在 setup 的最前面，Mixly 会自动将 `#include` 提升到文件顶部）：

```xml
<block type="inout_custom_code">
  <field name="CODE">#include &lt;Wire.h&gt;&#10;#include &lt;MyLib.h&gt;</field>
</block>
```

或者更规范的方式是在 setup 最前面放置 include：

```xml
<statement name="DO">
  <block type="inout_custom_code">
    <field name="CODE">#include &lt;Wire.h&gt;</field>
    <next>
      <block type="inout_custom_code">
        <field name="CODE">Wire.begin();</field>
      </block>
    </next>
  </block>
</statement>
```

---

## <next> 链串联规则

同级语句用 `<next>` 连接，形成链式结构：

```xml
<!-- 3 个同级 block 的串联 -->
<block type="blockA">
  <!-- blockA 的内容 -->
  <next>
    <block type="blockB">
      <!-- blockB 的内容 -->
      <next>
        <block type="blockC">
          <!-- blockC 的内容 -->
        </block>
      </next>
    </block>
  </next>
</block>
```

**计数规则**：N 个同级 block = N 个 `</block>` + (N-1) 个 `</next>`

**注意**：最内层（最后一个）block 没有 `<next>`，闭合标签从内向外依次为：
```
</block>        ← blockC
</next>         ← blockB 的 next
</block>        ← blockB
</next>         ← blockA 的 next
</block>        ← blockA（如果还有外层）
```
