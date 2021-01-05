from pygame import font, Rect, Surface
from pygame.sprite import Sprite
from settings import WIDTH, HEIGHT


class Button(Sprite):
    def __init__(self):
        super().__init__()
        # self.rect = rect
        # self.image = image
        self.width, self.height = 200, 80
        self.color = (0, 200, 0)
        self.txt_color = (255, 255, 255)
        self.font = font.SysFont('Serif', 48)

        self.rect = Rect(0, 0, self.width, self.height)
        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.msg_img = self.font.render('Play', True, self.txt_color, self.color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw(self, screen: Surface):
        screen.fill(self.color, self.rect)
        screen.blit(self.msg_img, self.msg_img_rect)
