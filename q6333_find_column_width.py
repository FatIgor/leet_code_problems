class q6333_find_column_width:

    def find_width(self, grid):
        length = len(grid[0])
        answer = []
        i = 0
        while i < length:
            answer.append(0)
            i += 1
        for line in grid:
            i = 0
            while i < length:
                n = str(line[i])
                if len(n) > answer[i]:
                    answer[i] = len(n)
                i += 1

        return answer

    def tests(self):
        print(self.__class__.__name__)
        grid = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]
        print(grid," = ", self.find_width(grid))
        grid = [[1], [22], [333]]
        print(grid," = ", self.find_width(grid))
