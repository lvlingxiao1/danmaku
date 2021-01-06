import pygame
from pygame import Rect, Surface, font
from pygame.sprite import Group

from background import Background
from button import Button
from game_state import GAME_OVER, START_MENU, GameState
from player import Player
from scoreboard import Scoreboard
from settings import GAME_RECT, HEIGHT, WIDTH


def draw(screen: Surface, background: Background, player: Player, player_bullets: Group, enemy_group: Group, enemy_bullets: Group, play_button: Button, game_state: GameState, scoreboard: Scoreboard):
    game_surface = Surface((WIDTH, HEIGHT))
    background.draw(game_surface)
    player.draw(game_surface)
    for i in player_bullets:
        i.draw(game_surface)
    for i in enemy_group:
        i.draw(game_surface)
    for i in enemy_bullets:
        i.draw(game_surface)
    if game_state.state == START_MENU:
        play_button.draw(game_surface)
    if game_state.state == GAME_OVER:
        draw_game_over(game_surface)

    screen.blit(game_surface, GAME_RECT)
    scoreboard.draw(screen)

    pygame.display.flip()


def draw_game_over(screen: Surface):
    text = font.SysFont('Serif', size=100).render('GAME OVER', True, (200, 0, 0, 0))
    rect = text.get_rect()
    rect.center = (WIDTH / 2, HEIGHT / 2)
    screen.blit(text, rect)
