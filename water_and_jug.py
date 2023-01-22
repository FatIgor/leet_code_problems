class water_and_jug:

    def can_measure(self, j1, j2, target):
        if j1 == target:
            return True
        if j2 == target:
            return True
        if j1 + j2 == target:
            return True
        if j1+j2<target:
            return False
        if target % j1 == 0:
            return True
        if target % j2 == 0:
            return True
        val1 = j1 - j2
        if val1 < 0:
            val1 *= -1
        if val1 > target and val1 % target == 0:
            return False
        if j1 > j2 and j1 / j2 > 2:
            val1 = j1 % j2
        if j2 > j1 and j2 / j1 > 2:
            val1 = j2 % j1
        if val1 % 2 != target % 2:
            return False
        return True

    def tests(self):
        print(f"3,5,4,{self.can_measure(3, 5, 4)}")  # T
        print(f"2,6,5,{self.can_measure(2, 6, 5)}")  # F
        print(f"1,2,3,{self.can_measure(1, 2, 3)}")  # T
        print(f"6,9,1,{self.can_measure(6, 9, 1)}")  # F
        print(f"34,5,6,{self.can_measure(34, 5, 6)}")  # T
        print(f"1,1,12,{self.can_measure(1, 1, 12)}")  # F
        print(f"11,3,13,{self.can_measure(11, 3, 13)}")  # F
