import cv2
import numpy as np


def none(x):
    pass


videoDrone = cv2.VideoCapture('data/plantVideo.mp4')

cv2.namedWindow('Control')

cv2.createTrackbar('H min', 'Control', 35, 179, none)
cv2.createTrackbar('H max', 'Control', 85, 179, none)
cv2.createTrackbar('S min', 'Control', 45, 255, none)
cv2.createTrackbar('S max', 'Control', 255, 255, none)
cv2.createTrackbar('V min', 'Control', 45, 255, none)
cv2.createTrackbar('V max', 'Control', 255, 255, none)

while True:
    _, imageD = videoDrone.read()

    videoDroneHsv = cv2.cvtColor(imageD, cv2.COLOR_BGR2HSV)

    H_min = cv2.getTrackbarPos('H min', 'Control')
    H_max = cv2.getTrackbarPos('H max', 'Control')
    S_min = cv2.getTrackbarPos('S min', 'Control')
    S_max = cv2.getTrackbarPos('S max', 'Control')
    V_min = cv2.getTrackbarPos('V min', 'Control')
    V_max = cv2.getTrackbarPos('V max', 'Control')

    lower_green = np.array([H_min, S_min, V_min])
    upper_green = np.array([H_max, S_max, V_max])

    windowGreen = np.zeros_like(imageD)
    windowGreen[:] = (0, 255, 0)

    mask = cv2.inRange(videoDroneHsv, lower_green, upper_green)

    height, length, _ = imageD.shape
    greenArea = cv2.countNonZero(mask)
    totalArea = height * length
    biomass = (greenArea / totalArea) * 100

    results = cv2.bitwise_and(imageD, imageD, mask=mask)
    resultsGreen = cv2.bitwise_and(imageD, windowGreen, mask=mask)
    cv2.putText(imageD, f'Biomass: {biomass:.2f}%', (10, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 2)

    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    stack = np.vstack([imageD, mask_3])
    stack1 = np.vstack([resultsGreen, results])
    grid = np.hstack([stack, stack1])

    resized = cv2.resize(grid, (0, 0), fx=0.4, fy=0.4)

    cv2.imshow('Window', resized)

    if cv2.waitKey(1) & 0xFF == ord('f'):
        break


cv2.destroyAllWindows()
