#Exercise 35: Even or Odd?
# num = int(input('Enter a integer number: '))

# #stuguma bajanvuma 2-i te che
# bajanum = num % 2

# if bajanum == 0:
#     print(num, 'is even number.')
# else:
#     print(num, 'is odd number.')


#Exercise 36: Dog Years
# input_value = float(input('Enter a human year: '))
#
# if input_value <= 0:
#     print('Entered value is negative or zero! Enter valid number')
#     exit()
# elif 0 < input_value <= 2:
#     dog_years = input_value * 10.5
#     print(input_value, 'human years is equivalent to', dog_years, 'dog years')
# else:
#     dog_years_2 = 2 * 10.5
#     dog_years = (input_value - 2) * 4 + dog_years_2
#     print(input_value, 'human years is equivalent to', dog_years, 'dog years')


#Exercise 37: Vowel or Consonant
# from string import ascii_lowercase, ascii_uppercase
# letter = input('Enter a letter: ')
# vowel_letter = 'aeiouAEIOU'
#
# if letter not in ascii_lowercase and letter not in ascii_uppercase or len(letter) > 1:
#     print('Enter a valid letter.')
# elif letter in vowel_letter:
#     print(f'Entered letter - {letter}, is vowel letter.')
# else:
#     print(f'Entered letter - {letter}, is consonant letter.')


#Exercise 38: Name That Shape
# koxm_qanak = int(input('Գրեք կողմերի քանակը 3-10 միջակայքում՝ '))
# if koxm_qanak not in range(3,11):
#     print('Ընտրեք ճիշտ թիվ 3-10 միջակայքում')
# elif koxm_qanak == 3: print('Եռանկյուն')
# elif koxm_qanak == 4: print('Քառանկյուն')
# elif koxm_qanak == 5: print('Հնգանկյուն')
# elif koxm_qanak == 6: print('Վեցանկյուն')
# elif koxm_qanak == 7: print('Յոթանկյուն')
# elif koxm_qanak == 8: print('Ութանկյուն')
# elif koxm_qanak == 9: print('Իննանկյուն')
# else:
#     koxm_qanak == 10
#     print('Տասանկյուն')



#Exercise 39: Month Name to Number of Days 
# month_name = input('Enter month name: ')
#
# m_days = [0, 31, "28 or 29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month_names = [0, 'january', 'february', 'march', 'april', 'may', 'june', 'jule', 'august', 'september', 'october', 'november', 'december']
#
# if month_name in month_names:
#     x = month_names.index(month_name)
#     print('Number of days in', month_name, 'is', m_days[x])
# else:
#     print(r'''Enter correct month name in this format.
# 'january', 'february', 'march', 'april', 'may', 'june', 'jule', 'august', 'september', 'october', 'november', 'december' ''')


#Exercise 40: Sound levels
# user_input = float(input('Enter value in decibels: '))

# db_range = [40, 70, 106, 130]
# noice_range = ["Quiet Room", "Alarm Clock", "Gas Lawnmower", "Jackhammer"]

# if user_input in range(db_range[0], db_range[3]+1):
#     if user_input in db_range:
#         db_range_idx = db_range.index(user_input)
#         result = noice_range[db_range_idx]
#         print('Noice level is similar to', result)
#     elif db_range[0] < user_input < db_range[1] :
#         print('Noice level is between', noice_range[0], 'and', noice_range[1])
#     elif db_range[1] < user_input < db_range[2] :
#         print('Noice level is between', noice_range[1], 'and', noice_range[2])
#     else: 
#         db_range[2] < user_input < db_range[3]
#         print('Noice level is between', noice_range[2], 'and', noice_range[3])
# elif user_input < db_range[0]:
#     print('Noice level is quieter than', noice_range[0])
# else:
#     user_input > db_range[3]
#     print('Noice level is higher than', noice_range[3])


#41 - 45@ heto kanem chem hascrel


# Exercise 46: What Color Is That Square?
# print(r'''
# 8   ■ □ ■ □ ■ □ ■ □      We have a chess board.
# 7   □ ■ □ ■ □ ■ □ ■
# 6   ■ □ ■ □ ■ □ ■ □      To determine color of square
# 5   □ ■ □ ■ □ ■ □ ■      You need to enter a position
# 4   ■ □ ■ □ ■ □ ■ □      in range a1 - h8
# 3   □ ■ □ ■ □ ■ □ ■
# 2   ■ □ ■ □ ■ □ ■ □
# 1   □ ■ □ ■ □ ■ □ ■
#
#     a b c d e f g h
# ''')
# user_input = input("Enter coordinate in range a1-h8: ")
#
# #arandznacnum enq tar@ ev tiv@
# letter_input = user_input[0]
# num_input = int(user_input[1])
#
# letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
#
# #gtnum enq tari index@ tvov
# idx_letter = letters.index(letter_input)+1
#
# #user input@ sarqum enq tiv
# user_input_tiv = idx_letter + num_input
#
# #logika - ete tiv@ zuyga uremn seva
# if user_input_tiv % 2 == 0:
#     print('Square in', user_input, 'is black')
# else:
#     print('Square in', user_input, 'is white')


