import pygame
from pygame import K_DOWN, K_LEFT, K_LSHIFT, K_RIGHT, K_UP, K_r, K_x, K_z

from button import Button
from game_state import GAME_OVER, RUNNING, START_MENU, GameState
from player import Player
from settings import MARGIN_LEFT, MARGIN_TOP


def handle_input(player: Player, enemy_group: pygame.sprite.Group, game_state: GameState, play_button: Button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.save_highscore()
            exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event.key, player)
        elif event.type == pygame.KEYUP:
            key_up(event.key, player)
            if event.key == K_r:
                game_state.reset()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state.state == START_MENU:
                x, y = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(x - MARGIN_LEFT, y - MARGIN_TOP):
                    game_state.game_start(enemy_group)
            elif game_state == GAME_OVER:
                game_state.reset()


def key_up(key, player):
    if key == K_RIGHT:
        player.go_right = False
    elif key == K_LEFT:
        player.go_left = False
    elif key == K_DOWN:
        player.go_down = False
    elif key == K_UP:
        player.go_up = False
    elif key == K_LSHIFT:
        player.slow = False
    elif key == K_z:
        player.shooting = False
    elif key == K_x:
        player.shooting2 = False


def key_down(key, player):
    if key == K_RIGHT:
        player.go_right = True
    if key == K_LEFT:
        player.go_left = True
    if key == K_DOWN:
        player.go_down = True
    if key == K_UP:
        player.go_up = True
    if key == K_LSHIFT:
        player.slow = True
    if key == K_z:
        player.shooting = True
    if key == K_x:
        player.shooting2 = True
