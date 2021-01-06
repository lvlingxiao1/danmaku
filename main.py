import pygame
from pygame.sprite import Group

from background import Background
from button import Button
from controller import handle_input
from enemy import Enemy
from game_state import RUNNING, GameState
from player import Player, PLAYER_RADIUS
from scoreboard import Scoreboard
from settings import (FPS, HEIGHT, HIT_SCORE, TIME_SCORE,
                      WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT)
from view import draw

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Danmaku')
    clock = pygame.time.Clock()

    game_state = GameState()

    play_button = Button()
    bg = Background()
    scoreboard = Scoreboard(game_state)

    player_bullets = Group()
    player = Player(player_bullets)

    enemy_group = Group()
    enemy_bullets = Group()
    enemy_group.add(Enemy(enemy_bullets, player))

    screenRect = pygame.Rect(0, 0, WIDTH, HEIGHT)

    while 1:
        handle_input(player, enemy_group, game_state, play_button)

        if game_state.state == RUNNING:
            player.update()
            player_bullets.update()
            enemy_group.update()
            enemy_bullets.update()

            # remove bullets outside of the screen
            for i in player_bullets.copy():
                if not i.rect.colliderect(screenRect):
                    player_bullets.remove(i)
            for i in enemy_bullets.copy():
                if not i.rect.colliderect(screenRect):
                    enemy_bullets.remove(i)

            # collision detection
            for i in enemy_bullets:
                if i.collide(player.x, player.y, PLAYER_RADIUS) and not player.invulnerable:
                    game_state.player_died()
                    player.die()
                    enemy_bullets.empty()
                    break

            for i in player_bullets:
                for j in enemy_group:
                    if i.collide(j.x, j.y, j.radius):
                        game_state.score += HIT_SCORE

            game_state.score += TIME_SCORE

            if game_state.score > game_state.highscore:
                game_state.highscore = game_state.score

        draw(screen, bg, player, player_bullets, enemy_group,
             enemy_bullets, play_button, game_state, scoreboard)

        # print(clock.get_fps())
        clock.tick(FPS)
