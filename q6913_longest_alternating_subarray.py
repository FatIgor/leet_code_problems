class q6913_longest_alternating_subarray:

    def long_sub(self, nums):
        index = 0
        longest = 0
        while index < len(nums) - 1:
            i = index
            flip = 1
            length = 1
            ok = True
            while ok and i < len(nums) - 1:
                val1 = nums[i + 1]
                val2 = nums[i]
                if nums[i + 1] - nums[i] == flip:
                    length += 1
                    flip *= -1
                    i += 1
                else:
                    ok = False
            if length > longest and length > 1:
                longest = length
            index += 1
        if longest == 0:
            longest = -1
        return longest

    def tests(self):
        print(self.__class__.__name__)
        nums = [2, 3, 4, 3, 4]
        print(self.long_sub(nums))
        nums = [4, 5, 6]
        print(self.long_sub(nums))
        nums = [21, 9, 5]
        print(self.long_sub(nums))
