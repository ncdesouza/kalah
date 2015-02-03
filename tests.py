import unittest

from board import *


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)

    def tearDown(self):
        self.board = None

    def test_across(self):
        self.assertEqual(self.board.board[0].across, self.board.board[12],
                         'across reference does not match from p1')
        self.assertEqual(self.board.board[10].across, self.board.board[2],
                         'across reference does not match from p2')


    def test_get_next(self):
        self.assertEquals(self.board.board[0].get_next(), self.board.board[1])

    def test_another_turn(self):
        turn = self.board.board[3].move_seeds(0)
        self.assertEquals(turn, 0)

    def test_bulk_transfer_p1(self):
        print("Bulk Transfer P1 Test")
        self.board.print_board()
        self.board.board[3].move_seeds(0)
        self.board.board[0].move_seeds(0)
        self.board.print_board()
        self.assertEquals(self.board.board[3].count_seeds(), 0)
        self.board.print_board()
        self.assertEquals((self.board.board[3].get_across()).count_seeds(), 0)

    def test_bulk_transfer_p2(self):
        print("Bulk Transfer P2 Test")
        self.board.print_board()
        self.board.board[10].move_seeds(1)
        self.board.print_board()
        self.board.board[7].move_seeds(1)
        self.board.print_board()
        self.assertEqual(self.board.board[10].count_seeds(), 0)
        self.assertEqual((self.board.board[10].get_across()).count_seeds(), 0)

    def test_regular_gameplay(self):
        print("Skip Opponents Home Test")
        self.board.print_board()
        self.board.board[0].move_seeds(0)
        self.board.board[1].move_seeds(0)
        self.board.print_board()
        self.board.board[2].move_seeds(0)
        self.board.print_board()
        self.board.board[3].move_seeds(0)
        self.board.print_board()
        self.board.board[4].move_seeds(0)
        self.board.print_board()
        self.board.board[5].move_seeds(0)
        self.board.print_board()


    def test_skip_opponents_home(self):
        self.board.print_board()
        for i in range(7):
            self.board.board[5].seeds.append(Seed(self.board.board[6]))
        self.board.print_board()
        self.board.board[5].move_seeds(0)
        self.board.print_board()
        self.assertEqual(self.board.board[13].count_seeds(), 0)

    def test_opponent_skip_my_home(self):
def suite():
    suite = unittest.makeSuite(KalahTestCase, 'test')
    return suite

if __name__ == '__main__':
    unittest.main()