from kalah import *


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


def transfer(piece):
    def count(p):
        return p.count_seeds()
    num_seeds = count(piece)

    def recurse(origin, dest=None, count=None):
        def isLastSeed():
            return count is 1
        count = num_seeds if count is None else count
        d = getNext(origin) if dest is None else getNext(dest)

        def put(o, d):
            def get(o):
                return o.get_seed()
            return d.put_seed((get(piece)))

        if isLastSeed():
            return put(piece, d)
        else:
            recurse(origin, d,  count - 1)
            return put(piece, d)
    return recurse(piece)



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