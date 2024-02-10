# print('Hello World')
import math

########## Exercises


# ### Task 1 Post adress
#
# print('Name: Argam''\n''adress: RA Tavush region, Khashtarak 14 street, 11 house')


### Task 2 Greeting

# name = input('Enter your name')
# print('Hello', name)

### Task 3 room area
#
# length = float(input('Enter the length of the room:'))
# width = float(input('Enter the width of the room:'))
# print('the area of the room is', length * width, 'm^2')


### Task 4 Garden area
#
# length = float(input('Enter the length of the garden in feet:'))
# width = float(input('Enter the width of the garden in feet:'))
# print('the area of the garden is', length * width * 43560, 'akr')


### Task 5 Handing over bottles
#
# small_bottles= 0.10
# big_bottles= 0.25
# quantity_s = int(input('The number of bottles of 1 liter or less:'))
# quantity_l = int(input('The number of bottles larger than 1 liter:'))
#
# print('Amount for the proceeds', round(quantity_s * small_bottles + quantity_l * big_bottles, 2), '$')

### Task 6 Taxes and tips
#
# sum = float(input('Enter the amount of the order at the restaurant'))
# tips = sum * (18/100)
# tax = sum * (10/100)
# print(tips,'\n',tax,'\n',round(sum + tips + tax, 2))

### Task 7 Sum of first n positive numbers
#
# n = int(input('Enter the number:'))
# sum = (n * (n + 1))/2
# print('The sum of first positive numbers is:', int(sum))

# ### Task 8 Souvenirs and trinkets
# c
# souv = 75
# trink = 112
# quant_souv = int(input('Enter the number of souvenirs:'))
# quant_trinkets = int(input('Enter the number of trinkets:'))
# print('The total weight of purhases:', quant_souv * souv + quant_trinkets * trink, 'gramm')

### Task 9 Compound interest

# sum = float(input('Enter the initial deposit amount:'))
# p = 4
# sum1 = round(sum * (1+(p/100)),2)
# sum2 = round(sum * (1+(p/100))**2,2)
# sum3 = round(sum * (1+(p/100))**3,2)
#
# print('Amount at the and of first year is:',sum1,'\n', 'Amount at the and of second year is', sum2,'\n', 'Amount at the and of third year is', sum3)


# ### Task 10 Arithmetic
#
# a = int(input('Enter the number a: '))
# b = int(input('Enter the number b:'))
#
# sum = a+b
# dif = a-b
# prod = a*b
# quot = a/b
# rem = a%b
# log_10 = math.log10(a)
# degree = a**b
#
# print(sum, dif, prod, quot, rem, log_10, degree, sep='\n')

## Task N 10

# a = input('Enter the first number:')
# b = input('Enter the second number:')
# a = int(a,2)
# a = bin(a)
# b = int(b,2)
# b = bin(b)
# n1 = a&b
# n2 = a|b
# n3 = a^b
# print(n1, n2, n3)


### Task 11 Fuel consuption





### Task 12 Distance between points on earth
#
# t1 = math.radians(float(input('Enter latitude of a point on the earths surface:')))
# g1 = math.radians(float(input('Enter longitude of a point on the earths surface:')))
# t2 = math.radians(float(input('Enter latitude of a point on the earths surface:')))
# g2 = math.radians(float(input('Enter longitude of a point on the earths surface:')))
#
# distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2 * math.cos(g1 - g2)))
#
# print('distance between points:', distance)


# ### Task 13 Exchange
#
# payment = float(input("Enter your money in cents:"))
# toonie = float(payment // 200 )
# loonie = float(payment - toonie*200) // 100
# quarters = float(payment %100)// 25
# nickles = float(payment %100 - quarters*25) //10
# pennies = float(payment %100 - quarters*25 -nickles*10)//5
# cents = float(payment %100 -  quarters*25 - nickles*10- pennies*5)
# print("Your change is:","\n","Toonies:",toonie,"\n","Loonies:",loonie,"\n","Quarters:",quarters,"\n","Nickles:",nickles,"\n","Pennies:",pennies,"Cents",cents,"\n" )


# ### Task 14 Height
#
# fut = float(input('Enter the distance number:'))
# duim = fut * 12
# yard = fut * 0.333
# mile = fut * 0.0000189
#
# print(duim, yard, mile, sep='\n')


### Task 15 Area and volume
#
# r = float(input('Enter the radius:'))
# area = math.pi * r**2
# volume = 4/3 * math.pi * r**3
#
# print(area, volume, sep='\n')

### Task 17 Heat capacity

# m = float(input('Enter amount of water in grams: '))
# t = float(input('Enter desired temperature change of water in celsius: '))
# q = m * t
#
# # To heat 1 kg water by 1 celsius an amount of heat equal to JOUL (J)
# j = q / 4.186
#
# # 1 joul equals to (1/3600000) kW
# kW = j / 3600000
# print(j, 'joules')
# print(kW, 'kW')


### Task 18 Cylinder volume

# r = float(input('Enter the cylinder radius:'))
# h = float(input('Enter the height: '))
# V = math.pi * r**2 * h
# print('The volume of the cylinder is:', V, 'm**3')


### Task 19 Free fall
#
# d = float(input('Enter the height:'))
# Vi = 0
# a = 9.8
#
# Vf = math.sqrt(Vi**2 + 2 * a * d)
# print('The speed of an object as it touches the ground:', Vf, 'm/s')




######### Task for looks ########

### Task 1

# n = int(input('n: '))
# counter = 1
# n = n // 10
# while n > 0:
#     n = n // 10
#     counter += 1
#
# print('Ranks:', counter)


### Task 2

# n = input('Enter num: ')
# even = 0
# odd = 0
#
# for i in n:
#     if int(i) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# while n:
#     last = n % 10
#     if last % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     n //= 10
#
# print(f"Evens count: {even} | Odds count: {odd}")



# for i in range(1, n+1):
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     print(f'Even: {even}, Odd: {odd}')


### Task 3

# num = int(input('Enter number: '))
# sum = 0
# prod = 1
# while num > 0:
#     i = num % 10
#     sum = sum + i
#     prod = prod * i
#     num = num // 10
#
# print(f'Sum: {sum}, Product of number: {prod}')


### Task 4

# n = int(input('Enter number: '))
# digit = n % 10
# n2 = digit
# n = n // 10
# while n > 0:
#     digit = n % 10
#     n = n // 10
#     n2 = n2 * 10
#     n2 = n2 + digit
#
# print('Its inverse number: ', n2)


### Task 5
# n = int(input())
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)


