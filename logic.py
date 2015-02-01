from kalah.rules import *


def isGameOver(board):
    """
    isGameOver():
        checks if there is anymore moves left
        on the board.
    :param: board: The game board
    :return: True if the game is over,
                otherwise False
    """
    pass


def areStoresEmpty(board, pl1=None, pl2=None, p1_empty=True, p2_empty=True):
    """
    areStoresEmpty():
        checks to see if all of either players
        stores are empty
    :param board: The board object
    :return: True if either players collection of stores
                are empty, otherwise False
    """
    if pl1 is None and pl2 is None:
        pl1 = toObject(0, board)
        pl2 = toObject(7, board)

    if isHouse(pl1) or isHouse(pl2):
        return True

    if p1_empty or p2_empty:
            return areStoresEmpty(board, getNext(pl1), getNext(pl2), isStoreEmpty(pl1), isStoreEmpty(pl2))
    else:
        return False


def isStoreEmpty(store):
    """
    isStoreEmpty():
        checks if a single store is empty
    :param store: The store object
    :return: True if empty, otherwise False
    """
    def compare(s):
        def count(s):
            return s.count_seeds()
        return count(s) == 0
    return compare(store)


def whoWon():
    """
    whoWon():
        checks which player has won the game.
    :return: 0 if player 0, otherwise 1
    """
    pass


def isLastSeed(piece):
    """
    isLastSeed():
        checks if the seed being placed is the last one
        in the selected store.
    :param: piece: The piece that is passing the seed
    :return: True if the seed being placed is last,
                otherwise False.
    """
    def check(p):
        def count(p):
            return p.count_seeds()
        return count(p) == 1
    return check(piece)


def isOwner(player, piece):
    """
    isOwner():
        checks if the player owns the piece
    :param player: the number of the player who made the move
    :param piece: A piece of the board
    :return: True if player owns the piece,
                otherwise False
    """
    pass


def isHouse(piece):
    """
    isHouse():
        checks to see if the piece is a home
    :param piece: The piece to check
    :return: True if the piece is a home,
                otherwise False
    """
    return piece.type is HOUSE


def isStore(piece):
    """
    isStore():
        checks to see if the piece is a store
    :param piece: The piece to check
    :return: True if the piece is a store,
                otherwise False
    """
    pass