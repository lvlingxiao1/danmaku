import pygame.font
from pygame import Rect

class Scoreboard():
	def __init__(self,setting,screen,stats):
		self.screen=screen
		self.scr_rect=screen.get_rect()
		self.setting=setting
		self.stats=stats
		self.txt_color=(60,60,60)
		self.bg_color=(0,0,0)
		self.rect=Rect(800,0,300,800)
		self.font=pygame.font.SysFont(None,36)
		self.font2=pygame.font.SysFont('Blackadder ITC',36)

	def prep(self):
		life='LIFE: %s'%self.stats.life_left
		self.l_img=self.font.render(life,True,self.txt_color)
		self.l_rect=self.l_img.get_rect()
		self.l_rect.centerx=self.rect.centerx
		self.l_rect.centery=self.rect.centery-50

		s='SCORE: %s'%'{:,}'.format(self.stats.score)
		self.s_img=self.font.render(s,True,self.txt_color)
		self.s_rect=self.s_img.get_rect()
		self.s_rect.centerx=self.rect.centerx
		self.s_rect.centery=self.rect.centery

		hs='HIGH SCORE: %s'%'{:,}'.format(self.stats.hscore)
		self.hs_img=self.font.render(hs,True,self.txt_color)
		self.hs_rect=self.hs_img.get_rect()
		self.hs_rect.centerx=self.rect.centerx
		self.hs_rect.centery=self.rect.centery+50

	def draw(self):
		self.prep()
		self.screen.fill(self.bg_color,self.rect)
		self.screen.blit(self.l_img,self.l_rect)
		self.screen.blit(self.s_img,self.s_rect)
		self.screen.blit(self.hs_img,self.hs_rect)