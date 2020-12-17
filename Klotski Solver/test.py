import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_slit(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello', 'world'])
        #checks that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestGameBoard(unittest.TestCase):

    def test_boardexists(game_board):
        game_board.assertIs()



if __name__ == '__main__':
    unittest.main()
    