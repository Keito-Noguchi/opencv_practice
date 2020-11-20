import cv2
import numpy as np

im = cv2.imread('/Users/keito/Pictures/images/IMG_0567s.jpg')
print(im.shape)
# (426, 640, 3)

print(im.dtype)
#unit8

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(im_gray.shape)
# (426, 640)

print(im_gray.dtype)
# uint8

cv2.imwrite('/Users/keito/Pictures/images/opencv_gray_cvtcolr.jpg', im_gray)
