import pygame as pg
from settings import WIDTH, HEIGHT, PIXEL
from color import RED, WHITE, BLACK


class Manager:
    def __init__(self):
        self.is_running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

    def start_game_loop(self):
        pg.Surface.fill(BLACK)
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
            pg.display.flip()

    def draw(self):
        pass

    def check_collision_objects(self):
        pass

    def check_bool_leave_border(self):
        pass
