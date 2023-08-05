class q6366_old_people:

    def find_oldies(self, details):
        count = 0
        i = 0
        while i < len(details):
            person = details[i]
            age = person[11:13]
            if int(age) > 60:
                count += 1
            i += 1
        return count

    def tests(self):
        print(self.__class__.__name__)
        array = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
        print(array)
        print(self.find_oldies(array))
        array = ["1313579440F2036", "2921522980M5644"]
        print(array)
        print(self.find_oldies(array))
