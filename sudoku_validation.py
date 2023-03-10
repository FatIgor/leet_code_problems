from typing import List


class sudoku_1:
    def __init__(self):
        self.offsets = [0, 0, 1, 0, 2, 0, 0, 1, 1, 1, 2, 1, 0, 2, 1, 2, 2, 2]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.check_lines(board):
            return False
        return self.check_squares(board)

    def check_squares(self, board):
        y = -3
        while y < 6:
            y += 3
            x = -3
            while x < 6:
                x += 3
                if self.check_square(board, x, y) == False:
                    return False
        return True

    def check_square(self, board, x, y):
        i = -2
        while i < 16:
            i += 2
            val = board[y + self.offsets[i + 1]][x + self.offsets[i]]
            if val != '.':
                j = i
                while j < 16:
                    j += 2
                    if val == board[y + self.offsets[j + 1]][x + self.offsets[j]]:
                        return False
        return True

    def check_lines(self, board):
        for line in board:
            x = -1
            while x < 7:
                x += 1
                val = line[x]
                if val != '.':
                    xx = x
                    while xx < 8:
                        xx += 1
                        if val == line[xx]:
                            return False
        x = -1
        while x < 8:
            x += 1
            y = -1
            while y < 7:
                y += 1
                val = board[y][x]
                if val != '.':
                    yy = y
                    while yy < 8:
                        yy += 1
                        if val == board[yy][x]:
                            return False
        return True

    def run_tests(self):
        board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        print(self.isValidSudoku(board1))
        print(self.isValidSudoku(board2))
