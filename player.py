import pygame,random,math
from bullet import Bullet
from loadPlayer00 import getNormal,getLR
from pygame.sprite import Sprite
from pygame import Rect

class Player():
	def __init__(self,screen,setting,bullets,name='reimu',speed=6.0):
		
		self.screen=screen
		self.bullets=bullets
		self.setting=setting

		#Load images
		self.imagesN=getNormal()
		self.imagesL,self.imagesR=getLR()
		self.image=self.imagesN[0]
		self.slow_effect0=pygame.image.load('images/eff_sloweffect.png')
		self.slow_effect=None
		self.shoot1=pygame.image.load('images/player00 (2).png').subsurface((0,144,64,16))
		self.shoot1=pygame.transform.rotate(self.shoot1,90)

		#Rect
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=float(self.setting.scr_width)/2
		self.rect.bottom=float(self.setting.scr_height)-30
		self.x=float(self.rect.centerx)
		self.y=float(self.rect.centery)

		self.hit_box=Sprite()
		self.hit_box.rect=Rect(0,0,4,4)

		#Self constants
		self.shoot_cd1=8
		self.shoot_cd2=60

		self.fast_speed=speed
		self.slow_speed=self.fast_speed/2
		self.speed=self.fast_speed
		self.reborn()
		self.update()

	def reborn(self):
		self.rect.centerx=float(self.setting.scr_width)/2
		self.rect.bottom=float(self.setting.scr_height)-30
		self.x=float(self.rect.centerx)
		self.y=float(self.rect.centery)

		self.go_left=False
		self.go_right=False
		self.go_up=False
		self.go_down=False
		self.shooting=False
		self.shooting2=False
		self.slow=False
		self.anime=[0,0,0]
		self.anime_slow=0
		self.cd1=0
		self.cd2=0

	def blitme(self):
		self.screen.blit(self.image,self.rect)
		self.screen.fill((0,0,0),self.hit_box.rect)
		if self.slow:
			self.screen.blit(self.slow_effect,self.slow_rect)

	def update(self):
		# Speed control
		if self.slow:
			self.speed=self.slow_speed
		else:
			self.speed=self.fast_speed
		
		#Left/Right motion and animation
		if self.go_left and (not self.go_right) and self.x-16>0:
			self.x-=self.speed
			self.update_image(1)
		elif self.go_right and (not self.go_left) and self.x+16<self.setting.scr_width:
			self.x+=self.speed
			self.update_image(2)
		elif not (self.go_left ^ self.go_right):
			self.update_image(0)
		
		#Up and down
		if self.go_up and not self.go_down and self.y-24>0:
			self.y-=self.speed
		elif self.go_down and not self.go_up and self.y+24<self.setting.scr_height:
			self.y+=self.speed

		#Sync position
		self.rect.centerx=self.x
		self.rect.centery=self.y
		self.hit_box.rect.centerx=self.x
		self.hit_box.rect.centery=self.y

		#Shooting
		if self.cd1>0:
			self.cd1-=1
		if self.cd2>0:
			self.cd2-=1

		if self.shooting and self.cd1==0:
			new_bul=Bullet(self.bullets,self.screen,self.rect,self.shoot1,-10,0,speed=32)
			self.bullets.add(new_bul)
			new_bul=Bullet(self.bullets,self.screen,self.rect,self.shoot1,10,0,speed=32)
			self.bullets.add(new_bul)
			self.cd1=self.shoot_cd1

		if self.shooting2 and self.cd2==0:
			for i in range(100):
				new_bul=self.gen_bullet_2()
				self.bullets.add(new_bul)
			self.cd2=self.shoot_cd2		

	def gen_bullet_2(self):
		angle=random.random()*6.2831
		angle_d=int(angle/math.pi*180-90)
		self.shoot2=pygame.transform.rotate(self.shoot1,angle_d)
		new_bul=Bullet(self.bullets,self.screen,self.rect,self.shoot2,0,0,6,angle)
		return new_bul

	def update_image(self,k):
		self.anime[k]+=1
		if k==0:
			self.anime[1]=0
			self.anime[2]=0
			if self.anime[0]==40:
				self.anime[0]=0
			self.image=self.imagesN[self.anime[0]//10]
		elif k==1:
			self.anime[2]=0
			if self.anime[1]==70:
				self.anime[1]=69
			else:
				self.image=self.imagesL[self.anime[1]//10]
		elif k==2:
			self.anime[1]=0
			if self.anime[2]==70:
				self.anime[2]=69
			else:
				self.image=self.imagesR[self.anime[2]//10]

		if self.slow:
			self.anime_slow+=1
			if self.anime_slow==360:
				self.anime_slow=0
			self.slow_effect=pygame.transform.rotate(self.slow_effect0,self.anime_slow)
			self.slow_rect=self.slow_effect.get_rect()
			self.slow_rect.centerx=self.rect.centerx
			self.slow_rect.centery=self.rect.centery



