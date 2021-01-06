import math

from pygame import Color, Rect, Surface, image, transform
import pygame
from pygame.sprite import Sprite, Group

from bullet import Bullet
from settings import HEIGHT, WIDTH

MOVEMENT_SPEED = 6
MOVEMENT_SPEED_SLOW = 3
SHOOT_CD = 8
SHOOT2_CD = 30
PLAYER_RADIUS = 3

NORMAL = 0
REBORNING = 1
DEAD = 2

REBORN_TIME = 120
REBORN_INVULNERABLE = 180

DEATH_TIMER = 60
DEATH_INVULNERABLE = 60

SHOOT_ANGLE_1 = math.pi / 2 + 0.09
SHOOT_ANGLE_2 = math.pi / 2 - 0.09


class Player(Sprite):
    def __init__(self, bullets: Group):
        super().__init__()
        self.bullets = bullets

        # Load images
        img = image.load('images/player03.png').convert_alpha()
        self.imagesN = []
        self.imagesL = []
        self.imagesR = []
        for i in range(4):
            self.imagesN.append(img.subsurface((64*i, 192, 64, 96)))
        for i in range(4):
            imgL = img.subsurface((64*i, 288, 64, 96))
            imgR = transform.flip(imgL, True, False)
            self.imagesL.append(imgL)
            self.imagesR.append(imgR)

        self.image = self.imagesN[0]
        self.rect = self.image.get_rect()

        self.slow_effect0 = image.load('images/sloweffect.png').convert_alpha()
        self.slow_effect = self.slow_effect0
        self.slow_rect = self.slow_effect.get_rect()
        self.slow_rect.center = self.rect.center

        self.shoot1_img = img.subsurface((384, 0, 64, 64))

        self.hit_box = Sprite()
        self.hit_box.rect = Rect(0, 0, 4, 4)

        self.reborn()

    def reborn(self):
        self.x: float = WIDTH / 2
        self.y: float = HEIGHT + 150
        self.rect.center = (self.x, self.y)

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
        self.timer = REBORN_TIME
        self.invulnerable_timer = REBORN_INVULNERABLE
        self.invulnerable = True
        self.state = REBORNING

    def draw(self, screen: Surface):
        if self.state == NORMAL or self.state == REBORNING:
            screen.blit(self.image, self.rect)
            # self.screen.fill((0, 0, 0), self.hit_box.rect)
            if self.slow:
                self.slow_rect.center = self.rect.center
                screen.blit(self.slow_effect, self.slow_rect)
        elif self.state == DEAD:
            self.death_animation(screen)

    def update(self):
        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False

        if self.state == NORMAL:
            if self.slow:
                speed = MOVEMENT_SPEED_SLOW
            else:
                speed = MOVEMENT_SPEED

            # Left/Right motion and animation
            if self.go_left and (not self.go_right) and self.x - 32 > 0:
                self.x -= speed
                self.update_image(1)
            elif self.go_right and (not self.go_left) and self.x + 32 < WIDTH:
                self.x += speed
                self.update_image(2)
            elif not (self.go_left ^ self.go_right):
                self.update_image(0)

            #Up and down
            if self.go_up and (not self.go_down) and self.y - 48 > 0:
                self.y -= speed
            elif self.go_down and (not self.go_up) and self.y + 48 < HEIGHT:
                self.y += speed

            # Shooting
            if self.cd1 > 0:
                self.cd1 -= 1
            if self.cd2 > 0:
                self.cd2 -= 1

            if self.shooting and self.cd1 == 0:
                new_bul = Bullet(self.bullets, self.rect, self.shoot1_img, 5, offset_x=-16)
                self.bullets.add(new_bul)
                new_bul = Bullet(self.bullets, self.rect, self.shoot1_img, 5, offset_x=16)
                self.bullets.add(new_bul)
                new_bul = Bullet(self.bullets, self.rect, self.shoot1_img, 5, offset_x=-16, angle=SHOOT_ANGLE_1)
                self.bullets.add(new_bul)
                new_bul = Bullet(self.bullets, self.rect, self.shoot1_img, 5, offset_x=16, angle=SHOOT_ANGLE_2)
                self.bullets.add(new_bul)
                self.cd1 = SHOOT_CD

            if self.shooting2 and self.cd2 == 0:
                for i in range(60):
                    new_bul = Bullet(self.bullets, self.rect, self.shoot1_img, 5, 0, 0, 6, math.pi / 30 * i)
                    self.bullets.add(new_bul)
                self.cd2 = SHOOT2_CD

        elif self.state == REBORNING:
            self.y -= MOVEMENT_SPEED_SLOW
            self.timer -= 1
            if self.timer <= 0:
                self.state = NORMAL
        elif self.state == DEAD:
            self.timer -= 1
            if self.timer <= 0:
                self.reborn()

        self.rect.center = (self.x, self.y)
        self.hit_box.rect.center = self.rect.center

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
            if self.anime[1] == 40:
                self.anime[1] = 39
            else:
                self.image = self.imagesL[self.anime[1]//10]
        elif k == 2:
            self.anime[1] = 0
            if self.anime[2] == 40:
                self.anime[2] = 39
            else:
                self.image = self.imagesR[self.anime[2]//10]

        if self.slow:
            self.anime_slow += 1
            if self.anime_slow == 360:
                self.anime_slow = 0
            self.slow_effect = transform.rotate(self.slow_effect0, self.anime_slow)
            self.slow_rect = self.slow_effect.get_rect()

    def die(self):
        self.state = DEAD
        self.timer = DEATH_TIMER
        self.invulnerable = True
        self.invulnerable_timer = DEATH_INVULNERABLE
        self.death_animation_radius1 = 0
        self.death_animation_radius2 = 0

    def death_animation(self, screen: Surface):
        s = Surface((self.death_animation_radius1*2, self.death_animation_radius1*2))
        brightness = self.timer * 35 // 60
        pygame.draw.circle(s, (brightness, brightness, brightness), (self.death_animation_radius1,
                                                                     self.death_animation_radius1), self.death_animation_radius1)
        rect = s.get_rect()
        rect.center = (self.x + 64, self.y + 64)
        screen.blit(s, rect, None, pygame.BLEND_ADD)
        rect.center = (self.x + 64, self.y - 64)
        screen.blit(s, rect, None, pygame.BLEND_ADD)
        rect.center = (self.x - 64, self.y + 64)
        screen.blit(s, rect, None, pygame.BLEND_ADD)
        rect.center = (self.x - 64, self.y - 64)
        screen.blit(s, rect, None, pygame.BLEND_ADD)
        self.death_animation_radius1 += 15
        if self.timer < 40:
            brightness *= 4
            s = Surface((self.death_animation_radius2*2, self.death_animation_radius2*2))
            pygame.draw.circle(s, (brightness, brightness, brightness), (self.death_animation_radius2,
                                                                         self.death_animation_radius2), self.death_animation_radius2)
            rect = s.get_rect()
            rect.center = (self.x, self.y)
            screen.blit(s, rect, None, pygame.BLEND_SUB)
            self.death_animation_radius2 += 25
