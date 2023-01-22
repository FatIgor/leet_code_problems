class my_atoi:
    def my_atoi(self, s):
        index = 0
        val = 0
        sign = 1
        s = s.lstrip()
        l = len(s)
        if l == 0:
            return 0
        while s[index] == ' ':
            index += 1
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        while index < l and s[index].isdigit():
            val = val * 10 + ord(s[index]) - 48
            index += 1
        if (val > 2147483648) and sign == -1:
            val = 2147483648
        elif val > 2147483647 and sign == 1:
            val = 2147483647
        return val * sign
