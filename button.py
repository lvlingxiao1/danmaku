import pygame.font

class Button():
	def __init__(self,setting,screen,msg):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.setting=setting

		self.width,self.height=200,50
		self.color=(0,255,0)
		self.txt_color=(255,255,255)
		self.font=pygame.font.SysFont(None,48)

		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.centerx=self.setting.scr_width/2
		self.rect.centery=self.setting.scr_height/2

		self.prep_msg(msg)

	def prep_msg(self,msg):
		self.msg_img=self.font.render(msg,True,self.txt_color,self.color)
		self.msg_img_rect=self.msg_img.get_rect()
		self.msg_img_rect.center=self.rect.center

	def draw(self):
		self.screen.fill(self.color,self.rect)
		self.screen.blit(self.msg_img,self.msg_img_rect)