class q27_remove_element:
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
        string = ''
        for item in nums:
            string = string + str(item) + ' '
        print(string)
        print(count)
        return count
