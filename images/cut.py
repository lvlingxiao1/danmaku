import cv2
x=0
y=0

a=cv2.imread('etama.png',cv2.IMREAD_UNCHANGED)

b=a[y:x+12,y:y+12]

cv2.imwrite('dan1.png',b)