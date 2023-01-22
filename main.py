from basiccalculator import BasicCalculator
from common_prefix import common_prefix
from euler_problem_373 import euler_problem_373
from first_missing_positive import first_missing_positive
from longest_pal_sub import longest_pal_sub
from my_atoi import my_atoi
from nth_digit import nth_digit
from q151_reverse_words_in_a_string import q151_reverse_words_in_a_string
from q27_remove_element import q27_remove_element
from q34_find_element import q34_find_element
from roman_to_decimal import roman_to_decimal

from sudoku_validation import sudoku_1
from two_sum import challenge_1
from water_and_jug import water_and_jug
from wildcard_matching import wildcard_matching

get_l=longest_pal_sub()
print(get_l.longest('qbmhukucteihghldwdobtvgwwnhflpceiwhbkmvxavmqxedfndegztlpjptpdowwavemasyrjxxnhldnloyizyxgqlhejsdylvkpdzllrzoywfkcamhljminikvwwvqlerdilrdgzifojjlgeayprejhaequyhcohoeonagsmfrqhfzllobwjhxdxzadwxiglvzwiqyzlnamqqsastxlojpcsleohgtcuzzrvwzqugyimaqtorkafyebrgmrfmczwiexdzcokbqymnzigifbqzvfzjcjuugdmvegnvkgbmdowpacyspszvgdapklrhlhcmwkwwqatfswmxyfnxkepdotnvwndjrcclvewomyniaefhhcqkefkyovqxyswqpnysafnydbiuanqphfhfbfovxuezlovokrsocdqrqfzbqhntjafzfjisexcdlnjbhwrvnyabjbshqsxnaxhvtmqlfgdumtpeqzyuvmbkvmmdtywquydontkugdayjqewcgtyajofmbpdmykqobcxgqivmpzmhhcqiyleqitojrrsknhwepoxawpsxcbtsvagybnghqnlpcxlnshihcjdjxxjjwyplnemojhodksckmqdvnzewhzzuswzctnlyvyttuhlreynuternbqonlsfuchxtsyhqlvifcxerzqepthwqrsftaquzuxwcmjjulvjrkatlfqshpyjsbaqwawgpabkkjrtchqmriykbdsxwnkpaktrvmxjtfhwpzmieuqevlodtroiulzgbocrtiuvpywtcxvajkpfmaqckgrcmofkxynjxgvxqvkmhdbvumdaprijkjxxvpqnxakiavuwnifvyfolwlekptxbnctjijppickuqhguvtoqfgepcufbiysfljgmfepwyaxusvnsratn'))
print(get_l.longest('a'))
print(get_l.longest('babad'))
print(get_l.longest('cbbd'))
print(get_l.longest('babadaaabbbbccaccaaa'))
exit()

rem = q27_remove_element()
nums = [3, 2, 2, 3]
val = 3
rem.remove(nums, val)
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
rem.remove(nums, val)
nums = [1]
val = 1
rem.remove(nums, val)
nums = [4, 5]
val = 5
rem.remove(nums, val)
exit()

conv = roman_to_decimal()
result = conv.convert('MCMXCIV')
print(result)
exit()

reverse = q151_reverse_words_in_a_string()
sentence = ''
print(f"{sentence},{reverse.reverse_words(sentence)}!")
sentence = '     '
print(f"{sentence},{reverse.reverse_words(sentence)}!")
sentence = 'the sky is blue'
print(f"{sentence},{reverse.reverse_words(sentence)}!")
sentence = '  hello world   '
print(f"{sentence},{reverse.reverse_words(sentence)}!")
sentence = 'a good   example'
print(f"{sentence},{reverse.reverse_words(sentence)}!")
exit()

find_it = q34_find_element()
nums = [1, 1, 1, 1, 1, 1, 1]
print(nums, find_it.search(nums, 1))
nums = [1, 2, 3]
print(nums, find_it.search(nums, 1))
nums = [1, 3]
print(nums, find_it.search(nums, 1))
nums = [5, 7, 7, 8, 8, 10]
print(nums, find_it.search(nums, 8))
nums = [5, 6, 6, 6, 7, 7, 8, 8, 10]
print(nums, find_it.search(nums, 1))
nums = [1]
print(nums, find_it.search(nums, 1))
nums = [1, 4]
print(nums, find_it.search(nums, 1))
exit()

int_calc = my_atoi()
print(int_calc.my_atoi('-91283472332'))
print(int_calc.my_atoi('21474836460'))
print(int_calc.my_atoi('-2147483648'))

rads = euler_problem_373()
rads.test_euler_problem_373()

jugs = water_and_jug()
jugs.tests()

digits = nth_digit()
digits.tests()

match = wildcard_matching()
match.tests()

pos = first_missing_positive()
pos.tests()

prefix = common_prefix()
prefix.run_tests()

calculator = BasicCalculator()
calculator.run_tests()

sudoku = sudoku_1()
sudoku.run_tests()
