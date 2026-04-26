---
name: oneup-design-system
description: 零一优创（One Up）官方品牌视觉规范。用于在为 One Up 公司开发任何前端界面、网站、UI 组件、营销物料、PPT 模板、PDF 报告封面、品牌图形时遵守统一的视觉语言。包含完整的颜色 token、字体、间距、组件样例、文案语气规则。默认主题为 warm-baseline（暖色）；备选主题 neo-brutalism-alt 仅在用户明确要求"反叛""极客""年轻态"风格时使用。触发于 "OneUp 网站""零一优创界面""设计稿""design system""品牌色""品牌字体""官网组件""营销页"等关键词，或当用户在 oneup-website / oneup-platform 项目中要求实现任何 UI。
---

# OneUp Design System — 零一优创视觉规范 v1.0.0

> 本规范是零一优创（One Up）所有面向外部的视觉物料的**唯一标准**。
> 任何为 One Up 开发的前端代码、UI 组件、品牌物料，**必须**遵循本规范。

## 主题选择（重要）

本设计系统提供 **2 个主题**：

| 主题 | 文件 | 默认/备选 | 适用场景 |
|------|------|----------|---------|
| **warm-baseline**（暖色基线） | `references/themes/warm-baseline.html` | ⭐ **默认** | 公司官网、家长营销页、PPT、研究报告封面、所有正式对外物料 |
| **neo-brutalism-alt**（粗野风备选） | `references/themes/neo-brutalism-alt.html` | 备选 | 极客向内部工具、开发者文档站、学生作品集（可选）、不面向家长的页面 |

**默认行为**：除非用户明确说"用反叛风格""粗野风格""kuangye"或类似关键词，**总是使用 warm-baseline**。

下面所有的 token、组件、文案规则都基于 **warm-baseline 主题**。备选主题有自己的视觉语言，详见 `references/themes/neo-brutalism-alt.html` —— 它使用黑色粗边框 + 高饱和度色块 + 硬阴影 + Space Grotesk 字体，但**文案语气和真实项目数据规则完全相同**（不能编造占位项目，不能写"申请名校"等装腔语）。

## 调性总结（必读）

零一优创是一家做青少年科技创新教育的公司，调性是：

| 是 | 不是 |
|---|---|
| 严肃、有学院感、克制 | 活泼卡通、儿童化、过度装饰 |
| 温暖、有人情味、关怀 | 冰冷、机械、说教 |
| 现代但克制（不堆动效） | 摇滚反叛、新粗野主义 |
| 中文为主，英文做装饰点缀 | 大量英文、装精英 |
| 强调"做出真实的东西" | 强调"申请名校"、"升学敲门砖" |

**目标读者画像**：30-45 岁北京家长，有受过教育，看重审美和专业感。能识别真诚和包装的差别。

---

## 一、颜色系统（绝对不要用其他颜色）

### 主色系：深咖系
| Token | Value | 用途 |
|-------|-------|------|
| `--oneup-brown-darkest` | `#2d1810` | hero 背景、主深色文字、CTA 按钮 |
| `--oneup-brown-dark` | `#3d2817` | 二级深色（容器、卡片深色） |
| `--oneup-brown-light` | `#7a6553` | 次级文字（描述、说明） |

### 强调色：焦糖橙
| Token | Value | 用途 |
|-------|-------|------|
| `--oneup-orange` | `#c97f4a` | 主强调色（按钮、链接、徽章） |
| `--oneup-orange-light` | `#e0a070` | hover lighter |
| `--oneup-orange-deep` | `#a85d2c` | hover deeper、强调态 |
| `--oneup-orange-tint` | `rgba(201,127,74,0.1)` | 徽章背景蒙版 |
| `--oneup-orange-line` | `rgba(201,127,74,0.4)` | 装饰细线、边框 |

### 中性色：米色系
| Token | Value | 用途 |
|-------|-------|------|
| `--oneup-bg-primary` | `#fdfaf4` | 暖米白主背景 |
| `--oneup-bg-secondary` | `#f5efe4` | 米色次背景（section 间隔） |
| `--oneup-bg-card` | `#ffffff` | 卡片纯白背景 |

### ⚠️ 严格禁止
- **不要**用纯白 `#ffffff` 作为页面主背景（用 `#fdfaf4`）
- **不要**用蓝色、紫色、绿色作为强调色（保持单一焦糖橙）
- **不要**用渐变（除了非常细微的暗化遮罩）
- **不要**用霓虹色、高饱和度色
- **不要**用纯黑 `#000000`（用 `#2d1810`）

---

## 二、字体系统

| 用途 | 字体 |
|------|------|
| 中文标题（h1/h2/h3） | `Noto Serif SC`（思源宋体） |
| 中文正文 | `Noto Sans SC`（思源黑体） |
| 英文装饰（Hero tag、section eyebrow） | `Cormorant Garamond` 斜体 |
| 数字（统计数据） | `Cormorant Garamond` 加粗 |
| 代码 | `JetBrains Mono` |

**核心原则**：中文宋体 + 英文 Garamond 斜体 = 学院感 + 温度。

### 字号规范
- **Hero h1**: `clamp(2.4rem, 4.5vw, 3.8rem)` + 字距 4px
- **Section h2**: `2.4rem` + 字距 4px（中文之间手动加宽）
- **卡片标题 h3**: `1.8rem`
- **副标题**: `1.4rem`
- **正文**: `1rem` + 行高 1.8
- **描述/section-desc**: `1rem` + 行高 2（更松，更"深度阅读"感）
- **次要小字**: `0.85rem`

### 字距（letter-spacing）规则
- 大标题中文之间字距 4px（`letter-spacing: 4px`）
- 中文标题相邻字之间也可以**用空格隔开**（如 `教 学 理 念`），更显院校感
- 装饰英文小字字距 2-5px

---

## 三、关键组件样例

### Hero Pattern
```html
<header class="hero">
  <span class="hero-tag">Where Real Things Are Built</span>  <!-- Garamond 斜体 -->
  <h1>以科创为<span class="highlight">体</span>，以 AI 为<span class="highlight">手</span></h1>
  <p>...描述段落，行高 2，最大宽 720px...</p>
  <button class="btn-solid-orange">预约一次深度沟通</button>
</header>
```
- 背景：深咖 + 0.85-0.95 透明度蒙版叠加图片
- 底部居中有一根 1px × 60px 的焦糖橙竖线作为装饰

### Section Header Pattern
```html
<div class="section-header">
  <span class="section-en-tag">Our Philosophy</span>  <!-- Garamond 斜体橙色 -->
  <h2>教 学 理 念</h2>                                  <!-- 中文用空格隔开 -->
  <div class="divider"></div>                           <!-- 60px 焦糖橙细线 -->
  <p class="section-desc">...一段引言，最大宽 640px...</p>
</div>
```

### Case Card Pattern（学生项目卡）
```html
<div class="case-card">
  <div class="case-img">           <!-- 4px double 焦糖橙边框 + 12px padding -->
    <img filter="sepia(0.08)" />   <!-- 轻微 sepia 让照片有"档案感" -->
  </div>
  <div class="case-content">
    <span class="case-meta">Garamond 斜体小字 · 标签</span>
    <h3>项目标题</h3>
    <p>描述...</p>
    <div class="case-stats">       <!-- 数据条：左 2px 焦糖橙竖线 -->
      <div class="stat-item">
        <div class="num">2000+</div>
        <div class="label">张过程照片</div>
      </div>
    </div>
    <div class="award-badge">      <!-- 焦糖橙 10% 蒙版 + 焦糖橙细边 -->
      <i data-lucide="medal"></i> 北京金鹏科技论坛 入围
    </div>
  </div>
</div>
```
- 项目卡左右**交替**排列（zigzag）：`.case-card:nth-child(even) { flex-direction: row-reverse; }`

### 按钮
```css
/* 主按钮：实心焦糖橙 */
.btn-solid-orange {
  background: var(--oneup-orange);
  color: white;
  padding: 16px 44px;
  letter-spacing: 3px;
  border: none;
}

/* 次按钮：边框焦糖橙 */
.btn-orange-outline {
  border: 1px solid var(--oneup-orange);
  color: var(--oneup-orange);
  background: transparent;
  padding: 10px 24px;
  letter-spacing: 2px;
}
.btn-orange-outline:hover {
  background: var(--oneup-orange);
  color: white;
}
```

---

## 四、交互与动效

- **滚动渐入**：使用 IntersectionObserver，元素从 `opacity:0; translateY(30px)` 渐入到 `opacity:1; translateY(0)`，duration 1s
- **hover 下划线**：导航链接 hover 时下方出现 1px 焦糖橙线，宽度 0→100%
- **卡片 hover**：轻微 `translateY(-4px)` + 焦糖橙边框 + 轻阴影
- **按钮 active**：保持现有焦糖橙变 deep 即可，不要做"按下移位"效果

⚠️ **不要做的动效**：
- 视差、3D 翻转、复杂粒子
- 弹簧 bounce 动画
- 持续旋转或脉冲

---

## 五、文案语气规则

### 应该用的词
- "做出真实的东西"
- "项目主权"
- "真实地做一件事"
- "以 X 为体，以 Y 为手"
- "深度沟通"
- "辅导 / 指导"
- "我们指导的学生"

### 不要用的词
- ❌ "精英"、"贵族"、"藤校"、"敲门砖"
- ❌ "前大厂算法工程师"（除非用户明确指示）
- ❌ "顶级"、"最强"、"独家"
- ❌ "Cultivating Tomorrow's Leaders" 这种装腔英文
- ❌ "保证获奖"、"保送名校"
- ❌ 卡通化的儿童词（"小朋友"、"宝贝"）

### Hero 标语正典
> **以科创为体，以 AI 为手**
> Where Real Things Are Built

这是 v1.0 锁定的主标语。任何 hero 区都用这个。

---

## 六、内容真实性

**永远使用真实学生项目数据**，不要编造占位项目。真实项目清单见 `references/real-projects.md`。

旗舰项目（首页 hero / 案例区优先用这些）：
1. 基于边缘 AI 视觉识别的医院自动取药系统 —— 陈嘉矞
2. 以水知安 · 独居老人用水监测系统 —— 洪一宁（4 年级）
3. 渐冻人看护呼叫器 —— 赵鸿憬
4. 智能坐位体前屈系统 —— 李铭钖（7 年级）

---

## 七、技术栈约定

- **HTML 原型**：单文件，Google Fonts CDN 引入字体，Lucide CDN 引入图标
- **生产实现**：Next.js + Tailwind（自定义主题映射 tokens.json）+ Sanity（CMS）
- **Tailwind 配色映射**：在 `tailwind.config.js` 中把 `--oneup-orange` 映射为 `theme.colors.brand.orange` 等
- **永不**使用 Material UI / Ant Design / Bootstrap 默认主题（它们的设计语言冲突）

---

## 八、如何使用本 skill

### 场景 1：写新 HTML 页面
1. 读取 `tokens/tokens.css` 注入到 `<style>` 中
2. 参考 `references/oneup-baseline.html` 的组件结构
3. 严格使用 token 变量，不要 hardcode 颜色

### 场景 2：搭 Next.js 项目
1. `tokens.json` 转换为 `tailwind.config.js` 主题
2. `tokens.css` 放到 `app/globals.css`
3. 把 `oneup-baseline.html` 的组件拆解成 React 组件

### 场景 3：做 PPT / PDF / 营销图
1. 按颜色 token 设置
2. 中文字体用思源宋体（标题）+ 思源黑体（正文）
3. 装饰用 Cormorant Garamond 斜体小字

### 场景 4：用户问"OneUp 的品牌色是什么？"
直接回答：
- 深咖 `#2d1810`
- 焦糖橙 `#c97f4a`
- 暖米白 `#fdfaf4`

并提示："详见 `oneup-design-system` skill 中 `tokens/tokens.css`"。

---

## 九、版本管理

- 当前版本：`v1.0.0`（暖色版基线）
- 任何对配色、字体、间距的**结构性**改动需要升 minor 版本，并在 `references/oneup-baseline.html` 中同步
- 添加新组件不需要升版本
- 历史版本快照保留在 `references/baselines/v1.0.0.html` 中

## 十、引用

- 默认主题 HTML（warm-baseline）：[references/themes/warm-baseline.html](references/themes/warm-baseline.html)
- 备选主题 HTML（neo-brutalism-alt）：[references/themes/neo-brutalism-alt.html](references/themes/neo-brutalism-alt.html)
- CSS 变量：[tokens/tokens.css](tokens/tokens.css)
- JSON tokens：[tokens/tokens.json](tokens/tokens.json)
- 真实学生项目数据：[references/real-projects.md](references/real-projects.md)
