import unittest

from board import *


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)

    def tearDown(self):
        self.board = None

    def test_across(self):
        self.assertEqual(self.board.board[0].get_across(), self.board.board[12],
                         'across reference does not match from p1')
        self.assertEqual(self.board.board[10].get_across(), self.board.board[2],
                         'across reference does not match from p2')

    def test_get_next(self):
        self.assertEquals(self.board.board[0].get_next(), self.board.board[1])

    def test_another_turn(self):
        turn = self.board.board[3].move_seeds(0)
        self.assertEquals(turn, 0)

    def test_bulk_transfer_p1(self):
        print("Bulk Transfer P1 Test")
        # self.board.print_board()
        self.board.board[3].move_seeds(0)
        self.board.board[0].move_seeds(0)
        # self.board.print_board()
        self.assertEquals(self.board.board[3].count(), 0)
        # self.board.print_board()
        self.assertEquals((self.board.board[3].get_across()).count(), 0)

    def test_bulk_transfer_p2(self):
        print("Bulk Transfer P2 Test")
        # self.board.print_board()
        self.board.board[10].move_seeds(1)
        # self.board.print_board()
        self.board.board[7].move_seeds(1)
        # self.board.print_board()
        self.assertEqual(self.board.board[10].count(), 0)
        self.assertEqual((self.board.board[10].get_across()).count(), 0)

    def test_regular_game_play(self):
        print("Skip Opponents Home Test")
        # self.board.print_board()
        self.board.board[0].move_seeds(0)
        self.board.board[1].move_seeds(0)
        # self.board.print_board()
        self.board.board[2].move_seeds(0)
        # self.board.print_board()
        self.board.board[3].move_seeds(0)
        # self.board.print_board()
        self.board.board[4].move_seeds(0)
        # self.board.print_board()
        self.board.board[5].move_seeds(0)
        # self.board.print_board()


    def test_skip_opponents_home(self):
        # self.board.print_board()
        for i in range(7):
            self.board.board[5].seeds.append(Seed(self.board.board[6]))
        # self.board.print_board()
        self.board.board[5].move_seeds(0)
        # self.board.print_board()
        self.assertEqual(self.board.board[13].count(), 0)

    def test_opponent_skip_my_home(self):
        pass

    def test_game_play(self):
        print("Game Play")
        # self.board.print_board()
        turn = self.board.board[3].move_seeds(0)
        # self.board.print_board()
        self.assertEqual(turn, PL_ONE,
                         "Move Player 1 piece 2: Wrong player turn")
        self.assertEqual(self.board.board[3].count(), 0,
                         "Move Player 1 piece 4")
        self.assertEqual(self.board.board[4].count(), 4,
                         "Move Player 1 piece 4 to 5")
        self.assertEqual(self.board.board[5].count(), 4,
                         "Move Player 1 piece 2 to 4")
        self.assertEqual(self.board.board[6].count(), 1,
                         "Move Player 1 piece 2 to ")

        turn = self.board.board[0].move_seeds(0)
        # self.board.print_board()
        self.assertEqual(self.board.board[0].count(), 0,
                         "Move Player 1 piece 0")
        self.assertEqual(self.board.board[1].count(), 4,
                         "Move Player 1 piece 0 to 1")
        self.assertEqual(self.board.board[2].count(), 4,
                         "Move Player 1 piece 0 to 2")
        self.assertEqual(self.board.board[3].count(), 0,
                         "Move Player 1 piece 0 to 3")
        self.assertEqual((self.board.board[3].get_across()).count(), 0,
                         "Bulk transfer 3 across to player 1 home")
        self.assertEqual(turn, PL_TWO,
                         "Result of turn from move 0 to 3: PL_TWO")

        turn = self.board.board[10].move_seeds(1)
        # self.board.print_board()
        self.assertEqual(turn, PL_TWO,
                         "Transfer 10: Turn failed")
        self.assertEqual(self.board.piece(10).count(), 0,
                         "Empty piece 10 failed")
        self.assertEqual(self.board.piece(11).count(), 4,
                         "Tansfer 10 -> 11 failed")
        self.assertEqual(self.board.piece(12).count(), 4,
                         "Tansfer 10 -> 12 failed")
        self.assertEqual(self.board.piece(13).count(), 1,
                         "Tansfer 10 -> 13 failed")

        turn = self.board.board[7].move_seeds(1)
        # self.board.print_board()
        self.assertEqual(turn, PL_ONE,
                         "Transfer 10: Turn return failed")
        self.assertEqual(self.board.piece(7).count(), 0,
                         "Empty piece 7 failed")
        self.assertEqual(self.board.piece(8).count(), 4,
                         "Tansfer 7 -> 8 failed")
        self.assertEqual(self.board.piece(9).count(), 1,
                         "Tansfer 7 -> 10 failed")
        self.assertEqual(self.board.piece(10).count(), 0,
                         "Bulk Tansfer 7 -> 11 -> p2 home failed")
        self.assertEqual((self.board.piece(10).get_across()).count(), 0,
                         "Bulk Transfer 7 -> 11.across() -> p2 home: failed")

    def test_areStoresEmpty(self):
        print("Are stores equal")
        self.assertFalse(areStoresEmpty(self.board))
        board_test = Board(0)
        self.assertTrue(areStoresEmpty(board_test))
        (board_test.piece(7)).put_seed(Seed(board_test.piece(7)))
        # board_test.print_board()
        self.assertTrue(areStoresEmpty(board_test))
        (board_test.piece(5)).put_seed(Seed(board_test.piece(5)))
        # board_test.print_board()
        self.assertFalse(areStoresEmpty(board_test))

    def test_isGameOver(self):
        print("Game Over Test")
        board_test = Board(0)
        board_test.print_board()
        self.assertTrue(isGameOver(board_test),
                        "Board empyt: expctd=True")

        print('Opponents Side Test')
        print("Before")
        board_test.print_board()
        (board_test.piece(10)).seeds.append(Seed(board_test.piece(10)))
        print("After Insert")
        board_test.print_board()
        self.assertEqual((board_test.piece(10)).count(), board_test.board[10].count())
        self.assertTrue(isGameOver(board_test),
                        "Seed on opponent side: Fail")
        print("After Clean")
        board_test.print_board()

        board_test.piece(3).seeds.append(Seed(board_test.piece(4)))
        board_test.print_board()
        check = isGameOver(board_test)
        self.assertTrue(check,
                        "Seed on one side: expctd=True")
        print("Seed on both sides")
        print("First seed inserted -> opponents side")
        board_test.piece(10).seeds.append(Seed(board_test.piece(10)))
        board_test.print_board()
        print("second seed inserted --> myside")
        board_test.piece(3).seeds.append(Seed(board_test.piece(4)))
        board_test.print_board()
        self.assertFalse(isGameOver(board_test),
                         "Seed on both sides: expctd=False")
        print("After Clean: Expected --> False: (No Clean)")
        board_test.print_board()

    def test_bulk_transfer_EOG(self):
        print("EndOfGame Bulk Transfer Test")
        board_test = Board(0)
        (board_test.piece(3)).put_seed(Seed(board_test.piece(3)))
        check = (board_test.piece(1)).bulk_transfer(True)
        self.assertTrue(check)
        check = (board_test.piece(10).put_seed(Seed(board_test.piece(10))))
        self.assertFalse(check)



def suite():
    suite = unittest.makeSuite(KalahTestCase, 'test')
    return suite

if __name__ == '__main__':
    unittest.main()