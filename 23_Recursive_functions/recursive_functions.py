# recursive functions
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:                  # base case
        return 1
    return n * factorial(n-1)   # recursive case

# n = 5
# fact = 1
# while n != 1:
#     fact *= n
#     n -= 1
# print(fact)
# fact = factorial(5)
# print(fact)

def my_sum():
    n = int(input('>>> '))
    if n == 0: 
        return 0
    return n + my_sum()


# result = my_sum()
# print(result)

import sys
from functools import cache

sys.setrecursionlimit(100000)

# cache = dict()
# def fibonacci(n):
#     if n <= 1:
#         return n 
    
#     if n in cache:
#         return cache[n]
#     else:
#         result = fibonacci(n-1) + fibonacci(n-2)
#         cache[n] = result
#         return cache[n]

# @cache
# def fibonacci(n): return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# fib = fibonacci(200)
# print(fib)



def evklid(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return evklid(b, c)
    
    
# result = evklid(123456415, 45124312275)
# print(result)

def int_to_binary(n):
    if n <= 1: return str(n)
    return int_to_binary(n//2) + str(n%2)

# result = int_to_binary(18)
# print(result)
# print(bin(18))


# def palindrome(text): 
#     if len(text) <= 1:
#         return True
    
#     if text[0] != text[-1]:
#         return False
#     return palindrome(text[1:-1])
    
    
# result = palindrome('level')
# print(result)


data = [1, 1, 1, [1, 1, [1, 1, 1, [1, 1, [1, [1, 1, [1, [1]]]]]]]]

def flatten_list(data):
    if not data:
        return []
    if type(data[0]) == int:
        return [data[0]] + flatten_list(data[1:])
    else:
        return flatten_list(data[0])


result = flatten_list(data)
print(result)