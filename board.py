import pygame as pg


class Board(pg.Rect):

    def __init__(self, color, width, height, left, top):
        self.color = color

        super().__init__(left, top, width, height)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self)





