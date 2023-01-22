from q0027_remove_element import q0027_remove_element
from q0034_find_element import q0034_find_element
from q0151_reverse_words_in_a_string import q0151_reverse_words_in_a_string
from q0191_number_of_1_bits import q0191_number_of_1_bits
from q1281_sub_prod_and_sum import q1281_sub_prod_and_sum
from q1491_average_salary import q1491_average_salary
from q1523_count_odd_numbers import q1523_count_odd_numbers
from basiccalculator import BasicCalculator
from common_prefix import common_prefix
from euler_problem_373 import euler_problem_373
from first_missing_positive import first_missing_positive
from longest_pal_sub import longest_pal_sub
from my_atoi import my_atoi
from nth_digit import nth_digit
from roman_to_decimal import roman_to_decimal
from sudoku_validation import sudoku_1
from two_sum import challenge_1
from water_and_jug import water_and_jug
from wildcard_matching import wildcard_matching

problem_list=[q0027_remove_element,q0034_find_element,q0151_reverse_words_in_a_string,q0191_number_of_1_bits,q1281_sub_prod_and_sum,q1491_average_salary,q1523_count_odd_numbers,BasicCalculator,common_prefix,euler_problem_373,first_missing_positive,longest_pal_sub,my_atoi,nth_digit,roman_to_decimal,sudoku_1,challenge_1,water_and_jug,wildcard_matching]

run_these=[27,34,151,191,1281,1491,1523]

for n in run_these:
    num=str(n)
    for name in problem_list:
        if num in name.__name__:
            problem=name()
            problem.tests()

exit()

rem = q0027_remove_element()
rem.tests()

reverse = q0151_reverse_words_in_a_string()
reverse.tests()

weight=q0191_number_of_1_bits()
weight.tests()

q1281=q1281_sub_prod_and_sum()
q1281.tests()

exit()




count_odds = q1523_count_odd_numbers()
answer = count_odds.count_odds(3, 7)

get_avg=q1491_average_salary()
print(get_avg.average([4000,3000,1000,2000]))

get_l = longest_pal_sub()
print(get_l.longest(
    'qbmhukucteihghldwdobtvgwwnhflpceiwhbkmvxavmqxedfndegztlpjptpdowwavemasyrjxxnhldnloyizyxgqlhejsdylvkpdzllrzoywfkcamhljminikvwwvqlerdilrdgzifojjlgeayprejhaequyhcohoeonagsmfrqhfzllobwjhxdxzadwxiglvzwiqyzlnamqqsastxlojpcsleohgtcuzzrvwzqugyimaqtorkafyebrgmrfmczwiexdzcokbqymnzigifbqzvfzjcjuugdmvegnvkgbmdowpacyspszvgdapklrhlhcmwkwwqatfswmxyfnxkepdotnvwndjrcclvewomyniaefhhcqkefkyovqxyswqpnysafnydbiuanqphfhfbfovxuezlovokrsocdqrqfzbqhntjafzfjisexcdlnjbhwrvnyabjbshqsxnaxhvtmqlfgdumtpeqzyuvmbkvmmdtywquydontkugdayjqewcgtyajofmbpdmykqobcxgqivmpzmhhcqiyleqitojrrsknhwepoxawpsxcbtsvagybnghqnlpcxlnshihcjdjxxjjwyplnemojhodksckmqdvnzewhzzuswzctnlyvyttuhlreynuternbqonlsfuchxtsyhqlvifcxerzqepthwqrsftaquzuxwcmjjulvjrkatlfqshpyjsbaqwawgpabkkjrtchqmriykbdsxwnkpaktrvmxjtfhwpzmieuqevlodtroiulzgbocrtiuvpywtcxvajkpfmaqckgrcmofkxynjxgvxqvkmhdbvumdaprijkjxxvpqnxakiavuwnifvyfolwlekptxbnctjijppickuqhguvtoqfgepcufbiysfljgmfepwyaxusvnsratn'))
print(get_l.longest('a'))
print(get_l.longest('babad'))
print(get_l.longest('cbbd'))
print(get_l.longest('babadaaabbbbccaccaaa'))
exit()


conv = roman_to_decimal()
result = conv.convert('MCMXCIV')
print(result)
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
