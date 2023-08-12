import cv2
import numpy as np


# Create a blank page

img = np.zeros((512, 512, 3), np.uint8)
# page size --> 512, 512
print(img.shape)

# img[:] = 255, 0, 0
#for change page color
# 1 - [:] = all pixels
# 2 - [y1, x1 : y2, x2] = start and end pixels
cv2.imshow("Image", img)



# ---------------------------------------------


# Drawing Line

cv2.line(img, (0,0), (300, 300), (0, 255, 0), 5)
# parameters : image, start point, end point, color, thickness
# note : In this method, the points are based on x, y but in shape methode the points are based y, x
cv2.imshow("Line", img)



# ---------------------------------------------


# Drawing Rectangle

cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 3)
# parameters : image, start point(top left), end point(bottom right), color, thickness ('''you can use cv2.FILLED''')
# note : In this method, the points are based on x, y but in shape methode the points are based y, x
cv2.imshow("Rectangle", img)



# ---------------------------------------------


# Drawing Circle

cv2.circle(img, (400, 400), 30, (255, 255, 0), 5)
# parameters : image, center circle point, radius, color, thickness
cv2.imshow("Circle", img)



# ---------------------------------------------


# Put Text

cv2.putText(img, " OPENCV ", (100, 200), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 150, 0), 7)
# parameters : image, text, start point, font, font size, color, thickness
cv2.imshow("Text", img)

cv2.waitKey(0)