from collections import OrderedDict


class Grid:
    def __init__(self, size):
        self.board = [0 for x in range(size * size)]
        self.stops = OrderedDict()
        self.size = size

    #
    # Provide a method for print() to use
    #
    def __str__(self):
        output = ""
        for i, x in enumerate(self.board):
            if i % self.size == 0 and i > 1:
                output += "\n"
            output += "{} ".format(x)
        return output

    #
    # Provide a way to insert a value into the board at an empty (x, y) coordinate
    #
    def insert(self, pos, value):
        x, y = pos
        pos = x + self.size * y
        if self.board[pos] == 0:
            self.board[pos] = value
            return True
        return False

    #
    # Add a stop to the grid
    #
    def add_stop(self, pos, value):
        x, y = pos
        self.insert(pos, value)
        self.stops[value] = x + self.size * y

    #
    # Merge another board into this grid (keep the history intact)
    #
    def merge_board(self, board):
        for i, x in enumerate(board):
            if x is 'X':
                self.board[i] = x
