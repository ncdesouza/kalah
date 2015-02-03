import sys

from pygame.constants import QUIT

from board import *


class Kalah:
    def __init__(self, p1, p2):
        pygame.init()
        self.screen = pygame.display.set_mode(kalah.BOARD_SIZE)
        self.board = Board(kalah.NUM_SEEDS)

    def update(self):
        self.screen.fill(0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        self.board.draw_board(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    p1 = 0
    p2 = 1
    game = Kalah(p1, p2)
    while True:
        game.update()