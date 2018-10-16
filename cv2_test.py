import cv2

a=cv2.imread('images\\dan.png')
a=cv2.resize(a,(1000,1000),interpolation = cv2.INTER_CUBIC)
cv2.imshow('image',a)

cv2.waitKey(0) 