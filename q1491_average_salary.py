class q1491_average_salary():
    def average(self, salary):
        lowest = 1000000
        highest = 10
        for i in salary:
            if i < lowest:
                lowest = i
            if i > highest:
                highest = i
        total = 0
        for i in salary:
            if i != lowest and i != highest:
                total += i
        return total / (len(salary) - 2)