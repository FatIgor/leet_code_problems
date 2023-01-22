class longest_pal_sub:
    def longest(self, s):
        longest = ''
        longest_len = 0
        sl = len(s)
        index1 = 0
        while index1 + longest_len < sl:
            check_len = longest_len + 1
            index2 = index1
            while index2 + check_len <= sl:
                s2 = s[index2:index2 + check_len]
                if (s2[0]==s2[check_len-1:check_len]):
                    if (s2 == s2[::-1]):
                        longest = s2
                        longest_len = len(s2)
                check_len += 1
            index1 += 1
        return longest
