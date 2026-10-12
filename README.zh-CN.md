# 照片转浮雕冰箱贴

[English](README.md)

这是一个开源 Codex Skill，用于把宠物、花束、风景、建筑、地标和纪念照片整理成可用于生图的彩绘树脂浮雕冰箱贴概念方案与完整提示词。

它会帮助 Agent 判断异形切边还是框景结构更合适，保留照片中真正重要的识别点，清理无关杂物，统一系列风格，并检查 PNG 是否真的含有透明像素。

## 原图与浮雕效果示例

下列示例将用户提供的原图与生成的彩绘浮雕概念图并列展示。它们是带展示背景的全不透明概念效果图，不是透明底素材，也不代表已经完成实物打样或生产验证。

| 原图 | 浮雕概念图 |
| --- | --- |
| ![穿红色衣服的猫](examples/a-red-outfit-cat-source.jpg) | ![穿红色衣服的猫浮雕概念图](examples/a-red-outfit-cat-relief.png) |
| ![怀抱中的猫](examples/b-held-cat-source.jpg) | ![怀抱中的猫浮雕概念图](examples/b-held-cat-relief.png) |
| ![猫爬架旁的猫](examples/c-cat-furniture-source.jpg) | ![猫爬架旁的猫浮雕概念图](examples/c-cat-furniture-relief.png) |
| ![古建与白花墙](examples/d-building-flowers-source.jpg) | ![古建与白花墙浮雕概念图](examples/d-building-flowers-relief.png) |
| ![粉色牡丹](examples/e-pink-peony-source.jpg) | ![粉色牡丹浮雕概念图](examples/e-pink-peony-relief.png) |
| ![花篮](examples/f-flower-basket-source.jpg) | ![花篮浮雕概念图](examples/f-flower-basket-relief.png) |

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

只上传你有权使用的照片。对人物、私人地点、品牌、二维码、受保护角色和纪念文字，发布前应人工复核。本仓库中的示例照片已获得照片权利方的明确公开授权。

## 许可证

[MIT](LICENSE)
