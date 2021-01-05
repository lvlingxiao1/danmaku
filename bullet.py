import math
from pygame import Surface, Rect
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, parent, src_rect: Rect, img: Surface, offset_x=0, offset_y=0, speed=64, angle=math.pi/2):
        super().__init__()
        self.image = img
        self.x = src_rect.centerx + offset_x    # rect only takes integer, need floating point speed
        self.y = src_rect.centery + offset_y
        self.rect = img.get_rect()
        self.rect.center = (self.x, self.y)

        self.parent = parent

        self.speed_x = speed * math.cos(angle)
        self.speed_y = -speed * math.sin(angle)
        self.flash = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.center = (self.x, self.y)

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)
        # if self.flash==0:
        #	self.screen.blit(self.image,self.rect)
        #	self.flash=1

        # elif self.flash==1:
        #	self.flash=0

    def destroy(self):
        self.parent.remove(self)
