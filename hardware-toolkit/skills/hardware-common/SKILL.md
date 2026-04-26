---
name: hardware-common
description: 硬件项目共享数据库 — 提供模块目录（sensor-catalog.json，65+ 集成模块的引脚/协议/默认接线）和开发板配置（board-profiles.json，ESP32/Arduino 等开发板的引脚限制和外设数量）。其他硬件 skill（hardware-arduino-project / hardware-platformio-project / hardware-sensor-library）会读取这两个文件作为生成代码的依据。触发于"模块清单""sensor catalog""开发板规格""board profile""ESP32 引脚限制"等关键词，或被其他硬件 skill 自动引用。
---

# Hardware Common — 硬件项目共享数据库

本 skill 提供两个核心数据文件，供其他硬件相关 skill 调用：

## sensor-catalog.json

包含 65+ 个集成模块的元数据：
- 传感器（环境/距离/运动/视觉/电流等）
- 显示模块（OLED、TFT、LED 矩阵、WS2812B）
- 通信模块（蓝牙、WiFi、ESP-NOW、LoRa、UWB）
- 执行器（舵机、电机驱动、继电器、步进电机）
- 输入设备（按键、编码器、摇杆）

每个模块条目记录：
- `category` — 分类
- `function` — 功能描述
- `protocol` — 通信协议（I2C / SPI / UART / OneWire / GPIO / PWM 等）
- `pins_required` — 所需引脚数与名称
- `default_pins` — 在不同开发板上的默认接线建议
- `i2c_address` — I2C 设备的默认地址（如有）
- `library` — 推荐使用的 Arduino/PlatformIO 库
- `notes` — 实战注意事项（如 ADC2 不可用、需要外接上拉等特殊情况）

## board-profiles.json

包含主流开发板的硬件规格与引脚限制：
- ESP32 DevKit / ESP32-S3 / ESP32-C3
- Arduino Nano / UNO / Mega
- 树莓派 Pico / 行空板（Unihiker）
- MaixCAM / K230

每个开发板条目记录：
- 芯片型号、电压逻辑、Flash/RAM/主频
- UART / I2C / SPI 数量
- ADC 分辨率与可用通道
- PWM 引脚限制
- 已知坑（如 ESP32 ADC2 在 WiFi 开启时不可用）

## references/

存放各模块的参考资料（notes.md / 数据手册 / 已验证例程）。
其他 skill 在生成代码前会优先读取本目录下对应模块的 `notes.md`。

## 触发与使用

本 skill 通常**不会被用户直接调用**，而是作为底层数据被以下 skill 自动引用：
- `hardware-arduino-project` — 生成项目脚手架时查询模块的默认引脚
- `hardware-platformio-project` — 同上
- `hardware-sensor-library` — 生成驱动代码时查询库名和注意事项
- `embedded-systems-engineer` — 推荐方案时查询模块能力
- `firmware-build-verify` — 编译失败时查询正确的库名

如果用户直接问"列出所有支持的模块""ESP32 有几个 UART""DHT22 默认接线"等问题，可以直接读取本目录下的两个 JSON 文件回答。
