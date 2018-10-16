import pygame,random,math
from bullet import Bullet
from pygame.sprite import Sprite

class Enemy(Sprite):
	def __init__(self,settings,bullets,target,screen):
		super().__init__()
		self.screen=screen
		self.bullets=bullets
		self.target=target
		self.image0=pygame.image.load('images/stg4aenm.png')
		self.image=self.image0.subsurface((0,0,64,80))
		
		self.rect=self.image.get_rect()
		self.x=settings.scr_width//2
		self.y=200
		self.rect.centerx=self.x
		self.rect.centery=self.y

		self.shoot1=pygame.image.load('images/player00 (2).png').subsurface((32,176,16,16))
		self.shoot2=pygame.image.load('images/player00 (2).png').subsurface((32,176,16,16))

		self.p1time=100000
		self.p2time=10000
		self.p1cd=30
		self.p2cd=20

		self.reset()

	def reset(self):
		self.timer=0
		self.phase=1
		self.cd1=0
		self.cd2=0

	def update(self):
		if self.phase==0:
			self.image=self.image0.subsurface((0,0,64,80))
		
		if self.phase==1:
			self.phase1()	
			if self.timer==self.p1time:
				self.phase=2

		if self.phase==2:
			#self.phase1()
			self.phase2()
			if self.timer==self.p2time:
				self.phase=0

		self.timer+=1
		self.cd1-=1
		self.cd2-=1
		
		self.rect.centerx=self.x
		self.rect.centery=self.y

	def phase1(self):
		if self.cd1<=0:
			for i in range(100):
				new_bul=self.gen_phase1_bullet()
				self.bullets.add(new_bul)
			self.cd1=self.p1cd


	def gen_phase1_bullet(self):
		angle=random.random()*6.2831
		angle_d=int(angle/math.pi*180-90)
		self.shoot2=pygame.transform.rotate(self.shoot1,angle_d)
		new_bul=Bullet(self.bullets,self.screen,self.rect,self.shoot2,0,0,3,angle)
		return new_bul

	def phase2(self):
		if self.cd2<=0:
			new_bul=self.gen_phase2_bullet(-100)
			self.bullets.add(new_bul)
			new_bul=self.gen_phase2_bullet(100)
			self.bullets.add(new_bul)
			self.cd2=p2cd

	def gen_phase2_bullet(self,xshift):
		angle=math.atan((self.target.y-self.y)/(self.target.x-self.x))
		if self.target.x<self.x:
			angle+=math.pi
		angle_d=int(angle/math.pi*180-90)
		self.shoot2=pygame.transform.rotate(self.shoot1,angle_d)
		new_bul=Bullet(self.bullets,self.screen,self.rect,self.shoot2,xshift,0,3,angle)
		return new_bul

	def blitme(self):
		self.screen.blit(self.image,self.rect)
