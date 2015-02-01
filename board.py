from kalah.rules import *
from kalah.settings import *


class Board:
    def __init__(self, num_seeds):
        self.board = []
        self.init_board(num_seeds)

    def init_board(self, num_seeds):
        for i in range(14):
            if i < 7:
                owner = PL_ONE
            else:
                owner = PL_TWO

            if i is 6 or i is 13:
                self.board.append(House(owner))
            else:
                self.board.append(Store(num_seeds, owner))

        def calcAcross(index):
            def multi(i):
                def under(i):
                    return 6 - i

                def over(i):
                    return i - 6

                if i < 6:
                    return 2 * under(i)
                else:
                    return -2 * over(i)

            return index + multi(index)

        for i in range(14):
            cur = self.board[i]
            next_property = self.toObject((i + 1) if i < 13 else 0)
            cur.setNext(next_property)
            if cur.type is STORE:
                home = self.toObject(6 if i < 7 else 13)
                across = self.toObject(calcAcross(i))

                cur.set_across(across)
                cur.set_home(home)

    def toObject(self, index):
        return self.board[index]

    def numSeeds(self, origin):
        return origin.count_seeds()

    def transfer_seeds(self, player, store):


        # game rules

        def checkOwner(dest):
            def owner(d):
                return d.owner

            return owner(dest) == player

        def checkType():
            pass

        def isLastMove():
            pass

        origin = self.toObject(store)
        num_seeds = self.numSeeds(origin)

        transfer(origin, num_seeds)


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
    def __init__(self, type, owner):
        self.type = type
        self.owner = owner
        self.next = None
        self.seeds = []

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
    def __init__(self, owner):
        Property.__init__(self, HOUSE, owner)


class Store(Property):
    def __init__(self, num_seeds, owner):
        Property.__init__(self, STORE, owner)
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
        self.location = location


if __name__ == '__main__':
    board = Board(3)
    print "Initial state: "
    board.print_board()

    board.transfer_seeds(0, 1)
    print("select house 1:")
    board.print_board()

    board.transfer_seeds(0, 2)
    print "select house 2:"
    board.print_board()

    board.transfer_seeds(0, 3)
    print("select house 3:")
    board.print_board()

    board.transfer_seeds(0, 0)
    print("select house 0:")
    board.print_board()