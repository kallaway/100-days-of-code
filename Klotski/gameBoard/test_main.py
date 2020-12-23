import unittest
import main
from tkinter import *




class TestGameBoard(unittest.TestCase):

    def test_plane(self):
        self.assertEquals(main.plane, main.tkinter.plane("hello"))

        # to fix tkinter unittest: https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app

# TODO: SEPARATE LOGIC FROM GUI AS MUCH AS POSSIBLE!!!!!

#  go here in case you are too lost https://github.com/Goshuujin/Klotski

if __name__ == '__main__':
    unittest.main()
