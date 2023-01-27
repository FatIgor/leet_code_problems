class q1502_arithmetic_progression:
    def progress(self, arr):
        arr.sort();
        diff = arr[0] - arr[1]
        i = 1
        while i < len(arr) - 1:
            if arr[i] - arr[i + 1] != diff:
                return False
            i += 1
        return True

    def tests(self):
        print(self.__class__.__name__)
        arr = [3, 5, 1]
        print(arr)
        print(self.progress(arr))
        arr = [1, 2, 4]
        print(arr)
        print(self.progress(arr))
