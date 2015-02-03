import sys

from pygame.constants import QUIT

from board import *


class Kalah:
    def __init__(self, player_num):
        pygame.init()
        self.screen = pygame.display.set_mode(kalah.BOARD_SIZE)
        self.board = Board(kalah.NUM_SEEDS)
        self.clock = pygame.time.Clock()
        self.count = 0
        self.turn = PL_TWO
        self.me = player_num

    def update(self):
        self.screen.fill(0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if self.turn == PL_ONE and not isStoreEmpty(self.board.board[0]):
                        self.board.board[0].move_seeds(PL_ONE)
                    if self.turn == PL_TWO and not isStoreEmpty(self.board.board[12]):
                        self.board.board[12].move_seeds(PL_TWO)
                if event.key == pygame.K_2:
                    if self.turn == PL_ONE and not isStoreEmpty(self.board.board[1]):
                        self.board.board[1].move_seeds(PL_ONE)
                    if self.turn == PL_TWO and not isStoreEmpty(self.board.board[11]):
                        self.board.board[11].move_seeds(PL_TWO)
                if event.key == pygame.K_3:
                    if self.turn == PL_ONE and not isStoreEmpty(self.board.board[2]):
                        self.board.board[2].move_seeds(PL_ONE)
                    if self.turn == PL_TWO and not isStoreEmpty(self.board.board[10]):
                        self.board.board[10].move_seeds(PL_TWO)
                if event.key == pygame.K_4:
                    if self.turn == PL_ONE and not isStoreEmpty(self.board.board[3]):
                        self.board.board[3].move_seeds(PL_ONE)
                    if self.turn == PL_TWO and not isStoreEmpty(self.board.board[9]):
                        self.board.board[9].move_seeds(PL_TWO)
                if event.key == pygame.K_5:
                    if self.turn == PL_ONE and not isStoreEmpty(self.board.board[4]):
                        self.board.board[4].move_seeds(PL_ONE)
                    if self.turn == PL_TWO and not isStoreEmpty(self.board.board[8]):
                        self.board.board[8].move_seeds(PL_TWO)
                if event.key == pygame.K_6:
                    if self.turn == PL_ONE and not isStoreEmpty(self.board.board[5]):
                        self.board.board[5].move_seeds(PL_ONE)
                    if self.turn == PL_TWO and not isStoreEmpty(self.board.board[7]):
                        self.board.board[7].move_seeds(PL_ONE)

        self.board.draw_board(self.screen)

        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(60)
        self.count += 1


if __name__ == '__main__':
    p1 = 0
    p2 = 1
    game = Kalah(p2)
    while True:
        game.update()