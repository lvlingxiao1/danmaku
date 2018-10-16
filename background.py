import pygame
from pygame import Rect

class Background():
	def __init__(self,screen,setting):
		self.img=pygame.image.load("images/bg.png")
		self.screen=screen
		self.rect=Rect(0,0,setting.scr_width,setting.scr_height)

	def draw(self):
		self.screen.blit(self.img,self.rect)