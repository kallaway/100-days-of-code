

class klotski_board:
    def __init__(self):
        self.board = self.create_board()


    def create_board(self):
        board_x = []

        for x in range(4):
            board_y = []
            