import numpy as np
import cv2
import sys 

imagePath = sys.argv[1]

image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fullbody_cascade = cv2.CascadeClassifier('./haarcascade_fullbody.xml')


bodies = fullbody_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3
)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bodies = fullbody_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in bodies:
	cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = image[y:y+h, x:x+w]


while(True):
	cv2.imshow('frame',gray)

	key = cv2.waitKey(1)

	if key == 27:
		break

cv2.destroyAllWindows()
