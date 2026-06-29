# Skills

个人 Codex Skills 集合仓库。每一个 skill 使用一个独立的一级文件夹，文件夹名称与 `SKILL.md` 中的 `name` 保持一致。

## 目录结构

```text
skills/
  README.md
  ui-design-ref/
    SKILL.md
    agents/
      openai.yaml
    references/
      artifact-templates.md
      design-systems.md
      iteration-workflow.md
    scripts/
      generate_design.py
  project-init-workshop/
    SKILL.md
    agents/
      openai.yaml
    references/
      01-product-definition.md
      02-execution-planning.md
      03-design-experience.md
      04-technical-decisions.md
      05-process-norms.md
    scripts/
      scaffold_docs.py
```

## 已收录 Skills

| Skill | 简介 | 状态 |
| --- | --- | --- |
| `ui-design-ref` | 产品开发前期的 UI 设计参考流程：先确定设计系统，再输出设计 tokens、组件清单和数据模型，最后进入实现。 | 初版 |
| `project-init-workshop` | 新项目初始调研与文档编写流程：产品想法、范围、MVP、设计、UI flow、文案、技术方案、项目结构和 GitHub 工作流。 | 初版 |

## 添加新的 Skill

后续添加 skill 时，直接在仓库根目录新增同名文件夹：

```text
new-skill-name/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
  assets/
```

其中只有 `SKILL.md` 是必需文件；`agents/`、`references/`、`scripts/`、`assets/` 按需要添加。Skill 文件夹内部尽量保持 Codex 标准结构，不额外放 README、安装说明或变更日志，避免增加上下文噪音。

## 致谢

`ui-design-ref` 的设计流程参考了 [@dotey（宝玉）](https://x.com/dotey/status/2063674134903603302) 关于 AI 辅助 UI 设计与开发工作流的公开总结，并参考了 [Adobe Spectrum / React Spectrum](https://github.com/adobe/react-spectrum) 的设计系统思路。
