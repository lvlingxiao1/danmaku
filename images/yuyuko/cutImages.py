import cv2

FILENAME='yuyuko'
EXT='.png'
ROW=8
COL=4
SIZE=36

k=0

a=cv2.imread(FILENAME+EXT,cv2.IMREAD_UNCHANGED)
"""
b=a[0:36,0:36]
cv2.imwrite('123.png',b)
"""
for i in range(ROW):
	for j in range(COL):
		s=FILENAME+str(k)+EXT
		cv2.imwrite(s,a[i*SIZE:(i+1)*SIZE,j*SIZE:(j+1)*SIZE])
		k+=1