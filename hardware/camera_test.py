import cv2
import time

# intended for a wansview 1080p camera
vid = cv2.VideoCapture(0)
if not vid.isOpened():
    raise IOError("Cannot open webcam")

vid.set(cv2.CAP_PROP_FPS, 10) # the camera has maximum resolution at low framerate
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while(True):
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    time.sleep(0.1)

    # the 'q' button is set as the
    # quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imwrite('omr/images/input.png', frame)
vid.release()
cv2.destroyAllWindows()
