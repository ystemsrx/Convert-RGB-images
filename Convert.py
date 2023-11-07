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
