class q1588_array_sum:

    def get_sum(self, arr):
        total = 0
        odd_len = len(arr)
        if odd_len % 2 != 1:
            odd_len -= 1
        while odd_len > 0:
            index = 0
            while index + odd_len <= len(arr):
                total += self.single_array_sum(arr, index, odd_len)
                index += 1
            odd_len -= 2
        return total

    def single_array_sum(self, arr, index, count):
        total = 0
        i = index
        while i < index + count:
            total += arr[i]
            i += 1
        return total

    def tests(self):
        print(self.__class__.__name__)
        list = [1, 4, 2, 5, 3]
        print(list, self.get_sum(list))
        list = [1, 2]
        print(list, self.get_sum(list))
        list = [10, 11, 12]
        print(list, self.get_sum(list))
