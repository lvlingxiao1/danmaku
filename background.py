from pygame import image, Rect, Surface
from settings import WIDTH, HEIGHT


class Background():
    def __init__(self):
        self.img = image.load("images/bg2.png")
        self.rect = Rect((0, 0), (WIDTH, HEIGHT))

    def draw(self, screen: Surface):
        screen.blit(self.img, self.rect)
