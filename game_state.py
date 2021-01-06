from os import makedirs
import pygame
from settings import LIFE_INIT


START_MENU = 0
RUNNING = 1
GAME_OVER = 2


class GameState:
    def __init__(self):
        try:
            with open("savedata/highscore.txt", 'r') as f:
                self.highscore = int(f.read())
        except:
            self.highscore = 0

        self.reset()

    def reset(self):
        self.state = START_MENU
        self.score = 0
        self.life_left = LIFE_INIT

    def save_highscore(self):
        if self.score < self.highscore:
            return
        makedirs("savedata", exist_ok=True)
        with open("savedata/highscore.txt", 'w') as f:
            f.write(str(self.highscore))

    def game_start(self, enemy_group):
        self.state = RUNNING
        # pygame.mouse.set_visible(False)
        for i in enemy_group:
            i.reset()

    def player_died(self):
        if self.life_left > 0:
            self.life_left -= 1
        else:
            self.state = GAME_OVER
            pygame.mouse.set_visible(True)
