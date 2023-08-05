class q6393_max_strength:

    def strength(self, nums):
        nums.sort()
        had_zero = False
        while nums.__contains__(0):
            had_zero = True
            nums.remove(0)
        if len(nums)==0:
            return 0
        if len(nums) == 1:
            if nums[0] < 0:
                if had_zero:
                    return 0
                return nums[0]
        num_neg = 0
        neg_index = 0
        i = 0
        ignore = []
        while i < len(nums):
            if nums[i] < 0:
                num_neg += 1
                neg_index = i
            i += 1
        if num_neg & 1 == 1:
            nums[neg_index] = 1
        strength = 1
        i = 0
        while i < len(nums):
            strength *= nums[i]
            i += 1
        return strength

    def tests(self):
        print(self.__class__.__name__)
        group = [3, -1, -5, 2, 5, -9]
        print(self.strength(group))
        group = [-4, -5, -4]
        print(self.strength(group))
        group = [0, -1]
        print(self.strength(group))
        group = [-9]
        print(self.strength(group))
        group = [-2, 0]
        print(self.strength(group))
        group = [0, -5, 0]
        print(self.strength(group))
