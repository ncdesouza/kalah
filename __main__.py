from controller import Kalah
from settings import *

def main():
    game = Kalah(PL_ONE, MOUSE_INPUT)
    while True:
        game.update()


if __name__ == '__main__':
    main()