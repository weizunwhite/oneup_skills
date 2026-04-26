# Paper Analysis Guide

How to extract research log content from a project paper or technical document.

## Table of Contents

1. [Extraction Strategy](#extraction-strategy)
2. [Timeline Estimation](#timeline-estimation)
3. [Phase Breakdown](#phase-breakdown)
4. [Entry Planning](#entry-planning)
5. [Style Assignment](#style-assignment)
6. [Photo Planning](#photo-planning)
7. [Supplement Document Planning](#supplement-document-planning)

---

## Extraction Strategy

### From Paper Sections

| Paper Section | Extract For | Log Phase |
|---|---|---|
| 摘要/引言 | Problem statement, motivation, project goal | 调研选题 entries |
| 文献综述/调研 | Survey data, prior work studied, technology comparison | 调研选题 entries |
| 方法/设计 | Architecture, component selection, algorithm design | 学习准备 + 开发 entries |
| 实现/制作 | Assembly steps, code modules, integration work | 硬件/软件开发 entries |
| 测试/结果 | Test procedures, measurements, data tables | 测试验证 entries |
| 讨论/结论 | Challenges, lessons learned, future work | 反思 entries |

### Key Information to Extract

1. **Hardware components**: List every module/sensor/board mentioned → learning entries + assembly entries
2. **Software tools**: IDE, libraries, languages → environment setup entries
3. **Algorithms/formulas**: Math used → calculation/experiment entries
4. **Problem-solution pairs**: Every challenge mentioned → debug entries
5. **Test data**: Numbers, measurements, comparisons → experiment entries
6. **Design decisions**: Why X was chosen over Y → narrative entries

---

## Timeline Estimation

Based on project complexity and grade level:

| Complexity | Grade | Duration | Entry Count |
|---|---|---|---|
| Simple (single sensor, basic code) | 小学 | 2-3 months | 12-18 |
| Medium (multi-module, ESP32) | 初中 | 3-5 months | 18-25 |
| Complex (IoT, algorithms, multi-device) | 高中 | 5-8 months | 25-35 |

### Date Pattern Rules

- **Primary work days**: 周六、周日 (students are in school on weekdays)
- **Occasional weekdays**: 周三、周五 evenings during intensive phases
- **Gaps are realistic**: Not every weekend has an entry
- **Clusters**: More entries during development phases, fewer during planning
- **Holiday breaks**: Account for 寒假/暑假 — may have more intensive work periods

---

## Phase Breakdown

Divide the project timeline into phases. Typical distribution:

### Phase 1: 调研选题 (15-20%)
**Entries**: 3-5
**Content**: Problem discovery, surveys, literature review, technology research, design direction
**Typical styles**: narrative (discovery), table (survey analysis), compact (quick research notes)

### Phase 2: 学习准备 (15-20%)
**Entries**: 3-5
**Content**: Tool installation, tutorials, basic component testing, learning new skills
**Typical styles**: compact (setup tasks), debug (first errors), table (structured learning)

### Phase 3: 硬件/软件开发 (30-40%)
**Entries**: 6-12
**Content**: Circuit assembly, coding, module integration, debugging, iteration
**Typical styles**: debug (troubleshooting), table (structured work), narrative (breakthroughs)

### Phase 4: 测试验证 (15-20%)
**Entries**: 3-5
**Content**: Functional tests, accuracy validation, user testing, stability testing
**Typical styles**: experiment (data collection), narrative (user feedback), debug (edge cases)

### Phase 5: 论文撰写 (5-10%)
**Entries**: 2-3
**Content**: Material organization, paper writing, presentation prep, final checks
**Typical styles**: narrative (reflection), compact (task list)

---

## Entry Planning

For each entry, decide:

1. **What happened** — the main activity of that session
2. **What went wrong** — realistic problems for the grade level
3. **How it was solved** — specific, actionable solutions
4. **What was learned** — brief insight or skill gained
5. **What photos exist or are needed** — physical evidence

### Content Density by Style

| Style | Content Amount | When to Use |
|---|---|---|
| narrative | 2-3 paragraphs | Important moments, discoveries, reflections |
| table | 5-7 structured fields | Detailed technical work |
| compact | 4-6 bullet points | Routine tasks, quick sessions |
| debug | 2-3 problem-solution pairs | Troubleshooting sessions |
| experiment | Data table + 2 analysis paragraphs | Measurement/testing sessions |

### Problem Realism by Grade Level

**小学**: 线接反了、软件安装失败、传感器没反应、不知道怎么用万用表
**初中**: SPI通信失败、I2C地址冲突、无线丢包、打印精度不够
**高中**: 算法复杂度过高、多线程竞争、边界条件处理、精度-速度权衡

---

## Style Assignment

After planning all entries, assign styles to create natural variety:

```
Phase 1 (调研):     narrative → table → narrative
Phase 2 (学习):     compact → debug → table → compact
Phase 3 (开发):     table → debug → narrative → table → debug → compact
Phase 4 (测试):     experiment → experiment → debug → narrative
Phase 5 (论文):     compact → narrative
```

**Rules**:
- Never use the same style 3 times in a row
- Each phase should use at least 2 different styles
- narrative fits best for first entry (discovery) and last entry (reflection)
- experiment only for entries with actual measurement data
- debug only for entries where real troubleshooting happened

---

## Photo Planning

### Photo Categories

1. **过程照片** (process): Student working — soldering, coding, testing
2. **硬件照片** (hardware): Components, circuits, assembled devices
3. **屏幕截图** (screens): Code editor, debugging output, test results
4. **手写记录** (handwritten): Sketches, calculations, notes on paper
5. **测试场景** (testing): Test setup, measurement process, user testing

### Photo Distribution

Aim for photos in at least 40-50% of entries. Concentrate photos in:
- Hardware assembly entries (circuit photos, component photos)
- Testing entries (test scene, data collection)
- Final entries (finished product)

### Placeholder Format

When photos are missing, add placeholders that clearly describe what's needed:

```
[待补充照片: 用万用表测量电路通断的特写照片]
[待补充照片: Arduino IDE串口监视器显示传感器数据的屏幕截图]
[待补充照片: 手写的系统架构草图（笔记本上）]
```

Placeholders should be specific enough that the student knows exactly what to photograph.

---

## Supplement Document Planning

While planning the log, simultaneously track what needs to go in the supplement document:

### A. Photo Checklist
For every `[待补充照片]` placeholder and every entry without photos, record:
- Entry date and title
- What to photograph
- Tips: 拍摄角度、是否需要特写、是否需要人入镜

### B. Handwritten Materials List
Based on project content, identify what should be hand-written:
- **必须有**: 实验数据记录表、至少一张手绘草图
- **建议有**: 问卷设计草稿、计算推导过程、调试笔记
- **加分项**: 思维导图、对比分析表

### C. Electronic Materials List
- Code screenshots (specify which function/module)
- Serial monitor / debug output screenshots
- 3D model screenshots (if applicable)
- Online survey results export

### D. Priority Marking
Mark each item as:
- ⭐⭐⭐ 必须补充 (required by competition rules)
- ⭐⭐ 建议补充 (strengthens the submission)
- ⭐ 可选补充 (nice to have)
