import unittest
import game_board





class TestGameBoard(unittest.TestCase):

    def test_boardfunction(self):
        self.assertEquals(game_board.board_function(), 3)

    def test_boardvariable(self):
        self.assertEquals(game_board.board, 2)



if __name__ == '__main__':
    unittest.main()
    