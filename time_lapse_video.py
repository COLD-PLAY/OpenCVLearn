# coding=utf-8
import cv2
import numpy as np
import time

interval = 6		# 捕获图像的间隔，单位：秒
num_frames = 500		# 捕获图像的总帧数
out_fps = 24			# 输出文件的帧率

# VideoCapture(0) 表示打开默认的相机
cap = cv2.VideoCapture(0)

# 获取捕获的分辨率
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 设置要保存视频的编码，分辨率和帧率
video = cv2.VideoWriter(
	'output/time_lapse.avi',
	cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
	out_fps,
	size
)

# 对于一些低画质的摄像头，前面的帧可能不稳定，略过
for i in range(42):
	cap.read()

# 开始捕获，通过read()函数获取捕获的帧
try:
	for i in range(num_frames):
		_, frame = cap.read()
		video.write(frame)

		# 如果希望把每一帧也存成文件，比如制作GIF，则取消下面的注释
        # filename = 'output/{:0>6d}.png'.format(i)
        # cv2.imwrite(filename, frame)

		print 'Frame {} is captured.'.format(i)
		time.sleep(interval)

except KeyboardInterrupt:
	# 提前停止捕获
	print 'Stopped! {}/{} frames" captured!'.format(i, num_frames)

# 释放资源并写入视频文件
video.release()
cap.release()