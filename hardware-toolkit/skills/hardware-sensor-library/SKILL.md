---
name: hardware-sensor-library
description: 为常见传感器/通信模块/显示模块/执行器生成驱动代码（.h/.cpp 封装），覆盖 DHT11/22、HC-SR04、MPU6050、SSD1306、WS2812B、舵机、L298N 等。所有模块按集成模块对待。触发于"传感器驱动""模块代码""sensor library""DHT 驱动""OLED 驱动"等关键词。
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
name: hardware-sensor-library
description: >
  Query, generate, and manage sensor driver code for hardware projects. Use this skill whenever
  users ask about sensors, need driver code for a specific sensor/module, want to check sensor
  specs, or need wiring instructions. Covers all common sensors used in student innovation
  projects: temperature, distance, IMU, gas, weight, water quality, displays, motors, communication
  modules, and more. Trigger on: 传感器, sensor, 驱动, driver, 接线, wiring, 引脚, pin,
  模块, module, 怎么用, how to use, 连接, connect. Also trigger when users mention specific
  sensor model numbers like DHT11, VL53L0X, MPU6050, HX711, MQ-2, HC-SR04, etc.
---

# Hardware Sensor Library (传感器驱动库)

## Overview

Manage and generate standardized sensor/module driver code for ESP32/Arduino hardware projects.
This skill provides:
1. **Sensor lookup** — query specs, wiring, and compatibility from the sensor catalog
2. **Driver generation** — create standardized driver classes following a unified interface
3. **Wiring validation** — check pin assignments against board constraints
4. **Integration guidance** — how to combine multiple sensors in a project

## Data Files

Before generating any code or answering sensor questions, ALWAYS read these reference files:

```
/mnt/skills/user/hardware-sensor-library/
├── SKILL.md (this file)

Shared data (read from hardware-common):
/mnt/skills/user/hardware-common/
├── sensor-catalog.json    ← Full sensor specs, default pins, libraries, notes
├── board-profiles.json    ← Board pin maps, constraints, conflict rules
```

**CRITICAL**: Always `view` the sensor-catalog.json to look up accurate sensor information before answering.

## Unified Driver Interface

All generated drivers MUST follow this pattern:

```cpp
#ifndef SENSOR_NAME_DRIVER_H
#define SENSOR_NAME_DRIVER_H

#include <Arduino.h>

class SensorNameDriver {
public:
    // Constructor with pin configuration
    SensorNameDriver(uint8_t pin1, uint8_t pin2 = 0);
    
    // Initialize sensor, return true if successful
    bool begin();
    
    // Read sensor data, return true if successful
    bool read();
    
    // Get formatted JSON string for IoT upload
    String getJSON();
    
    // Self-test / status check
    String getStatus();
    
    // Sensor-specific getters
    float getValue();
    
private:
    uint8_t _pin1, _pin2;
    float _lastValue;
    bool _initialized;
};

#endif
```

## Workflow

### Query Mode (user asks about a sensor)

1. Look up sensor in `sensor-catalog.json`
2. Return: specs, wiring diagram (text), library requirements, gotchas
3. Include board-specific notes (e.g., "ESP32 ADC2 conflicts with WiFi")

### Generate Mode (user needs driver code)

1. Look up sensor specs and default pins for target board
2. Check pin conflicts against `board-profiles.json`
3. Generate .h and .cpp files following unified interface
4. Include: initialization, reading, JSON output, error handling
5. Generate a simple example .ino/.cpp showing usage

### Pin Validation Mode (user has a pin plan)

1. Parse user's pin assignments
2. Cross-check against board constraints:
   - Input-only pins used for output?
   - ADC2 pins used with WiFi?
   - I2C address conflicts?
   - Boot-sensitive pins with wrong pull?
3. Report conflicts with severity (error/warning/info)
4. Suggest fixes

## Code Style Rules

- Use `#define` for pin numbers at top of file
- Include timeout in all I2C/SPI reads (no infinite loops)
- Always check sensor.begin() return value
- Use `Serial.println()` debug output with `[SensorName]` prefix
- Comments in Chinese (学生项目, 便于学生理解)
- Keep code simple — avoid templates, complex inheritance
- For ESP32: use `ESP32Servo` not `Servo`; use `ledcWrite` for PWM

## Common Patterns

### Multiple I2C Sensors (same address)
```cpp
// Use XSHUT pins to assign different addresses
// 1. Keep all XSHUT low (all off)
// 2. Set sensor1 XSHUT high, change address
// 3. Set sensor2 XSHUT high, change address
// 4. Repeat...
```

### ESP32 Analog Reading with WiFi
```
// ONLY use ADC1 pins: GPIO 32,33,34,35,36,39
// ADC2 (GPIO 0,2,4,12-15,25-27) CONFLICTS with WiFi!
```

### SoftwareSerial on Arduino Nano
```
// RX must be interrupt-capable pin: D2 or D3
// Avoid baud rates > 57600
// Only one SoftwareSerial can listen at a time
```

## Output

- Driver files: `SensorName.h` + `SensorName.cpp`
- Example: `SensorName_example.ino`
- Wiring table in response text
- All files to `/mnt/user-data/outputs/`
