class q6425_semi_rep:

    def semi_rep(self, s):
        current_index = 0
        current_best_index = 0
        current_best_len = 1
        while current_index < len(s):
            pair_count = 0
            index = current_index
            while pair_count < 2 and index < len(s) - 1:
                if (s[index] == s[index + 1]):
                    pair_count += 1
                index += 1
            if pair_count<2:
                index+=1
            if index - current_index > current_best_len:
                current_best_len = index - current_index
                current_best_index = current_index
            current_index += 1
        return current_best_len

    def tests(self):
        print(self.__class__.__name__)
        s = "52233"
        print(s, self.semi_rep(s))
        s = "5494"
        print(s, self.semi_rep(s))
        s = "1111111"
        print(s, self.semi_rep(s))
