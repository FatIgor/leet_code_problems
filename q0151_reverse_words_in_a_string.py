class q151_reverse_words_in_a_string:
    def reverse_words(self, s):
        word_list = s.split(' ')
        index = len(word_list)
        if index == 1:
            return word_list[0].replace(" ", "")
        index -= 1
        retval = word_list[index].replace(" ", "")
        while index > 0:
            index -= 1
            if word_list[index] != '':
                if retval=='':
                    retval=word_list[index]
                else:
                    retval = retval + ' ' + word_list[index].replace(" ", "")
        return retval
