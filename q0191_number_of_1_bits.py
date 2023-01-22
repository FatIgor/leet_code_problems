class q0191_number_of_1_bits:

    def hammingWeight(self,n):
        count=0
        s=format(int(n),'032b')
        for c in s:
            if c=='1':
                count+=1
        return count

    def tests(self):
        print(self.__class__.__name__)
        n=0b00000000000000000000000000001011
        print(bin(n),self.hammingWeight(n))
        n=0b00000000000000000000000010000000
        print(bin(n),self.hammingWeight(n))
        n=0b11111111111111111111111111111101
        print(bin(n),self.hammingWeight(n))