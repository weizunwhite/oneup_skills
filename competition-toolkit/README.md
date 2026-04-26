# Competition Toolkit — 青创赛/金鹏材料生成工具集

为参加全国青少年科技创新大赛、北京金鹏科技论坛等竞赛的师生和教练提供的一站式材料生成工具。

## 包含的 Skills

- **competition-paper-generator** — 生成竞赛论文/研究报告（Word，含图表照片）
- **tech-proposal-generator** — 生成项目技术方案文档
- **project-research-log** — 生成研究日志（含补充材料清单）
- **presentation-generator** — 生成竞赛答辩 PPT
- **jinpeng-video-ppt** — 金鹏论坛视频专用 PPT + 视频脚本
- **jinpeng-submission-organizer** — 检查并整理金鹏提交材料
- **photo-checklist-generator** — 生成项目拍照清单
- **research-material-templates** — 生成原始研究资料模板
- **project-drawio-generator** — 生成项目图表（架构图/流程图/统计图）
- **lesson-plan-generator** — 生成科技创新项目教案

## 典型工作流

一个完整的项目从立项到提交，常见调用顺序：

```
1. lesson-plan-generator       (备课阶段)
       ↓
2. photo-checklist-generator   (开始拍照之前)
       ↓
3. project-research-log        (项目过程文档)
       ↓
4. project-drawio-generator    (生成项目图表)
       ↓
5. competition-paper-generator (撰写论文)
6. tech-proposal-generator     (技术方案)
       ↓
7. presentation-generator      (答辩 PPT)
   jinpeng-video-ppt           (金鹏视频 PPT)
       ↓
8. research-material-templates (原始资料补充)
       ↓
9. jinpeng-submission-organizer (最终材料整理提交)
```

## 安装

```
/plugin marketplace add weizunwhite/oneup_skills
/plugin install competition-toolkit@oneup-edu
```

## License

MIT
