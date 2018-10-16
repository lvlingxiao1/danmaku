import pygame

FILENAME='images\player00.png'

def getNormal():
	img=pygame.image.load(FILENAME)
	A=[]
	for i in range(4):
		A.append(img.subsurface(pygame.Rect(32*i,0,32,48)))
	return A

def getLR():
	img=pygame.image.load(FILENAME)
	A=[]
	B=[]
	for i in range(7):
		imgL=img.subsurface(pygame.Rect(32*i,48,32,48))
		imgR=pygame.transform.flip(imgL,True,False)
		A.append(imgL)
		B.append(imgR)
	return A,B

def main():
	A=getNormal()



if __name__ == '__main__':
	main()
