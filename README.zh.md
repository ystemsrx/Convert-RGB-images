[English](README.md)

# PNG转灰度图像转换器

## 概述
这个Python脚本“Convert.py”旨在将当前目录中的所有PNG图像转换为灰度图像。它利用OpenCV库处理图像，是一个简单高效的批量灰度转换工具。

## 特点
- **批量转换：** 自动将当前目录中的所有PNG图像转换为灰度图。
- **图像处理：** 使用OpenCV进行图像读取和转换。
- **易用性：** 简单执行，无需复杂配置。

## 系统要求
- Python 3
- OpenCV Python库 (`cv2`)

## 安装
1. 确保您的系统上安装了Python 3。
2. 安装OpenCV库：`pip install opencv-python`。

## 使用方法
1. 将脚本放在包含PNG图像的目录中。
2. 使用Python运行脚本：`python Convert.py`。
3. 目录中的所有PNG图像都将被转换为灰度图并以`gray_`前缀保存。

```txt
# 脚本中选取的代码片段
import cv2
import os
import glob

# 获取当前目录下所有的png文件
png_files = glob.glob('*.png')

# 遍历找到的png文件
for file in png_files:
    # 读取图像文件
    image = cv2.imread(file)
    # 转换成灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 构建灰度图像的保存路径
    gray_image_path = 'gray_' + file
    # 保存灰度图像
    cv2.imwrite(gray_image_path, gray_image)

print("所有PNG图像已转换为灰度图像。")
```

## exe下载
https://drive.google.com/file/d/1B2AaL8otDfm8FUk6FjBaDfy7wUnbFTZh/view?usp=sharing
