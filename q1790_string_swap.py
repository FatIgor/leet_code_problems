class q1790_string_swap:
    def swap(self, s1, s2):
        if s1 == s2:
            return True
        i = 0
        count = 0
        indices = []
        while i < len(s1):
            if (s1[i] != s2[i]):
                count += 1
                indices.append(i)
            if count > 2:
                return False
            i += 1
        if count != 2:
            return False
        if s1[indices[0]] != s2[indices[1]]:
            return False
        return s1[indices[1]] == s2[indices[0]]

    def tests(self):
        print(self.__class__.__name__)
        s1 = "bank"
        s2 = "kanb"
        print(s1, s2, self.swap(s1, s2))
        s1 = "attack"
        s2 = "defend"
        print(s1, s2, self.swap(s1, s2))
        s1 = "kelb"
        s2 = "kelb"
        print(s1, s2, self.swap(s1, s2))
        s1 = "caa"
        s2 = "aaz"
        print(s1, s2, self.swap(s1, s2))
