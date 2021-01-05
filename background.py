from pygame import image, Rect, Surface
from settings import SCREEN_SIZE


class Background():
    def __init__(self):
        self.img = image.load("images/bg.png")
        self.rect = Rect((0, 0), SCREEN_SIZE)

    def draw(self, screen: Surface):
        screen.blit(self.img, self.rect)
