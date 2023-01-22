class q1281_sub_prod_and_sum:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        while n > 0:
            prod *= n % 10
            sum += n % 10
            n //= 10
        return prod - sum

    def tests(self):
        print(self.__class__.__name__)
        n = 234
        print(n,self.subtractProductAndSum(n))
        n = 4421
        print(n,self.subtractProductAndSum(n))