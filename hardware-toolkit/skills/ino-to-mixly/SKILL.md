---
name: ino-to-mixly
description: >
  Convert Arduino .ino firmware to Mixly 2.0 .mix files (Blockly XML).
  Supports Arduino AVR (Nano/Uno/Mega) and ESP32. Reads .ino source code,
  maps C++ constructs to Mixly visual blocks, generates valid XML, and
  validates with xmllint. Trigger on: mixly, 米思齐, .mix, ino转mixly,
  转Mixly, Mixly转换.
---

# ino-to-mixly: Arduino .ino → Mixly .mix 转换

将 Arduino .ino 固件源码转换为 Mixly 2.0 可打开的 .mix 文件（Blockly XML 格式）。

## 触发条件

用户提到以下关键词时激活：mixly、米思齐、.mix、ino转mixly、转Mixly、Mixly转换。

## 输入

- **必须**：.ino 文件路径
- **可选**：目标板型号（默认自动检测）

### 目标板自动检测

按优先级检测：
1. 用户明确指定 → 直接使用
2. 代码中包含 `ESP32` / `WiFi.h` / `esp_` 前缀 → ESP32
3. 代码中包含 `Arduino.h` / 标准 AVR 引脚 → Arduino AVR
4. 同目录下有 `platformio.ini` → 读取 board 配置
5. 默认 → Arduino AVR (Arduino Nano)

### Board 字符串映射

| 板子 | board 属性值 |
|------|-------------|
| Arduino Nano | `Arduino AVR@Arduino Nano` |
| Arduino Uno | `Arduino AVR@Arduino Uno` |
| Arduino Mega | `Arduino AVR@Arduino Mega2560` |
| ESP32 | `ESP32@ESP32 Dev Module` |

## 转换工作流

### Step 1: 分析代码结构

读取 .ino 文件，识别并分类：

| 代码区域 | 提取内容 |
|----------|---------|
| 全局区 | `#include`、`#define`、全局变量、enum、struct |
| `setup()` | 引脚模式、串口初始化、库初始化 |
| `loop()` | 主循环逻辑、条件分支、函数调用 |
| 自定义函数 | 函数名、参数、函数体 |

**复杂度评估与转换策略自动选择**：

| 复杂度 | 判定条件 | 转换策略 |
|--------|---------|---------|
| **简单** | < 80 行，无 struct/enum | 直接 1:1 全量转换 |
| **中等** | 80-300 行，有简单 struct 或 enum | 展开 struct/enum，拆分函数，生成单个 .mix |
| **大型** | 300-600 行，多函数、多状态 | 骨架+代码块模式（见下方） |
| **超大型** | > 600 行，复杂架构 | 模块拆分模式（见下方） |

#### 大型项目：骨架+代码块模式

整体结构用积木表达，复杂内部逻辑用 `inout_custom_code` 嵌入：

1. **setup/loop 框架** → 用积木（`base_setup`、函数调用）
2. **函数定义** → 每个函数用 `procedures_defnoreturn` 积木
3. **函数内部**：
   - 简单逻辑（pinMode、digitalWrite、delay、if/else）→ 用积木
   - 复杂逻辑（算法、状态机细节、字符串处理）→ 用 `inout_custom_code` 嵌入
4. **变量声明** → 关键变量用积木声明，辅助变量放代码块

**优点**：学生在 Mixly 中能看到程序的整体结构和函数调用关系，同时保留了完整功能。

#### 超大型项目：模块拆分模式

将代码按功能模块拆成多个独立 .mix 文件：

1. **分析代码**，识别功能模块（如：传感器、显示、通信、控制逻辑）
2. **每个模块**生成独立 .mix 文件，只包含该模块相关的变量、函数和演示用的 setup/loop
3. **主程序**生成一个骨架 .mix，用函数调用 + 代码块展示整体流程
4. **输出文件命名**：`{项目名}_主程序.mix`、`{项目名}_传感器模块.mix`、`{项目名}_显示模块.mix` 等

**拆分原则**：
- 每个 .mix 文件的积木 XML 控制在 **2000 行以内**
- 每个 .mix 文件的变量声明不超过 **20 个**
- 每个 .mix 文件的函数定义不超过 **5 个**
- 模块间的数据依赖用全局变量 + 注释说明

**输出时额外生成**：`{项目名}_模块说明.txt`，列出各 .mix 文件的内容和对应关系。

### Step 2: 规划积木结构

在生成 XML 之前，先列出文字版积木清单：

```
[变量声明] int sensorValue = 0
[变量声明] boolean isActive = false
[setup] pinMode(5, INPUT_PULLUP)
[setup] Serial.begin(9600)
[loop] 读取传感器 → 判断 → 执行动作
[函数] shortBeep: digitalWrite + delay
```

**关键原则**：
- 每个 `procedures_defnoreturn` 函数体控制在 **5 层嵌套以内**
- 超过 5 层 → 拆分为子函数
- `<next>` 链不超过 **10 个同级 block**，超过则分组到函数

### Step 3: 生成 XML

参考 `references/mixly-block-reference.md` 中的精确 XML 语法，逐块生成。

**XML 生成顺序**：
1. `<xml>` 根元素（含 version、board、xmlns）
2. `<variables>` 声明区
3. 全局变量 `variables_declare` 块（用 `<next>` 串联）
4. `base_setup` 块（含 setup 语句）
5. 自定义函数 `procedures_defnoreturn` 块
6. `</xml>` 关闭

**坐标分配**（让积木在画布上整齐排列）：
- 变量声明链：`x="20" y="20"`
- base_setup：`x="20" y="300"`（或变量链结束后 +200）
- 每个自定义函数：`x="20" y+=300`

### Step 4: XML 闭合验证

生成后**必须**运行验证：

```bash
xmllint --noout output.mix
```

如果报错：
1. 用 `python3 -c "import xml.etree.ElementTree as ET; ET.parse('output.mix')"` 定位行号
2. 检查 `<next>` / `</next>` 配对数量（N 个同级 block = N 个 `</block>` + N-1 个 `</next>`）
3. 检查 `<statement>` / `</statement>` 配对
4. 修复后重新验证，直到通过

### Step 5: 输出

- 保存 .mix 文件到 .ino 同目录，文件名为 `{原文件名}.mix`
- 如果在项目工作流中，保存到 `输出/` 目录
- 报告转换结果：积木数量、函数数量、是否有降级处理

## 核心转换规则

### C++ → 积木映射

| C++ 构造 | Mixly 积木 | 备注 |
|----------|-----------|------|
| `int x = 0;` | `variables_declare` (TYPE=int) | 全局变量 |
| `x = 5;` | `variables_set` | |
| `x` (读取) | `variables_get` | |
| `enum State {A, B, C}` | `int` 变量 + 注释 | enum 值映射为 0, 1, 2... |
| `struct Button {bool last; bool now;}` | 多个变量，前缀命名 | `btnA_last`, `btnA_now` |
| `switch(x) { case 1: ... }` | `controls_if` + elseif 链 | mutation elseif="N" |
| `for(int i=0; i<10; i++)` | `controls_for` | |
| `while(condition)` | `controls_whileUntil` (WHILE) | |
| `sprintf(buf, "%d:%02d", h, m)` | `text_join` 嵌套 | 用 `number_to_text` 转换数字 |
| `#define LED_PIN 13` | 直接内联数值 | 不保留宏名 |
| `void myFunc()` | `procedures_defnoreturn` | |
| `myFunc()` | `procedures_callnoreturn` | |
| `void myFunc(int x)` | `procedures_defnoreturn` + mutation arg | |
| `myFunc(5)` | `procedures_callnoreturn` + value ARG0 | |
| `delay(1000)` | `controls_delay` (UNIT=delay) | |
| `millis()` | `controls_millis` (UNIT=millis) | |
| `pinMode(5, INPUT)` | `inout_pinMode` | |
| `digitalRead(5)` | `inout_digital_read2` | |
| `digitalWrite(5, HIGH)` | `inout_digital_write2` | |
| `analogRead(A0)` | `inout_analog_read` | |
| `analogWrite(3, 128)` | `inout_analog_write` | |
| `Serial.begin(9600)` | `serial_begin` | |
| `Serial.println(x)` | `serial_print` (new_line=println) | |

### 代码块兜底策略

当 C++ 代码无法用积木表达时，使用 Mixly 的代码块积木直接嵌入原始代码：

| 积木类型 | 用途 | 放置位置 |
|----------|------|---------|
| `inout_custom_code` | 插入语句（无返回值） | setup/loop/函数体中，用 `<next>` 串联 |
| `inout_custom_code_value` | 插入表达式（有返回值） | `<value>` 内部（赋值、条件判断等） |

**转换优先级**（从高到低）：
1. **有对应积木** → 用积木（最佳，学生能看懂）
2. **可以简单改写后用积木** → 改写（如 enum→int、struct→变量组）
3. **无对应积木但代码简单** → 用 `inout_custom_code` 嵌入（保留功能完整性）
4. **整段复杂逻辑无法转换** → 整段放入 `inout_custom_code`，加注释说明

**典型使用场景**：
- 位运算：`TCCR1B = TCCR1B & 0b11111000 | 0x01;`
- 无积木的库调用：`Wire.begin();`、`myLib.init(0x50);`
- 寄存器操作：`PORTB |= (1 << PB5);`
- 复杂表达式：`analogRead(A3) * 0.0048828125`（用 `inout_custom_code_value`）
- `#include` 头文件：放在 setup 最前面，Mixly 会自动提升到文件顶部

**XML 注意事项**：`<field name="CODE">` 中的特殊字符必须转义：
- `&` → `&amp;`、`<` → `&lt;`、`>` → `&gt;`、`"` → `&quot;`
- 换行用 `&#10;`

### 不可直接转换的特性

优先使用代码块积木（`inout_custom_code` / `inout_custom_code_value`）保留原始功能，仅在必要时才简化：

| C++ 特性 | 处理方式 |
|----------|---------|
| 指针 / 引用参数 | 改用全局变量传值 |
| 类 / 继承 | 展开为函数 + 全局变量 |
| 模板 | 为具体类型生成对应积木 |
| 位运算 (`<<`, `>>`, `&`, `|`) | 用 `inout_custom_code` 原样嵌入 |
| 三目运算符 `? :` | 展开为 `controls_if`，或用 `inout_custom_code_value` |
| 数组（有限支持） | 简单数组用 `lists` 积木，复杂操作用代码块 |
| 无积木的库调用 | 用 `inout_custom_code` 嵌入，`#include` 放 setup 开头 |
| 寄存器操作 | 用 `inout_custom_code` 原样嵌入 |
| 复杂数学表达式 | 用 `inout_custom_code_value` 嵌入 |

## 第三方库积木映射

### DS1302 时钟模块
需安装：`fyshi2016/Mixly_DS1302`

| Arduino 代码 | Mixly Block |
|-------------|-------------|
| `Ds1302 rtc(RST, DAT, CLK)` | `DS1302_init` |
| `rtc.getDateStr()` | `DS1302_get_date` |
| `rtc.getTimeStr()` | `DS1302_get_time` |
| `rtc.setDate(...)` | `DS1302_set_date` |

### OLED 显示 (U8g2)
内置积木，无需额外安装。

| Arduino 代码 | Mixly Block |
|-------------|-------------|
| `u8g2.begin()` | `oled_init` (ADDRESS=0x3C) |
| `u8g2.firstPage() / nextPage()` | `oled_page` + statement DO |
| `u8g2.drawStr(x, y, text)` | `oled_print` |
| `u8g2.clearBuffer()` | `oled_clear` |
| `u8g2.drawLine(...)` | `oled_drawLine` |
| `u8g2.drawCircle(...)` | `oled_drawCircle` |
| `u8g2.drawFrame(...)` | `oled_drawFrame` |

### DHT11 温湿度传感器
需安装对应 Mixly 库。

| Arduino 代码 | Mixly Block |
|-------------|-------------|
| `dht.readTemperature()` | `dht_readTemperature` |
| `dht.readHumidity()` | `dht_readHumidity` |

## 平台差异：AVR vs ESP32

| 特性 | AVR | ESP32 |
|------|-----|-------|
| board 属性 | `Arduino AVR@Arduino Nano` | `ESP32@ESP32 Dev Module` |
| 数字引脚 shadow | `pins_digital` (2-13) | `pins_digital` (0-39) |
| 模拟引脚 shadow | `pins_analog` (A0-A7) | `pins_analog` (0, 2, 4, 12-15, 25-27, 32-39) |
| PWM shadow | `pins_pwm` (3,5,6,9,10,11) | `pins_pwm` (所有数字引脚) |
| EEPROM | 内置 `store_eeprom_*` | 使用 Preferences 库（不同积木） |
| WiFi | 无 | `wifi_*` 系列积木 |
| 蓝牙 | 无 | `bluetooth_*` 系列积木 |

## 函数拆分策略

当函数体嵌套过深时，按以下策略拆分：

1. **识别可独立的逻辑块**：如按钮检测、显示更新、传感器读取
2. **每个逻辑块提取为 `procedures_defnoreturn`**
3. **原位替换为 `procedures_callnoreturn`**
4. **参数传递**：
   - 优先用全局变量（Mixly 对函数参数支持有限）
   - 简单参数可用 mutation arg（但不超过 3 个）

**拆分阈值**：
- `<next>` 链超过 10 个 block → 拆分
- `<statement>` 嵌套超过 5 层 → 拆分
- `controls_if` 有超过 4 个 elseif → 考虑拆分条件判断函数

## XML 闭合防错清单

生成 XML 时逐项检查：

- [ ] 每个 `<block>` 有对应 `</block>`
- [ ] 每个 `<next>` 有对应 `</next>`，且 `<next>` 内恰好包含一个 `<block>...</block>`
- [ ] N 个同级 block（用 `<next>` 串联）= N 个 `</block>` + (N-1) 个 `</next>`
- [ ] 每个 `<statement>` 有对应 `</statement>`
- [ ] 每个 `<value>` 有对应 `</value>`
- [ ] `<shadow>` 块必须在 `<value>` 内部
- [ ] `<mutation>` 是自闭合标签（`<mutation ... />`）或有 `</mutation>`
- [ ] `<field>` 标签内容不为空（至少有文本节点）
- [ ] 根 `<xml>` 标签正确关闭
- [ ] 变量声明链：最外层 block 在最前面，最内层在最后面（洋葱结构）

## 输出示例

转换一个简单的 LED 闪烁程序：

**输入** (`blink.ino`):
```cpp
#define LED_PIN 13

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(1000);
  digitalWrite(LED_PIN, LOW);
  delay(1000);
}
```

**输出** (`blink.mix`):
```xml
<xml version="Mixly 2.0 Beta11" board="Arduino AVR@Arduino Nano" xmlns="http://www.w3.org/1999/xhtml">
  <block type="base_setup" x="20" y="20">
    <statement name="DO">
      <block type="inout_pinMode">
        <field name="MODE">OUTPUT</field>
        <value name="PIN">
          <shadow type="pins_digital"><field name="PIN">13</field></shadow>
        </value>
      </block>
    </statement>
    <statement name="DO2">
      <block type="inout_digital_write2">
        <value name="PIN">
          <shadow type="pins_digital"><field name="PIN">13</field></shadow>
        </value>
        <value name="STAT">
          <shadow type="inout_highlow"><field name="BOOL">HIGH</field></shadow>
        </value>
        <next>
          <block type="controls_delay">
            <field name="UNIT">delay</field>
            <value name="DELAY_TIME">
              <shadow type="math_number"><field name="NUM">1000</field></shadow>
            </value>
            <next>
              <block type="inout_digital_write2">
                <value name="PIN">
                  <shadow type="pins_digital"><field name="PIN">13</field></shadow>
                </value>
                <value name="STAT">
                  <shadow type="inout_highlow"><field name="BOOL">LOW</field></shadow>
                </value>
                <next>
                  <block type="controls_delay">
                    <field name="UNIT">delay</field>
                    <value name="DELAY_TIME">
                      <shadow type="math_number"><field name="NUM">1000</field></shadow>
                    </value>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </statement>
  </block>
</xml>
```
