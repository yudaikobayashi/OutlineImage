import sys
import numpy as np
import cv2


if len(sys.argv) != 3:
    print("Usage: outline.py <input file> <output directory>")
    exit(1)

width = 5 # some odd number
color = np.array([0,0,0,255])

gray = cv2.imread(sys.argv[1], 0)
alpha = cv2.imread(sys.argv[1], -1)
kernel = np.ones((width,width))

dilation = cv2.dilate(gray, kernel, iterations=3)

for i in range(np.shape(gray)[0]):
    for j in range(np.shape(gray)[1]):
        if alpha[i,j,3] == 0 and dilation[i,j] == 255:
            alpha[i,j] = color

cv2.imwrite(sys.argv[2] + "/" + sys.argv[1], alpha)
