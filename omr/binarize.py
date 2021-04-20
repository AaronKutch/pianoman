import cv2
import numpy as np

img = cv2.imread('omr/images/input.png',0)

# even at 1080p, the lines will still be 2-3 pixels across, so we must upscale
img = cv2.pyrUp(img)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,8)
# smooth out some of the roughness
img = cv2.bilateralFilter(img, 9, 256, 256)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,8)

cv2.imwrite('omr/images/binarized.png', img)
