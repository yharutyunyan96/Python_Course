import random
import string

# *args, **kwargs
def func(*args, **kwargs):
    print(type(args))
    print(args)

    print()

    print(type(kwargs))
    print(kwargs)

# func(1,2,3,4,5, a=1, b=2, c=3)

def concatenate(*args, symbol): return f'{symbol}'.join(args)
# result = concatenate('abc', 'cde', 'efg', 'xyz', 'fga', symbol='*')
# print(result)

# positional_only, keyword_only
# def my_range(pos_only, /, pos_or_kwd, *, kwd_only):
#     for i in range(pos_only, pos_or_kwd, kwd_only): print(i, end=' ')
#
# my_range(1, pos_or_kwd=10, kwd_only=1)


def password_generator(length, *, strong=False):
    if strong:
        password = ''.join(random.sample(string.printable, k=length))
    else:
        password = ''.join(random.sample(string.ascii_letters, k=length))

    return password

# password = password_generator(8, strong=True)
# print(password)


# scopes, namespace, LEGB
#
# var = 'global var'
#
# def f1():
#     global var
#     var = 'local var'
#     print(var)
#
# f1()
# print(var)


# var = 'global var'
#
# def f1():
#
#     var = 'enclosed var'
#
#     def f2():
#         nonlocal var
#         var = 'local var'
#         print(var)
#
#     f2()
#     print(var)
#
# print(var)
# f1()


# def base(x):
#     def exponent(y):
#         return x ** y
#     return exponent

# base_2 = base(2)(10)
# print(base_2(10))
# base_2_exponents = [base_2(i) for i in range(2, 10)]
# base_3 = base(3)
# base_3_exponents = [base_3(i) for i in range(2, 10)]
# print(base_2_exponents)
# print(base_3_exponents)
# print(base_2)


# lambda
# add = lambda x, y: x + y
# print(add(3, 4))

# l = ['adsva', 'faasfgga', 'dghfa', 'dfa', 'xy']
# l = sorted(l, key=lambda word: len(word))
# print(l)


# map, filter, reduce
# l = ['a', 'b', 'c', 'd']
# l = list(map(str.upper, l))
# l = list(map(lambda text: text.upper(), l))
# print(l)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)

# l = [12, 32412, 51, 35461, 111]
# l = list(map(lambda num: num if num > 100 else ..., l))
# l = [i for i in l if i > 100]
# print(l)

# l = [12, 32412, 51, 35461, 111]
# l = list(filter(lambda num: num > 100, l))
# print(l)


# from functools import reduce
#
# l1 = [1, 2, 3, 4, 5]
# _sum = reduce(lambda x, y: x + y, l1)
# _prod = reduce(lambda x, y: x * y, l1)
# print(_sum)
# print(_prod)


# num_list = list(map(lambda num: int(num)**2, input('Enter numbers seperated by a comma: ').split(',')))
# print(num_list)

def square(x):
    return int(x) ** 2


num_list = list(map(square, input('Enter numbers seperated by a comma: ').split(',')))
print(num_list)