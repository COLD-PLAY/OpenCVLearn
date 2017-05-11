import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)

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

# read one picture of 640x640
color_img = cv2.imread('/home/coldplay/Desktop/beauty.jpg')
print color_img.shape

# read solar directally
gray_img = cv2.imread('/home/coldplay/Desktop/beauty.jpg', cv2.IMREAD_GRAYSCALE)
print gray_img.shape

# save with solar, read it again, it's still 3
cv2.imwrite('output/beauty_gray.jpg', gray_img)
reload_grayscale = cv2.imread('output/beauty_gray.jpg')
print reload_grayscale.shape

# cv2.IMWRITE_JPEG_QUALITY point the quality of jpg, from 0 to 100, default is 95
cv2.imwrite('output/beauty.jpg', color_img)
cv2.imwrite('output/beauty_100.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 100))
cv2.imwrite('output/beauty_80.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))
cv2.imwrite('output/beauty_5.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 5))

cv2.waitKey()