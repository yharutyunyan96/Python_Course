# memebrship operators
# logical operators
# bitwise operators


# membership operators
# in, not in

# word = 'python'
# letter = 'ytj'

# print(letter in word)
# print(letter not in word)

# num = 1234
# digit = 1
#
# print(digit in num)     # TypeError


# logical operators
# and, or, not

# my_bool = 5 > 4 and 1 < 0 and 8 > 4 and 3 > 2
# my_bool = True or False or False or False
# print(my_bool)

# my_bool = bool(0.000001)
# print(my_bool)
# my_bool = bool(' ')
# print(my_bool)

# my_bool = not(6 > 4 and 6 > 7)
# print(my_bool)


# my_bool = (6 > 4 or 5 > 7) and 4 > 14
#         True         False
#               True
# print(my_bool)


# bitwise operators
#       8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0
# 17                    1   0   0   0   1
# 27                    1   1   0   1   1

# &                     1   0   0   0   1
# |                     1   1   0   1   1
# ^                     0   1   0   1   0
# ~ 17                  0   1   1   1   0
# <<              1  0  0   0   1   0   0  | 0 0 0 0 0 0 0
# >>                            1   0   0  | 0 1 0 0 0 0 0 0 0 0

# bitwise_and = 17 & 27
# bitwise_or = 17 | 27
# bitwise_xor = 17 ^ 27
# bitwise_not = ~ 17
# left_shift = 17 << 2
# right_shift = 17 >> 2

# item assignment operators
# num = 17
# num >>= 3
# num <<= 4
# num &= 27
# num |= 27
# num ^= 27       # num = num ^ 27
# print(num)


