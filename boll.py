import pygame as pg
from color import RED, WHITE, BLACK
from settings import PIXEL


class Boll(pg.Rect):
    """Шар"""

    def __init__(self, color, left, top, width, height):
        self.color = color
        self.speed_vertical = PIXEL
        self.speed_horizontal = PIXEL
        super().__init__(left, top, width, height)

    def draw(self, screen):
        """Отрисовка шара"""
        pg.draw.circle(screen, self.color, (self.centerx, self.centery), self.width // 2)

    def move(self):
        self.x += self.speed_horizontal
        self.y += self.speed_vertical
