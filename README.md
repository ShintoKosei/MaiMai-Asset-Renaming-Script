# MaiMai Asset Renaming Script
这是一个用于批量重命名MaiMai资源文件的脚本项目。**需要自行解包资源自行导入**。它从两个文件夹中读取文件，并根据文件名的部分匹配规则重命名文件。
脚本会对比 `wait_assets` 文件夹中的文件和 `Original_assets` 文件夹中的文件，将 `wait_assets` 文件夹中的文件名后缀ID替换为 `Original_assets` 文件夹中的文件名后缀ID，并将重命名后的文件输出到 `output` 文件夹中

## 使用方法
1. 将待处理的文件分别放入 `wait_assets` 文件夹和 `Original_assets` 文件夹中
2. 确保 `output` 文件夹为空。如果 `output` 文件夹中已有内容，脚本会提示是否删除其中的文件
3. 运行脚本 `rename.py`。

## 示例
假设 `wait_assets` 文件夹和 `Original_assets` 文件夹中的文件如下：

**wait_assets/**
- UI_CMN_TabTitle_BonusSong-resources.assets-**4230**.png
- OtherFile-resources.assets-**4231**.png

**Original_assets/**
- UI_CMN_TabTitle_BonusSong-resources.assets-**4344**.png
- OtherFile-resources.assets-**4345**.png

脚本运行后，会在 `output` 文件夹中生成如下文件：

**output/**
- UI_CMN_TabTitle_BonusSong-resources.assets-**4344**.png
- OtherFile-resources.assets-**4345**.png

## 贡献
欢迎任何形式的贡献。如果你发现了问题或者有改进建议，请提交issue或pull request。

## 许可证
该项目采用 MIT 许可证。详情请参见 `LICENSE` 文件
