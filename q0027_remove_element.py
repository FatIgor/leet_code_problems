class q0027_remove_element:
    def remove(self, nums, val):
        count = len(nums)
        index1 = 0
        index2 = len(nums) - 1
        while index1 <= index2:
            if nums[index1] == val:
                count -= 1
                while nums[index2] == val and index2 > index1:
                    index2 -= 1
                    count -= 1
                nums[index1] = nums[index2]
                index2 -= 1
            index1 += 1
        if len(nums) > 0 and nums[0] == val:
            count = 0
        return count

    def tests(self):
        print(self.__class__.__name__)
        nums = [3, 2, 2, 3]
        val = 3
        print(nums,val)
        print(self.remove(nums, val))
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        print(nums,val)
        print(self.remove(nums, val))
        nums = [1]
        val = 1
        print(nums,val)
        print(self.remove(nums, val))
        nums = [4, 5]
        val = 5
        print(nums,val)
        print(self.remove(nums, val))
