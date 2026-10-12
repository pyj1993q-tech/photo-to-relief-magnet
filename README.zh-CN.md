# 照片转浮雕冰箱贴

[English](README.md)

这是一个开源 Codex Skill，用于把宠物、花束、风景、建筑、地标和纪念照片整理成可用于生图的彩绘树脂浮雕冰箱贴概念方案与完整提示词。

它会帮助 Agent 判断异形切边还是框景结构更合适，保留照片中真正重要的识别点，清理无关杂物，统一系列风格，并检查 PNG 是否真的含有透明像素。

## 主要能力

- 多张照片默认分别设计，只有在用户明确要求时才融合。
- 区分实体磁贴、展示画布和接触阴影，避免把展示背景误当成产品的一部分。
- 修改方案时，将新意见整合进完整提示词重新生成，并保留未要求改变的已确认设定。
- 提供异形、徽章/圆牌、横竖向圆角框等结构判断。
- 提供完整提示词框架和浮雕层级、材质、边界、避坑项。
- 附带 PNG Alpha 检查脚本，避免把画出来的棋盘格或全不透明图片误称为透明底。

本 Skill 产出的是**概念图和生成提示词**，不等于已经打样的实物，也不直接生成 CAD、STL、深度图、模具方案或经过工程验证的生产文件。

## 安装

把本仓库下载或克隆到 Codex skills 目录：

```bash
git clone https://github.com/pyj1993q-tech/photo-to-relief-magnet.git ~/.codex/skills/photo-to-relief-magnet
```

Windows PowerShell 默认路径：

```powershell
git clone https://github.com/pyj1993q-tech/photo-to-relief-magnet.git "$env:USERPROFILE\.codex\skills\photo-to-relief-magnet"
```

安装后重启 Codex，或新建一个任务。

## 使用

上传图片并输入：

```text
使用 $photo-to-relief-magnet，把这张照片做成高级彩绘树脂浮雕冰箱贴概念图。
保留小狗的表情和格纹领巾，删除店铺背景，用白色展示画布呈现。
```

最好同时说明：

- 必须保留什么；
- 可以删除或简化什么；
- 多张图片是分别设计还是融合；
- 是否有必须逐字保留的文字；
- 需要展示图，还是真透明 PNG。

## 检查 PNG 透明通道

脚本只使用 Python 标准库，无需安装第三方依赖。检查一张或多张 PNG：

```bash
python scripts/check_png_alpha.py output.png
python scripts/check_png_alpha --json output-a.png output-b.png
```

脚本会区分三种情况：没有 Alpha 通道、存在但完全不透明、确实存在透明或半透明像素。它不负责验证印刷刀线或生产可行性。

## 隐私与权利

只上传你有权使用的照片。对人物、私人地点、品牌、受保护角色和纪念文字，发布前应人工复核。本仓库不包含原项目中的私人照片或生成样例。

## 许可证

[MIT](LICENSE)
