import cv2
import numpy as np


def none(x):
    pass


imagePlants = cv2.imread('data/imagePlant.jpg')
imagePlantsHsv = cv2.cvtColor(imagePlants, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Calibrate')

cv2.createTrackbar('H min', 'Calibrate', 35, 179, none)
cv2.createTrackbar('H max', 'Calibrate', 90, 179, none)
cv2.createTrackbar('S min', 'Calibrate', 40, 255, none)
cv2.createTrackbar('S max', 'Calibrate', 255, 255, none)
cv2.createTrackbar('V min', 'Calibrate', 40, 255, none)
cv2.createTrackbar('V max', 'Calibrate', 255, 255, none)


while True:
    h_min = cv2.getTrackbarPos('H min', 'Calibrate')
    h_max = cv2.getTrackbarPos('H max', 'Calibrate')
    s_min = cv2.getTrackbarPos('S min', 'Calibrate')
    s_max = cv2.getTrackbarPos('S max', 'Calibrate')
    v_min = cv2.getTrackbarPos('V min', 'Calibrate')
    v_max = cv2.getTrackbarPos('V max', 'Calibrate')

    lower_green = np.array([h_min, s_min, v_min])
    upper_green = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imagePlantsHsv, lower_green, upper_green)
    result = cv2.bitwise_and(imagePlants, imagePlants, mask=mask)

    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    stack = np.vstack([imagePlants, mask_3, result])

    stack_resized = cv2.resize(stack, (0, 0), fx=0.4, fy=0.4)

    cv2.imshow("Results", stack_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
