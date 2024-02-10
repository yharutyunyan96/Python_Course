#                 _______   _______   _______
#      |         |       | |       | |       | 
#      |         |       | |       | |_______|     
#      |         |       | |       | |       
#      |_______  |_______| |_______| |  
#
#          ----------EXERCICES---------- 
#       ----------Ben Stephenson----------
#       ----------HAPPY NEW YEAR----------


# Exercise 67: Compute the Perimeter of a Polygon
# from math import sqrt

# x1 = xk1 = float(input('Enter the first x-coordinate: '))
# y1 = yk1 = float(input('Enter the first y-coordinate: '))

# x2 = 0
# y2 = 0
# paragic = 0

# while x2 != '':
#     x2 = input('Enter the next x-coordinate (blank to quit): ')
#     if x2 == '':
#         avelacum = sqrt((x1-xk1)**2 + (y1-yk1)**2)
#         paragic += avelacum
#         print(f'Perimeter is: {paragic}')
#     else:
#         x2 = float(x2)
#         y2 = float(input('Enter the next y-coordinate: '))

#         avelacum = sqrt((x2-x1)**2 + (y2-y1)**2)
#         paragic += avelacum

#         x1, y1 = x2, y2
#         continue



# Exercise 68: Compute a Grade Point Average
# grade_list = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
# points_list = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
# user_input = input('Enter grade letter: ')

# points = 0
# qunatity = 0

# while user_input != '' and user_input in grade_list:
#     idx = grade_list.index(user_input)
#     points += points_list[idx]
#     qunatity += 1
#     user_input = input('Enter next grade letter: ')

# average = round(points/qunatity, 2)
# print(f'Average of points is: {average}.')



# Exercise 69: Admission Price
# guest_age = 0
# price = 0
# guest_quantity = 1

# while True:
#   guest_age = input(f'Enter age of guest {guest_quantity} (blank to quit): ')
#   if guest_age != "" and guest_age.isdigit():
#     guest_quantity += 1
#     if float(guest_age) < 3:
#       price += 0
#     elif 3 <= float(guest_age) < 12:
#       price += 14
#     elif 12 <= float(guest_age) < 65:
#       price += 23
#     else:
#       price += 18
#     continue
#   elif guest_age == "":
#     guest_quantity -= 1
#     break
#   else:
#     print('Enter valid age!')
#     continue
# print(f'Total price for {guest_quantity} guest/s/ is ${price}')



# Exercise 70: Parity Bits
# user_input = 0
# while True:
#     user_input = input('Enter 8 bits (leave blank to quit): ')
#     if len(user_input) == 8 and ('0' in user_input or '1' in user_input):
#         x = user_input.count('1')
#         y = user_input.count('0')
#         print('Parity bit: 0' if x % 2 == 0 else 'Parity bit: 1')
#     elif user_input == '':
#         break
#     else:        
#         print('enter correct values.')
        


# Exercise 71: Approximate π
# tiv = 3
# for i in range(1, 16):
#     x = 4 / (i*2 * (i*2+1) * (i*2+2))
#     if i % 2 == 0:
#         tiv -= x
#         print(f'Approximation π of {i} is: {tiv}')
#     else:
#         tiv += x 
#         print(f'Approximation π of {i} is: {tiv}')



# Exercise 72: Fizz-Buzz
# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print('fizz - buzz')
#     elif i % 3 == 0:
#         print('fizz')
#     elif i % 5 == 0:
#         print('buzz')
#     else:
#         print(i)
    

    
# Exercise 73: Caesar Cipher
# from string import ascii_lowercase, ascii_uppercase

# ascii_lowercase, ascii_uppercase = ascii_lowercase*2, ascii_uppercase*2

# user_input = input('Enter messege to encrypt: ')
# shift = int(input('Enter shift amount (-25 to 25): '))

# poxvac = ''
# for i in user_input:
#     if i in ascii_lowercase*2:
#         idx = ascii_lowercase.index(i)
#         poxvac += ascii_lowercase[idx + shift]
        
#     elif i in ascii_uppercase*2:
#         idx = ascii_uppercase.index(i)
#         poxvac += ascii_uppercase[idx + shift]
#     else:
#         poxvac += i
# print(f'Original input - "{user_input}"')
# print(f'Encrypted input - "{poxvac}"')



# Exercise 74: Square Root
# x = float(input('Enter a number: '))
# guess = x / 2

# while (guess * guess - x) > 10**(-12):
#   guess = (guess + x/guess) / 2
  
# print(f'Square root of {x} is {guess}')



# Exercise 75: Is a String a Palindrome?
# user_input = input('Enter a word to determine is "Palindromity": ')

# user_input = user_input.lower()
# reverse = user_input[::-1]

# if user_input == reverse:
#   print(f'{user_input} is palindrome.')
# else:
#   print(f'{user_input} is not palindrome.')



# Exercise 76: MultipleWord Palindromes
# from string import punctuation as nshanner

# nshanner = list(nshanner)
# nshanner.append(' ')

# user_input = input('Enter a word to determine is "Palindromity": ')

# #prabelnern u mnacac@ hanum enq kpcnum enq irar, tarer@ poqracnum enq
# raw_text = user_input.lower()
# for char in raw_text:
#   try:
#     idx = nshanner.index(char)
#     raw_text = raw_text.replace(nshanner[idx], '')
#   except ValueError:
#     continue
    
# reverse = raw_text[::-1]

# if raw_text == reverse:
#   print(f'{user_input} is palindrome.')
# else:
#   print(f'{user_input} is not palindrome.')



# Exercise 77: Multiplication Table
# print('     ', end='')

# for i in range(1, 11):
#     print(f'{i:3}', end=' | ')

# print('\n' + '----' * 16)

# for i in range(1, 11):
#     print(f'{i:2} |', end=' ')
#     for k in range(1, 11):
#         print(f'{i * k:3}', end=' | ')
#     print()



# Exercise 78: The Collatz Conjecture
# x = int(input('Enter a number >>> '))
# count = []
# iter_count = 0
# while x > 1:
#   if x % 2 == 0:
#     x = x - x/2
#     count.append(int(x))
#     iter_count += 1
#     continue
#   else:
#     x = x*3 + 1
#     count.append(int(x))
#     iter_count += 1
#     continue
    
# print(count)
# print(f'Iterations to one - {iter_count}')



# Exercise 79: Greatest Common Divisor
# a = int(input('Enter first number: ')) 
# b = int(input('Enter second number: '))
# c = min(a, b)

# if a > 0 and b > 0 and a != b:
#     while a % c != 0 or b % c != 0:
#         c -= 1
#     print(f'Greatest common divisor for {a} and {b} is {c}')
# else:
#     print('Input positive and different numbers!')



# Exercise 80: Prime Factors
# tiv = user_input = int(input('Enter a number: '))

# factor = 2
# listulik = []

# while factor <= user_input:
#     if user_input % factor == 0:
#         listulik.append(factor)
#         user_input /= factor
#     else: 
#         factor += 1

# print(f'The prime factors of {tiv} are: {listulik}')



# Exercise 81: Binary to Decimal



# Exercise 83: Maximum Integer
# import random

# listik = []
# qanak = 0

# lider = random.randrange(1, 101)  # araji patahac tvin talis enq amenamec arjeq@ hl@ vor
# listik.append(lider)              # araji tiv@ qcum enq listi mej

# for i in range(1, 100):  # 99 hat for a frum, lcnuma listi mej
#   listik.append(random.randrange(1, 101))  # >> listik = [random1, random2]
#   if listik[i] > lider:
#     lider = listik[i]
#     listik[i] = f'{listik[i]} << update'
#     qanak += 1

# for item in listik:  # listik@ irar tak tpum enq
#   print(item)

# print(f'The maximum value found was {lider}')
# print(f'The maximum value was updated {qanak} times')



# Exercise 84: Coin Flip Simulation
# from random import randint

# flip_times = []
# listik = []

# for _ in range(1, 11):
#   while True:
#     x = randint(0, 1)
#     listik.append(x)

#     if len(listik) >= 3 and listik[-3:] == [x, x, x]:
#       break
      
#   flip_times.append(len(listik))
  
#   for item in listik:
#     print(item, end=' ')
#   print(f'({len(listik)} flips)')

#   listik = []

# flip_average = sum(flip_times) / 10
# print(f'On average, {flip_average} flips were needed')
