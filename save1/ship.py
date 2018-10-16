import pygame

class Ship():
	def __init__(self,screen,setting):
		self.screen=screen

		self.image=pygame.image.load('images/yuyuko/yuyuko1.png')
		self.images=[]
		for i in range(32):
			s='images/yuyuko/yuyuko'+str(1)+'.png'

		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		self.rect.centerx=float(self.screen_rect.centerx)
		self.rect.bottom=float(self.screen_rect.bottom)

		self.x=float(self.rect.centerx)
		self.y=float(self.rect.centery)

		self.go_left=False
		self.go_right=False
		self.go_up=False
		self.go_down=False
		self.shooting=False
		self.slow=False

		self.fast_speed=1.0
		self.slow_speed=0.5
		self.speed=self.fast_speed


	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self,setting):
		if self.slow:
			self.speed=self.slow_speed
		else:
			self.speed=self.fast_speed
		if self.go_left and self.x>0:
			self.x-=self.speed
		if self.go_right and self.x<setting.scr_width:
			self.x+=self.speed
		if self.go_up and self.y>0:
			self.y-=self.speed
		if self.go_down and self.y<setting.scr_height:
			self.y+=self.speed

		self.rect.centerx=self.x
		self.rect.centery=self.y