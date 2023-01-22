class nth_digit:
    def find_digit(self, n) -> int:
        power = 2
        previous_limit = 10
        if n < previous_limit:
            return n
        while True:
            next_limit = (pow(10, power) - pow(10, power - 1)) * power + previous_limit
            if n < next_limit:
                number = n - previous_limit
                index = number % power
                number //= power
                number += pow(10, power - 1)
                s = str(number)
                return int(s[index])
            power += 1
            previous_limit = next_limit

    def tests(self):
        print(self.find_digit(11))
        print(self.find_digit(101))
        print(self.find_digit(100))
        print(self.find_digit(3))
        print(self.find_digit(333))
        print(self.find_digit(1000))
