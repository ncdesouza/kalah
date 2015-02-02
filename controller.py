import pygame
import sys

from pygame.constants import QUIT

from kalah import *
import kalah


class Kalah:
    def __init__(self, p1, p2):
        pygame.init()
        self.screen = pygame.display.set_mode(kalah.BOARD_SIZE)
        self.board = Board(kalah.NUM_SEEDS)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.update()


if __name__ == '__main__':
    p1 = 0
    p2 = 1
    game = Kalah(p1, p2)
    while True:
        game.update()