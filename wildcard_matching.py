class wildcard_matching:

    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        if "*" in p:
            return True
        if len(s) != len(p):
            return False
        for i in range(len(s)):
            if (p[i] != '?'):
                if p[i] != s[i]:
                    return False
        return True

    def tests(self):
        print(self.isMatch("acdcb", "a*c?b"))
        print(self.isMatch("adceb", "*a*b"))
        print(self.isMatch("aa", "a"))
        print(self.isMatch("aa", "*"))
        print(self.isMatch("cb", "?a"))
        print(self.isMatch("cab", "c?b"))
