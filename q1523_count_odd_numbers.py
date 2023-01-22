class q1523_count_odd_numbers:
    def count_odds(self, low, high):
        count = int(high - low + low % 2 + high % 2) / 2
        print(count)
        return count
