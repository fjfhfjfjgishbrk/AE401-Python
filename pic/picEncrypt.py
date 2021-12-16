import cv2
import numpy as np

message = [21, 14, 3, 3, 12, 9, 14, 25, 18, 1, 7, 22, 1, 18, 6, 17, 14, 12]

imageEnc = cv2.imread("a.jpg", cv2.IMREAD_UNCHANGED)
a = 0

for i in imageEnc:
    for j in i:
        j = np.append(j, message[a])
        a = (a + 1) % len(message)

cv2.imwrite("b.png", imageEnc)
