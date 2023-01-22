from datetime import datetime
from math import sqrt


class euler_problem_373:

    def radius(self, a, b, c) -> float:
        s = (a + b + c) / 2
        val1 = s * (s - a) * (s - b) * (s - c)
        val1 = sqrt(val1) * 4
        return (a * b * c) / val1

    def get_sum(self, max_radius) -> int:
        total = 0
        for a in range(max_radius + 1):
            start_val = int((a + 1) / 2)
            for b in range(start_val, a + 1):
                start_val2 = a + 1 - b
                for c in range(start_val2, b + 1):
                    rad = self.radius(a * 2, b * 2, c * 2)
                    if rad.is_integer() and rad > 0:
                        if rad <= max_radius:
                            total += int(rad)
        return total

    def test_euler_problem_373(self):
        start = datetime.now()
        # The time of execution of 100 is : 2298.420ms
        # The time of execution of 1200 is : 5606744.675ms
        # The time of execution of 10000 is: 524m 10.291s
        desired_rad = 10000
        print(desired_rad)
        if True:
            count = self.get_sum(desired_rad)
            print(count)

        else:
            print(self.get_sum_v2(desired_rad))
        end = datetime.now()
        td = (end - start).total_seconds()
        minutes = 0
        while td >= 60:
            td -= 60
            minutes += 1
        print(f"The time of execution of {desired_rad} is : {minutes}m {td:.03f}s")
