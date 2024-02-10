# ~~~~~~~~~~~EXERCISES 37~~~~~~~~~~~~~~
# number = int(input( "Enter the number: " ))
# even = 0
# odd = 0 
# while number > 0:
#     if number % 2 == 0:
#         even += 1
#         print( " The number is even" )
#         break
#     else:
#         odd += 1
#         print( " The number is odd " )
#         break
# else:
#     print( " Enter the number bigger than 0 " )

# ~~~~~~~~~~~EXERCISES 38~~~~~~~~~~~~~~~~
# a = int(input( " Enter the number: " ))
# even = 0
# odd = 0
 
# while a > 0:
#     if  a % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     a = a // 10

# print("Even " , even , "Odd " , odd )

#~~~~~~~~~~~EXERCISES 39~~~~~~~~~~~~~~~~~~
# number = int(input( " Enter the number: " ))
# number2 = 0
# number3 = 1
# while number > 0:
#     tiv = number % 10
#     number2 = number2 + tiv 
#     number3 = number3 * tiv
#     number = number // 10
# print ( "Gumar: " , number2)
# print( "Bazmapatkum: " , number3)

#~~~~~~~~~~~EXERCISES 40~~~~~~~~~~~~~~~~~~~~
# a = int(input( " Enter the number: " ))
# a2 = 0
# while a > 0:
#     tiv = a % 10
#     a = a // 10
#     a2 = a2 * 10
#     a2 = a2 + tiv
# print(a2)