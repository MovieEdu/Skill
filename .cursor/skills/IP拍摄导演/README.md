# Video Director Skill v1.0 - 短视频现场导演

把选题 brief 工程化产出：拍前手卡、现场提问脚本、场记 tag、剪辑装配、标题封面。基于 **6 发动机 + 真实对话场域 + 燃/硬/温** 模式。**所有运行时文件均在 项目根/outputs/ 下，不在 skill 目录下创建或写入任何文件。**

## 快速开始（推荐：直接给参考内容）

**你**：直接粘贴或输入参考内容（不必按模板写），例如电影、话题一句、想说的方向、评论区会吵什么、3 个电影场景、观众带走的一句话等；有就写，没有也可。

**我**：按模板整理进 **项目根/outputs/inputs/brief.md**，然后**自动从计划开始做到拍前全套**（vd_00_plan → vd_01～vd_04）。  
也可在给内容的同时说「执行 /vd_start」或「按导演流程做」。

## 或：先填 brief 再跑

1. 在 **项目根/outputs/inputs/** 下创建或编辑 **brief.md**（可参考 skill 内 `templates/input_brief_template.md`），填满至少 10 项必填。
2. 按序执行 `/vd_00_plan` → … → `/vd_99_publish`，或单步执行所需命令。

## 你每次需要输入什么（最小必填 10 项）

放在 **项目根/outputs/inputs/brief.md**（用 skill 内 `templates/input_brief_template.md` 作模板）：

- 电影/素材源、话题一句话、风格模式、目标观众、评论区会吵什么（至少 3 条）、**反方与边界（必填）**、**一步动作（必填，具体到怎么做/做多久/做到什么算完成）**、彭老师当下状态、想表达方向（≤3 条）、「不够透」的点、电影场景锚 3 个、观众带走的一句话等。

## 工作模式

### 直接给参考内容（默认）
给一段参考内容（或说「执行 /vd_start」）→ 我整理成 **项目根/outputs/inputs/brief.md** → 自动执行 vd_00_plan 并继续 vd_01～vd_04（拍前全套）。

### 完整流水线（brief 已存在）
`/vd_00_plan` → … → `/vd_04_runofshow` → 拍摄 → `/vd_05_edit` → `/vd_06_packaging` → `/vd_07_iterate` → `/vd_99_publish`；发布后可填 **09_metrics.md**（或执行 `/vd_10_metrics`）做复盘数据闭环。

### 单步命令
- `/vd_start` - 从参考内容整理 brief 并做到拍前全套
- `/vd_00_plan` ～ `/vd_99_publish`、`/vd_10_metrics` - 见 SKILL.md 命令一览

## 仓库结构（所有文件在 项目根/outputs/ 下）

```
项目根/                          # 当前工作区根目录（如 IP导演现场）
  outputs/
    inputs/                      # 输入：brief、transcript、ip_profile、refs
      brief.md
      transcript.md
      ip_profile.md
      refs.md
    {时间戳}-{主题概括}/          # 每个话题独立工作目录（严格隔离）
      00_brief.md                # 本话题 brief 备份（来自 inputs/brief.md）
      00_plan.md                 # 本话题拍摄计划
      01_topic_card.md … 08_revision_notes.md
      09_metrics.md              # 复盘数据表（发布后填，可 /vd_10_metrics 生成）
      PUBLISH.md
  # 不再使用 plans/ 或 current_run_dir；运行目录 = 用户指定或 outputs 下最近含 00_plan.md 的子目录
  .cursor/skills/video-director-skill/   # 仅 skill 定义，不在此目录下创建或写入任何文件
    SKILL.md
    prompts/commands/
    checklists/
    templates/
```

**规则**：**每个话题严格对应一个工作目录，完全隔离**。时间戳（如 20260304）+ 主题（限20字）→ **项目根/outputs/{时间戳}-{主题概括}/**；每次新话题将 inputs/brief.md 备份到该目录 00_brief.md，计划写入该目录 00_plan.md，其余产出（01～09、PUBLISH）均在此目录。**不使用 plans/ 或 current_run_dir**；单步执行时运行目录由用户指定或取 outputs 下最近含 00_plan.md 的子目录。禁止在 skill 目录下创建或写入文件。

## 质量闸门

上线前必须过 skill 内 `checklists/quality_gate.md`：证据锚、现场必拿片段、抽象词翻译、机制可转述、动作可执行、结尾把人扶起来、**事实核查（数字/剧情/因果断言）**等。

## 下一步

直接给我你的参考内容，或填好 **项目根/outputs/inputs/brief.md** 后说「从 vd_00_plan 开始」。
