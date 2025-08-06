from models.sprite import Sprite
from pygame import *


class Block(Sprite):
    def __init__(self, x, y, img, width, height, symbol='_'):
        super().__init__(x, y, img, width, height)
        self.type = 0
        self.img=img
        self.symbol=symbol

    def update_type(self, blocks):
        bitmask = 0
        for other in blocks:
            if other is self:
                continue
            if other.rect.colliderect(
                    Rect(self.rect.x, self.rect.y - self.rect.height, self.rect.width, self.rect.height)):
                bitmask |= 1  # Зверху
            if other.rect.colliderect(
                    Rect(self.rect.x + self.rect.width, self.rect.y, self.rect.width, self.rect.height)):
                bitmask |= 2  # Справа
            if other.rect.colliderect(
                    Rect(self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height)):
                bitmask |= 4  # Знизу
            if other.rect.colliderect(
                    Rect(self.rect.x - self.rect.width, self.rect.y, self.rect.width, self.rect.height)):
                bitmask |= 8  # Зліва

        self.type = bitmask  # 0-15

    def copy(self):
        # Створює новий об'єкт з таким самим зображенням і розмірами
        return Block(self.rect.x, self.rect.y, self.img, self.rect.width, self.rect.height, self.symbol)
