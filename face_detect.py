import cv2, sys

# get user supplied values
# imagePath = sys.argv[1]
# cascPath = sys.argv[2]

def facedetect(imagePath, faceCascPath, eyeCascPath):
	# create the haar
	facecascade = cv2.CascadeClassifier(faceCascPath)
	eyecascade = cv2.CascadeClassifier(eyeCascPath)

	# read the image
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# delete faces in the image
	faces = facecascade.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (30, 30),
		flags = cv2.CASCADE_SCALE_IMAGE
	)

	eyes = eyecascade.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (30, 30),
		flags = cv2.CASCADE_SCALE_IMAGE
	)

	print "Found {0} faces!".format(len(faces))

	# draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
		# cv2.imshow('Faces found', image)
	for (x, y, w, h) in eyes:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
		# cv2.imshow('Eyes found', image)
	
	cv2.imshow('Faces found', image)
	cv2.waitKey(0)

if __name__ == '__main__':
	# imagePath = input('please input image path: ')
	# cascPath = input('please input casc path: ')
	# imagePath = sys.argv[1]
	# cascPath = sys.argv[2]

	imagePath = 'test0.png'
	# imagePath = 'test1.jpg'
	# imagePath = 'test2.jpg'
	# imagePath = '/home/coldplay/Desktop/wifi.jpg'
	faceCascPath = 'haarcascade_frontalface_alt.xml'
	eyeCascPath = 'haarcascade_eye.xml'
	facedetect(imagePath, faceCascPath, eyeCascPath);