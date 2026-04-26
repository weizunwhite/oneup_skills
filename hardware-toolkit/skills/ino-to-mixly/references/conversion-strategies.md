# C++ → Mixly 积木转换策略

## 项目复杂度判定

| 复杂度 | 代码行数 | 特征 | 转换策略 |
|--------|---------|------|---------|
| **简单** | < 80 行 | 无 struct/enum，≤ 2 个自定义函数 | 1:1 全量积木转换 |
| **中等** | 80-300 行 | 有简单 struct 或 enum，3-5 个函数 | 展开 struct/enum，拆分函数，单个 .mix |
| **大型** | 300-600 行 | 多函数、多状态、有库调用 | 骨架+代码块模式 |
| **超大型** | > 600 行 | 复杂架构、多模块、多库 | 模块拆分为多个 .mix |

### 大型项目：骨架+代码块模式

目标：让学生在 Mixly 中看到程序整体结构，同时保留完整功能。

**转换规则**：
- setup/loop 框架 → 积木（`base_setup` + 函数调用链）
- 每个函数 → `procedures_defnoreturn` 积木
- 函数内部简单逻辑（I/O、delay、简单 if）→ 积木
- 函数内部复杂逻辑（算法、状态机、字符串处理）→ `inout_custom_code`
- 关键变量 → 积木声明；辅助变量 → 放代码块里

**判断"简单"vs"复杂"**：
- 能用 1-2 个积木表达的 → 用积木
- 需要 5+ 层嵌套或 10+ 个积木才能表达的 → 用代码块

### 超大型项目：模块拆分模式

目标：按功能模块生成多个独立 .mix 文件，每个文件可单独在 Mixly 中打开。

**拆分流程**：

1. 分析代码，识别功能模块（传感器、显示、通信、控制等）
2. 每个模块生成独立 .mix，包含：
   - 该模块的变量声明
   - 该模块的函数定义
   - 演示用的 setup/loop（只调用该模块的函数）
3. 主程序生成骨架 .mix，用函数调用 + 代码块展示整体流程
4. 额外输出 `{项目名}_模块说明.txt`

**每个 .mix 文件的限制**：
- 积木 XML ≤ 2000 行
- 变量声明 ≤ 20 个
- 函数定义 ≤ 5 个

**文件命名**：
- `{项目名}_主程序.mix`
- `{项目名}_{模块名}.mix`（如 `_传感器模块.mix`、`_显示模块.mix`）

## C++ 构造映射规则

### 变量与类型

| C++ | Mixly | 备注 |
|-----|-------|------|
| `int x = 0;` | `variables_declare` TYPE=int, VALUE=math_number(0) | |
| `long x = 0;` | `variables_declare` TYPE=long | |
| `float x = 0.0;` | `variables_declare` TYPE=float | |
| `bool x = false;` | `variables_declare` TYPE=boolean, VALUE=logic_boolean(FALSE) | |
| `byte x = 0;` | `variables_declare` TYPE=byte | |
| `char x = 'A';` | `variables_declare` TYPE=char | |
| `String x = "";` | `variables_declare` TYPE=String, VALUE=text("") | |
| `const int X = 5;` | 直接内联数值，不声明变量 | |
| `#define X 5` | 直接内联数值 | |
| `unsigned long` | 用 `long` 替代 | Mixly 无 unsigned |

### enum → int 变量

```cpp
// C++
enum State { IDLE, RUNNING, ALARM };
State currentState = IDLE;
```

转换为：
```
变量声明：int currentState = 0
// IDLE=0, RUNNING=1, ALARM=2
// 在 if 判断中用数字代替 enum 值
```

### struct → 前缀命名变量组

```cpp
// C++
struct Button {
  int pin;
  bool lastState;
  bool currentState;
  unsigned long lastDebounce;
};
Button btnA = {5, HIGH, HIGH, 0};
Button btnB = {6, HIGH, HIGH, 0};
```

转换为：
```
变量声明：
  int btnA_pin = 5
  boolean btnA_last = true    (HIGH=true)
  boolean btnA_now = true
  long btnA_debounce = 0
  int btnB_pin = 6
  boolean btnB_last = true
  boolean btnB_now = true
  long btnB_debounce = 0
```

**命名规则**：`{实例名}_{字段名}`

### 控制流

| C++ | Mixly | 备注 |
|-----|-------|------|
| `if (a) {...}` | `controls_if` | |
| `if (a) {...} else {...}` | `controls_if` + mutation else="1" | |
| `if (a) {...} else if (b) {...}` | `controls_if` + mutation elseif="1" | |
| `switch(x) { case 1: ... }` | `controls_if` + elseif 链 | 每个 case 变成一个 elseif |
| `for (int i=0; i<10; i++)` | `controls_for` FROM=0 TO=9 STEP=1 | 注意 TO 是含端点 |
| `while (condition)` | `controls_whileUntil` MODE=WHILE | |
| `do {...} while(cond)` | `do_while` | |
| `a ? b : c` | 展开为 if/else 赋值 | 用临时变量存结果 |

### switch-case → if-elseif

```cpp
// C++
switch(state) {
  case 0: doA(); break;
  case 1: doB(); break;
  case 2: doC(); break;
  default: doD(); break;
}
```

转换为：
```xml
<block type="controls_if">
  <mutation elseif="2" else="1"></mutation>
  <value name="IF0">  <!-- state == 0 -->
    <block type="logic_compare">
      <field name="OP">EQ</field>
      <value name="A"><block type="variables_get"><field name="VAR">state</field></block></value>
      <value name="B"><block type="math_number"><field name="NUM">0</field></block></value>
    </block>
  </value>
  <statement name="DO0"><!-- doA --></statement>
  <value name="IF1"><!-- state == 1 --></value>
  <statement name="DO1"><!-- doB --></statement>
  <value name="IF2"><!-- state == 2 --></value>
  <statement name="DO2"><!-- doC --></statement>
  <statement name="ELSE"><!-- doD --></statement>
</block>
```

### 函数

| C++ | Mixly | 备注 |
|-----|-------|------|
| `void func() {...}` | `procedures_defnoreturn` NAME=func | |
| `func()` | `procedures_callnoreturn` name=func | |
| `void func(int x) {...}` | `procedures_defnoreturn` + mutation arg(x, int) | |
| `func(5)` | `procedures_callnoreturn` + ARG0=5 | |
| `int func() { return x; }` | `procedures_defreturn` + RETURN value | |
| `int y = func()` | `variables_set` VAR=y, VALUE=procedures_callreturn | |

**参数限制**：建议不超过 3 个参数。超过时考虑用全局变量替代部分参数。

### 字符串操作

| C++ | Mixly | 备注 |
|-----|-------|------|
| `"hello"` | `text` TEXT="hello" | |
| `String a + String b` | `text_join` A=a, B=b | |
| `String(number)` | `number_to_text` | |
| `sprintf(buf, "%d:%02d", h, m)` | 嵌套 `text_join` | 见下方示例 |

**sprintf 转换示例**：

```cpp
sprintf(buf, "%d:%02d", hours, minutes);
```

转换为嵌套的 text_join：
```
text_join(
  A: number_to_text(hours),
  B: text_join(
    A: text(":"),
    B: number_to_text(minutes)
  )
)
```

注意：Mixly 无法实现 `%02d`（补零格式），需要额外的 if 判断来手动补零，或接受不补零。

## 函数拆分策略

### 何时拆分

- `<next>` 链超过 **10 个** 同级 block
- `<statement>` 嵌套超过 **5 层**
- `controls_if` 有超过 **4 个** elseif 分支
- 一个功能逻辑块可以被命名为一个独立动作

### 如何拆分

1. **识别逻辑边界**：按功能划分——传感器读取、显示更新、按钮检测、蜂鸣器控制等
2. **提取为函数**：每个逻辑块变成一个 `procedures_defnoreturn`
3. **原位替换为调用**：在 setup/loop 中用 `procedures_callnoreturn` 代替
4. **共享数据**：通过全局变量传递（Mixly 的惯用方式）

### 拆分示例

**拆分前**（loop 中 15 个连续操作）：
```
loop:
  读取按钮A → 消抖 → 判断 → 切换状态
  读取按钮B → 消抖 → 判断 → 调整值
  读取传感器 → 计算
  更新显示 → 画文字 → 画图形
  检查闹钟 → 响铃
```

**拆分后**：
```
函数 checkBtnA: 读取按钮A → 消抖 → 判断 → 切换状态
函数 checkBtnB: 读取按钮B → 消抖 → 判断 → 调整值
函数 readSensor: 读取传感器 → 计算
函数 updateDisplay: 更新显示 → 画文字 → 画图形
函数 checkAlarm: 检查闹钟 → 响铃

loop:
  调用 checkBtnA
  调用 checkBtnB
  调用 readSensor
  调用 updateDisplay
  调用 checkAlarm
```

## 变量命名规范

| 场景 | 命名规则 | 示例 |
|------|---------|------|
| 普通全局变量 | 驼峰命名 | `sensorValue`, `isActive` |
| struct 展开 | `{实例名}_{字段名}` | `btnA_pin`, `alarm_hour` |
| enum 替代 | 原 enum 变量名，值用数字 | `currentState` (0=IDLE, 1=RUN) |
| 循环变量 | 单字母 | `i`, `j` |
| 临时变量 | `temp` 前缀 | `tempValue`, `tempStr` |

## 代码块兜底策略

Mixly 支持 `inout_custom_code`（语句）和 `inout_custom_code_value`（表达式）积木，可以直接嵌入 C/C++ 代码。这是处理"无对应积木"情况的最佳方案。

### 转换优先级

1. **有对应积木** → 用积木（学生能看懂，首选）
2. **可改写后用积木** → 改写（如 enum→int、struct→变量组）
3. **无对应积木** → 用代码块嵌入原始代码（保留完整功能）
4. **整段无法转换** → 整段放入代码块 + 注释

### 代码块使用场景

| 场景 | 用哪个积木 | 示例 |
|------|-----------|------|
| 无积木的库初始化 | `inout_custom_code` | `Wire.begin();` |
| 无积木的库调用 | `inout_custom_code` | `myLib.setMode(3);` |
| `#include` 头文件 | `inout_custom_code` | `#include <Wire.h>` (放 setup 开头) |
| 位运算 / 寄存器 | `inout_custom_code` | `TCCR1B = TCCR1B & 0xF8 \| 0x01;` |
| 复杂数学表达式 | `inout_custom_code_value` | `analogRead(A3) * 0.0048828125` |
| 无积木的库返回值 | `inout_custom_code_value` | `myLib.isReady()` |
| 三目运算符 | `inout_custom_code_value` | `(x > 10) ? 255 : 0` |

### XML 转义规则

`<field name="CODE">` 中的特殊字符必须转义：

| 字符 | 转义 |
|------|------|
| `&` | `&amp;` |
| `<` | `&lt;` |
| `>` | `&gt;` |
| `"` | `&quot;` |
| 换行 | `&#10;` |

### 积木与代码块混合示例

积木和代码块可以自由混合在 `<next>` 链中：

```xml
<!-- 积木: Serial.begin(9600) -->
<block type="serial_begin">
  <field name="serial_select">Serial</field>
  <value name="CONTENT">
    <block type="math_number"><field name="NUM">9600</field></block>
  </value>
  <next>
    <!-- 代码块: Wire.begin() — 无对应积木 -->
    <block type="inout_custom_code">
      <field name="CODE">Wire.begin();</field>
      <next>
        <!-- 积木: pinMode -->
        <block type="inout_pinMode">
          <field name="MODE">OUTPUT</field>
          <value name="PIN">
            <shadow type="pins_digital"><field name="PIN">13</field></shadow>
          </value>
        </block>
      </next>
    </block>
  </next>
</block>
```

## 不可转换特性处理

优先使用代码块积木保留原始功能，仅在必要时才做结构性改写：

| C++ 特性 | 处理方式 |
|----------|---------|
| **指针 / 引用参数** | 改用全局变量传值 |
| **类 / 继承** | 展开为函数 + 全局变量 |
| **模板** | 为实际使用的具体类型生成积木 |
| **位运算** (`<<`, `>>`, `&`, `\|`) | 用 `inout_custom_code` 原样嵌入 |
| **三目运算符** `? :` | 用 `inout_custom_code_value` 嵌入，或展开为 if/else |
| **数组** | 简单数组用 `lists` 积木；复杂操作用 `inout_custom_code` |
| **多文件** (.h/.cpp) | 合并为单文件逻辑再转换 |
| **volatile** | 忽略，直接作为普通变量 |
| **中断** (ISR) | Mixly 有 `attachInterrupt` 积木，可直接映射 |
| **PROGMEM** | 忽略，数据放普通变量 |
| **无积木的库** | 用 `inout_custom_code` 嵌入调用，`#include` 放 setup 开头 |
| **寄存器操作** | 用 `inout_custom_code` 原样嵌入 |
| **复杂表达式** | 用 `inout_custom_code_value` 嵌入 |

## 第三方库积木对照

### 常用库 → Mixly 积木

| Arduino 库 | Mixly 积木前缀 | 需要安装 |
|-----------|---------------|---------|
| DS1302 | `DS1302_*` | fyshi2016/Mixly_DS1302 |
| U8g2 (OLED) | `oled_*` | 内置 |
| DHT | `dht_*` | 内置 |
| Servo | `servo_*` | 内置 |
| IRremote | `ir_*` | 内置 |
| Ultrasonic (HC-SR04) | `ultrasonic_*` | 内置 |
| Stepper | `stepper_*` | 内置 |
| Tone | `tone_*` | 内置 |
| NeoPixel (WS2812) | `neopixel_*` | 需安装 |

### 无对应积木的库

如果 .ino 使用了 Mixly 没有对应积木的库：

1. 用 `inout_custom_code` 嵌入库调用代码（`#include` 放 setup 开头）
2. 用 `inout_custom_code_value` 嵌入有返回值的库调用
3. 在转换报告中标注"以代码块方式嵌入的库调用"
4. 建议用户在 Mixly 中安装对应扩展库后，可手动替换为积木
