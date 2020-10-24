import numpy as np
import cv2
import sys 

imagePath = sys.argv[1]

image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

while(True):
	cv2.imshow('frame',gray)

	key = cv2.waitKey(1)

	if key == 27:
		break

cv2.destroyAllWindows()
