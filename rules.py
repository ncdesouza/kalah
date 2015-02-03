from kalah import *


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


def getAcross(piece):
    """
    getAcross():
        this function will move to the piece across from it.
    :param piece: The piece you wish to move from
    :return: An object of the piece across
    """
    return piece.get_across


def transfer(piece):
    """
    transfer():
        provides a method of transferring seeds from a location
        to other locations
    :param piece: the piece distributing the seeds
    :return: None
    """
    def count(p):
        return p.count()
    num_seeds = count(piece)

    def recurse(origin, dest=None, count=None):
        def isLastSeed():
            return count == 1
        count = num_seeds if count is None else count
        d = getNext(origin) if dest is None else getNext(dest)

        def put(o, d):
            def get(o):
                return o.get_seed()
            return d.put_seed((get(piece)))

        if isLastSeed():
            put(piece, d)
            checkSpecialMove(d)

        else:
            recurse(origin, d,  count - 1)
            return put(piece, d)
    return recurse(piece)





