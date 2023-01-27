class q0976_triangle_perimeter:
    def getPerimeter(self, nums):
        if len(nums) < 3:
            return 0
        nums.sort()
        i= len(nums) - 3
        while i>=0:
            if nums[i]+nums[i + 1]>nums[i + 2]:
                return nums[i]+nums[i + 1]+nums[i + 2]
            i-=1
        return 0


    def tests(self):
        print(self.__class__.__name__)
        side_list = [2,1,2]
        print(side_list)
        print(self.getPerimeter(side_list))
        side_list = [1,2,1]
        print(side_list)
        print(self.getPerimeter(side_list))
        side_list = [3,2,3,4]
        print(side_list)
        print(self.getPerimeter(side_list))
        side_list = [3,6,2,3]
        print(side_list)
        print(self.getPerimeter(side_list))
        side_list = [1,2,1,10]
        print(side_list)
        print(self.getPerimeter(side_list))
