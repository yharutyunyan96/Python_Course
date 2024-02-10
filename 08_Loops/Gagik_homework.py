# 1

# a = int(input("write your number - "))
# count = 0
# while a:
#    a = a // 10
#    count += 1
# print(count)
# 2
#
# a = int(input("write your number - "))
# b = 0
# c = 0
# while a :
#     k = a % 10
#     if(k == 0 or k == 1):
#         a = a // 10
#     elif( k == 2 or k == 3):
#         a = a // 10
#         c += 1
#     elif(k % 2 == 0):
#         b += 1
#         a = a // 10
#     elif(k % 3 == 0):
#         b +=1
#         a = a // 10
#     else:
#         c  += 1
#         a = a // 10
#
#
# print(c)
# print(b)


# 3
# a = int(input("write your number - "))
# _sum = 0
# _prod = 1
# while a:
#    last = a % 10
#    _sum += last
#    _prod *= last
#    a //= 10
#
# print(_sum)
# print(_prod)

# 4

# num = int(input("write your number - "))
# reversed_num = 0
#
# while num != 0:
#     last = num % 10
#     reversed_num *= 10
#     reversed_num += last
#     num = num // 10
#
# print(reversed_num)
# 5

# n = int(input("Enter number - "))
#
# a = 1
# while a <= n:
#     print(n ** a)
#     a += 1

# 6

# n = int(input("Write your number - "))
# if (n < 0 ):
#     print("Error")
# elif (n == 0  or n == 1):
#     print(1)
# elif (n > 1):
#     f = 1
#     while n:
#         f = f * n
#         n -= 1
#
# print(f)

# n! = 1 * 2 * 3 * ... * n

# n = int(input('>>> '))
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
#
# print(factorial)