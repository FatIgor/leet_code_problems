class q0034_find_element:
    def search(self, nums, target):
        min = 0
        max = len(nums) - 1
        while min <= max:
            mid = (min + max) >> 1
            if nums[mid] == target:
                return self.get_positions(nums, target, mid)
            if target < nums[mid]:
                max = mid - 1
            else:
                min = mid + 1
        return [-1, -1]

    def get_positions(self, nums, target, index):
        i2 = index
        while index > 0 and nums[index - 1] == target:
            index -= 1
        while i2 < len(nums) - 1 and nums[i2 + 1] == target:
            i2 += 1
        return [index, i2]
