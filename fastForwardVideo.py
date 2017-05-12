import cv2

input_video_path = 'data/PrisonBreak3/PrisonBreakS3E1.mkv'
output_video_path = 'output/prisonbreak_forward.avi'

cap = cv2.VideoCapture(input_video_path)

n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

video = cv2.VideoWriter(
	output_video_path,
	cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
	48,
	size
)

try:
	for i in range(n_frames):
		_, frame = cap.read()
		video.write(frame)
		print 'writing the {} frames! please waiting patiently'.format(i)
except KeyboardInterrupt:
	print 'keyboardinterrupt'