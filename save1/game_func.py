import pygame,sys



def check_event(ship):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			key_down(event.key,ship)
		elif event.type==pygame.KEYUP:
			key_up(event.key,ship)
			

def update_screen(scr,ship,setting):
	scr.fill(setting.bg_colour)
	ship.blitme()
	pygame.display.flip()

def key_up(key,ship):
	if key==pygame.K_RIGHT:
		ship.go_right=False
	elif key==pygame.K_LEFT:
		ship.go_left=False
	elif key==pygame.K_DOWN:
		ship.go_down=False
	elif key==pygame.K_UP:
		ship.go_up=False
	elif key==pygame.K_LSHIFT:
		ship.slow=False

def key_down(key,ship):
	if key==pygame.K_RIGHT:
		ship.go_right=True
	elif key==pygame.K_LEFT:
		ship.go_left=True
	elif key==pygame.K_DOWN:
		ship.go_down=True
	elif key==pygame.K_UP:
		ship.go_up=True
	elif key==pygame.K_LSHIFT:
		ship.slow=True