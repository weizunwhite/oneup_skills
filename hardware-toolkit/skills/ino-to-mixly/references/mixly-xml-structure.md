# Mixly .mix 文件 XML 结构规范

## 文件格式

.mix 文件是标准 Blockly XML。macOS 上 Mixly 也可能保存为 .xml，内容格式完全相同。

## 根元素

```xml
<xml version="Mixly 2.0 Beta11" board="Arduino AVR@Arduino Nano" xmlns="http://www.w3.org/1999/xhtml">
  <!-- 所有积木 -->
</xml>
```

### Board 字符串

| 板子 | board 值 |
|------|---------|
| Arduino Nano | `Arduino AVR@Arduino Nano` |
| Arduino Uno | `Arduino AVR@Arduino Uno` |
| Arduino Mega 2560 | `Arduino AVR@Arduino Mega2560` |
| ESP32 Dev Module | `ESP32@ESP32 Dev Module` |
| ESP32-S3 | `ESP32@ESP32-S3 Dev Module` |

## XML 核心元素

### `<block type="...">` — 积木

每个积木是一个 `<block>`。顶层积木需要 `x` 和 `y` 坐标属性。

```xml
<block type="base_setup" x="20" y="20">
  ...
</block>
```

### `<field name="...">` — 字段值

用户可编辑的值：下拉框、文本输入、数字等。

```xml
<field name="VAR">myVariable</field>
<field name="OP">EQ</field>
<field name="NUM">42</field>
```

### `<value name="...">` — 值输入

其他积木作为输入值连接的位置。内部可包含 `<block>` 或 `<shadow>`。

```xml
<value name="PIN">
  <shadow type="pins_digital"><field name="PIN">13</field></shadow>
</value>
```

### `<shadow type="...">` — 默认值积木

放在 `<value>` 内部，提供默认值。当用户拖入其他积木时会被覆盖。

```xml
<value name="DELAY_TIME">
  <shadow type="math_number"><field name="NUM">1000</field></shadow>
</value>
```

### `<statement name="...">` — 语句输入

语句类型的输入位置（如循环体、函数体）。

```xml
<statement name="DO">
  <block type="...">...</block>
</statement>
```

### `<next>` — 顺序连接

将同级积木串联成序列。

```xml
<block type="A">
  ...
  <next>
    <block type="B">
      ...
    </block>
  </next>
</block>
```

### `<mutation>` — 变异属性

控制积木的动态配置（如 if 的分支数、函数的参数列表）。

**controls_if 的 mutation**：
```xml
<mutation elseif="2" else="1"></mutation>
```

**procedures 的 mutation**（注意 xmlns）：
```xml
<mutation xmlns="http://www.w3.org/1999/xhtml">
  <arg name="param1" vartype="int"></arg>
  <arg name="param2" vartype="String"></arg>
</mutation>
```

## 嵌套规则

### `<next>` 串联同级语句

```
block A
  ├── (A 自身的 field/value/statement)
  └── <next>
        └── block B
              ├── (B 自身内容)
              └── <next>
                    └── block C
                          └── (C 自身内容，无 next = 链结束)
```

**闭合计数**：N 个同级 block = N 个 `</block>` + (N-1) 个 `</next>`

### `<value>` 嵌入值

```
block (主积木)
  └── <value name="A">
        └── block (值积木，输出型)
```

### `<statement>` 嵌入语句体

```
block (控制积木，如 if/for/while)
  └── <statement name="DO">
        └── block (第一条语句)
              └── <next>
                    └── block (第二条语句)
                          └── ...
```

### 变量声明链（洋葱结构）

变量声明用 `<next>` 串联，形成从外到内的嵌套：

```xml
<block type="variables_declare" x="20" y="20">   ← 第1个变量（最外层）
  <field name="VAR">var1</field>
  <field name="TYPE">int</field>
  <value name="VALUE">...</value>
  <next>
    <block type="variables_declare">              ← 第2个变量
      <field name="VAR">var2</field>
      <field name="TYPE">boolean</field>
      <value name="VALUE">...</value>
      <next>
        <block type="variables_declare">          ← 第3个变量（最内层）
          <field name="VAR">var3</field>
          <field name="TYPE">String</field>
          <value name="VALUE">...</value>
        </block>                                  ← 关闭 var3
      </next>                                     ← 关闭 var2 的 next
    </block>                                      ← 关闭 var2
  </next>                                         ← 关闭 var1 的 next
</block>                                          ← 关闭 var1
```

## XML 闭合防错清单

### 必须检查项

1. **block 配对**：每个 `<block>` 必须有对应 `</block>`
2. **next 配对**：每个 `<next>` 必须有对应 `</next>`，且内部恰好一个 `<block>...</block>`
3. **next 计数**：N 个同级 block = N 个 `</block>` + (N-1) 个 `</next>`
4. **statement 配对**：每个 `<statement>` 必须有对应 `</statement>`
5. **value 配对**：每个 `<value>` 必须有对应 `</value>`
6. **shadow 位置**：`<shadow>` 只能出现在 `<value>` 内部
7. **mutation 闭合**：自闭合 `<mutation ... />` 或配对 `<mutation>...</mutation>`
8. **field 内容**：`<field>` 不能为空标签，至少有文本内容
9. **xml 根标签**：正确闭合 `</xml>`

### 常见错误模式（来自实际调试经验）

#### 错误1：next 链多一个闭合对

**症状**：`Opening and ending tag mismatch: statement line X and next`

**原因**：N 个同级 block 却有 N 个 `</next></block>` 对（应该是 N-1 个 `</next>`）

**修复**：数清楚链中的 block 数量，最后一个 block 不需要被 `</next>` 包裹

#### 错误2：深层嵌套中 block 和 statement 混淆

**症状**：`Opening and ending tag mismatch: block line X and statement`

**原因**：在深层嵌套中，`</block>` 和 `</statement>` 的顺序搞反了

**修复**：从最内层开始向外检查闭合顺序

#### 错误3：mutation xmlns 缺失

**症状**：Mixly 打开文件后函数参数丢失

**原因**：`procedures_defnoreturn` 和 `procedures_callnoreturn` 的 mutation 缺少 `xmlns="http://www.w3.org/1999/xhtml"`

**修复**：始终在 procedures 相关的 mutation 中加上 xmlns

### 验证方法

```bash
# 方法1：xmllint 快速验证
xmllint --noout output.mix

# 方法2：Python 定位错误行号
python3 -c "import xml.etree.ElementTree as ET; ET.parse('output.mix')"

# 方法3：统计标签配对
grep -c '<block' output.mix    # 开标签数
grep -c '</block>' output.mix  # 闭标签数（应相等）
grep -c '<next>' output.mix    # next 开标签
grep -c '</next>' output.mix   # next 闭标签（应相等）
```

## 坐标分配建议

让积木在 Mixly 画布上整齐排列：

| 积木类型 | x | y |
|----------|---|---|
| 变量声明链 | 20 | 20 |
| base_setup | 20 | 变量链结束后 +200 |
| 第1个函数定义 | 20 | base_setup 后 +300 |
| 第2个函数定义 | 20 | 上一个函数后 +300 |
| ... | 20 | 递增 +300 |
