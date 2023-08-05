class q6395_buy_two_chocolates:

    def chocolates(self, prices, money):
        l1 = money
        l2 = money
        i = 0
        while i < len(prices):

            if prices[i] < l1:
                if l1<l2:
                    l2=l1
                l1 = prices[i]
            elif prices[i] < l2:
                l2 = prices[i]
            i += 1
        print(l1,l2)
        if l1 + l2 <= money:
            return money - (l1 + l2)
        else:
            return money

    def tests(self):
        print(self.__class__.__name__)
        prices = [1, 2, 2]
        money = 3
        print(self.chocolates(prices, money))
        prices = [3, 2, 3]
        money = 3
        print(self.chocolates(prices, money))
        prices = [69,91,78,19,40,13]
        money = 94
        print(self.chocolates(prices, money))
