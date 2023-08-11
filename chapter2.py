import cv2

img = cv2.imread("Resources\Lena.png")

# Gray Scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)



# ---------------------------------------------


# Blur Scale

imgBlur = cv2.GaussianBlur(imgGray, (19, 19), 0)
# parameters --> image, (tow odd number for blure size),
# (this parameter is the blur impact rate, the 0 is no rate and auto impact)

cv2.imshow("Blur Image", imgBlur)



# ---------------------------------------------


# Canny Detection

imgCanny = cv2.Canny(img, 150, 200)
# parameters --> image, (low threshold), (high threshold)
cv2.imshow("Canny Image", imgCanny)



# ---------------------------------------------


# Dialation

import numpy as np
kernel = np.ones((5, 5), np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=3)
cv2.imshow("Dialation Image", imgDialation)



# ---------------------------------------------


# Eroded
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Eroded Image", imgEroded)


cv2.waitKey(0)
