import pygame as pg
from settings import WIDTH, HEIGHT, PIXEL
from color import RED, WHITE, BLACK
from time import sleep
from boll import Boll
from board import Board


class Manager:
    def __init__(self):
        self.is_running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.boll = Boll(WHITE, WIDTH // 2, HEIGHT // 2, PIXEL, PIXEL)
        self.board_left = Board(RED, PIXEL, PIXEL * 3, 2 * PIXEL, HEIGHT // 2)
        self.board_right = Board(RED, PIXEL, PIXEL * 3, WIDTH - 2 * PIXEL, HEIGHT // 2)

    def start_game_loop(self):
        while self.is_running:
            sleep(0.1)
            self.check_collision_objects()
            self.screen.fill(BLACK)
            self.boll.move()
            self.draw()
            self.key_board1()
            self.key_board2()
            self.check_leave_border()
            self.check_boll_leave_border()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
            pg.display.flip()

    def draw(self):
        self.board_left.draw(self.screen)
        self.board_right.draw(self.screen)
        self.boll.draw(self.screen)

    def check_collision_objects(self):
        if (self.boll.right == self.board_right.left and
                self.boll.top >= self.board_right.top and
                self.boll.bottom <= self.board_right.bottom):
            self.boll.speed_horizontal *= -1

        elif (self.boll.left == self.board_left.right and
              self.boll.top >= self.board_left.top and
              self.boll.bottom <= self.board_left.bottom):
            self.boll.speed_horizontal *= -1

    def check_boll_leave_border(self):
        if self.boll.bottom == HEIGHT or self.boll.top == 0:
            self.boll.speed_vertical *= -1

    def key_board1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.board_left.top -= PIXEL
        if keys[pg.K_s]:
            self.board_left.top += PIXEL

    def key_board2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.board_right.top -= PIXEL
        if keys[pg.K_DOWN]:
            self.board_right.top += PIXEL

    def check_leave_border(self):

        if self.board_left.top < 0:
            self.board_left.top = 0
        if self.board_left.bottom > HEIGHT:
            self.board_left.bottom = HEIGHT

        if self.board_right.top < 0:
            self.board_right.top = 0
        if self.board_right.bottom > HEIGHT:
            self.board_right.bottom = HEIGHT
        if self.boll.left < 0:
            print('Правый победил.')
            self.is_running = False
        elif self.boll.right > WIDTH:
            print('Левый победил')
            self.is_running = False

