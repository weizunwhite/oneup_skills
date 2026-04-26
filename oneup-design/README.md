# OneUp Design — 零一优创品牌设计系统

零一优创（One Up）官方品牌视觉规范包。所有面向外部的网站、UI 组件、营销物料、PPT 模板都应遵循本规范。

## 包含的 Skill

### `oneup-design-system`
完整的设计 token + 组件样例 + 文案语气规则 + 真实项目数据。当你（或 AI）需要为 One Up 开发任何 UI 时自动触发。

## 核心资产

| 文件 | 用途 |
|------|------|
| `skills/oneup-design-system/SKILL.md` | 给 AI 看的规范文档（核心） |
| `skills/oneup-design-system/tokens/tokens.css` | CSS 变量，可直接 `@import` |
| `skills/oneup-design-system/tokens/tokens.json` | JSON tokens，给 Tailwind / Sanity 等工具消费 |
| `skills/oneup-design-system/references/oneup-baseline.html` | 基线 HTML 实现，**视觉对照标准** |
| `skills/oneup-design-system/references/real-projects.md` | 真实学生项目数据库 |

## 设计基线一览

- **配色**：深咖 `#2d1810` + 焦糖橙 `#c97f4a` + 暖米白 `#fdfaf4`
- **字体**：思源宋体（中文标题）+ 思源黑体（中文正文）+ Cormorant Garamond 斜体（英文装饰）
- **调性**：严肃、有学院感、有温度、克制；不卡通、不反叛、不装精英
- **核心标语**：以科创为体，以 AI 为手 / Where Real Things Are Built

## 安装

```
/plugin marketplace add weizunwhite/oneup_skills
/plugin install oneup-design@oneup-edu
```

## 在新项目中使用

### 单文件 HTML 项目
```html
<head>
  <link rel="stylesheet" href="path/to/tokens.css">
</head>
<body>
  <button style="background: var(--oneup-orange); color: white;">按钮</button>
</body>
```

### Next.js + Tailwind
1. 复制 `tokens.json` 到项目
2. 在 `tailwind.config.js` 中映射 token 为 Tailwind 主题
3. 在 `app/globals.css` 中 `@import` `tokens.css`

详见 `skills/oneup-design-system/SKILL.md` 第八节。

## 版本

当前 v1.0.0 · 暖色版基线（2026-04-26）

## License

MIT
