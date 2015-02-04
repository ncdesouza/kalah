import sys

from pygame.constants import QUIT

from board import *
from settings import *


class Kalah:
    def __init__(self, player_num):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.board = Board(NUM_SEEDS)
        self.clock = pygame.time.Clock()
        self.count = 0
        self.turn = PL_ONE
        self.me = player_num

        print("You are player:" + str(self.me))
        print("Player " + str(self.turn) + "'s turn")

    def update(self):
        self.screen.fill(0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if self.turn is self.me and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if self.me is PL_ONE and not isStoreEmpty(self.board.board[0]):
                        self.turn = self.board.board[0].move_seeds(PL_ONE)
                    if self.me is PL_TWO and not isStoreEmpty(self.board.board[12]):
                        self.turn = self.board.board[12].move_seeds(PL_TWO)
                if event.key == pygame.K_2:
                    if self.me is PL_ONE and not isStoreEmpty(self.board.board[1]):
                        self.turn = self.board.board[1].move_seeds(PL_ONE)
                    if self.me is PL_TWO and not isStoreEmpty(self.board.board[11]):
                        self.turn = self.board.board[11].move_seeds(PL_TWO)
                if event.key == pygame.K_3:
                    if self.me is PL_ONE and not isStoreEmpty(self.board.board[2]):
                        self.turn = self.board.board[2].move_seeds(PL_ONE)
                    if self.me is PL_TWO and not isStoreEmpty(self.board.board[10]):
                        self.turn = self.board.board[10].move_seeds(PL_TWO)
                if event.key == pygame.K_4:
                    if self.me is PL_ONE and not isStoreEmpty(self.board.board[3]):
                        self.turn = self.board.board[3].move_seeds(PL_ONE)
                    if self.me is PL_TWO and not isStoreEmpty(self.board.board[9]):
                        self.turn = self.board.board[9].move_seeds(PL_TWO)
                if event.key == pygame.K_5:
                    if self.me is PL_ONE and not isStoreEmpty(self.board.board[4]):
                        self.turn = self.board.board[4].move_seeds(PL_ONE)
                    if self.me is PL_TWO and not isStoreEmpty(self.board.board[8]):
                        self.turn = self.board.board[8].move_seeds(PL_TWO)
                if event.key == pygame.K_6:
                    if self.me is PL_ONE and not isStoreEmpty(self.board.board[5]):
                        self.turn = self.board.board[5].move_seeds(PL_ONE)
                    if self.me is PL_TWO and not isStoreEmpty(self.board.board[7]):
                        self.turn = self.board.board[7].move_seeds(PL_TWO)

            self.me = self.turn
            print("Player " + str(self.turn) + "'s turn")
            print("Actual:" + str(self.me))
        isGameOver(self.board)
        self.board.draw_board(self.screen)

        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(60)
        self.count += 1


if __name__ == '__main__':
    game = Kalah(PL_ONE)
    while True:
        game.update()