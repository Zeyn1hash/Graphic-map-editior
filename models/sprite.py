from config import *

class Sprite:
    def __init__(self, x, y, img_path, width, height):
        self.image = transform.scale(image.load(img_path), (width, height))
        self.rect = Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.color=(100, 100, 100)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (100, 100, 100), self.rect, 5)

    def show_hitbox(self):
        draw.rect(window, self.color, self.rect, 5)
