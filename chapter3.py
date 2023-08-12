import cv2
import numpy as np

img = cv2.imread("Resources\Lambo.png")
print(img.shape)
cv2.imshow("Image", img)



# ---------------------------------------------


# Resize Methode

imgResize = cv2.resize(img, (300, 200))
# the secend parameter is recive x and y but return y and x in shape function. 
print(imgResize.shape)
cv2.imshow("Image Resize", imgResize)



# ---------------------------------------------


# Cropp Methode

imgCropped = img[0:200, 200:500]
# in this methode tow parameters, the first parameter is start x and y point
# and the secend parameter is end x and y point
cv2.imshow("Image Crpped", imgCropped)


cv2.waitKey(0)