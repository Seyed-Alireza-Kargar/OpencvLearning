import cv2



# --> import image <--

# img = cv2.imread("Resources\Lenna.png")

# cv2.imshow("output", img)
# cv2.waitKey(0)


# --> import video or using webcam <--

# for using webcam add to valiue equel to 0 or 1
cap = cv2.VideoCapture("Resources/test_video.mp4")
# cap.set(3, 176)
# cap.set(4, 144)
# cap.set(10, 1)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
