import unittest
import pieces
import pygame

class TestGamePieces(unittest.TestCase):

    def test_pieceExists(self):
        self.assertEquals(pieces.smallest_cube, pygame.draw.rect )


if __name__ == '__main__':
    unittest.main()