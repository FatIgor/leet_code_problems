from typing import List

import numpy as numpy


class first_missing_positive:
    def __init__(self):
        pass

    def missingPositive(self, nums: List[int]) -> int:
        nums = numpy.sort(nums)
        index = 0
        while index < len(nums) and nums[index] < 1:
            index += 1
        if index >= len(nums):
            return 1
        if nums[index] > 1:
            return 1
        val = 1
        while index < len(nums) and val == nums[index]:
            index += 1
            if index < len(nums) and nums[index] != val:
                val += 1
            if index >= len(nums) and nums[index - 1] == val:
                return val + 1
        return val

    def tests(self):
        print(self.missingPositive([0, 2, 2, 1, 1]))
        print(self.missingPositive([0]))
        print(self.missingPositive([1, 2, 0]))
        print(self.missingPositive([3, 4, -1, 1]))
        print(self.missingPositive([7, 8, 9, 11, 12]))
