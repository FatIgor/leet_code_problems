from typing import List

from sudoku_validation import sudoku_1


class q0037_sudoku_solver:

    def __init__(self):
        self.solved = False
        self.theBoard = None
        self.missingInSquares = []
        self.possibilitiesBoard = []
        self.updateCount = -1
        board = self.theBoard

    def solver(self, board):
        self.possibilitiesBoard = []
        self.updateCount = -1
        for i in range(0, 9):
            new = []
            for j in range(0, 9):
                new.append('123456789')
            self.possibilitiesBoard.append(new)
        checker = sudoku_1()
        valid = checker.isValidSudoku(board)
        if valid == False:
            print('Invalid board.')
            exit()
        self.theBoard = board
        self.print_board()
        tries = 100
        while (self.check_solved() == False) and tries > 0:
            tries -= 1
            while self.updateCount != 0:
                self.updateCount = 0
                for x in range(0, 9):
                    self.check_singles(x)
                    for y in range(0, 9):
                        if self.theBoard[y][x] != ".":
                            self.check_horizontal(x, y)
                            self.check_vertical(x, y)
                for x in range(0, 9, 3):
                    for y in range(0, 9, 3):
                        self.check_square(x, y)
        self.print_board()
        valid = checker.isValidSudoku(self.theBoard)
        if valid == False:
            print('Invalid board.')
            exit()

    def check_singles(self, x):
        count = []
        for i in range(0, 9):
            count.append(0)
        for y in range(0, 9):
            p = self.possibilitiesBoard[y][x]
            for j in range(0, len(p)):
                num = int(p[j])-1
                count[num] += 1
        for i in range(0, 9):
            if count[i] == 1:
                for j in range(0, 9):
                    if str(i+1) in self.possibilitiesBoard[j][x]:
                        self.possibilitiesBoard[j][x] = str(i+1)

    def check_square(self, x, y):
        for i in range(0, 3):
            for j in range(0, 3):
                self.clear_possibles(x, y, self.theBoard[y + i][x + j])

    def clear_possibles(self, x, y, check_val):
        if check_val == ".":
            return
        for i in range(0, 3):
            for j in range(0, 3):
                if check_val in self.possibilitiesBoard[y + i][x + j] and len(
                        self.possibilitiesBoard[y + i][x + j]) != 1:
                    self.possibilitiesBoard[y + i][x + j] = self.possibilitiesBoard[y + i][x + j].replace(check_val, "")
                    self.updateCount += 1
                if check_val == self.possibilitiesBoard[y + i][x + j]:
                    self.theBoard[y + i][x + j] = check_val

    def check_vertical(self, x, y):
        checkVal = self.theBoard[y][x]
        for i in range(0, 9):
            if i == y:
                self.possibilitiesBoard[i][x] = checkVal
            elif checkVal in self.possibilitiesBoard[i][x]:
                self.possibilitiesBoard[i][x] = self.possibilitiesBoard[i][x].replace(checkVal, "")
                self.updateCount += 1
            if len(self.possibilitiesBoard[i][x]) == 1:
                self.theBoard[i][x] = self.possibilitiesBoard[i][x]

    def check_horizontal(self, x, y):
        checkVal = self.theBoard[y][x]
        for i in range(0, 9):
            if i == x:
                self.possibilitiesBoard[y][i] = checkVal
            elif checkVal in self.possibilitiesBoard[y][i]:
                self.possibilitiesBoard[y][i] = self.possibilitiesBoard[y][i].replace(checkVal, "")
                self.updateCount += 1
            if len(self.possibilitiesBoard[y][i]) == 1:
                self.theBoard[y][i] = self.possibilitiesBoard[y][i]

    def check_solved(self):
        for y in range(0, 9):
            for x in range(0, 9):
                if self.theBoard[y][x] == ".":
                    return False
        return True

    def print_board(self):
        for y in range(0, 9):
            str = ""
            for x in range(0, 9):
                str = str + self.theBoard[y][x] + " "
            print(str)
        print("")

    def tests(self):
        print(self.__class__.__name__)
        board = [[".", ".", ".", "2", "6", ".", "7", ".", "1"],
                 ["6", "8", ".", ".", "7", ".", ".", "9", "."],
                 ["1", "9", ".", ".", ".", "4", "5", ".", "."],

                 ["8", "2", ".", "1", ".", ".", ".", "4", "."],
                 [".", ".", "4", "6", ".", "2", "9", ".", "."],
                 [".", "5", ".", ".", ".", "3", ".", "2", "8"],

                 [".", ".", "9", "3", ".", ".", ".", "7", "4"],
                 [".", "4", ".", ".", "5", ".", ".", "3", "6"],
                 ["7", ".", "3", ".", "1", "8", ".", ".", "."]]
        self.solver(board)
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
        board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
                 ["7", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", "2", ".", "1", ".", "9", ".", ".", "."],
                 [".", ".", "7", ".", ".", ".", "2", "4", "."],
                 [".", "6", "4", ".", "1", ".", "5", "9", "."],
                 [".", "9", "8", ".", ".", ".", "3", ".", "."],
                 [".", ".", ".", "8", ".", "3", ".", "2", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "6"],
                 [".", ".", ".", "2", "7", "5", "9", ".", "."]]
        self.solver(board)
