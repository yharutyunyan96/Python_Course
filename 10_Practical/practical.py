# ex.1
# n, m = int(input('>>> ')), int(input('>>> '))

# maximum = n if n > m else m
# k = maximum
# while True:
#     if maximum % n == 0 and maximum % m == 0:
#         print(maximum)
#         break
#     maximum += k


# maximum = n if n > m else m
#
# for num in range(maximum, n * m + 1, maximum):
#     if num % n == 0 and num % m == 0:
#         print(num)
#         break



# ex.2

evens_count = odds_count = 0

# for i_num in range(1, 101):
#     if i_num % 2 == 0:
#         evens_count += 1
#     else:
#         odds_count += 1
#

# i_num = 1
# while i_num < 101:
#     if i_num % 2 == 0:
#         evens_count += 1
#     else:
#         odds_count += 1
#
#     i_num += 1
#
# print(evens_count, 'evens')
# print(odds_count, 'odds')


# ex.3
n = 40
# a, b = 0, 1

# while a < n:
#     print(a, end='|')
#     a, b = b, a+b

# a, b = 0, 1
# for fibo in range(10000000):
#         a, b = b, a+b
#         if a >= 41:
#             break
#         print(a, end=' ')


# ex.4
# import string
#
# text = 'Python 3.9'
# letters_count = digits_count = 0
# for char in text:
#     # if char.isalpha():
#     if char in string.ascii_letters:
#         letters_count += 1
#     # elif char.isdigit():
#     elif char in string.digits:
#         digits_count += 1
#
# print('Letters count', letters_count)
# print(f"Digits count: {digits_count}")


# ex.5
# number = 12345
# _sum = 0
#
# while number != 0:
#     _sum += number % 10
#     number //= 10
#
# print(_sum)


# ex.6
# import math

# factorial_5 = math.factorial(5)

num = 5
f = 1
# for fact in range(1, num+1):
#     f *= fact

# while num > 1:
#     f *= num
#     num -= 1
# print(f)
# print(factorial_5)

# import math
# result = sum(list(range(1, 101)))
# result = math.prod(list(range(1, 101)))
# print(result)

# _sum = 0
#
# for i in range(1, 101):
#     _sum += i
#
# print(_sum)


#
# for i in range(1, 50):
#     print(i*'*')








