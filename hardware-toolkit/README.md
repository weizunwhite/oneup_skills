# Hardware Toolkit — Arduino / ESP32 硬件开发工具集

为青少年科技项目硬件开发提供的工具集，覆盖 Arduino IDE、PlatformIO、ESP32 全栈开发。

## 设计原则

- **模块级开发**：所有传感器/通信/显示/执行器按集成模块对待，不处理裸元器件电路
- **数据驱动**：通过共享的 `sensor-catalog.json`（65+ 模块）和 `board-profiles.json`（多种开发板）保证生成的代码引脚正确、库选对、不踩 ESP32 ADC2 等已知坑
- **生产可用**：禁止用 `delay()` 长等待，串口波特率统一 115200，每个模块封装独立驱动

## 包含的 Skills

### 核心数据
- **hardware-common** — 共享数据库（模块目录 + 开发板规格 + 实战笔记）

### 项目脚手架
- **hardware-arduino-project** — Arduino IDE 项目（扁平结构）
- **hardware-platformio-project** — PlatformIO 项目（src/lib/ini）

### 代码生成
- **hardware-sensor-library** — 模块驱动代码（.h/.cpp）

### 编译与调试
- **firmware-build-verify** — 固件编译、烧录、串口验证（写代码后自动触发）
- **esp32-firmware-debugger** — ESP32 崩溃/通信/连接问题专项诊断

### 系统集成
- **edge-iot-integration** — 端云架构、MQTT、OTA、设备-应用集成
- **embedded-systems-engineer** — 资深嵌入式工程师 agent（架构咨询）

### 格式转换
- **ino-to-mixly** — Arduino `.ino` 转 Mixly 2.0 `.mix`（图形化编程）

## 典型工作流

```
1. hardware-arduino-project / hardware-platformio-project   (新建项目)
       ↓
2. hardware-sensor-library                                  (生成模块驱动)
       ↓
3. firmware-build-verify                                    (编译+烧录+验证)
       ↓ (出问题时)
4. esp32-firmware-debugger                                  (调试)
       ↓
5. edge-iot-integration                                     (接云)
       ↓ (面向小学生时)
6. ino-to-mixly                                             (转图形化)
```

## 支持的开发板

ESP32 DevKit / ESP32-S3 / ESP32-C3 / Arduino Nano / Arduino UNO / Arduino Mega / 树莓派 Pico / 行空板（Unihiker）/ MaixCAM / K230

## 已收录的常用模块

环境（DHT11/22, BMP280, MQ-2/7）/ 距离（HC-SR04, VL53L0X, UWB）/ 运动（MPU6050, HX711）/ 视觉（MLX90640, OV2640/5640）/ 显示（SSD1306, TFT, WS2812B）/ 通信（ESP-NOW, MQTT, BLE）/ 电机驱动（L298N, TB6612, 舵机, 步进电机）

详见 `skills/hardware-common/sensor-catalog.json`。

## 安装

```
/plugin marketplace add weizunwhite/oneup_skills
/plugin install hardware-toolkit@oneup-edu
```

## License

MIT
