import unittest
import game_board
import pygame



class TestGameBoard(unittest.TestCase):

    def test_boardfunction(self):
        self.assertEquals(game_board.board_function(), 3)

    def test_boardvariable(self):
        self.assertEquals(game_board.board, 2)

    def test_plane(self):
        self.assertEquals(game_board.plane, pygame.display.set_mode((800,600)))


if __name__ == '__main__':
    unittest.main()
