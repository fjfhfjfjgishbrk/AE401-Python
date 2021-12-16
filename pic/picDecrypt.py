import cv2
import numpy as np

alpha = "abcdefghijklmnopqrstuvwxyz"
message = ""

#imageOri = cv2.imread("a.jpg", cv2.IMREAD_UNCHANGED)
imageDec = cv2.imread("b.png", cv2.IMREAD_UNCHANGED)

for i in imageDec:
    for j in i:
        print(j)
        message += alpha[255 - j[3]]

print(message)