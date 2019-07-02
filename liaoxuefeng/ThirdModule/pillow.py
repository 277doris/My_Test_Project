# Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
# 安装的命令：pip install pillow
# 如果遇到Permission denied安装失败，请加上sudo重试。
# 操作图像
from PIL import Image
import os

# 打开一个jpg图像文件，注意是当前路径：
# im = Image.open('C://Users//22648//Desktop//test.jpg')
# # 获取图像尺寸：
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%：
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存：
# im.save('thumbnail.jpg', 'jpeg')

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全
# 比如，模糊效果也只需几行代码：
# from PIL import Image, ImageFilter
# import os
# # 打开一个jpg图像文件，注意是当前路径
# im = Image.open('C://Users//22648//Desktop//test.jpg')
# # 应用模糊滤镜
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')

# PIL的ImageDraw提供一系列绘画方法，让我们可以直接绘图：
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1：
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2：
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240*60
width = 60 * 4      # 设置四个随机字母，每个字母宽度为60
height = 60         # 设置字母的高度
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象：
font = ImageFont.truetype('arial.ttf', 36)  # 设置系统自带的字体，winds下在C:\Windows\Fonts中
# 创建Draw对象：
draw = ImageDraw.Draw(image)
# 填充每个像素：
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字：
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊：
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
