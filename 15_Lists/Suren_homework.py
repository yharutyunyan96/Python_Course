# ############ LOOPS from ZADACHI################
## 1
# number = int(input('Enter the number'))
#
# n = 0
#
# while number > 0:
#     number //= 10
#     n +=1
# print(n)


# # 2
#
# number = input('Enter the number')
#
# even = 0
# odd = 0
# for i in number:
#
#     if int(i) % 2 ==0:
#         even += 1
#     else:
#         odd += 1
#
#
# print('Even:',even)
# print('Odd:',odd)

# 3

# number = input('Enter the number')
#
# sum = 0
# prod = 1
# for i in number:
#     sum += int(i)
#     prod *= int(i)
#
# print('Sum:',sum, 'Prod:', prod)

# 4

# number = input('Enter the number:')
# i = 1
# while i <= len(number):
#         print(number[-i], end='')
#         i += 1


# # 5
#
# number = int(input('Enter the number:'))
# i = 1
# while i ** 2 <=number:
#
#     print(i,'^ 2=', i**2)
#     i += 1

# 6
# number = int(input('Enter the number:'))
# factorial = 1
#
# while number//10 > 0:
#     number %= 10
#     factorial *= number
#
# print(factorial)


# # 6
#
# n = int(input('Enter the number'))
# fac = 1
# while n-1 > 0:
#         fac *= n
#         n -= 1
# print(fac)


# # 7
# n = int(input('Enter the number'))
# a, b = 0, 1
#
# for i in range(n-1):
#         a, b = b, a+b
# print(a)

# # 8
# n = int(input('Enter the number'))
# a, b = 0, 1
# print(a, end='|')
# for i in range(n-1):
#         a, b = b, a+b
#         print(a, end='|')


#9

# for i in range(32,127):
#     print(chr(i), end='|')
#     if (i-1) % 10 ==0:
#         print()


########### LISTS FROM BEN STEPANYAN ###############

# #110
# my_list = []
#
# while number:= input('enter the number'):
#     if int(number) != 0:
#         my_list.append(number)
#     else:
#         break
# print(my_list)

# #111

# my_list = []
#
# while number := input('enter the number'):
#     if int(number) != 0:
#         my_list.append(number)
#     else:
#         break
# my_list.sort(reverse=True)
#
# print(my_list)







