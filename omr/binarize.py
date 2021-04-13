import cv2

img = cv2.imread('omr/images/input.png',0)
# maybe ADAPTIVE_THRESH_GAUSSIAN_C
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,8)
cv2.imwrite('omr/images/binarized.png', img)

# then truncate the image and run:
#python tf-end-to-end/ctc_predict.py -image ./omr/images/truncated.png -model ./tf-end-to-end/Models/semantic_model.meta -vocabulary ./tf-end-to-end/Data/vocabulary_semantic.txt