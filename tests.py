import unittest
from kalah import *


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)

    def tearDown(self):
        self.board = None

    def test_across(self):
        self.assertEqual(self.board.board[0].across, self.board.board[12],
                         'across reference does not match')

    def test_next(self):
        i = 1
        for b in self.board.board:
            self.assertEqual(b.next, self.board.board[i])
            i = 0 if i is 13 else (i + 1)

    def test_nav(self):
        n = 15
        b = self.board.board[0]
        for i in range(n):
            b = b.next
        self.assertEqual(b, self.board.board[1])

    def test_transfer(self):
        self.board = Board(3)
        store = toObject(1, self.board)
        transfer(store)
        self.assertEqual(self.board.board[1].count_seeds(), 0)
        self.assertEqual(self.board.board[2].count_seeds(), 4)
        self.assertEqual(self.board.board[3].count_seeds(), 4)
        self.assertEqual(self.board.board[3].count_seeds(), 4)

    def test_transfer_seeds(self):
        self.board = Board(3)
        store = toObject(3, self.board)
        transfer(store)
        self.assertEqual(self.board.board[3].count_seeds(), 0)
        self.assertEqual(self.board.board[4].count_seeds(), 4)
        self.assertEqual(self.board.board[5].count_seeds(), 4)
        self.assertEqual(self.board.board[6].count_seeds(), 1)

    def test_isStoreEmpty(self):
        self.board = Board(3)
        store = toObject(1, self.board)
        transfer(store)
        self.assertEqual(isStoreEmpty(toObject(1, self.board)), True)
        self.assertEqual(isStoreEmpty(toObject(2, self.board)), False)

    def test_areStoresEmpty(self):
        self.board = Board(0)
        self.assertEqual(areStoresEmpty(self.board), True)
        self.board = Board(3)
        self.assertEqual(areStoresEmpty(self.board), False)

    def test_isLastPiece(self):
        store1 = Store(3, 1)
        store2 = Store(0, 1)


def suite():
    suite = unittest.makeSuite(KalahTestCase, 'test')
    return suite

if __name__ == '__main__':
    unittest.main()