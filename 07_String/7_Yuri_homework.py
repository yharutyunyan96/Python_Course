#Exercise 37: Vowel or Consonant
# from string import ascii_lowercase, ascii_uppercase
# letter = input('Enter a letter: ')
# vowel_letter = 'aeiouAEIOU'

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

# m_days = [0, 31, "28 or 29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month_names = [0, 'january', 'february', 'march', 'april', 'may', 'june', 'jule', 'august', 'september', 'october', 'november', 'december']

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



#Exercise 41: Classifying Triangles
# side_1 = float(input('Enter first side of triangle: '))
# side_2 = float(input('Enter second side of triangle: '))
# side_3 = float(input('Enter third side of triangle: '))

# if side_1 == side_2 == side_3:
#     print('The triangle is equilateral.')
# elif side_1 != side_2 == side_3 or side_1 == side_2 != side_3 or side_1 == side_3 != side_2:
#     print('The triangle is isosceles.')
# else:
#     print('The triangle is scalene.')



#Exercise 42: Note to Frequency
# user_input = input('Enter value between A0 - G8: ')

# freq_range = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88] #HZ
# #               C4      D4     E4      F4      G4      A4      B4

# tarer = ["C", "D", "E", "F", "G", "A", "B"]

# if len(user_input) == 2 and user_input[0] in tarer and user_input[1].isdigit() and int(user_input[1]) in range(0, 9):
#     # #arandznacnum enq tar@ ev tiv@
#     tar_input = user_input[0]           
#     input_tar_index = tarer.index(tar_input)  
#     num_input = int(user_input[1])

#     #petqa 0-ovner@ gtnenq vor hesht lini
#     #orinak C0 = C4 / 16 = C4 / 2**4 = C4 / 2**(4-0))
#     #orinak C1 = C4 / 8 = C4 / 2**3 = C4 / 2**(4-1))
#     # es logikayov sharjvum enq araj

#     result = freq_range[input_tar_index] / 2**(4-num_input)

#     print(f'{user_input} Frequency is {result:.2f} HZ')
# else:
#     print('Enter correct value in A0 - G8')



#Exercise 43: Note to Frequency
# freq_range = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88] #HZ
# #               C4      D4     E4      F4      G4      A4      B4

# user_input = float(input(f'Enter frequency in {freq_range[0]-1} - {freq_range[6]+1}: '))

# tarer = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]

# note_ranges = {
#     "C4": [freq_range[0]-1, freq_range[0]+1],
#     "D4": [freq_range[1]-1, freq_range[1]+1],
#     "E4": [freq_range[2]-1, freq_range[2]+1],
#     "F4": [freq_range[3]-1, freq_range[3]+1],
#     "G4": [freq_range[4]-1, freq_range[4]+1],
#     "A4": [freq_range[5]-1, freq_range[5]+1],
#     "B4": [freq_range[6]-1, freq_range[6]+1],
# }

# for note, x in note_ranges.items():
#     if x[0] <= user_input <= x[1]:
#         print(f'This is {note}')
#         break
# else:
#     print('Note not found.')



#Exercise 44: Faces on Money
# dollar = [1, 2, 5, 10, 20, 50, 100]
# demq = ['George Washington', 'Thomas Jefferson', 'Abraham Lincoln', 'Alexander Hamilton', 'Andrew Jackson', 'Ulysses S. Grant', 'Benjamin Franklin']

# user_input = int(input('Please input a dollar banknote: '))

# if user_input in dollar:
#     d_index = dollar.index(user_input)
#     print(demq[d_index])
# else:
#     print('No such banknote exists.')



# Exercise 45: Date to Holiday Name
# print("Canada has three national holidays in a year. Lets guess them.")
# user_input = input("Enter a date in this format: MMMM DD (example: March 28): ")

# holiday_list = ['New Year’s Day', 'Canada Day', 'Christmas Day']
# day_list = ['January 1', 'July 1', 'December 25']

# if user_input in day_list:
#   user_input_idx = day_list.index(user_input)
#   result = holiday_list[user_input_idx]
#   print(result)
# else:
#   print('There are no holidays or invalid date format')


# Exercise 47: Season from Month and Day
# from datetime import datetime
# months_list = [
#   'January', 
#   'February', 
#   'March', 
#   'April', 
#   'May', 
#   'June',
#   'July',
#   'August',
#   'September',
#   'October',
#   'November',
#   'December'
# ]

# print('Enter month name from list below\n', *months_list, sep='\n')
# month_input = input('''
# >>> ''')
# day_input = int(input('''Enter day of month 
# >>> '''))

# months_day_list = [
#   range(1, 32), #January    0
#   range(1, 30), #February   1
#   range(1, 32), #March      2
#   range(1, 31), #April      3
#   range(1, 32), #May        4
#   range(1, 31), #June       5 
#   range(1, 32), #July       6
#   range(1, 32), #August     7
#   range(1, 31), #September  8
#   range(1, 32), #October    9 
#   range(1, 31), #November   10
#   range(1, 32), #December   11
# ]

# index_month = months_list.index(month_input)

# if day_input in months_day_list[index_month]:
#   #Gtnum enq te tvyal or@ tarva vorerord orn a
#   x = datetime(year=2023, month=(index_month+1), day=day_input).timetuple().tm_yday

#   if x in range(79, 172):                # March 20        79
#     print('It is Spring!')               # June 21         172
#   elif x in range(172, 265):             # September 22    265
#     print('It is Summer bebe!!!')        # December 21     355
#   elif x in range(265, 355):
#     print('It is Fall!')
#   else:
#     print('It is Winter!')
# else:
#   print('Sxal tiv es grum hopar')



# Exercise 48: BirthDate to Astrological Sign
# from datetime import datetime
# months_list = [
#   'January', 
#   'February', 
#   'March', 
#   'April', 
#   'May', 
#   'June',
#   'July',
#   'August',
#   'September',
#   'October',
#   'November',
#   'December'
# ]

# print('Enter month name from list below\n', *months_list, sep='\n')
# month_input = input('''
# >>> ''')
# day_input = int(input('''Enter day of month 
# >>> '''))

# months_day_list = [
#   range(1, 32), #January    0
#   range(1, 30), #February   1
#   range(1, 32), #March      2
#   range(1, 31), #April      3
#   range(1, 32), #May        4
#   range(1, 31), #June       5 
#   range(1, 32), #July       6
#   range(1, 32), #August     7
#   range(1, 31), #September  8
#   range(1, 32), #October    9 
#   range(1, 31), #November   10
#   range(1, 32), #December   11
# ]

# index_month = months_list.index(month_input)

# if day_input in months_day_list[index_month]:
#   #Gtnum enq te tvyal or@ tarva vorerord orn a
#   x = datetime(year=2023, month=(index_month+1), day=day_input).timetuple().tm_yday

#   goroscope_list = [
#     range(356, 365),   #0   Dec 22 - Jan 19 - Capricorn   
#     range(1, 19),      #1   Dec 22 - Jan 19 - Capricorn
#     range(20, 49),     #2   Jan 20 - Feb 18 - Aquarius
#     range(50, 79),     #3   Feb 19 - Mar 20 - Pisces
#     range(80, 109),    #4   Mar 21 - Apr 19 - Aries
#     range(110, 140),   #5   Apr 20 - May 20 - Taurus
#     range(141, 171),   #6   May 21 - Jun 20 - Gemini
#     range(172, 203),   #7   Jun 21 - Jul 22 - Cancer   
#     range(204, 234),   #8   Jul 23 - Aug 22 - Leo
#     range(235, 265),   #9   Aug 23 - Sep 22 - Virgo
#     range(266, 295),   #10  Sep 23 - Oct 22 - Libra      
#     range(296, 325),   #11  Oct 23 - Nov 21 - Scorpio  
#     range(326, 355),   #12  Nov 22 - Dec 21 - Sagittarius
#   ]

#   if x in goroscope_list[0] or x in goroscope_list[1]:              
#     print('Capricorn!')            
#   elif x in goroscope_list[2]:          
#     print('Aquarius')
#   elif x in goroscope_list[3]:          
#     print('Pisces')
#   elif x in goroscope_list[4]:          
#     print('Aries')
#   elif x in goroscope_list[5]:          
#     print('Taurus')
#   elif x in goroscope_list[6]:          
#     print('Gemini')
#   elif x in goroscope_list[7]:          
#     print('Cancer')
#   elif x in goroscope_list[8]:          
#     print('Leo')
#   elif x in goroscope_list[9]:          
#     print('Virgo')
#   elif x in goroscope_list[10]:          
#     print('Libra')
#   elif x in goroscope_list[11]:          
#     print('Scorpio')
#   else:
#     print('Sagittarius')          
# else:                                 
#   print('Sxal tiv es grum hopar')     



# Exercise 49: Chinese Zodiac
# print('''This is a chinese zodiac from book
# Year  Animal
# 2000  Dragon
# 2001  Snake
# 2002  Horse
# 2003  Sheep
# 2004  Monkey
# 2005  Rooster
# 2006  Dog
# 2007  Pig
# 2008  Rat
# 2009  Ox
# 2010  Tiger
# 2011  Hare
# ''')

# #gnum enq 0 tvakan vor hesht lini hashvark@
# zodiac = [
#     'Monkey',    # 0 tvakan, 12 tvakan
#     'Rooster',   # 1 tvakan
#     'Dog',       # .....
#     'Pig',       # .....
#     'Rat',       # .....
#     'Ox',        # .....
#     'Tiger',
#     'Hare',
#     'Dragon',
#     'Snake',
#     'Horse',
#     'Sheep',     # 11 tvakan
#     ]

# user_input = int(input('Enter year greater than zero to determine zodiac: '))

# if user_input > 11:
#     mnacord = user_input % 12
#     print(zodiac[mnacord])
# elif 0 <= user_input <= 11:
#     print(zodiac[user_input])
# else:
#     print('Please enter year great than 0 dude!!!')



# Exercise 50: Richter Scale
# scale_val = [
#     [0, 2],
#     [2, 3],
#     [3, 4],
#     [4, 5],
#     [5, 6],
#     [6, 7],
#     [7, 8],
#     [8, 10]
# ]

# descriptor = [
#     'Micro',
#     'Very Minor',
#     'Minor',
#     'Light',
#     'Moderate',
#     'Strong',
#     'Major',
#     'Great',
#     'Meteoric'
# ]

# user_input = float(input('Enter magnitude value: '))

# for i in range(len(scale_val)):
#     if scale_val[i][0] <= user_input < scale_val[i][1]:
#         print(descriptor[i])
#         break
# else:
#     print(descriptor[8])



# Exercise 51: Roots of a Quadratic Function
# ban chhaskaca


# Exercise 52: Letter Grade to Grade Points
# grade_list = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
# points_list = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
# user_input = input('Enter grade letter: ')

# if user_input in grade_list:
#   for i in range(len(grade_list)):
#     if user_input == grade_list[i]:
#       print(f'Grade points for {user_input} is {points_list[i]}')
#       break
# else:
#   print('Invalid letter grade.')




# Exercise 53: Grade Points to Letter Grade
# grade_list = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
# points_list = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]

# user_input = float(input('Enter grade point: '))

# if 0 <= user_input < points_list[0]:
#   if points_list[2] <= user_input < points_list[1]:
#     print(grade_list[1])
#   elif points_list[3] <= user_input < points_list[2]:
#     print(grade_list[2])
#   elif points_list[4] <= user_input < points_list[3]:
#     print(grade_list[3])
#   elif points_list[5] <= user_input < points_list[4]:
#     print(grade_list[4])
#   elif points_list[6] <= user_input < points_list[5]:
#     print(grade_list[5])
#   elif points_list[7] <= user_input < points_list[6]:
#     print(grade_list[6])
#   elif points_list[8] <= user_input < points_list[7]:
#     print(grade_list[7])
#   elif points_list[9] <= user_input < points_list[8]:
#     print(grade_list[8])
#   elif points_list[10] <= user_input < points_list[9]:
#     print(grade_list[9])
#   elif points_list[11] < user_input < points_list[10]:
#     print(grade_list[10])
#   else:
#     print(grade_list[11])
# elif user_input >= points_list[0]:
#   print(grade_list[0])
# else:
#   print('Enter positive number.')



# Exercise 54: Assessing Employees
# x = float(input('Enter rating scale (0 or 0.4 or 0.6 or more) to award an employee: '))

# if x >= 0 and x == 0 or x == 0.4 or x >= 0.6:
#   if x == 0:
#     print('The rating is 0.0, there is no raise.')
#   elif x == 0.4:
#     raise_val = x * 2400
#     print(f'The rating is {x}, raise of employee is ${raise_val:.2f}.')
#   else:
#     raise_val = x * 2400
#     print(f'The rating is {x}, raise of employee is ${raise_val:.2f}.')
# else:
#   print('Enter correct number.')


# Exercise 55: Wavelengths of Visible Light
# color_list = [
#   'Violet',
#   'Blue',
#   'Green',
#   'Yellow',
#   'Orange',
#   'Red'
# ]

# wawe_list = [
#   range(380, 450),
#   range(450, 495),
#   range(495, 570),
#   range(570, 590),
#   range(590, 620),
#   range(620, 750),
# ]

# x = int(input('Enter wavelength in nanometers from 380 - 750: '))

# if x in range(380, 751):
#   for i in range(len(color_list)):
#     if x in wawe_list[i]:
#       print(f'The color is {color_list[i]}')
#       break
# else:
#   'The value entered is outside of the visible spectrum.'



