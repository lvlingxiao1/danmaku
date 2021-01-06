import math
import random

import pygame

from bullet import Bullet
from player import NORMAL, Player
from settings import WIDTH

# time in frames
PHASE1_TIME = 100
PHASE2_TIME = 10000

PHASE1_SHOOT_CD = 30
PHASE2_SHOOT_CD = 60

RADIUS = 10


class Enemy(pygame.sprite.Sprite):
    def __init__(self, bullets: pygame.sprite.Group, player: Player):
        super().__init__()
        self.bullets = bullets
        self.target = player
        self.image0 = pygame.image.load('images/stg4aenm.png').convert_alpha()
        self.image = self.image0.subsurface((0, 0, 128, 160))

        self.rect = self.image.get_rect()
        self.x = WIDTH / 2
        self.y = 200
        self.rect.center = (self.x, self.y)

        self.radius = RADIUS

        shoot_img = pygame.image.load('images/etama2.png').convert_alpha()
        self.shoot1 = shoot_img.subsurface((64, 224, 32, 32))
        self.shoot1 = pygame.transform.rotate(self.shoot1, -90)
        self.shoot2 = shoot_img.subsurface((128, 224, 32, 32))
        self.shoot2 = pygame.transform.rotate(self.shoot2, -90)
        self.reset()

    def reset(self):
        self.timer = 0
        self.phase = 1
        self.cd1 = 0
        self.cd2 = 0
        self.bullets.empty()

    def update(self):
        if self.target.state != NORMAL:
            return

        if self.phase == 1:
            self.phase1()
            if self.timer >= PHASE1_TIME:
                self.phase = 2

        if self.phase == 2:
            self.phase1()
            self.phase2()
            if self.timer >= PHASE2_TIME:
                self.phase = 0

        self.timer += 1
        self.cd1 -= 1
        self.cd2 -= 1

    def phase1(self):
        if self.cd1 <= 0:
            self.gen_phase1_bullet()
            self.cd1 = PHASE1_SHOOT_CD

    def gen_phase1_bullet(self):
        angle = random.random() * math.pi
        for _ in range(32):
            new_bul = Bullet(self.bullets, self.rect, self.shoot1, 10, 0, 0, 3, angle + 0.03)
            self.bullets.add(new_bul)
            new_bul = Bullet(self.bullets, self.rect, self.shoot1, 10, 0, 0, 3.1, angle + 0.06)
            self.bullets.add(new_bul)
            new_bul = Bullet(self.bullets, self.rect, self.shoot1, 10, 0, 0, 3.2, angle + 0.09)
            self.bullets.add(new_bul)
            new_bul = Bullet(self.bullets, self.rect, self.shoot1, 10, 0, 0, 3.3, angle + 0.12)
            self.bullets.add(new_bul)
            angle += math.pi / 16

    def phase2(self):
        if self.cd2 <= 0:
            self.gen_phase2_bullet()
            self.cd2 = PHASE2_SHOOT_CD

    def gen_phase2_bullet(self):
        angle = math.atan2(-self.target.y + self.y, self.target.x - self.x + 100)
        new_bul = Bullet(self.bullets, self.rect, self.shoot2, 10, -100, 0, 3, angle)
        self.bullets.add(new_bul)
        angle = math.atan2(-self.target.y + self.y, self.target.x - self.x - 100)
        new_bul = Bullet(self.bullets, self.rect, self.shoot2, 10, 100, 0, 3, angle)
        self.bullets.add(new_bul)
        return new_bul

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
