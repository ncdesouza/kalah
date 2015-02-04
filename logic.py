from settings import *

def isGameOver(board):
    """
    isGameOver():
        checks if there is anymore moves left
        on the board.
    :param: board: The game board
    :return: True if the game is over,
                otherwise False
    """
    if areStoresEmpty(board):
        return (board.piece(0)).bulk_transfer(True)
    else:
        return False


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
        pl1 = board.piece(0)
        pl2 = board.piece(7)

    p1_empty = p1_empty if not p1_empty else isEmpty(pl1)
    p2_empty = p2_empty if not p2_empty else isEmpty(pl2)

    if isHouse(pl1) or isHouse(pl2):
        return True

    if p1_empty or p2_empty:
        return areStoresEmpty(board, pl1.get_next(),
                              pl2.get_next(), p1_empty,
                              p2_empty)
    else:
        return False


def isEmpty(store, was=False):
    """
    isStoreEmpty():
        checks if a single store is empty
    :param store: The store object
    :return: True if empty, otherwise False
    """

    def compare(s):
        def count(s):
            return s.count()

        return count(s) == (0 if not was else 1)

    return compare(store)


def whoWon():
    """
    whoWon():
        checks which player has won the game.
    :return: 0 if player 0, otherwise 1
    """
    pass


def checkSpecialMove(piece, player=1):
    """
    checkSpecialMove():
        This function checks whether the move qualifies
        for any special treatment.
    :return:
    """
    if isHouse(piece):
        return PL_ONE if player is PL_ONE else PL_TWO
    # check if the piece is a store, who owns it and if it has pieces across
    if isStore(piece):
        if isOwner(player, piece):
            test = isEmpty(piece.get_across())
            if not isEmpty(piece.get_across()):
                test = isEmpty(piece, True)
                if isEmpty(piece, True):
                    # transfer all seeds in the house and the house across to the
                    # players home who's turn it is
                    piece.bulk_transfer()
    return PL_ONE if player is PL_TWO else PL_TWO


def isOwner(turn, piece):
    """
    isOwner():
        checks if the player owns the piece
    :param player: the number of the player who made the move
    :param piece: A piece of the board
    :return: True if player owns the piece,
                otherwise False
    """

    def comp(p):
        return piece.owner == turn

    return comp(piece)


def isHouse(piece):
    """
    isHouse():
        checks to see if the piece is a home
    :param piece: The piece to check
    :return: True if the piece is a home,
                otherwise False
    """

    return True if piece.get_type() == HOUSE else False


def isStore(piece):
    """
    isStore():
        checks to see if the piece is a store
    :param piece: The piece to check
    :return: True if the piece is a store,
                otherwise False
    """
    return True if piece.get_type() == STORE else False