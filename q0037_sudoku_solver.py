from typing import List

from sudoku_validation import sudoku_1


class q0037_sudoku_solver:

    def __init__(self):
        self.theBoard = None
        self.missingInSquares = []
        self.possibilitiesBoard = None

    def solver(self, board):
        checker = sudoku_1()
        valid = checker.isValidSudoku(board)
        if valid == False:
            print('Invalid board.')
            exit()
        self.theBoard = board
        self.create_possibilities_board()
        print('This problem not yet solved')

    def create_possibilities_board(self):
        y = 0
        while y < 9:
            x = 0
            while x < 9:
                self.missingInSquares.__add__(self.get_missing_in_squares(x, y))
                x += 3
            y += 3

    def get_missing_in_squares(self, x, y):
        missing = ''
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if (self.theBoard[y + j][x + i] == '.'):
                    missing += str(1 + i + j * 3)
                j += 1
            i += 1
        return missing

    def tests(self):
        print(self.__class__.__name__)
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.solver(board)
