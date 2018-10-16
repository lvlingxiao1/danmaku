import pygame,sys,time
import pygame.font

pygame.font.init()
BIGFONT=pygame.font.SysFont(None,190)
GAMEOVER=BIGFONT.render('GAME OVER',True,(0,0,0,0))
GAMEOVER_rect=GAMEOVER.get_rect()

def check_event(player,enemy,stats,play_button):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			save_hs(stats)
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			key_down(event.key,player)
		elif event.type==pygame.KEYUP:
			key_up(event.key,player)
		elif event.type==pygame.MOUSEBUTTONDOWN:
			if stats.game_state==0:
				x,y=pygame.mouse.get_pos()
				check_play_button(stats,play_button,x,y,enemy)
			elif stats.game_state==2:
				stats.game_state=0
				stats.reset()

def save_hs(stats):
	f=open('highscore.py','w')
	f.write('HSCORE=%s'%stats.hscore)
	f.close()

def update_screen(scr,bg,player,bullets,enemy,enemy_bul,play_button,stats,sb,setting):
	scr.fill(setting.bg_colour)
	bg.draw()
	player.blitme()
	for i in bullets:
		i.blitme()
	for i in enemy:
		i.blitme()
	for i in enemy_bul:
		i.blitme()
	sb.draw()
	if stats.game_state==0:
		play_button.draw()
	if stats.game_state==2:
		GAMEOVER_rect.centerx=setting.scr_width/2
		GAMEOVER_rect.centery=setting.scr_height/2
		scr.blit(GAMEOVER,GAMEOVER_rect)
	pygame.display.flip()

def check_play_button(stats,play_button,x,y,enemy):
	if play_button.rect.collidepoint(x,y):
		stats.game_state=1
		pygame.mouse.set_visible(False)
		for i in enemy:
			i.reset()

def key_up(key,player):
	if key==pygame.K_RIGHT:
		player.go_right=False
	if key==pygame.K_LEFT:
		player.go_left=False
	if key==pygame.K_DOWN:
		player.go_down=False
	if key==pygame.K_UP:
		player.go_up=False
	if key==pygame.K_LSHIFT:
		player.slow=False
	if key==pygame.K_z:
		player.shooting=False
	if key==pygame.K_x:
		player.shooting2=False

def key_down(key,player):
	if key==pygame.K_RIGHT:
		player.go_right=True
	if key==pygame.K_LEFT:
		player.go_left=True
	if key==pygame.K_DOWN:
		player.go_down=True
	if key==pygame.K_UP:
		player.go_up=True
	if key==pygame.K_LSHIFT:
		player.slow=True
	if key==pygame.K_z:
		player.shooting=True
	if key==pygame.K_x:
		player.shooting2=True

def miss(stats,player,enemy_bul):
	if stats.life_left>0:
		stats.life_left-=1
	else:
		stats.game_state=2
		pygame.mouse.set_visible(True)

	player.reborn()
	enemy_bul.empty()
	time.sleep(0.5)