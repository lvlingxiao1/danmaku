import pygame
import random
import math
from bullet import Bullet
from pygame import Rect, Surface
from settings import WIDTH, HEIGHT


SRC_IMG1 = 'images/reimu_yym.png'
SRC_IMG2 = 'images/reimu_yyc.png'
MOVEMENT_SPEED = 6
MOVEMENT_SPEED_SLOW = 3
SHOOT_CD = 8
SHOOT2_CD = 30


class Player(pygame.sprite.Sprite):
    def __init__(self, bullets: pygame.sprite.Group):
        super().__init__()
        self.bullets = bullets

        # Load images
        img = pygame.image.load(SRC_IMG1).convert_alpha()
        self.imagesN = []
        self.imagesL = []
        self.imagesR = []
        for i in range(4):
            self.imagesN.append(img.subsurface(pygame.Rect(32*i, 0, 32, 48)))
        for i in range(7):
            imgL = img.subsurface(pygame.Rect(32*i, 48, 32, 48))
            imgR = pygame.transform.flip(imgL, True, False)
            self.imagesL.append(imgL)
            self.imagesR.append(imgR)

        self.image = self.imagesN[0]
        self.slow_effect0 = pygame.image.load('images/eff_sloweffect.png').convert_alpha()
        self.slow_effect = None
        self.shoot1_img = pygame.image.load(SRC_IMG2).convert_alpha().subsurface((0, 144, 64, 16))
        self.shoot1_img = pygame.transform.rotate(self.shoot1_img, 90)

        # Rect
        self.rect = self.image.get_rect()

        self.hit_box = pygame.sprite.Sprite()
        self.hit_box.rect = Rect(0, 0, 4, 4)

        self.reborn()

    def reborn(self):
        self.rect.center = (WIDTH / 2, HEIGHT - 30)

        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False
        self.shooting = False
        self.shooting2 = False
        self.slow = False
        self.anime = [0, 0, 0]
        self.anime_slow = 0
        self.cd1 = 0
        self.cd2 = 0

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)
        # self.screen.fill((0, 0, 0), self.hit_box.rect)
        if self.slow:
            screen.blit(self.slow_effect, self.slow_rect)

    def update(self):
        if self.slow:
            speed = MOVEMENT_SPEED
        else:
            speed = MOVEMENT_SPEED_SLOW

        # Left/Right motion and animation
        if self.go_left and (not self.go_right) and self.rect.centerx-16 > 0:
            self.rect.move_ip(-speed, 0)
            self.update_image(1)
        elif self.go_right and (not self.go_left) and self.rect.centerx+16 < WIDTH:
            self.rect.move_ip(speed, 0)
            self.update_image(2)
        elif not (self.go_left ^ self.go_right):
            self.update_image(0)

        #Up and down
        if self.go_up and (not self.go_down) and self.rect.centery-24 > 0:
            self.rect.move_ip(0, -speed)
        elif self.go_down and (not self.go_up) and self.rect.centery+24 < HEIGHT:
            self.rect.move_ip(0, speed)

        # Sync position
        self.hit_box.rect.center = self.rect.center

        # Shooting
        if self.cd1 > 0:
            self.cd1 -= 1
        if self.cd2 > 0:
            self.cd2 -= 1

        if self.shooting and self.cd1 == 0:
            new_bul = Bullet(self.bullets, self.rect, self.shoot1_img, -10, 0, speed=32)
            self.bullets.add(new_bul)
            new_bul = Bullet(self.bullets, self.rect, self.shoot1_img, 10, 0, speed=32)
            self.bullets.add(new_bul)
            self.cd1 = SHOOT_CD

        if self.shooting2 and self.cd2 == 0:
            for i in range(100):
                new_bul = self.gen_bullet_2()
                self.bullets.add(new_bul)
            self.cd2 = SHOOT2_CD

    def gen_bullet_2(self):
        angle = random.random()*6.2831
        angle_d = angle/math.pi*180-90
        image = pygame.transform.rotate(self.shoot1_img, angle_d)
        new_bul = Bullet(self.bullets, self.screen, self.rect, image, 0, 0, 6, angle)
        return new_bul

    def update_image(self, k):
        self.anime[k] += 1
        if k == 0:
            self.anime[1] = 0
            self.anime[2] = 0
            if self.anime[0] == 40:
                self.anime[0] = 0
            self.image = self.imagesN[self.anime[0]//10]
        elif k == 1:
            self.anime[2] = 0
            if self.anime[1] == 70:
                self.anime[1] = 69
            else:
                self.image = self.imagesL[self.anime[1]//10]
        elif k == 2:
            self.anime[1] = 0
            if self.anime[2] == 70:
                self.anime[2] = 69
            else:
                self.image = self.imagesR[self.anime[2]//10]

        if self.slow:
            self.anime_slow += 1
            if self.anime_slow == 360:
                self.anime_slow = 0
            self.slow_effect = pygame.transform.rotate(self.slow_effect0, self.anime_slow)
            self.slow_rect = self.slow_effect.get_rect()
            self.slow_rect.center = self.rect.center
