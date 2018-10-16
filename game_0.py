import pygame
from gameSetting import Setting
from background import Background
from player import Player
from game_func import check_event,update_screen,miss
from pygame.sprite import Group
from enemy import Enemy
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def main():
	pygame.init()
	setting=Setting()

	clock=pygame.time.Clock()
	fps=setting.FPS
	H=setting.scr_height
	W=setting.scr_width
	
	screen=pygame.display.set_mode((W+300,H))
	pygame.display.set_caption('Hmmmmmmm...')

	bg=Background(screen,setting)

	players=Group()
	p1bullets=Group()
	enemies=Group()
	enemy_bul=Group()

	player=Player(screen,setting,p1bullets)
	
	players.add(player.hit_box)
	enemies.add(Enemy(setting,enemy_bul,player,screen))

	stats=GameStats(setting)

	play_button=Button(setting,screen,'Play')

	scoreboard=Scoreboard(setting,screen,stats)

	while 1:

		check_event(player,enemies,stats,play_button)

		if stats.game_state==1:
			player.update()
			p1bullets.update()

			enemies.update()
			enemy_bul.update()

			for i in p1bullets.copy():
				if i.rect.bottom<=0 or i.rect.top>=H or i.rect.left>=W or i.rect.right<=0:
					p1bullets.remove(i)
			for i in enemy_bul.copy():
				if i.rect.bottom<=0 or i.rect.top>=H or i.rect.left>=W or i.rect.right<=0:
					enemy_bul.remove(i)


			'''
			collide_dict=pygame.sprite.groupcollide(p1bullets,enemies,False,False)
			for i in collide_dict:
				if collide_dict[i]:
					i.destroy()

			collide_dict=pygame.sprite.groupcollide(p1bullets,enemy_bul,False,False)
			for i in collide_dict:
				if collide_dict[i]:
					collide_dict[i][0].destroy()
					i.destroy()
			'''
			collide_dict=pygame.sprite.groupcollide(p1bullets,enemies,True,False)
			for i in collide_dict:
				stats.score+=setting.hit_sc

			stats.score+=setting.time_sc

			if stats.score>stats.hscore:
				stats.hscore=stats.score

			collide_dict=pygame.sprite.spritecollide(player.hit_box,enemy_bul,False)
			for i in collide_dict:
				miss(stats,player,enemy_bul)
				break
			
		update_screen(screen,bg,player,p1bullets,enemies,enemy_bul,play_button,stats,scoreboard,setting)

		#print(clock.get_fps())
		clock.tick(fps)

main()




"""
彈幕對決
"""