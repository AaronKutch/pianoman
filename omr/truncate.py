# This script requires the input image to have been taken with the staff lines at the center and
# and almost perfectly horizontal. If the script truncates too much, take the image from farther
# away.

import cv2
import numpy as np

img = cv2.imread('omr/images/binarized.png',0)
edges = cv2.Canny(img, 64, 192)

cv2.imwrite('omr/images/edges.png', edges)

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 64  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 128  # minimum number of pixels making up a line
max_line_gap = 64  # maximum gap in pixels between connectable line segments
line_image = np.copy(img) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# This is a pretty bad hack, but this is really the only solution because of how insanely
# slow and bad dynamic programming languages are. Simple iteration over a 8000x6000 image takes
# minutes, so instead we resort to this.

# draw very thick lines, which fills in the staff as a solid block
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 32)

half_len_x = line_image.shape[1] // 2
half_len_y = line_image.shape[0] // 2

#print(line_image.shape[0])
#print(line_image.shape[1])

# starting from the center, find the staff
staff_y = half_len_y
for i in range(half_len_y):
    if line_image[half_len_y + i, half_len_x] == 255:
        staff_y = half_len_y + i
        break
    if line_image[half_len_y - i, half_len_x] == 255:
        staff_y = half_len_y - i
        break

# find the staff height
staff_min_y = staff_y
staff_max_y = staff_y
min_notdone = True
max_notdone = True
for i in range(max(half_len_y - staff_y, staff_y)):
    if max_notdone and line_image[staff_y + i, half_len_x] == 0:
        staff_max_y = staff_y + i
        max_notdone = False
    if min_notdone and line_image[staff_y - i, half_len_x] == 0:
        staff_min_y = staff_y - i
        min_notdone = False
    if max_notdone:
        line_image[staff_y + i, half_len_x] = 128
    if min_notdone:
        line_image[staff_y - i, half_len_x] = 128

# find the staff width
middle_y = (staff_min_y + staff_max_y) // 2
staff_min_x = half_len_x
staff_max_x = half_len_x
min_notdone = True
max_notdone = True
for i in range(half_len_x):
    if max_notdone and line_image[middle_y, half_len_x + i] == 0:
        staff_max_x = half_len_x + i
        max_notdone = False
    if min_notdone and line_image[middle_y, half_len_x - i] == 0:
        staff_min_x = half_len_x - i
        min_notdone = False
    if max_notdone:
        line_image[middle_y, half_len_x + i] = 128
    if min_notdone:
        line_image[middle_y, half_len_x - i] = 128

#print(staff_min_y)
#print(staff_max_y)
#print(staff_min_x)
#print(staff_max_x)

# write for debugging purposes
cv2.imwrite('omr/images/line_image.png', line_image)

# expand in the y axis because of notes that extend above and below
height = staff_max_y - staff_min_y
height = height * 0.2
staff_max_y = int(staff_max_y + height)
staff_min_y = int(staff_min_y - height)

# save truncated image
cv2.imwrite('omr/images/truncated.png', img[staff_min_y:staff_max_y, staff_min_x:staff_max_x])
