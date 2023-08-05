class q6461_is_fascinating:

    def is_fascinating(self, n):
        mystr = str(n) + str(n * 2) + str(n * 3)
        if len(mystr) != 9:
            return False
        i = 1
        while i < 10:
            if not mystr.__contains__(str(i)):
                return False
            i += 1
        return True;

    def tests(self):
        print(self.__class__.__name__)
        n=192
        print(n,self.is_fascinating(n))
        n=100
        print(n,self.is_fascinating(n))
