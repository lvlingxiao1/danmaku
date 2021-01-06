import pygame
from pygame import Color, Rect, Surface

from game_state import GameState
from settings import (MARGIN_BOTTOM, MARGIN_BOTTOM_TOP, MARGIN_LEFT,
                      MARGIN_TOP, SCOREBOARD_LEFT, SCOREBOARD_WIDTH, WIDTH,
                      WINDOW_HEIGHT)

TEXT_COLOUR = Color(255, 255, 255)


class Scoreboard():
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.font = pygame.font.SysFont('Sans Serif', 36)
        self.font2 = pygame.font.SysFont('Blackadder ITC', 36)

        frame_image = pygame.image.load("images/front00.png").convert_alpha()
        self.margin_left_rect = Rect(0, 0, MARGIN_LEFT, WINDOW_HEIGHT)
        self.margin_left = frame_image.subsurface((0, 0, MARGIN_LEFT, WINDOW_HEIGHT))
        self.margin_top_rect = Rect(MARGIN_LEFT, 0, WIDTH, MARGIN_TOP)
        self.margin_top = frame_image.subsurface((0, 960, 768, 32))
        self.margin_bottom_rect = Rect(MARGIN_LEFT, MARGIN_BOTTOM_TOP, WIDTH, MARGIN_BOTTOM)
        self.margin_bottom = frame_image.subsurface((0, 992, 768, 32))
        self.scoreboard_rect = Rect(SCOREBOARD_LEFT, 0, SCOREBOARD_WIDTH, WINDOW_HEIGHT)
        self.scoreboard_img = frame_image.subsurface((64, 0, 448, 960))

    def prep(self):
        life = 'LIFE: {}'.format(self.game_state.life_left)
        self.l_img = self.font.render(life, True, TEXT_COLOUR)
        self.l_rect = self.l_img.get_rect()
        self.l_rect.centerx = self.scoreboard_rect.centerx
        self.l_rect.centery = self.scoreboard_rect.centery - 150

        s = 'SCORE: {}'.format(self.game_state.score)
        self.s_img = self.font.render(s, True, TEXT_COLOUR)
        self.s_rect = self.s_img.get_rect()
        self.s_rect.centerx = self.scoreboard_rect.centerx
        self.s_rect.centery = self.scoreboard_rect.centery - 100

        hs = 'HIGH SCORE: {}'.format(self.game_state.highscore)
        self.hs_img = self.font.render(hs, True, TEXT_COLOUR)
        self.hs_rect = self.hs_img.get_rect()
        self.hs_rect.centerx = self.scoreboard_rect.centerx
        self.hs_rect.centery = self.scoreboard_rect.centery - 50

    def draw(self, screen: Surface):
        self.prep()
        screen.blit(self.margin_left, self.margin_left_rect)
        screen.blit(self.margin_top, self.margin_top_rect)
        screen.blit(self.margin_bottom, self.margin_bottom_rect)
        screen.blit(self.scoreboard_img, self.scoreboard_rect)

        screen.blit(self.l_img, self.l_rect)
        screen.blit(self.s_img, self.s_rect)
        screen.blit(self.hs_img, self.hs_rect)
