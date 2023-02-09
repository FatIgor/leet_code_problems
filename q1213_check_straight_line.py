import math


class q1213_check_straight_line:
    def check(self, coordinates):
        if len(coordinates) == 2:
            return True
        i = 0
        while i < len(coordinates) - 2:
            v1 = (coordinates[i + 2][1] - coordinates[i][1]) * (coordinates[i + 1][0] - coordinates[i][0])
            v2 = (coordinates[i + 1][1] - coordinates[i][1]) * (coordinates[i + 2][0] - coordinates[i][0])
            if v1 != v2:
                return False
            i += 1
        return True

    def tests(self):
        print(self.__class__.__name__)
        points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [8, 9]]
        print(points, self.check(points))
        points = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
        print(points, self.check(points))
        points = [[0, 0], [0, 1], [0, -1]]
        print(points, self.check(points))
        points = [[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]
        print(points, self.check(points))
        points = [[0, 1], [1, 3], [-4, -7], [5, 11]]
        print(points, self.check(points))
