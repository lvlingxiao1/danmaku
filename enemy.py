import math
import random

import pygame

from bullet import Bullet
from player import Player
from settings import WIDTH

# time in frames
PHASE1_TIME = 1000
PHASE2_TIME = 10000

PHASE1_SHOOT_CD = 30
PHASE2_SHOOT_CD = 20


class Enemy(pygame.sprite.Sprite):
    def __init__(self, bullets: pygame.sprite.Group, player: Player):
        super().__init__()
        self.bullets = bullets
        self.target = player
        self.image0 = pygame.image.load('images/stg4aenm.png').convert_alpha()
        self.image = self.image0.subsurface((0, 0, 64, 80))

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 200)

        shoot_img = pygame.image.load('images/reimu_yyc.png').convert_alpha()
        self.shoot1 = shoot_img.subsurface((32, 176, 16, 16))

        self.reset()

    def reset(self):
        self.timer = 0
        self.phase = 1
        self.cd1 = 0
        self.cd2 = 0

    def update(self):
        if self.phase == 1:
            self.phase1()
            if self.timer >= PHASE1_TIME:
                self.phase = 2

        if self.phase == 2:
            # self.phase1()
            self.phase2()
            if self.timer >= PHASE2_TIME:
                self.phase = 0

        self.timer += 1
        self.cd1 -= 1
        self.cd2 -= 1

    def phase1(self):
        if self.cd1 <= 0:
            for _ in range(100):
                new_bul = self.gen_phase1_bullet()
                self.bullets.add(new_bul)
            self.cd1 = PHASE1_SHOOT_CD

    def gen_phase1_bullet(self):
        angle = random.random() * 2 * math.pi
        image = pygame.transform.rotate(self.shoot1, math.degrees(angle))
        new_bul = Bullet(self.bullets, self.rect, image, 0, 0, 3, angle)
        return new_bul

    def phase2(self):
        if self.cd2 <= 0:
            new_bul = self.gen_phase2_bullet(-100)
            self.bullets.add(new_bul)
            new_bul = self.gen_phase2_bullet(100)
            self.bullets.add(new_bul)
            self.cd2 = PHASE2_SHOOT_CD

    def gen_phase2_bullet(self, x_shift):
        angle = math.atan2(-self.target.rect.centery + self.rect.centery, self.target.rect.centerx - self.rect.centerx)
        image = pygame.transform.rotate(self.shoot1, math.degrees(angle))
        new_bul = Bullet(self.bullets, self.rect, image, x_shift, 0, 3, angle)
        return new_bul

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
