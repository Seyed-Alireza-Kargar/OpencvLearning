import cv2
import numpy as np

img = cv2.imread('Resources\Lena.png')

cv2.imshow('img', img)

imgHor = np.hstack((img, img))

cv2.imshow("horizontal", imgHor)

cv2.waitKey(0)