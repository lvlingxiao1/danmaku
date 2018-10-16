import pygame,math
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,parent,screen,source_rect,img,xoffset=0,yoffset=0,speed=64,angle=math.pi/2):
		super().__init__()
		self.screen=screen
		self.image=img
		self.parent=parent

		self.rect=self.image.get_rect()
		self.rect.centerx=source_rect.centerx+xoffset
		self.rect.centery=source_rect.centery+yoffset

		self.x=float(self.rect.x)
		self.y=float(self.rect.y)

		self.xspeed=speed*math.cos(angle)
		self.yspeed=speed*math.sin(angle)

		self.flash=0

	def update(self):
		self.x+=self.xspeed
		self.y-=self.yspeed
		self.rect.x=self.x
		self.rect.y=self.y

	def blitme(self):
		self.screen.blit(self.image,self.rect)
		#if self.flash==0:
		#	self.screen.blit(self.image,self.rect)
		#	self.flash=1

		#elif self.flash==1:
		#	self.flash=0

	def destroy(self):
		self.parent.remove(self)




