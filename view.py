from game_state import GAME_OVER, START_MENU
import pygame
from settings import BACKGROUND_COLOUR


def draw(screen, background, player, player_bullets, enemy, enemy_bullets, play_button, stats, scoreboard):
    screen.fill(BACKGROUND_COLOUR)
    background.draw(screen)
    player.draw(screen)
    for i in player_bullets:
        i.draw(screen)
    for i in enemy:
        i.draw(screen)
    for i in enemy_bullets:
        i.draw(screen)
    scoreboard.draw(screen)
    if stats.state == START_MENU:
        play_button.draw(screen)
    if stats.state == GAME_OVER:
        draw_game_over(screen)

    pygame.display.flip()


def draw_game_over(screen: pygame.Surface):
    text = pygame.font.SysFont('Serif', 190).render('GAME OVER', True, (200, 0, 0, 0))
    rect = text.get_rect()
    screen.blit(text, rect)
