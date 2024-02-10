# Exercise 17: Heat Capacity
# m = float(input('Enter amount of water in grams: '))
# t = float(input('Enter desired temperature change of water in celsius: '))
# q = m * t
#
# # 1 gram of water to raise 1 celsius needed 1 JOULS of energy
# J = q / 4.186 #Energy in joules
#
# #One joule is equal to (1/3600000)kWh
# kwh = J / 3600000
# print(J, 'joules')
# print(kwh, 'kwh')


# Exercise 18: Volume of a Cylinder
# from math import pi
#
# r = float(input('Enter radius of the cylinder: '))
# h = float(input('Enter height of the cylinder: '))
#
# v = pi * r**2 * h
# rounded_v = round(v, 1)
#
# print("Volume of cilinder is:", rounded_v)


# Exercise 19: Free Fall
# from math import sqrt
# init_speed = 0
# acc = 9.8
# distance = float(input('Enter distance from floor in meters: '))
# final_speed = sqrt(init_speed**2 + 2 * acc * distance)
# rounded_f_speed = round(final_speed, 2)
# print('When it reaches the ground, its speed will be:', rounded_f_speed, 'm/s')


#Exercise 20: Ideal Gas Law
"""
PV = nRT where:
n -> is amount of substance in moles
P -> pressure in Pascals
r-> ideal gas constant
T -> temperature in degrees Kelvin
V -> Volume in litres
"""

# R = 8.314
# P = float(input('Enter the pressure in pascals: '))
# V = float(input('Enter the volume in litres: '))
# T = float(input('Enter the temperature in celsius: '))+273.15
#
# n = (P * V) / (R * T)
# rounded_n = round(n, 3)
# print('Moles of gas is:', rounded_n)


##Exercise 21: Area of a Triangle
print('''
      /\\         We have a triangle like this, where
     /  \\        b is the length of the base of the triangle,
    /    \\       h is its height.
   /|     \\      To calculate area of triangle, please
  / |      \\     enter value of b and h.
 /  |h      \\
/___|________\\
      b
''')

b = float(input('Enter value of b: '))
h = float(input('Enter value of h: '))
area = (b * h) / 2
print('Area of triangle is', area)


#Exercise 22: Area of a Triangle (Again)
# from math import sqrt
# print('this program reads the lengths of the sides of a triangle and prints its area')
# s1 = float(input('Enter value of first side: '))
# s2 = float(input('Enter value of second side: '))
# s3 = float(input('Enter value of third side: '))
#
# s = (s1 + s2 + s3) / 2
# area = sqrt(s * (s-s1) * (s-s2) * (s-s3))

# print('Area of triangle is:', area)

#Exercise 23: Area of a Regular Polygon
# from math import tan, pi
#
# print(r'''
#    ________         We have a regular polygon like this.
#   /        \\
#  /          \\
# /            \\
# \            /      This program will calculate area
#  \          /       of that regular polygon based
#   \________/        on values that user input.
#
# ''')
#
# n = int(input("Enter number of sides: "))
# s = int(input("Enter length of a side: "))
#
# area = (n * s**2) / 4 * tan(pi / n)
#
# print('Area of polygon based on input values is:', area)


#Exercise 24: Units of Time
# print('Enter duration!')
# days = int(input('Days: '))
# hours = int(input('Hours: '))
# minutes = int(input('Minutes: '))
# seconds = int(input('Seconds: '))

# min_in_sec = minutes * 60
# houres_in_sec = hours * 60 * 60
# days_in_sec = days * 24 * 60 * 60

# all_sec = seconds + min_in_sec + houres_in_sec + days_in_sec

# print(all_sec)

