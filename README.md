# OneUp Skills — 零一优创 Claude Code 插件市场

零一优创（One Up）青少年科技创新教育配套的 Claude Code 插件市场，包含两个独立插件：竞赛材料生成工具集 + 硬件开发工具集。

## 📦 包含的插件

### 🎓 competition-toolkit — 青创赛/金鹏材料生成工具集

为参加全国青少年科技创新大赛、北京金鹏科技论坛等竞赛的师生和教练提供的一站式材料生成工具。

包含 10 个 skills：

| Skill | 功能 |
|-------|------|
| `competition-paper-generator` | 生成竞赛论文/研究报告（Word，含图表照片） |
| `tech-proposal-generator` | 生成项目技术方案文档 |
| `project-research-log` | 生成研究日志（含补充材料清单） |
| `presentation-generator` | 生成竞赛答辩 PPT |
| `jinpeng-video-ppt` | 金鹏论坛视频专用 PPT + 视频脚本 |
| `jinpeng-submission-organizer` | 检查并整理金鹏提交材料 |
| `photo-checklist-generator` | 生成项目拍照清单 |
| `research-material-templates` | 生成原始研究资料模板（手填或带内容版） |
| `project-drawio-generator` | 生成项目架构图、流程图、统计图等 Draw.io 图表 |
| `lesson-plan-generator` | 生成科技创新项目教案 |

### 🔧 hardware-toolkit — Arduino / ESP32 硬件开发工具集

为青少年科技项目硬件开发提供的工具集，覆盖 Arduino IDE、PlatformIO、ESP32 全栈开发。

包含 9 个 skills：

| Skill | 功能 |
|-------|------|
| `hardware-common` | 硬件项目共享数据库（65+ 集成模块目录 + 开发板规格） |
| `hardware-arduino-project` | 生成 Arduino IDE 项目脚手架 |
| `hardware-platformio-project` | 生成 PlatformIO 项目脚手架 |
| `hardware-sensor-library` | 生成传感器/模块驱动代码（.h/.cpp） |
| `firmware-build-verify` | 固件编译、烧录、串口验证工作流 |
| `embedded-systems-engineer` | 嵌入式系统资深工程师 agent |
| `esp32-firmware-debugger` | ESP32 崩溃/通信/连接问题诊断 |
| `edge-iot-integration` | IoT 端云架构与协议集成 |
| `ino-to-mixly` | Arduino .ino 转 Mixly 2.0 .mix（图形化编程） |

## 🚀 安装

### 第一步：添加 marketplace

在 Claude Code 中执行：

```
/plugin marketplace add weizunwhite/oneup_skills
```

### 第二步：安装需要的插件

```
/plugin install competition-toolkit@oneup-edu
/plugin install hardware-toolkit@oneup-edu
```

只装一个也可以，按需选择。

## ♻️ 多机同步（推荐用法）

如果你有多台开发机器，这个仓库是天然的 skills 同步盘：

```
机器 A: /plugin marketplace add weizunwhite/oneup_skills
机器 A: /plugin install competition-toolkit@oneup-edu
机器 A: /plugin install hardware-toolkit@oneup-edu
机器 B: 同样三条命令

# 之后任何一台机器修改 → push → 另一台 /plugin update
```

## 🔄 更新

每次远程仓库有新版本：

```
/plugin update
```

## 🛠️ 给开发者：本地修改与发布流程

```bash
# 1. 克隆仓库
git clone https://github.com/weizunwhite/oneup_skills.git
cd oneup_skills

# 2. 修改某个 skill
vim competition-toolkit/skills/competition-paper-generator/SKILL.md

# 3. 提交并推送
git add -A
git commit -m "improve: paper generator outline structure"
git push

# 4. 通知用户更新
# 各机器执行 /plugin update 即可
```

### 仓库结构

```
oneup_skills/
├── .claude-plugin/
│   └── marketplace.json          ← marketplace 总入口
├── competition-toolkit/
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       ├── competition-paper-generator/
│       ├── tech-proposal-generator/
│       └── ...
├── hardware-toolkit/
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       ├── hardware-common/
│       ├── hardware-arduino-project/
│       └── ...
├── LICENSE
└── README.md
```

## 📜 License

MIT
