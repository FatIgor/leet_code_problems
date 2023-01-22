from typing import List


class common_prefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        index = 1
        while index < len(strs):
            str1 = strs[index]
            if len(prefix) > len(str1):
                prefix = prefix[0:len(str1)]
            if prefix != str1:
                check_len = len(str1)
                while prefix[0:check_len] != str1[0:check_len]:
                    check_len -= 1
                    if (check_len == 0):
                        return ""
                    prefix = prefix[0:check_len]
            index+=1
        return prefix

    def run_tests(self):
        print(self.longestCommonPrefix(["flower", "flow", "flight"]))
        print(self.longestCommonPrefix(["dog", "racecar", "car"]))
