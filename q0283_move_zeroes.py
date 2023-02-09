class q0283_move_zeroes:
    def movez(self, nums):
        i1 = 0
        while i1 < len(nums):
            if nums[i1] == 0:
                i2 = i1 + 1
                while i2 < len(nums):
                    if nums[i2] != 0:
                        nums[i1] = nums[i2]
                        nums[i2] = 0
                        break
                    i2 += 1
            i1 += 1
        return nums

    def tests(self):
        print(self.__class__.__name__)
        nums = [0, 1, 0, 3, 12]
        print(nums, self.movez(nums))
        nums = [0]
        print(nums, self.movez(nums))
