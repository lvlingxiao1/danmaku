from game_state import GameState
import pygame.font
from pygame import Rect, Surface


class Scoreboard():
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.txt_color = (60, 60, 60)
        self.bg_color = (0, 0, 0)
        self.rect = Rect(800, 0, 300, 800)
        self.font = pygame.font.SysFont('Sans Serif', 36)
        self.font2 = pygame.font.SysFont('Blackadder ITC', 36)

    def prep(self):
        life = 'LIFE: %s' % self.game_state.life_left
        self.l_img = self.font.render(life, True, self.txt_color)
        self.l_rect = self.l_img.get_rect()
        self.l_rect.centerx = self.rect.centerx
        self.l_rect.centery = self.rect.centery-50

        s = 'SCORE: %s' % '{:,}'.format(self.game_state.score)
        self.s_img = self.font.render(s, True, self.txt_color)
        self.s_rect = self.s_img.get_rect()
        self.s_rect.centerx = self.rect.centerx
        self.s_rect.centery = self.rect.centery

        hs = 'HIGH SCORE: %s' % '{:,}'.format(self.game_state.highscore)
        self.hs_img = self.font.render(hs, True, self.txt_color)
        self.hs_rect = self.hs_img.get_rect()
        self.hs_rect.centerx = self.rect.centerx
        self.hs_rect.centery = self.rect.centery+50

    def draw(self, screen: Surface):
        self.prep()
        screen.fill(self.bg_color, self.rect)
        screen.blit(self.l_img, self.l_rect)
        screen.blit(self.s_img, self.s_rect)
        screen.blit(self.hs_img, self.hs_rect)
