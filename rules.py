from .settings import *


def toObject(index, board):
    """
    toObject():
        converts an index to its object
    :param index: an int to represent the index of the array
    :param board: the board object
    :return: <Object> representing the piece
    """
    return board.board[index]


def getNext(piece):
    """
    getNext():
        provides a method of traversing the board like
        a circular linked list
    :param piece: The present piece
    :return: An object of the next piece
    """
    return piece.next


def transfer(player, piece):
    def recurse(orig, count, dest=None):
            def get_next(o):
                d = o.next if dest is None else dest.next
                if count is 1:
                    return d
                else:
                    recurse(o, count - 1, d)
                    return d
            def put(o, d):
                def get(o):
                    return o.get_seed()
                return d.put_seed(get(o))
            return put(orig, get_next(orig))


# def bulk_transfer(dest):
#     def house(o):
#         return o.home
#
#     def across(o):
#         return o.across
#
#     for x in range(self.numSeeds(dest)):
#         transfer(dest, house(dest))
#     store2 = across(dest)
#     for x in range(self.numSeeds(store2)):
#         transfer(store2, house(dest))



# destination = self.toObject(store + i)
        #
        #     # On the last seed transfer
        # if i is num_seeds:
        #     # check if player owns the property
        #     if checkOwner(destination):
        #         # check to see if its a house
        #         if destination.type is HOUSE:
        #             # put the seed in the house
        #             transfer(origin)
        #             # signal another turn
        #             return player
        #         # check to see if its a store
        #         if destination.type is STORE:
        #             # check to see if the number of seeds is 0
        #             if destination.count_seeds() is 0:
        #                 # check to see if the across store has any seeds
        #                 if destination.across.count_seeds() > 0:
        #                     # first transfer seed
        #                     transfer(origin)
        #                     # transfer all seeds from destination and it's across to home
        #                     bulk_transfer(destination)
        #                 else:
        #                     # regular transfer
        #                     destination.put_seed(self.board[store].get_seed())
        #                     return 0 if player is 0 else 1
        #             else:
        #                 destination.put_seed(self.board[store].get_seed())
        #                 return 0 if player is 0 else 1
        #         else:
        #             destination.put_seed(self.board[store].get_seed())
        #             return 0 if player is 0 else 1
        #     else:
        #         destination.put_seed(self.board[store].get_seed())
        #         return 0 if player is 0 else 1
        # else:
            # destination.put_seed(self.board[store].get_seed())