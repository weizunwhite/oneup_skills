# 模块参考资料库

按模块名建子文件夹，放入官方例程和实战笔记。Claude Code 生成代码前会自动检查这里。

## 目录结构

```
references/
├── DHT11/
│   ├── notes.md          ← 你的踩坑笔记（最高优先级）
│   └── official-example.ino  ← 验证过能跑的例程
├── VL53L0X/
│   ├── notes.md
│   └── pololu-example.cpp
├── UWB_MK8000/
│   ├── notes.md
│   ├── vendor-demo.ino
│   └── datasheet.pdf
└── ...
```

## 文件夹命名

使用 sensor-catalog.json 中的 key 名，例如：
- `DHT11`（不是 dht11 或 DHT-11）
- `VL53L0X`
- `UWB_MK8000`
- `OLED_SSD1306`
- `DC_motor_L298N`

## notes.md 模板

```markdown
# 模块名 使用笔记

## 推荐库
- 库名及版本

## 初始化要点
- 关键配置项

## 踩过的坑
- 问题描述 → 解决方法

## 与其他模块配合
- 共用总线/引脚注意事项
```

## 使用方式

不需要一次填满，每次项目做完把有价值的丢进来就行，越用越准。
