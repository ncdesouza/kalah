import pygame

from logic import *


class Board:
    def __init__(self, num_seeds):
        self.board = {}
        interval = (BOARDER_SIZE + HOUSE_WIDTH)
        for i in range(7):
            if i is 6:
                self.board[i] = House(i, PL_ONE,
                                      ((i * interval) + interval + BOARDER_SIZE),
                                      BOARDER_SIZE)

                self.board[13] = House(13, PL_TWO, BOARDER_SIZE, BOARDER_SIZE)
            else:
                new_x = (interval + (i * interval) + BOARDER_SIZE)
                self.board[i] = Store(i, num_seeds, PL_ONE,
                                      new_x, BOARDER_SIZE + interval)
                self.board[i + ((6 - i) * 2)] = Store(i, num_seeds, PL_TWO,
                                                      new_x, BOARDER_SIZE)
        for i in range(7):
            if i < 6:
                store1 = self.board[i]
                store2 = self.board[i + ((6 - i) * 2)]
                store1.set_across(store2)
                store1.set_home(self.board[6])
                store1.set_next(self.board[i + 1])
                store2.set_across(store1)
                store2.set_home(self.board[13])
                store2.set_next(self.board[1 + (i + ((6 - i) * 2))])
            else:
                home1 = self.board[i]
                home2 = self.board[13]
                home1.set_next(self.board[i + 1])
                home2.set_next(self.board[0])

    def piece(self, i):
        return self.board[i]

    def draw_board(self, screen):
        for i in range(len(self.board)):
            self.board[i].draw(screen)

    def print_board(self):
        count1 = []
        count2 = []
        for i in range(len(self.board)):
            if i < 7:
                count2.append(self.board[i].count())
            else:
                count1.append(self.board[i].count())
        count1.reverse()
        print " 13 12 11 10 9  8  7     "
        print "-----------------------"
        print count1
        print "  ", count2
        print("-----------------------")
        print "    0  1  2  3  4  5  6"
        print


class Property:
    def __init__(self, name, isa, owner, width, height, x, y):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.position = None
        self.colour = LIME if owner is PL_ONE else RED
        self.isa = isa
        self.owner = owner
        self.next = None
        self.seeds = []

    def get_rect(self):
        return self.get_pos(), self.get_size()

    def get_size(self):
        return self.width, self.height

    def get_pos(self):
        return self.x, self.y

    def set_position(self, (x, y)):
        self.position = (x, y)

    def get_next(self):
        return self.next

    def set_next(self, next_store):
        self.next = next_store

    def get_type(self):
        return self.isa

    def get_owner(self):
        return self.owner

    def count(self):
        return len(self.seeds)

    def put_seed(self, seed):
        seed.location = self
        self.seeds.append(seed)

    def draw(self, screen):
        def inner_rect():
            def split(rect):
                def alter((x, y), sub=False):
                    b = 5 if not sub else -10
                    return x + b, y + b

                return alter(rect[0]), alter(rect[1], True)

            return split(self.get_rect())

        def center(text, labels=False):
            def calc(var):
                opt = self.width if var is self.x else self.height
                size = text.get_width() if var is self.x else text.get_height()
                return var + (opt // 2) - (size // 2)

            if labels:
                return calc(self.x), 225

            return calc(self.x), calc(self.y)

        pygame.draw.rect(screen, self.colour, pygame.Rect(self.get_rect()))
        pygame.draw.rect(screen, BLACK, pygame.Rect(inner_rect()))
        font = pygame.font.Font(None, 25)
        # for x in range(1, 7):
        # labels = font.render("{0}".format(x), True, WHITE)
        # screen.blit(labels, center(labels, True))

        text = font.render("{0}".format(self.count()), True, WHITE)
        screen.blit(text, center(text))


class House(Property):
    def __init__(self, name, owner, x, y):
        Property.__init__(self, name, HOUSE, owner, HOUSE_WIDTH, HOUSE_HEIGHT, x, y)

    def bullk_transfer(self, game_over=True):
        return True


class Store(Property):
    def __init__(self, name, num_seeds, owner, x, y):
        Property.__init__(self, name, STORE, owner, STORE_WIDTH, STORE_HEIGHT, x, y)
        self.home = None
        self.across = None
        self.seeds = [Seed(self)] * num_seeds

    def set_across(self, store):
        self.across = store

    def get_across(self):
        return self.across

    def get_home(self):
        return self.home

    def set_home(self, home):
        self.home = home

    def get_seed(self):
        return self.seeds.pop()

    def move_seeds(self, player, destination=False):
        if isEmpty(self) and isOwner(player, self) and isStore(self):
            print("Invalid Move: Player " + str(player) + "'s store " + str(self.name) + " is empty. Try again")
            return PL_ONE if player is PL_ONE else PL_TWO
        count = self.count()
        nxt = self.get_next() if not destination else destination.get_next()
        if isHouse(nxt) and not isOwner(player, nxt):
            return self.move_seeds(player, nxt)

        nxt.put_seed(self.get_seed())
        if count == 1:
            next_turn = checkSpecialMove(nxt, player)
            return PL_ONE if next_turn is PL_ONE else PL_TWO
        return self.move_seeds(player, nxt)

    def bulk_transfer(self, game_over=False):
        def transfer(o, dest=None):
            d = o if dest is None else dest

            def put(d):
                def get(o):
                    return o.get_seed()

                return (d.get_home()).put_seed(get(o))

            return put(d)

        if not game_over:
            c = self.across.count()
            for x in range(c):
                transfer(self.across, self)

            c = self.count()
            for x in range(c):
                transfer(self)
        else:
            # If the across piece is not empty,
            # transfer all pieces to its home
            if not isEmpty(self.get_across()):
                for x in range((self.get_across()).count()):
                    transfer(self.get_across())

            # If the piece is not empty,
            # transfer all pieces to its home
            if not isEmpty(self):
                for x in range(self.count()):
                    transfer(self)

            # Base case: Reached a house
            check = isHouse(self.get_next())
            if check:
                # return true to caller function
                return True

            # recurse to next piece
            return (self.get_next()).bulk_transfer(True)


class Seed():
    def __init__(self, location):
        self.color = WHITE
        self.radius = SEED_RADIUS
        self.x = location.x
        self.y = location.y
        self.location = location
        self.target_pos = (self.x, self.y)

    def get_size(self):
        return self.radius

    def get_position(self):
        return self.x, self.y

    def set_target(self, new_position):
        self.target_pos = new_position
        (x, y) = new_position

    def display(self, screen):
        pygame.draw.circle(screen, self.color, self.get_position(), self.get_size())


if __name__ == '__main__':
    board = Board(3)
    print "Initial state: "
    board.print_board()
    board.board[0].move_seeds()
    board.print_board()