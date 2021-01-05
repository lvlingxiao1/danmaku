import pygame
from pygame.sprite import Group
from background import Background
from player import Player
from controller import handle_input
from enemy import Enemy
from button import Button
from scoreboard import Scoreboard
from game_state import GameState, RUNNING
from view import draw
from settings import WIDTH, SCOREBOARD_WIDTH, HEIGHT, SCREEN_SIZE, FPS, HIT_SCORE, TIME_SCORE

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size=(WIDTH+SCOREBOARD_WIDTH, HEIGHT))
    pygame.display.set_caption('Hmmmmmmm...')
    clock = pygame.time.Clock()

    game_state = GameState()

    play_button = Button()
    bg = Background()
    scoreboard = Scoreboard(game_state)

    playerBullets = Group()
    player = Player(playerBullets)

    enemy_group = Group()
    enemy_bullets = Group()
    enemy_group.add(Enemy(enemy_bullets, player))

    screenRect = pygame.Rect(0, 0, WIDTH, HEIGHT)

    while 1:
        handle_input(player, enemy_group, game_state, play_button)

        if game_state.state == RUNNING:
            player.update()
            playerBullets.update()
            enemy_group.update()
            enemy_bullets.update()

            for i in playerBullets.copy():
                if not i.rect.colliderect(screenRect):
                    playerBullets.remove(i)
            for i in enemy_bullets.copy():
                if not i.rect.colliderect(screenRect):
                    enemy_bullets.remove(i)

            collide_dict = pygame.sprite.groupcollide(playerBullets, enemy_group, True, False)
            for i in collide_dict:
                game_state.score += HIT_SCORE

            game_state.score += TIME_SCORE

            if game_state.score > game_state.highscore:
                game_state.highscore = game_state.score

            for i in enemy_bullets:
                if i.rect.colliderect(player.rect):
                    game_state.player_died(player, enemy_bullets)
                    break

        draw(screen, bg, player, playerBullets, enemy_group,
             enemy_bullets, play_button, game_state, scoreboard)

        # print(clock.get_fps())
        clock.tick(FPS)
