# Zun Skills - Claude 自定义技能集

这是零一优创（One Up）的 Claude 自定义技能集，用于支持科技创新教育项目的教学和竞赛准备。

## 📦 包含的 Skills

### 1. lesson-plan-generator（教案生成器）
**功能**：基于标准化 8 阶段方法论生成科技创新项目课程的详细教案

**适用场景**：
- 项目式学习课程设计
- STEM 教育课程规划
- 创客教育教案编写
- 青少年科技创新大赛课程准备

**核心特性**：
- 完整的 120 分钟课程结构（4-6 个教学环节）
- 详细的教学目标（知识、能力、素养）
- 具体的学生活动和教师话术
- 常见问题与应对策略
- 根据年级自动调整难度（小学/初中/高中）

**触发关键词**：教案、课程设计、第 X 节课、lesson plan

---

### 2. project-research-log（项目研究日志生成器）
**功能**：根据技术论文生成完整的项目研究日志，用于青少年科技竞赛材料准备

**适用场景**：
- 全国青少年科技创新大赛
- 北京金鹏科技论坛
- 其他需要研究日志的科技竞赛

**核心特性**：
- 自动将论文"倒推"成逐日开发过程
- 生成 15-30 条日志记录，跨度 3-8 个月
- 每条记录包含：日期、内容、问题、解决方法、照片占位符、心得体会
- 输出格式化 Word 文档
- 符合竞赛评审要求

**触发关键词**：研究日志、填研究日志、青少年科技创新大赛、research log

---

### 3. tech-doc-generator（技术文档生成器）
**功能**：生成完整的项目技术文档、竞赛论文和技术报告

**适用场景**：
- 科技竞赛参赛论文
- 项目技术报告
- 学术申报材料
- 项目展示文档

**核心特性**：
- 支持硬件、软件、系统集成等多种项目类型
- 根据年级调整文档复杂度和语言风格
- 包含完整章节：摘要、背景、方法、实现、测试、创新点、结论
- 自动生成图表说明和参考文献格式
- 可输出 Markdown 或 Word 格式

**触发关键词**：项目文档、技术报告、学术论文、参赛材料、technical documentation

---

## 🚀 快速开始

### 方法一：通过 Claude.ai 界面导入

1. 登录 Claude.ai
2. 进入 Settings → Skills
3. 点击"导入 Skill"
4. 上传对应的 skill 文件夹

### 方法二：克隆此仓库后手动导入

```bash
git clone https://github.com/YOUR_USERNAME/zun-skills.git
cd zun-skills
```

然后在 Claude.ai 中逐个上传三个文件夹。

### 方法三：在 Claude 对话中直接导入

1. 下载仓库压缩包
2. 在 Claude 对话中上传文件
3. 说："帮我安装这些 skills"

---

## 📖 使用示例

### 生成教案
```
你：帮我设计智能药盒项目的第1节课教案，初中生，一对一授课
Claude：[自动触发 lesson-plan-generator，生成完整教案]
```

### 生成研究日志
```
你：根据这篇智能书包的论文，帮我生成研究日志
Claude：[自动触发 project-research-log，分析论文并生成日志]
```

### 生成技术文档
```
你：帮我写一份智能火灾报警器的参赛论文，高中组
Claude：[自动触发 tech-doc-generator，生成完整论文]
```

---

## 📁 文件结构

```
zun-skills/
├── README.md                           # 本文件
├── lesson-plan-generator/
│   ├── SKILL.md                        # Skill 主配置
│   └── references/                     # 参考资料
│       ├── methodology.md              # 8阶段方法论
│       ├── templates.md                # 教案模板
│       └── example-lesson1.md          # 示例教案
│
├── project-research-log/
│   ├── SKILL.md
│   ├── references/
│   │   └── paper_analysis.md           # 论文分析方法
│   └── scripts/
│       └── generate_log.py             # Word 生成脚本
│
└── tech-doc-generator/
    ├── SKILL.md
    └── references/
        ├── document-structures.md      # 文档结构模板
        ├── examples.md                 # 优秀案例
        └── chinese-templates.md        # 中文技术写作模板
```

---

## 🔧 自定义和修改

所有 skills 都可以根据你的需求自由修改：

1. **修改触发条件**：编辑 `SKILL.md` 中的 `description` 字段
2. **调整生成逻辑**：修改 `SKILL.md` 中的工作流程描述
3. **更新模板**：编辑 `references/` 文件夹中的模板文件
4. **添加新功能**：在 `SKILL.md` 中添加新的步骤和指令

---

## 🎯 适用对象

- **教育机构**：科技创新教育培训机构
- **学校老师**：STEM、创客、科技课程教师
- **竞赛辅导员**：青少年科技竞赛指导老师
- **学生**：参加科技创新竞赛的中小学生
- **家长**：辅导孩子参加科技竞赛的家长

---

## 🏢 关于零一优创（One Up）

零一优创是一家专注于青少年科技创新教育的公司，提供：
- **B2B 业务**：与学校合作的 20 小时科创课程
- **B2C 业务**：一对一学生辅导（24-30 小时）
- **竞赛辅导**：全国青少年科技创新大赛、金鹏科技论坛等

**教学理念**：以科创为体，以 AI 为手
学生是创造者，而非观察者

---

## 📄 许可证

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

如有问题或建议，请联系：
- 邮箱：wei@oneup.tech
- 公司：零一优创（One Up）

---

## 📝 更新日志

### v1.0.0 (2025-01-27)
- 初始版本
- 包含三个核心 skills：lesson-plan-generator、project-research-log、tech-doc-generator
- 支持小学、初中、高中三个年级段
- 支持硬件、软件、系统集成等多种项目类型
