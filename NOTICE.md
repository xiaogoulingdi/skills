# 来源与许可说明 / Provenance and Licensing

本仓库中的 `claude-design/` 与 `claude-design-system/` 两个 skill 来自本地安装的 Codex 全局 skill，
仅供个人备份与后续修改使用。收录时未做任何删改，原有声明与第三方许可文本一并保留。

These two skills are copied verbatim from a local Codex installation for personal backup and
editing. Nothing was removed: all notices and third-party license texts are kept as shipped.

## 上游 / Upstream

- 两个 `SKILL.md` 的 `license` 字段声明为 **mixed**：正文、reference 与 editor 改编自
  Anthropic 的 claude.ai Artifact 类型，仍归 Anthropic，且 **不是** MIT；本地工具部分声明为 MIT。
  该字段指向的声明文件地址为
  `https://github.com/JimLiu/baoyu-design/blob/main/NOTICE.md`。
- 截至收录时，该地址重定向到 `https://github.com/JimLiu/open-artifact`，仓库为空
  （无 commit、无 LICENSE、无 NOTICE.md），因此 MIT 部分无法从上游取得许可全文。
- 作者的其他 skill 集合见 `https://github.com/JimLiu/baoyu-skills`（MIT，Copyright (c) 2026 Jim Liu），
  但不包含这两个 skill。

## 目录内的许可文本 / License texts kept in place

| 路径 | 内容 |
| --- | --- |
| `claude-design/scripts/editor/third-party-licenses.txt` | 25 个 npm 依赖的 MIT / Apache-2.0 / BSD-2-Clause / ISC 许可全文 |
| `claude-design-system/scripts/editor/third-party-licenses.txt` | 18 个 npm 依赖的许可全文 |
| `*/scripts/editor/artifact-type/reference/google-fonts-notices.json` | Google Fonts 1773 个字体家族的许可告示（源 `github.com/google/fonts`） |
| `*/scripts/editor/artifact-type/reference/google-fonts-reserved.json` | 字体保留名清单 |
| `*/scripts/editor/artifact-type/babel.min.js`、`vendor/react*.js` 等 | 打包产物中内联的逐包 MIT 许可头 |

上述第三方许可是再分发条件，请勿删除。

## 商标与品牌资产 / Trademarks

两个 skill 内含 Anthropic 品牌资料与资产，不属于开源许可范围：

- `artifact-type/reference/brand-colors.md`、`brand-typography.md`（Anthropic / Claude 品牌色与字体栈）
- `artifact-type/reference/craft.md` 中的 `Branded Anthropic work` 章节（Claude Spark、Claude/Anthropic 标识使用规则）
- `scripts/editor/assets/anthropicons-fizzy-lake-*.woff2` 与打包产物内联的 `baoyu-comments-icons` 图标字体
- CSS/LESS 变量中的 `Anthropic Sans`、`Anthropic Serif`、`Anthropic Mono`、`Anthropic Sans Display` 字体名

Anthropic、Claude 名称与标识归 Anthropic 所有，本仓库不主张任何相关权利。

## 说明

以上说明用于如实披露来源与许可状态，不构成对任何内容的再授权。
