---
name: hardware-arduino-project
description: 生成 Arduino IDE 项目脚手架（扁平目录结构，.ino + 引脚/模块驱动头文件）。所有传感器/执行器按集成模块对待，不处理裸元器件。触发于"Arduino 项目""arduino 脚手架""新建 Arduino 工程""Nano 项目""UNO 项目"等关键词。
---

## 重要前提：模块级开发

本技能体系中所有传感器、通信模块、显示模块、执行器均为**集成模块**（非裸元器件）。
模块内部已集成必要的电阻、电容、稳压、电平转换等电路。

接线说明一律基于模块排针（VCC/GND/DATA/SCL/SDA等），不涉及裸芯片引脚。
不要在生成的代码注释或接线说明中提示"需外接上拉电阻""需分压电路"等，除非 sensor-catalog.json 的 notes 中明确标注（如HC-SR04的Echo引脚保护）。

## 参考资料优先原则

在生成任何模块的驱动代码之前，**必须先检查** `references/` 目录下是否存在该模块的参考资料：

```
~/.claude/skills/hardware-common/references/{模块名}/
```

如果存在，按以下优先级使用：
1. **notes.md** — 开发者的实战笔记和踩坑记录，最高优先级，必须遵守其中的建议
2. **官方例程**（.ino / .cpp） — 已验证可用的代码，生成新代码时优先参考其初始化流程和调用方式
3. **数据手册**（.pdf） — 补充 sensor-catalog.json 中没有的细节

如果 references/ 下没有对应模块的资料，则按 sensor-catalog.json 的信息正常生成。
如果 notes.md 中的信息与 sensor-catalog.json 冲突，以 notes.md 为准（因为是实际验证过的）。

## Skills 自检与纠错机制

**Skills 文件（包括本 SKILL.md、sensor-catalog.json、board-profiles.json）可能存在错误。**
不要盲目信任，遵守以下规则：

### 优先级（从高到低）
1. **用户当前对话中的明确指示** — 最高优先级，永远覆盖 Skills 内容
2. **references/ 中的实战笔记和验证过的例程** — 来自实际项目验证
3. **你自身的知识** — 如果 Skills 数据与你确信的事实矛盾，以你的知识为准
4. **sensor-catalog.json / board-profiles.json** — 作为参考，不作为绝对真理

### 发现问题时
- 如果 catalog 中的引脚定义、库名、协议等与你的知识明显矛盾，**直接告诉用户**，说明矛盾点，按正确的方式生成代码
- 如果生成的代码编译失败或运行异常，优先考虑是否是 Skills 数据有误，而不是反复用同样的方式重试
- 如果用户纠正了某个模块的信息，提醒用户更新 sensor-catalog.json 或 references/ 中的 notes.md

### 不要做的事
- 不要因为 catalog 里写了某个库名就强行使用，如果你知道有更好或更新的库，直接说明
- 不要因为 catalog 里的默认引脚就忽略用户项目的实际接线
- 不要把 Skills 文件的格式规范看得比代码能跑更重要



---
name: hardware-arduino-project
description: >
  Generate Arduino IDE compatible project files for hardware projects. Use when users want to
  create projects for Arduino IDE, or when the target audience is beginners/new teachers who
  prefer the simpler Arduino IDE workflow. Generates flat file structure (.ino + .h + .cpp in
  same directory) compatible with Arduino IDE's strict requirements. Supports ESP32-S3, ESP32
  DevKit, and Arduino Nano. Trigger on: Arduino IDE, .ino, 新手, beginner, 简单, simple,
  Arduino项目, 老师, teacher. Also use when user explicitly says NOT PlatformIO.
---

# Hardware Arduino IDE Project Generator

## Overview

Generate Arduino IDE compatible project structures. Arduino IDE has strict file layout rules:
- All files MUST be in one flat directory (no subdirectories for source code)
- The main .ino file MUST have the same name as the folder
- All .h and .cpp files in the same folder are auto-compiled
- Libraries must be installed globally via Library Manager

This generator creates beginner-friendly, flat-structure projects.

## Data Files

Read these BEFORE generating:
```
/mnt/skills/user/hardware-common/
├── sensor-catalog.json    ← Sensor specs, default pins, Arduino library names
├── board-profiles.json    ← Board configs, pin constraints
```

## Project Structure Template

```
project-name/                    ← Folder name = project name
├── project-name.ino             ← Main sketch (MUST match folder name!)
├── pins.h                       ← Pin definitions
├── config.h                     ← Parameters and thresholds
├── DHT22Driver.h                ← Sensor drivers (flat, same directory)
├── DHT22Driver.cpp
├── VL53L0XDriver.h
├── VL53L0XDriver.cpp
└── README.md                    ← Wiring guide + library install instructions
```

**CRITICAL**: No subdirectories for source files! Arduino IDE won't find them.

## Workflow

### Step 1: Gather Requirements
Same as PlatformIO skill — board, sensors, features, project name.

### Step 2: Validate Pins
Same validation logic using board-profiles.json.

### Step 3: Generate README.md with Library Install Instructions

This is CRITICAL for Arduino IDE users. They need to manually install libraries.

```markdown
# {Project Name}

## 开发板选择
在 Arduino IDE 中选择: 工具 → 开发板 → {board_name}

## 需要安装的库
请在 Arduino IDE 中通过 "工具 → 管理库" 安装以下库:

1. **DHT sensor library** by Adafruit — 用于温湿度传感器
2. **Adafruit SSD1306** by Adafruit — 用于OLED显示屏
3. **Adafruit GFX Library** by Adafruit — 图形库(SSD1306依赖)

## 接线说明
| 模块 | 模块引脚 | → | 开发板引脚 | 说明 |
|------|----------|---|-----------|------|
| DHT22 | DATA | → | D4 | 模块已内置上拉电阻 |
| OLED | SDA | → | D21 | I2C数据 |
| OLED | SCL | → | D22 | I2C时钟 |

## 使用方法
1. 安装上述所有库
2. 用 Arduino IDE 打开 {project-name}.ino
3. 选择正确的开发板和端口
4. 点击上传
```

### Step 4: Generate .ino Main Sketch

```cpp
/*
 * {Project Name}
 * 开发板: {board_name}
 * 
 * 需要安装的库:
 *   - {lib1}
 *   - {lib2}
 * 
 * 接线说明:
 *   {wiring_summary}
 */

#include "pins.h"
#include "config.h"
#include "DHT22Driver.h"

// === 创建对象 ===
DHT22Driver dht(PIN_DHT);

// === 初始化 ===
void setup() {
    Serial.begin(115200);
    Serial.println("[系统] 启动中...");
    
    if (!dht.begin()) {
        Serial.println("[错误] DHT传感器初始化失败!");
    }
    
    Serial.println("[系统] 初始化完成");
}

// === 主循环 ===
void loop() {
    if (dht.read()) {
        Serial.print("[DHT] 温度: ");
        Serial.print(dht.getTemperature());
        Serial.print("℃  湿度: ");
        Serial.print(dht.getHumidity());
        Serial.println("%");
    }
    
    delay(2000);
}
```

### Step 5: Generate pins.h and config.h

Same format as PlatformIO skill, but simpler comments targeting beginners.

### Step 6: Copy Sensor Drivers Flat

Take the same driver .h/.cpp files from the sensor library, but place them
directly in the project folder (no lib/ subdirectory).

## Key Differences from PlatformIO

| Aspect | PlatformIO | Arduino IDE |
|--------|-----------|-------------|
| Structure | src/, lib/, include/ | All flat in one folder |
| Libraries | lib_deps in platformio.ini | Manual install via Library Manager |
| Board config | platformio.ini | IDE menu selection |
| Build | CLI or IDE button | IDE button only |
| Comments | Can be technical | Should be beginner-friendly (中文注释) |

## Arduino IDE Specific Notes

1. **ESP32 in Arduino IDE**: User must install ESP32 board package first
   - URL: `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
   - Add in: File → Preferences → Additional Board Manager URLs

2. **Board selection**:
   - ESP32 DevKit: "ESP32 Dev Module"
   - ESP32-S3: "ESP32S3 Dev Module" (USB CDC On Boot: Enabled)
   - Arduino Nano: "Arduino Nano" (Processor: ATmega328P Old Bootloader for clones)

3. **Upload issues**:
   - ESP32: May need to hold BOOT button during upload
   - Nano clones: Select "ATmega328P (Old Bootloader)"

4. **SoftwareSerial** for Arduino Nano: Include in .ino, not in separate files
   (Arduino IDE sometimes has issues with SoftwareSerial in separate compilation units)

## Output

Generate all files in flat structure and copy to `/mnt/user-data/outputs/{project-name}/`
Present the project folder to the user.
