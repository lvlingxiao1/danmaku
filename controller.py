from button import Button
import pygame
from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN, K_LSHIFT, K_z, K_x
import sys
import time
from game_state import GameState, GAME_OVER, RUNNING, START_MENU
from player import Player


def handle_input(player: Player, enemy_group, game_state: GameState, play_button: Button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.save_highscore()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event.key, player)
        elif event.type == pygame.KEYUP:
            key_up(event.key, player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state.state == START_MENU:
                x, y = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(x, y):
                    game_state.game_start(enemy_group)
            elif game_state == GAME_OVER:
                game_state.state = START_MENU
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
