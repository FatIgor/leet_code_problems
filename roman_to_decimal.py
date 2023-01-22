class roman_to_decimal:
    def convert(self, roman):
        vals = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                'IV': 4,
                'IX': 9,
                'XL': 40,
                'XC': 90,
                'CD': 400,
                'CM': 900,
                }
        index = 0
        total = 0
        while index < len(roman):
            if len(roman) - index > 1:
                s = roman[index:index + 2]
                val = vals.get(s)
                if val is not None:
                    total += val
                    index += 2
                    continue
            s = roman[index]
            total += vals.get(s)
            index += 1
        return total
