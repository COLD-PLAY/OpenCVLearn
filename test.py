import numpy as np
import time, cv2

# a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
# print a

canvas = np.zeros((400, 600, 3), dtype=np.uint8)
canvas += 255
# print canvas

# l = [c for c in np.random.randint(0, 255, 3)]
# print l

# cap = cv2.VideoCapture('output/time_lapse.avi')
cap = cv2.VideoCapture(0)

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video = cv2.VideoWriter(
	'output/test.avi',
	cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
	24,
	size
)

try:
	for i in range(100):
		_, frame = cap.read()

		print 'this is {} pictrue'.format(i)	
		# cv2.imshow('winname', frame)
		# cv2.waitKey(1000)
		video.write(frame)
		time.sleep(6)

except KeyboardInterrupt:
	print 'interrupt'