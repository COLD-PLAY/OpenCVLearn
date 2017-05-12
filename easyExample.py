# -*- coding=utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

# img = np.array([
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#     [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
#     [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
# ], dtype=np.uint8)

# save with matplotlib
# plt.imsave('output/img_pyplot.png', img)

# save with OpenCV
# cv2.imwrite('output/img_cv2.jpg', img)

# img_pyplot = cv2.imread('output/img_pyplot.png')
# img_cv2 = cv2.imread('output/img_cv2.jpg')

# show images
# cv2.imshow('img_pyplot.png', img_pyplot)
# cv2.imshow('img_cv2.jpg', img_cv2)

# beauty = cv2.imread('/home/coldplay/Desktop/beauty.jpg')
# beauty_gray = cv2.cvtColor(beauty, cv2.COLOR_BGR2GRAY)

# cv2.imshow('beauty_gray', beauty_gray)

# # read one picture of 640x640
# color_img = cv2.imread('/home/coldplay/Desktop/beauty.jpg')
# print color_img.shape

# # read solar directally
# gray_img = cv2.imread('/home/coldplay/Desktop/beauty.jpg', cv2.IMREAD_GRAYSCALE)
# print gray_img.shape

# # save with solar, read it again, it's still 3
# cv2.imwrite('output/beauty_gray.jpg', gray_img)
# reload_grayscale = cv2.imread('output/beauty_gray.jpg')
# print reload_grayscale.shape

# # cv2.IMWRITE_JPEG_QUALITY point the quality of jpg, from 0 to 100, default is 95
# cv2.imwrite('output/beauty.jpg', color_img)
# cv2.imwrite('output/beauty_100.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 100))
# cv2.imwrite('output/beauty_80.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))
# cv2.imwrite('output/beauty_5.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 5))

# read one picture
img = cv2.imread('/home/coldplay/Desktop/beauty_boy.jpg')

# 缩放成200x200的方形图像
# img_resize = cv2.resize(img, (600, 600))

# 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
# 等效于img_200x300 = cv2.resize(img, (300, 200))，注意指定大小的格式是(宽度,高度)
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
# img_resize = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_NEAREST)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像
# img_resize = cv2.copyMakeBorder(img, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value = (0, 0, 0))

img_resize = img[20:150, -180:-50]

cv2.imshow('/home/coldplay/Desktop/beauty_boy.jpg', img_resize)
cv2.waitKey()