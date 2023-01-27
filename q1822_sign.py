class q1822_sign:
    def get_sign(self, nums):
        x=nums[0]
        i=1
        while i<len(nums):
            x*=nums[i]
            i+=1
        if x==0:
            return 0
        if x>0:
            return 1
        return -1

    def tests(self):
        print(self.__class__.__name__)
        nums = [1,5,0,2,-3]
        print(nums)
        print(self.get_sign(nums))
        nums = [-1,-2,-3,-4,3,2,1]
        print(nums)
        print(self.get_sign(nums))
        nums = [-1,1,-1,1,-1]
        print(nums)
        print(self.get_sign(nums))