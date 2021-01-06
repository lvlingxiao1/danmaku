import math
from pygame import Surface, Rect, transform
from pygame.sprite import Sprite, Group


class Bullet(Sprite):
    def __init__(self, group: Group, src_rect: Rect, img: Surface, radius: float, offset_x=0, offset_y=0, speed=32, angle=math.pi/2):
        super().__init__()
        self.image = transform.rotate(img, math.degrees(angle))
        self.x = src_rect.centerx + offset_x    # rect only takes integer, need floating point speed
        self.y = src_rect.centery + offset_y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.radius = radius

        self.group = group

        self.speed_x = speed * math.cos(angle)
        self.speed_y = -speed * math.sin(angle)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.center = (self.x, self.y)

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    def collide(self, x, y, radius):
        return (self.x - x)**2 + (self.y - y)**2 < (self.radius + radius)**2
