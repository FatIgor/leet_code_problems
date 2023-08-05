class q6367_sum_in_a_matrix:

    def find_sum2(self, nums):
        i = 0
        count = 0
        while i < nums.__len__():
            nums[i].sort()
            i += 1
        j = 0
        while j < nums[0].__len__():
            max = -1
            i = 0
            while i < nums.__len__():
                if nums[i][j] > max:
                    max = nums[i][j]
                i += 1
            count += max
            j += 1
        return count

    def find_sum(self, nums):
        repeat_count = nums[0].__len__()
        start_len = nums.__len__()
        i = 0
        total = 0
        while repeat_count > 0:
            max = 0
            i = 0
            while i < start_len:
                j = 0
                biggest = -1
                while j < nums[i].__len__():
                    if nums[i][j] > biggest:
                        biggest = nums[i][j]
                        biggest_index = j
                    j += 1
                if biggest > max:
                    max = biggest
                nums[i][biggest_index] = -1
                i += 1
            total += max
            repeat_count -= 1
        return total

    def tests(self):
        print(self.__class__.__name__)
        nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
        print(nums)
        print(self.find_sum2(nums))
        nums = [[1]]
        print(nums)
        print(self.find_sum2(nums))
