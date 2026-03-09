# /vd_05_edit - 拍后从逐字稿提炼可剪片段 + 装配

读取 **项目根/outputs/inputs/transcript.md** + **项目根/outputs/{时间戳}-{主题概括}/01_topic_card.md**。运行目录 = 用户指定 或 **项目根/outputs/** 下最近包含 **00_plan.md** 的子目录。
生成 **项目根/outputs/{时间戳}-{主题概括}/05_edit_tags.md** 与 **项目根/outputs/{时间戳}-{主题概括}/06_assembly_map.md**。

## 05_edit_tags.md

- 按标签提取候选片段（HOOK / SCENE / CONFLICT / MECH / QUOTE / ACTION / BOUNDARY / HUMAN）
- 每段给：为什么值得剪 + 建议字幕标题
- 若无时间戳：给定位关键词；若有时间戳则保留

## 06_assembly_map.md

- 60s / 90s / 120s 三种装配方案
- 每种：开头 3-6 秒怎么放、转折点在哪里、动作怎么落、结尾怎么燃
- 额外给：开头钩子句 2 个、字幕金句 5 条

## 文件契约

- 两个输出文件顶部都写：目标 / 输入 / 输出 / 6 发动机自检
- 只写入 **项目根/outputs/{时间戳}-{主题概括}/05_edit_tags.md** 与 **项目根/outputs/{时间戳}-{主题概括}/06_assembly_map.md**

## 前提

**项目根/outputs/inputs/transcript.md** 中已有拍后逐字稿（可含时间戳）。
