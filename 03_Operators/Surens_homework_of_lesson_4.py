# #task N 1: apples
import math
# students = int(input('Enter the number of students'))                                          #inputing quantitiy of students
# apples = int(input('Enter the number of apples'))                                            #inputing quantitiy of apples
# students_apples, basket_apples = divmod(apples, students)
# print('Every student will get',students_apples, 'apples')        # output result
# print('There will be',basket_apples,'apples left in the basket') # output result


# #task N 2 alphabet
# import string

# alphabet = string.ascii_lowercase # if you don't understand what this is, then there is no point in reading further
# print('Enter the number of letter')     # էսել չասեմ, հասկացաք
# num = int(input()) - 1                    # determining letter position
# letter = alphabet[num]                  # finding the letter
# print(letter)                           # OMG! I can't belive, it's works


# # task N 3

# from math import sqrt
# print('Enter the length of first side')
# a = float(input())
# print('Enter the length of second side')
# b = float(input())
# c = sqrt(a**2+b**2) # or (a**2+b**2)**0.5 if you don't want to use math
#
# area = a*b/2
# perimeter = a+b+c
# print('The area of triangle is', area)
# print('The perimeter of triangle is', perimeter)


# # task N 4
# import random
# print('Enter the begining of the numeric range:')
# a = int(input())
# print('Enter the end of the numeric range:')
# b= int(input())
# random_number = random.randint(a,b)
# print(random_number)

# # task N 5

# import random
# random_number = round(random.uniform(0.1, 0.5), 2)
# print(random_number)

# # task 6

# import random
# random_number = random.randint(100,999)
# a = random_number // 100
# b = (random_number % 100) // 10
# c = random_number % 10
#
# print(random_number, a+b+c)

# # # task 7
# from math import pi
#
# print('Enter the radius of the circle')
# r = float(input())
# l = 2*pi*r
# s = pi*r**2
# print('the area of circle will be:',s)
# print('the length of circle will be:',l)

# # task 8

# from math import pi
#
# print('Enter the radius of the cylinder')
# r = float(input())
# print('Enter the height of the circle')
# h = float(input())
# s = 2*pi*r*h + 2 * pi*r**2
# print('the area of the lateral surface of the cylinder is equal to',s)


#### tasks from en myus girq


## 11

# print('enter the vehicle fuel consuption indicator')
# MPG = float(input())
# LPK = 387.5/ (MPG *1.609)
# print('fuel consuption in Canadian', LPK)

## 12
# from math import radians
# print('enter the latitude of first  point')
# t1 = radians(float(input()))
# print('enter the longitude of first point')
# g1 = radians(float(input()))
#
# print('enter the latitude of second point')
# t2 = radians(float(input()))
# print('enter the longitude of second point')
# g2 = radians(float(input()))
#
# distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
# print('the distance betwen two points is:', distance )


# # 13

# print('Enter the change amount in cents:')
# change_amount = int(input())
#
# toonie = change_amount // 200
# change_amount %= toonie
# loonie = change_amount // 100
# cent25 = (change_amount % 100)//25
# cent10 = (change_amount % 100-cent25*25) // 10
# cent5  = (change_amount % 100-cent25*25-cent10*10) //5
# cent1  =  change_amount % 100-cent25*25-cent10*10-cent5*5
#
# print('Տալիս ես էտ անասունին')
#
# print('toonies:', toonie, 'loonies:', loonie, '25 cent:', cent25, '10 cent:', cent10, '5 cent:', cent5, '1 cent:', cent1, sep='\n')
# print('loonies:', loonie)
# print('25 cent:', cent25)
# print('10 cent:', cent10)
# print('5 cent:', cent5)
# print('1 cent:', cent1)
#
# print('-Մերսի ազիզ ջան', '-նորեն համեցեք',sep='\n')
# #
