# -*- coding=utf-8 -*-
import cv2, os, sys

# 第一个输入参数是包含视频片段的路径
# input_path = sys.argv[1]
input_path = 'data/video'

# 第二个输入参数是设定每隔多少帧截取一帧
# frame_interval = int(sys.argv[2])
frame_interval = 1

# 列出文件夹下所有的视频文件
filenames = os.listdir(input_path)

# 获取文件夹名称
video_prefix = input_path.split(os.sep)[-1]

# 建立一个新的文件夹，名称为原文件夹名称后加上_frames
frame_path = '{}_frames'.format(input_path)

if not os.path.exists(frame_path):
	os.mkdir(frame_path)

# 初始化一个VideoCapture对象
cap = cv2.VideoCapture()

# 遍历所有文件
for filename in filenames:
	filepath = os.sep.join([input_path, filename])

	# VideoCapture::open函数可以从文件获取视频
	cap.open(filepath)

   	# 获取视频帧数
	n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	# 同样为了避免视频头几帧质量低下，黑屏或者无关等
	# for i in range(42):
	# 	cap.read()

	for i in range(n_frames):
		ret, frame = cap.read()
		# 每隔frame_interval帧进行一次截屏操作
		if i % frame_interval == 0:
			imagename = '{}_{}_{:0>6d}.jpg'.format(video_prefix, filename.split('.')[0], i)
			imagepath = os.sep.join([frame_path, imagename])
			print 'exported {}!'.format(imagepath)
			cv2.imwrite(imagepath, frame)

# 执行结束释放资源
cap.release()