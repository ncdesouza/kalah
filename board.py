from kalah import *
from kalah.settings import *
import kalah


class Board:
    def __init__(self, num_seeds):
        self.board = []
        self.init_board(num_seeds)

    def init_board(self, num_seeds):
        for i in range(14):
            owner = kalah.PL_ONE if i < 7 else kalah.PL_TWO
            if i is 6 or i is 13:
                pos = kalah.HOUSE0_POS if (owner is kalah.PL_TWO) else kalah.HOUSE1_POS
                self.board.append(House(owner, (pos[0], pos[1])))
            else:
                if i < 7:
                    x = kalah.STORE0_POS[0] + (100 * i)
                    y = kalah.STORE0_POS[1]
                    self.board.append(Store(kalah.NUM_SEEDS, owner, (x, y)))
                else:
                    x = kalah.STORE7_POS[0] - (100 * (13 - i))
                    y = kalah.STORE7_POS[1]
                    self.board.append(Store(NUM_SEEDS, owner, (x, y)))

        # initialize component settings
        for i in range(14):
            cur = self.board[i]
            next_property = self.toObject((i + 1) if i < 13 else 0)
            cur.setNext(next_property)
            if cur.type is kalah.STORE:
                home = self.toObject(6 if i < 7 else 13)
                across = self.toObject(kalah.calcAcross(i))

                cur.set_across(across)
                cur.set_home(home)

    def toObject(self, index):
        return self.board[index]

    def numSeeds(self, origin):
        return origin.count_seeds()

    def draw_board(self):


    def print_board(self):
        count1 = []
        count2 = []
        for i in range(len(self.board)):
            if i < 7:
                count2.append(self.board[i].count_seeds())
            else:
                count1.append(self.board[i].count_seeds())
        count1.reverse()
        print " 13 12 11 10 9  8  7     "
        print "-----------------------"
        print count1
        print "  ", count2
        print("-----------------------")
        print "    0  1  2  3  4  5  6"
        print


class Property:
    def __init__(self, type, owner, width, height, (x, y)):
        self.width = width
        self.height = height
        self.position = (x, y)
        self.type = type
        self.owner = owner
        self.next = None
        self.seeds = []

    def get_position(self):
        return self.width, self.height

    def set_position(self, (x, y)):
        self.position = (x, y)

    def setNext(self, next_store):
        self.next = next_store

    def get_owner(self):
        return self.owner

    def count_seeds(self):
        return len(self.seeds)

    def put_seed(self, seed):
        seed.location = self
        self.seeds.append(seed)


class House(Property):
    def __init__(self, owner, (x, y)):
        Property.__init__(self, kalah.HOUSE, owner, kalah.HOUSE_WIDTH, kalah.HOUSE_HEIGHT, (x, y))


class Store(Property):
    def __init__(self, num_seeds, owner, (x, y)):
        Property.__init__(self, kalah.STORE, owner, kalah.STORE_WIDTH, kalah.STORE_HEIGHT, (x, y))
        self.across = None
        self.seeds = [Seed(self)] * num_seeds

    def set_across(self, store):
        self.across = store

    def set_home(self, home):
        self.home = home

    def get_seed(self):
        return self.seeds.pop()


class Seed:
    def __init__(self, location):
        self.width = kalah.SEED_HEIGHT
        self.height = kalah.SEED_WIDTH
        self.position = location.get_position()
        self.location = location

    def get_position(self):
        return self.width, self.height

    def set_position(self, new_position):
        self.position = new_position

if __name__ == '__main__':
    board = Board(3)
    print "Initial state: "
    board.print_board()