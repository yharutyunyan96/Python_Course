#A_practical_intro_to_python_loops_exersices

#ex1_name
# name= input("Enter your name: ")
# for i in range(0,100):
#     print(name)

# #ex2_horiz_vertic
# name = input("Enter your name:")
# for i in range(16):
#     print(name + (name*15))

# #ex3_name
# name= input("Enter your name:")
# for i in range (0,100):
#     print(i + 1, name)

# #ex4_squares
# for i in range (1,21):
#     print(i,"---",i*i)
    
    
# #ex5_+3
# for i in range (8,90,3):
#     print (i)

# #ex6_reversed_num
# for i in reversed(range(2,101,2)):
#     print(i)

#ex7_4FOR_loops
# letter_e="E"
# letter_g="G"
# for i in range (8):
#     print("A",end="")
# for i in range (6):
#     print("B",end="")
# for i in range (1):
#     print("CD"*4, end="")
#     print(letter_e,end="")
# for i in range (5):
#     print("F",end="")
# print(letter_g)

# #ex8_name_xtimes
# name = input("enter your name:")
# quantity = int(input("enter how many times your would like it to be printed:"))
# for i in range(quantity):
#     print(name)

#unsolved
# #ex9_fibbonacci_number
# fibbonacci = int(input("Enter the fibbonacci number:"))
# series = [0, 1]
# while len(series) < fibbonacci:
#     series.append(series[-1] + series[-2])
# print(series)
#ex10_*
# wide = int(input("Enter how wide you want our box to be:"))
# high = int(input("Enter how high your want our box to be:"))
# for i in range(high):
#     print("*"*wide,)


#unsolved
######ex11_*---*
# wide = int(input("Enter how wide you want our box to be:"))
# high = int(input("Enter how high your want our box to be:"))
"""
******
*    *
******
"""
# print('*'*wide)
# for _ in range(high-2):
#     print('*' + ' ' * (wide-2) + '*')
# print('*'*wide)


# for i in range(wide):
#     print("*",end="")
# for i in range(high - 1):
#     print("*")
# for i in range (high-2):
#     print()
# for i in range(wide):
#     print(" "*wide+"*")
# for i in range(0,high,high):
#     print("*"*wide)

#solved
# #ex12_*triangle_straight
# high = int(input("Enter how high you want the triangle to be:"))
# for i in range(0,high,1):
#     print("*"*( i+1))

#solved
# #ex13_*triangle_upside_down
# high = int(input("Enter the high of your triangle:"))
# for i in reversed(range(high)):
#     print("*" *(i+1))

#unsolved
#ex14_diamond
# size = 7
#
# for i in range(1, size, 2):
#     print(('*' * i).center(size))
# for i in range(size, 0, -2):
#     print(('*' * i).center(size))


# high = int(input("Enter the high of our diamond:"))
# half=high//2
# for i in range(half):
#     for j in range(half-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end= "")
#     print()
# for i in range(high-3):
#     print("*",end="")

