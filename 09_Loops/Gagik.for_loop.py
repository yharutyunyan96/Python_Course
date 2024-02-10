# homework new

# 3

# y = -3x^2 - 4x + 20

# for x in range(1,11):
#     y = -3 * (x ** 2) - 4 * x + 20
#     print("if x =",x)
#     print("then y =",y,"\n")

# 4

# a = int(input("Your number - "))
# if(a <= 0):
#     print("wrong type of number")
# else:
#     n = int(input("Number - "))
#     if(n < 1):
#         print("Error")
#     else:
#         i = 1
#         result = a * (a + i)
#         for i in range(2,n):
#             result = result * (a + i)
# print(result)

#  5

# n = int(input("Your number - "))
# our_number = 1
# sum = 0
# for i in range (1,n):
#     sum = sum + our_number
#     our_number = our_number * -0.5
# print(sum)

# 6

# high_part = 1
# low_part = 2
# number = high_part / low_part
# quantity  = 0
# sum = 0
# while number > 0.001:
#     if( number <= 0.001):
#         print(quantity)
#         print(sum)
#
#     else:
#         quantity += 1
#         sum = sum + number
#         high_part = high_part + 1
#         low_part = low_part * 2
#

# 9

# our_number = int(input("write your number - "))
# for i in range(2, our_number//2 + 1):
#     if our_number % i == 0:
#         print("NO")
#         break
#
#     if(i == our_number/2):
#         print("simple")
#

# previous homework

# 1

# a = int(input("write your number - "))
# sum = 0
# while a :
#    k = a % 10
#    sum += 1
#    a = a // 10
# print(sum)

# 2

# our_number = int(input("Write your number - "))
# number_of_odd_numbers = 0
# number_of_even_numbers = 0
# while our_number >= 1:
#     remainder = our_number % 10
#     if(remainder % 2 == 0):
#         number_of_even_numbers += 1
#     else:
#         number_of_odd_numbers +=1
#     our_number = our_number // 10
# print(number_of_odd_numbers)
# print(number_of_even_numbers)

# 3

# our_number = int(input("write your number - "))
# sum = 0
# prod = 1
# while our_number :
#    remainder = our_number % 10
#    sum = remainder + sum
#    prod = remainder * prod
#    our_number = our_number // 10
#
# print(sum)
# print(prod)

# 4

# a = int(input("write your number - "))
#
# while a :
#    k = a % 10
#    print(k,end = "")
#    a = a // 10

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

# 7

# number = int(input("Write the number you want - "))
# previous_value = 1
# pre_previous_value = 0
# current_value = previous_value + pre_previous_value
# if(number == 1 or number == 2):
#     print(current_value)
# else:
#     for i in range(3,number + 1):
#         pre_previous_value = previous_value
#         previous_value = current_value
#         current_value = previous_value + pre_previous_value
#     print(current_value)

# 8

# number = int(input("Write the number you want - "))
# previous_value = 1
# pre_previous_value = 0
# current_value = previous_value + pre_previous_value
# print(current_value)
# print(current_value)
# for i in range(3,number + 1):
#     pre_previous_value = previous_value
#     previous_value = current_value
#     current_value = previous_value + pre_previous_value
#     print(current_value)