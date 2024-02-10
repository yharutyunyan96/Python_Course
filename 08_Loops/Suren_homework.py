######################### З А Д А Ч И #######################

############# L I N E A R   A L GO  R I T M S ###############

#task 1: apples

# print('Enter the number of students')
# students = int(input())                                          #inputing quantitiy of students
# print('Enter the number of apples')
# apples = int(input())                                            #inputing quantitiy of apples
# sdudents_apples = apples // students
# basket_apples = apples % students
# print('Every student will get',sdudents_apples, 'apples')        # output result
# print('There will be',basket_apples,'apples left in the basket') # output result


# #task 2 alphabet

# alphabet = 'abcdefghijklmnopqrstuvwxyz' # if you don't understand what this is, then there is no point in reading further
# print('Enter the number of letter')     # էսել չասեմ, հասկացաք
# num = int(input())-1                    # determining letter position
# letter = alphabet[num]                  # finding the letter
# print(letter)                           # OMG! I can't belive, it's works


# # task 3

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


# # task 4
# import random
# print('Enter the begining of the numeric range:')
# a = int(input())
# print('Enter the end of the numeric range:')
# b= int(input())
# random_number = random.randint(a,b)
# print(random_number)

# # task 5

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
# s = 2*pi*h + 2 * pi*r**2
# print('the area of the lateral surface of the cylinder is equal to',s)


# # Task 9
#
print(''''It is necessary to find the equation of a line passing trough two points.

                ^y
                |    / y=kx+b                       The equation of a line has the form:
                |  ./
                |  / M(x1,y1)                                         y = kx+b,
                | /
                |/                                  where "k" is the tangent of the angle
     -----------|----------------->                 between  the line and the abscis axis,
               /|                 x                 and "b" is the displacementof the line
   N(x1,y1) . / |                                      along the ordinateaxis.
             /  |                                   -------------------------------------
            /   |                                                                     ''')

print('''Having the coordinates of the given points and inserting them into the equation if
the line passing trough these points, we can easily obtain the values of "b" and "k".
-------------------------------------------------------------------------------------------
The equation if the line passing trough two points has the form:

x - x1     y-y1     x-x2    y-y2
------- = ------ or ----- = ----- , => y = X*(y2-y1)/(x2-x1)+(x1y2+x2y1)/(x1-x2)
x2 - x1    y2-y1    x2-x1   y2-y1
''') ############ Ձև ենք տալիս, որ մաթեմ գիտենք
#
x1 = float(input('Enter the x1'))
y1 = float(input('Enter the y1'))
x2 = float(input('Enter the x2'))
x2 = float(input('Enter the y2'))

print('y =', (y2-y1)/(x2-x1),'x+',(x1*y2+x2*y1)/(x1-x2))


# Task 10

# a = input('Entet the first binar number:')
# b = input('Enter the second binar number:')
# a = int(a,2)
# b = int(b,2)
# n1 = bin(a&b)
# n2 = bin(a|b)
# n3 = bin(a^b)
#
# print(n1, n2, n3)



################# B R A N C H I N G #####################


# #Task 1 broken function
#
# x = float(input('Enter the meaning of "x":'))
# if x > 0:
#     y = x - 0.5
# elif x == 0:
#     y = 0
# elif x < 0:
#     y = abs(x)
# print('The meaning of function is:', y)

## Task 2 Calculation of Weigth, density and Volume

# print('Calculation of mass, volume and density'.center(50, '-'))
# print('_' * 50)
# print('1. Weigth 2. density 3.Volume'.center(50, '-'))
# print('_' * 50)
#
# user_choice = input('Select >')
#
# if user_choice == '1':
#     Ro = float(input('Enter the density in kg/m^3:'))
#     V = float(input('Enter the volume in m^3:'))
#     print('The weigth is:', Ro * V, 'kg')
#
# elif user_choice == '2':
#     m = float(input('Enter the weigth in kg:'))
#     Ro = float(input('Enter the density in kg/m^3:'))
#     print('The volume is:', m / Ro, 'm^3')
#
# elif user_choice == '3':
#     m = float(input('Enter the mass in kg:'))
#     V = float(input('Enter the volume in m^3:'))
#     print('The density is:', m / V, 'kg/m^3')
# else:
#     print('enter a number from1 to 3 or go home')


# # Task 3 Area calculation

# from math import sqrt
#
# print('Area calculation'.center(50, '-'))
# print('_' * 50)
# print ('1. Rectangle 2. Triangle'.center(50,'-'))
# print('_' * 50)
#
# user_choice = input('Select >')
#
# if user_choice == '1':
#     a = float(input('Enter the small side of the rectangle in m:'))
#     b = float(input('Enter the big side of the rectangle in m:'))
#     print('The area of rectangle is', a * b, 'm ^ 2')
#
# elif user_choice == '2':
#     a = float(input('Enter the first side of the rectangle in m:'))
#     b = float(input('Enter the second side of the rectangle in m:'))
#     c = float(input('Enter the third side of the rectangle in m:'))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print(p)
#     print('The area of triangle is', s, 'm ^ 2')
# else:
#     print('select 1 or 2 or go home')

# # Task 4 Determining the possibility of constructing a triangle
#
# a = float(input('Enter the first side of the rectangle in m:'))
# b = float(input('Enter the second side of the rectangle in m:'))
# c = float(input('Enter the third side of the rectangle in m:'))
#
# if a + b > c and b + c > a and a + c > b:
#     print('Դուք շահել եք DVD')
# else:
#     print("Կրկին փորձիր.")


# Task 5 Determining of membership of a point on a circle

# x = float(input('Enter the abscissa of point (x):'))
# y = float(input('Enter the ordinate of point (y):'))
# R = float(input('Enter the radius of circle:'))
#
# if x**2 + y**2 == R**2:
#     print('The point belongs to the circle')
# else:
#     print('The point does not belong to the circle')


# # Task 6 Calculator
#
# a = float(input('Enter the first number:'))
# b = float(input('Enter the second number:'))
# action = input('+,-,/,*')
# if action == '+':
#     print(a+b)
# elif action == '-':
#     print(a-b)
# elif action == '/':
#     print(a/b)
# elif action == '*':
#     print(a*b)


# # Task 7 Determining of quarter
#
# x = float(input('Enter the abscissa of point (x):'))
# y = float(input('Enter the ordinate of point (y):'))
#
# if x>0 and y>0:
#    print ('The point is in first quarter')
# elif x<0 and y>0:
#    print ('The point is in second quarter')
# elif x<0 and y<0:
#    print ('The point is in third quarter')
# elif x>0 and y<0:
#    print ('The point is in fourth quarter')
# else:
#     print('You are on the cross')


# # Task 8 Is the year is a leap year?
#
# year = int(input('Enter the year after the birth of Christ:'))
#
# if year % 4 != 0:
#     print('The year is not a leap year')
# elif year % 100 == 0:
#     if year % 400 == 0
#         print('The year is a leap year')
#     else:
#         print('The year is not a leap year')
# else:
#     print('The year is a leap year')
#
# # Task 9 Celsius vs Farenheit
#
# print("1. Celsius to Farenheit 2. Farenheit to Celsius".center (50,'-'))
# print('_' * 50)
# user_choice = input('Select >'.center (50,'-'))
# if user_choice =='1':
#     c = float(input('Enter the temperature in F:'))
#     print('The temperature in Farenheit is', (c*1.8)+32,'F')
#     print('Thank you for choosing our airline')
# elif user_choice =='2':
#     f = float(input('Enter the temperature in C:'))
#     print('The temperature in Farenheit is', round((f-32)*5/9,2),'C')
# else:
#     print('Plesase select 1 or 2')
# print('Thank you for choosing our airline')

# # Task 10 Discriminant
#
# from math import sqrt
#
# print('aX^2 + bX + c = 0')
# a = float(input('Enter a:'))
# b = float(input('Enter b:'))
# c = float(input('Enter c:'))
#
# print(r'''
#                _____________
#          D = \/ b^2 -4*a*c")
#                                ''')
#
# D = b**2 - 4*a*c
# print('D =',D)
# if D>0:
#     x1 = (-b+sqrt(D))/(2*a)
#     x2 = (-b-sqrt(D))/(2*a)
#     print(r'''
#               ___
#          -b-\/ D
#     X1 =---------
#           2 * a     ''')
#     print('X1=',x1)
#
#     print(r'''
#               ___
#          -b+\/ D
#     X2 = ---------
#           2 * a     ''')
#
#     print('X2=', x2)
#
#
# elif D == 0:
#      print('X= ', -b/(2*a))
# else: print('The equation has no roots,')


##################################  Python Сборник упражнений ###############################

# #1
# name = 'Suren'
# surname = 'Nersisyan'
# adress = 'Vagharshapat, CHarents street, 7'
# print(name, surname, adress)

# #2
# name = input('Enter your name')
# print('Hello', name)

# #3

# length = float(input('Enter the length'))
# width = float(input('Enter the width'))
# square = length * width
# print('the area is', square, 'm^2')

# #4
# length = float(input('Enter the length in feet'))
# width = float(input('Enter the width in feet'))
# square = (length * width)/43560
# print('the area is', square, 'akr^2')

# #5

# quant1 = int(input('Enter the quantity of bottles with a volume less1l'))
# quant2 = int(input('Enter the quantity of bottles with a volume greater l'))
# price = quant1 * 0.10 + quant2 * 0.25
# print('bottle price is', price)

#6#7#8#9#10########################################################################################


# # 11

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
# loonie = (change_amount -toonie*200) // 100
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

# # 35 odd or even

# number = int(input('Enter the number'))
#
# if number % 2 == 0:
#     print('odd')
# else: print ('even')

# Task 36 Dog age

print('''Let's solve this task like Yuri''')

next =  input('Are you ready? Press enter>')

print('Once upon a time, there was a dog. His name was Hachiko.')

print(r'''  Look how cute hi was                                

        __
     o- ''|\_______/)
       \_/ |_)     )
           \  __  /
           (_/ (_/                     ''')


next =  input('Press Enter to continue')

print(r''' Hachiko grew older every year

   / \__
  (    @\___
  /          O
 /   (_____/
/_____/ U           ''')


next =  input('Artur jan wake up, this is not a bedtime story')

next = input('Press Enter to wake up Artur')

print(r'''I don't remember his owner's name. But it seems was Richard Gere. Every morning Hachiko accompanied him to the station and waited untill he returned.


                                                                                                             ~~~~~~~            
                                                                                                                  ~~~~~~
                                                                                                                      ~~~~
                                                                                                                        ~~~
                                                                                                                         ~~
                                                                                                                        _____  
                                                                                                                        \ ___/
                                                         _______________   ________________     _____        ______      |  |
                                                        | |_|   |_|  |_|  |  |  |_|   |_  |_|__(_____)_____| |_| |_| _____\_/___
                                                        | **********   |  |  **********   | |..............| |   |_| ......... |__
                                                        |______________|  |_______________| |______________| |_______________  \ \ \                                                                                                      ~ ~~~~~~~
                                                          O-O       O-O     O-O        O-O   O-O         O-O  O-O O-O O-O O-O   \ \ \                                                                                                    ~~~ ~~ ~~~~
                                                          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                              /__     ~ ~~~~
                                                        << << << << << << << << << << << << << << << << << << << << << << << << <<                                                                                                     / @      ~ )) ~
                                                                                                                                                                                                                                      /_       ~  ) ~~ 
                                                                                                                                                                                                                                       (            /~
                                           / \__                                                                                                                                                                                          *_       |
                                          (    @\___                                                                                                                                                                                          / --- \
                                         /          O                                                                                                                                                                                      / /    \  \
                   |                   /   (_____/                                                                                                                                                                                        | |     |  |
                   |             _____/      / U                                                                                                                                                                                          |  |     | |
                   \ __________/             \                                                                                                                                                                                            |  |     | |
                  /                          |                                                                                                                                                                                             \  \    | /
                 /     _____                 \                                                                                                                                                                                                \ /////
                /  /  /     \ ____            \                                                                                                                                                                                                /|   \
               /  /  /            \___  |   |  |                                                                                                                                                                                              /      \
              /  /  /                    \   \  \                                                                                                                                                                                            /        \
                                                                                                                                                                                                                                            /    /\    \
                                                                                                                                                                                                                                           /__ /   \ __ \
                                                                                                                                                                                                                                                        ''')
next =  input('Press enter to continue')
print('''Richard once tried to covert his age to dog's age. But suddenly got heart attack. Nothing interesting after this even. Hachiko continued to wait... bla bla bla .. THE END''')
next =  input('You will ask: What is the meaning og history?')
print('I propose to dedicate a minute of sielence to this kind man and to fuftil his last wish')

print('''now our program will convert human age to dog age''')

human_age = float(input('Enter the human age:'))

if human_age < 0: print('Տղա ջան, ովա էղե մաթեմիդ դասատուն?') #############################
if human_age > 0  and human_age <= 2:
    print('if that man was a dog, he was:',human_age*10.5)
elif  human_age >2:
    dogs_age = (human_age-2)*4+21
    print('if that man was a dog, he was:', dogs_age)


# # 40  Sound volume

# volume = float(input('Enter the sound volume in db'))
# if volume == 130:
#     print('it is a jackhammer')
# elif volume == 106:
#     print('it is a epilator')
# elif volume == 70:
#     print('it is a alarm. As Serje Tangian said: wake up!')
# elif volume == 40:
#     print('it is a quiet room')
# elif volume < 40:
#     print('you are deaf and you need to make an appointment widh a doctor')
# elif 40 < volume < 70:
#     print('between a quiet room and alarm')
# elif 70 < volume <106:
#    print('between alarm and epilator')
# elif 106 < volume < 130:
#     print('between a epiator and jackhammer')
# elif volume > 130:
#     print('Տուգանք 50 000 դրամ')

# 62 Casino
# import random
# print('Welcome to Roulett'.center(50, '-'))
# print('_' * 50)
#
# red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
# black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 10, 22, 24, 26, 28, 29, 31, 35]
# green = [37, 38]  # since for natural numbers we use the rand.int opetator instead of generating 0 and 00 we will generate the values 37 and 38
#
# win_num = random.randint(1, 38)
#
# if  win_num < 37:
#     print('The drawn number:', win_num)
#     print('The wiining bid:',win_num)
#
#     if win_num % 2 ==0:
#         print('The wiining bid: Even')
#     else:
#         print('The wiining bid: Odd')
#
#     if win_num > 18:
#         print('The winning bid: From 19 to 36')
#     else:
#         print('The winning bid: From 1 to 18')
#
#     if win_num in red:
#         print('The winning bid: Red')
#     elif win_num in black:
#         print('The winning bid: Black')
# elif win_num == 37:
#     print('The drawn number is: 0')
#     print('The wiining bid is: 0')
# elif win_num ==38:
#     print('The drawn number is: 00')
#     print('The wiining bid is: 00')

# if win_num >= 1 and win_num <= 36:
#     print('The drawn number is', win_num)
# elif win_num == 37:
#     print('The drawn numbet is 0')
# elif win_num == 38:
#     print('The winning number is 00')

# if win_num is in red:
#     print('The winning bid: red')
# elif win_num is in black:
#     print('The winning bid: black')
# elif win_num > 36:
#     print('The winning bid: green')
#
# if win_num $ 2 == 0
# print('The winning bid: even')
# else:
# print('The winning bid: odd')
# if win_num < 18
#     print('The winning bid: 1-18')
# elif win_num > 18 and win num < 37
# print('The winning bid: 19-36')
# elif win_num > 18 and win
# num > 36
# print(nobody
# win)