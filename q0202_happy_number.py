class q0202_happy_number:
    count = 0

    def isHappy(self, n):
        if n == 1:
            return True
        total = 0
        while True:
            digit = n % 10
            total += digit * digit
            n = (n - digit) / 10
            if n == 0:
                break
        self.count += 1
        if self.count > 800:
            return False
        return self.isHappy(total)

    def tests(self):
        print(self.__class__.__name__)
        num = 19
        self.count = 0
        print(num, self.isHappy(num))
        num = 2
        self.count = 0
        print(num, self.isHappy(num))
        self.count = 0
        num = 7
        print(num, self.isHappy(num))
