

'''23/12/23 homework'''
#ex14_height
#height_foot = float(input("Enter your height in feet: "))
#inches = height_foot * 12
#centimeters = round(inches * 2.54, 1)
#print ("Your height in centimeters is equal to:", centimeters,"centimeters.")

#ex15_distance units ___ same way as ex14

#ex16_area and volume
# import math
# radius = float(input("Enter the radius of the circle:"))
# area = round(math.pi * radius**2, 2)
# volume = round((4*math.pi*radius**3)/3, 2)
# print ("The area of your circle is equal:",area,"\nThe volume of your circle is equal:",volume)

#ex19_free fall
# from math import sqrt
# distance = float(input("Enter distance:"))
# initial = 0 
# acceleration = 9.8
# final = sqrt(initial**2 + (2*acceleration*distance))
# print("The final speet is equal:", round(final, 2),"m/s")

#ex23_polygon
# from math import pi,tan
# lenght_of_side = float(input("Enter the length of the polygon's side:"))
# number_of_sides = int(input("Enter the number of the sides:"))
# area = (lenght_of_side**2 * number_of_sides)/4*tan(pi/number_of_sides)
# print ("The area of the polygon is equal:", area)

#ex24
# seconds = int(input("Enter seconds:"))
# seconds_per_minut = 60
# seconds_per_hour = 3600
# seconds_per_day = 86400
# #dividing the taking the reminder so seconds in hours will remeine the reminder of seconds of day
# days = seconds/seconds_per_day
# seconds = seconds%seconds_per_day
# #same here as with days
# hours = seconds/seconds_per_hour
# seconds = seconds%seconds_per_hour

# minut = seconds/seconds_per_minut
# seconds = seconds%seconds_per_minut
# print("The equivalent duration is","\n",round(days, 2),":days","\n",round(hours, 2),":hours","\n",round(minut, 2),":minutes","\n",round(seconds, 2),":seconds")

#ex32
#num = int(input("Enter your 4 digit number:"))
#first_num = num//1000
#_2nd = num//100%10
#_3rd = num//10%10
#last_num = num%10
#print(last_num,_3rd,_2nd,first_num)

'''exercises for decision making____if_else_elif'''

#ex35_even_odd
# number = int(input("Enter number:"))
# even = number%2
# if even == 0:
#       print("Your number is even:")
# elif even !=0:
#         print("Your number is odd:")

#ex36_dog_age
#your_age = int(input("Enter your age: "))
#if your_age <= 0:
    #print("You entered negative number,please enter valid age!")
#elif your_age <=21:
    #dog_age = your_age // 10.5
    #print ("if we change your age:",your_age,"with dog's,it will be equal to:",dog_age)
#else:
    #dog_age2 = 2 + (your_age-21) //4
    #print ("Dog's age will be:", dog_age2)


# #ex45_holidays
# import time
# days = ("January 1","July 1","December 25", "sep = \n")
# print(days)
# your_day = input("Enter the date:" "")
# NY = ("January 1")
# CD = ("July 1")
# ChD = ("December 25")
# january_1 = ("New Year's day")
# July_1 = ("Canada day")
# December_25 = ("Christman day")
# if your_day in NY:
#     print(january_1)
# elif your_day in CD:
#     print(July_1)
# elif your_day in ChD:
#     print(December_25)
# else:
#     print("Enter valid date:")


#ex46_chess
# print ('''
       
# 1  ||  ||  ||  ||        This is a chess board                              
# 2    ||  ||  ||  ||      please enter your square coordinates,          
# 3  ||  ||  ||  ||        and i will tell you if it is black or white!                 
# 4    ||  ||  ||  ||                                
# 5  ||  ||  ||  ||                                     
# 6    ||  ||  ||  ||                           
# 7  ||  ||  ||  ||                                       
# 8    ||  ||  ||  ||    
#   a b c d e f g h 

# Please choose from vertical and horizontal coordinates! ''')
# coord = input("Enter your coordinate: ")
# a= "_abcdefgh"
# letter = coord[1]
# num = int(coord[0])
# hor_coord = a.find(letter)
# if (num + hor_coord)%2==0:
#    print("your square is even!")
# else:
#    print("Your square is odd!")

# #ex49_chinese_horoscope
# year = int(input("Enter your year:"))
# if year % 12 == 0:
#     print("Monkey")
# elif year % 12 == 1:
#     print("Rooster")
# elif year %12 == 2:
#     print("Dog")
# elif year % 12 == 3:
#     print ("Pig")
# elif year % 12 == 4:
#     print("Rat")
# elif year % 12 == 5:
#      print("Ox")
# elif year % 12 == 6:
#     print("Tiger")
# elif year % 12 == 7:
#     print ("Hare")
# elif year % 12 == 8:
#     print ("Dragon")
# elif year % 12 == 9:
#     print("Snake")
# elif year %12 == 10:
#     print ("Horse")
# elif year % 12 == 11:
#     print ("Sheep")
# else:
#     print("Enter valid year:")


'''Exercises for loops'''

#ex
# for ascii_index in range(97,123):
#     print(f'{ascii_index: ^9} | {chr(ascii_index): ^9}')


