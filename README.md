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
  residential-exit-setup/
    SKILL.md
    references/
      checklist.md
      current-hk-tw-example.md
      local-routing.md
      migration.md
      scenarios.md
      troubleshooting.md
  claude-design/
    SKILL.md
    artifact-type/
      reference/
    scripts/
      artifact.mjs
      server.mjs
      editor/
        assets/          # 预构建的压缩产物，按原样保存，不要手改
  claude-design-system/
    SKILL.md
    artifact-type/
      demo.json
      reference/
    scripts/
      artifact.mjs
      server.mjs
      editor/
        assets/          # 同上
```

## 已收录 Skills

| Skill | 简介 | 状态 |
| --- | --- | --- |
| `ui-design-ref` | 产品开发前期的 UI 设计参考流程：先确定设计系统，再输出设计 tokens、组件清单和数据模型，最后进入实现。 | 初版 |
| `project-init-workshop` | 新项目初始调研与文档编写流程：产品想法、范围、MVP、设计、UI flow、文案、技术方案、项目结构和 GitHub 工作流。 | 初版 |
| `residential-exit-setup` | 家宽 VPS 出口接入与迁移：前置链路、分流、DNS、动态 IP、测试和回滚。 | 初版 |
| `claude-design` | 可编辑的 Design 画布：生成 `project/canvas.json` 与多个 `.dc.html` 画板，在本地编辑器中并排查看和修改。 | 直接引用（见下节） |
| `claude-design-system` | 本地设计系统：tokens、字体、组件预览与品牌资源，可在本地页面中浏览和编辑。 | 直接引用（见下节） |

## 直接引用的 Skills：claude-design 与 claude-design-system

这两个 skill 直接从本地已安装的同名 skill 引用而来，内容原样收录，并非本仓库原创。

**授权说明：** 这两个 skill 的内容直接引用了上游同名 skill。原上游仓库（原 `JimLiu/baoyu-design`，后跳转至 `JimLiu/open-artifact`）现已不可访问，页面显示为空仓库，无法再从上游取得许可声明或授权条款。本仓库仅作个人私有使用，不公开发布、不对外分发；日后如要公开或再分发，应自行核实并补充相应的授权信息。

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
