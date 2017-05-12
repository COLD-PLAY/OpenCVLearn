# -*- coding=utf-8 -*-
import cv2
import numpy as np

# 读取一张廖舟的自拍照
img = cv2.imread('data/handsome.jpg')

# 沿着横纵轴放大1.6 倍，然后平移(-150, -240)，最后沿原图大小截取，等效于裁剪并放大。
M_corp_liaozhou = np.array([
	[1.6, 0, -150],
	[0, 1.6, -240]
], dtype = np.float32)

img_liaozhou = cv2.warpAffine(img, M_corp_liaozhou, (640, 640))

cv2.imwrite('output/handsome_corp.jpg', img_liaozhou)
# cv2.imshow('handsome_corp', img_liaozhou)

# x 轴的剪切变换，角度15
theta = 15 * np.pi / 180
M_shear = np.array([
	[1, np.tan(theta), 0],
	[0, 1, 0]
], dtype=np.float32)

img_sheared = cv2.warpAffine(img, M_shear, (640, 640))
cv2.imwrite('output/handsome_sheared.jpg', img_sheared)
# cv2.imshow('handsome_sheared', img_sheared)

# 顺时针旋转，角度15
M_rotate = np.array([
	[np.cos(theta), -np.sin(theta), 0],
	[np.sin(theta), np.cos(theta), 0]
], dtype=np.float32)

img_rotate = cv2.warpAffine(img, M_rotate, (640, 640))
cv2.imwrite('output/handsome_rotate.jpg', img_rotate)
# cv2.imshow('handsome_rotate', img_rotate)

# 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
M = np.array([
	[1, 1.5, -400],
	[0.5, 2, -100]
], dtype=np.float32)

img_transformed = cv2.warpAffine(img, M, (640, 640))
cv2.imwrite('output/handsome_transformed.jpg', img_transformed)
cv2.imshow('handsome_transformed', img_transformed)

cv2.waitKey()