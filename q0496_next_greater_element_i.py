class q0496_next_greater_element_i:
    def next_greater(self, nums1, nums2):
        nums3 = []
        for num in nums1:
            nums3.append(self.get_ng(num, nums2))
        return nums3

    def get_ng(self, num, nums2):
        i = 0
        while i < len(nums2) - 1:
            if num == nums2[i]:
                while i < len(nums2) - 1:
                    i += 1
                    if nums2[i] > num:
                        return nums2[i]
                return -1
            i += 1
        return -1

    def tests(self):
        print(self.__class__.__name__)
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        print(nums1, nums2, self.next_greater(nums1, nums2))
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        print(nums1, nums2, self.next_greater(nums1, nums2))
