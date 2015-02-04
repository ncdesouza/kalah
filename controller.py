import sys
import math

from pygame.constants import QUIT

from board import *
from settings import *


class Kalah:
    def __init__(self, player_num, input_type):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.board = Board(NUM_SEEDS)
        self.clock = pygame.time.Clock()
        self.count = 0
        self.turn = PL_ONE
        self.me = player_num

        if input_type is KEY_INPUT:
            self.input_type = self.keyboard_controls
        if input_type is MOUSE_INPUT:
            self.input_type = self.mouse_controls

        print("You are player:" + str(self.me))
        print("Player " + str(self.turn) + "'s turn")

    def update(self):

        if isGameOver(self.board):
            pass

        self.screen.fill(0)
        self.board.draw_board(self.screen)
        self.input_type()

        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(60)
        self.count += 1

    def keyboard_controls(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if self.turn is self.me and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.turn = self.move(1, self.me)
                if event.key == pygame.K_2:
                    self.turn = self.move(2, self.me)
                if event.key == pygame.K_3:
                    self.turn = self.move(3, self.me)
                if event.key == pygame.K_4:
                    self.turn = self.move(4, self.me)
                if event.key == pygame.K_5:
                    self.turn = self.move(5, self.me)
                if event.key == pygame.K_6:
                    self.turn = self.move(6, self.me)
                self.switch_turn()
                self.print_turn()


    def mouse_controls(self):
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            x = int(math.ceil(mouse[0]) / 110)
            y = 2 - (int(math.ceil(mouse[1]) / 110))

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if self.turn is self.me and event.type == pygame.MOUSEBUTTONUP:
                if self.me is y:
                    self.turn = self.move(x, self.me)
                    self.switch_turn()
                    self.print_turn()
                else:
                    self.invalid_move(self.me)

    def switch_turn(self):
        self.me = self.turn

    def move(self, input, player):
        def index():
            if player is PL_ONE:
                return input - 1
            elif player is PL_TWO:
                return (input - 1) + ((6 - (input - 1)) * 2)

        def piece(index):
            return self.board.board[index]

        return piece(index()).move_seeds(player)

    def invalid_move(self, player):
        print("Invalid move: you are Player " + str(player) + ". Try again.")

    def print_turn(self):
        print("Player " + str(self.turn) + "'s turn")

if __name__ == '__main__':
    game = Kalah(PL_ONE, MOUSE_INPUT)
    while True:
        game.update()