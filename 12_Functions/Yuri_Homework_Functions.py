#    ----------Functions EXERCICES---------- 
#       ----------Ben Stephenson----------
#       ----------HAPPY NEW YEAR----------

'''
Ֆունկցիաներն աշխատացնելու համար uncomment անել համապատասխան ֆունկցիայի տակի main() ու if __name__ բլոկները: 
Կամ էլ ուրիշ տեղից import անել:
'''

# Exercise 85: Compute the Hypotenuse (ներքնաձիգ)
from math import sqrt
def nerqnadzig(a, b):
    '''Computes hypotenuse of a true triangle'''

    x = sqrt(a**2 + b**2)
    return x

# def main():
#     a = float(input('Enter length of first side of triangle: '))
#     b = float(input('Enter length of second side of triangle: '))
#     result = nerqnadzig(a, b)
#     print(f'The length of the hypotenuse is: {result:.3f}')

# if __name__ == '__main__':
#     main()



# Exercise 86: Taxi Fare
def taxi_fare(distance: float) -> float:
    '''Calculates total fare based on kilometer that user inputs.'''

    base_fare = 4      # 4 dollars minimal
    km_fare = 0.25     # 0.25 dollars for 140 meters
    meters = 140       # 0.25 dollars for 140 meters
    total_fare = base_fare + km_fare * distance * 1000 / meters
    return total_fare

# def main():
# # for taxi raw source thanks to Sergo, file - sergo_function_homework1.py
#     print(r'''
#                                  ______                                        ~
#                                 / TAXI \                                        ~                              ~~~~~~~
#                      __________/________\___________                            ~                             ( _  _  )
#                     /   _________   |   _________   \              .           ~                         \\   (  {    )
#                    /   /         |  |  |        |\   \             |          ~                           \\   \ ~~~ /
#                   /   /          |  |  |        | \   \            |         ~                             \\  __||__
#     _____________/   /___________|  |  |________|__\   \___________|___       ~                             \\|      |\
#    /_______                   .==   |           .==                 ___\       ~                             \|      |\\
#   /_O_/_O_/          ____________   |   ____________         (__.)  \ o \     ~                               |______| \\
#  /                                  |                                \_o_\    ~                              / /   | |  \\
# /_=_/    _______                    |                   _______          /==o                               / /    | |
# ========| OOOOO |======================================| OOOOO |========/                                  / /     | |
#          O  w  O                                        O  w  O                                        ___/ /      | |_
#           OOOOO                                          OOOOO                                         \___/       |___\
# __________________________________________________________________________________________________________________________________
# ''')
#     x = float(input('Enter distance in kilometers: '))
#     result = taxi_fare(x)
#     print(f'Total fare of {x} kilometers are ${result:.2f}')

# if __name__ == '__main__':
#      main()



# Exercise 87: Shipping Calculator
def shipping_charge(x: int) -> float:
    '''Calculates shipping charge based on items quantity.'''
    
    first = 10.95      #first item's price
    next_item = 2.95   #next item's price 
    if x == 1:
        return first
    elif x > 1:
        result = first + (x-1) * next_item
        return result
    else:
        return 0
        
# def main():
#      x = int(input('Enter quantity of shipping items: '))
#      printik = shipping_charge(x)
#      print(f'Shipping charge for {x} items is: {printik:.2f} dollars')

# if __name__ == '__main__':
#         main()
    


# Exercise 88: Median of Three Values
def median(a: float, b: float, c: float) -> float:
    '''Returns median of 3 numbers.'''
    
    l = [a, b, c]
    l.sort()
    return l[1]

# def main():
#      a = float(input('First number >>> '))
#      b = float(input('Second number >>> '))
#      c = float(input('Third number >>> '))
#      print(f'Median is : {median(a, b, c)}')

# if __name__ == '__main__':
#         main()



# Exercise 89: Convert an Integer to Its Ordinal Number
def num_to_string(x: int) -> str:
    '''1 -> first, 2 -> second .... (between 1-12).'''
    
    l = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth']
    if 1 <= x <= 12:
        return l[x-1]
    else:
        return f'OOPS! {x} is not supported yet.'
    
# def main():
#     for i in range (1, 13): 
#         #xndri pahanjn a vor cuyc tanq te vonc a ashxatum kod@
#         print(f'{i} -> {num_to_string(i)}')

# if __name__ == '__main__':
#         main()



# Exercise 90: The Twelve Days of Christmas
def ankaperg(n: int) -> str:
    '''Returns one verse of song based on its day number (1-12).'''
    
    first = f'On the {num_to_string(n).lower()} day of Christmas\n' 
    second ='my true love sent to me:\n'
    third = 'A partridge in a pear tree.\n\n'
    last = 'And ' + third.lower()

    l = [
        "Two turtle doves,\n",      
        "Three French hens,\n",      
        "Four calling birds,\n",
        "Five golden rings,\n",
        "Six geese a-laying,\n",
        "Seven swans a-swimming,\n",
        "Eight maids a-milking,\n",
        "Nine ladies dancing,\n",
        "Ten lords a-leaping,\n",
        "Eleven pipers piping,\n",
        "Twelve drummers drumming,\n"]
    
    if n == 1:
        return first + second + third
    elif n in range(2, 13):
        kuplet = ''
        for i in range((n-2), -1, -1):     
            kuplet += l[i]
        return first + second + kuplet + last
    
# def main():
#     x = ''
#     for i in range(1, 13):
#         x += ankaperg(i)
#     return print(x)
#
# if __name__ == '__main__':
#         main()




# Exercise 91: Gregorian Date to Ordinal Date
def ordinalDate(day: int, month: int, year: int) -> int:
    '''Returns day number in given date'''

    m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        m_days[2] = 29
    if month in range(1, 13):
        x = day
        for i in range(0, month):
            x += m_days[i]
        return x
    else:
        return ValueError('ERROR! Given value of month is not correct.')

# def main():
#     day = int(input('Enter day >>> '))
#     month = int(input('Enter month >>> '))
#     year = int(input('Enter year >>> '))
#     result = ordinalDate(day, month, year)
#     return print(f'Day number for {day}/{month}/{year} is {result}')

# if __name__ == '__main__':
#         main()



# Exercise 92: Ordinal Date to Gregorian Date
def days_later(day: int, month: int, year: int, period: int) -> int:
    '''Veradardznum a tvyal amsatvic qani or hetoi amsativ@'''
    '''2 angam tari fraluc heto sxala hashvum!!'''

    m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        m_days[2] = 29

    p = period
    x = ordinalDate(day, month, year) + p

    a = day
    b = month
    c = year

    while ordinalDate(a, b, c) != x:       
        if a == m_days[month]:
            a = 1
            if b == 12:
                b = 1
                #Chem kara bacatrem stex incha katarvum
                x = p - (ordinalDate(31, 12, c) - ordinalDate(day, month, year))
                p -= x
                c += 1
            else:
                b += 1
        else:
            a += 1
    
    result = f'{a:02d}/{b:02d}/{c:04d}'
    return result

# def main():
#     day = int(input('Enter day >>> '))
#     month = int(input('Enter month >>> '))
#     year = int(input('Enter year >>> '))
#     period = int(input('Enter a period >>> '))

#     result = days_later(day, month, year, period)
#     return print(f'Date {period} days later is {result}')

# if __name__ == '__main__':
#         main()



# Exercise 93: Center a String in the Terminal Window
def center_string(text: str, width: int, symbol=' ') -> str:
  '''Centering string in terminal window'''
  
  if len(text) >= width:
    return text
  else:
    gic = '|'
    x = (width - len(text)) // 2
    result = f'{gic}{x * symbol} {text} {x * symbol}{gic}'
    return result

# def main():
#   text = "-> bari or hopar!"
#   width = 40
#   print(center_string(text, width, '*'))
#
#   text = "- bari or."
#   width = 40
#   print(center_string(text, width))
#
#   text = "-> dzyadz karoxa imanas ste vaxtin opeli raskulachit kar che? tesel es?"
#   width = 40
#   print(center_string(text, width))
#
#   text = "- senc uxix gna ajit garajneri hetevna."
#   width = 40
#   print(center_string(text, width))
#
# if __name__ == '__main__':
#   main()


# Exercise 94: Is It a Valid Triangle?
def triangle_validity(a: float, b: float, c: float) -> bool:
  '''returns boolean of possibility to form a triangle of given values'''
  
  return not (a >= b + c or b >= a + c or c >= a + b or a <= 0 or b <= 0
              or c <= 0)

# def main():
#   a = float(input('Enter first value > '))
#   b = float(input('Enter second value >> '))
#   c = float(input('Enter third value >>> '))
#   return print(triangle_validity(a, b, c))

# if __name__ == '__main__':
#   main()

# Exercise 95: Capitalize It
from string import punctuation
def capitalize(text: str) -> str:
  '''Capitalizes sentences first words, and "i"-s.'''
  
  nshanner = punctuation + "’"

  # texti araji tarn a mecatar sarqum
  text = text[0].upper() + text[1:]

  new_text = ''

  for i in range(len(text)):
    #ete miaynyak 'i' a gtnum sarqum a I
    if 0 < i < len(text) - 1 and text[i] == 'i' and text[
        i - 1] == ' ' and text[i + 1] == ' ':
      new_text += text[i].upper()

    #Inchvor nshanic heto ete prabela tenum heto mecatar a sarqum
    elif text[i - 2] in nshanner and text[i - 1] == ' ':
      new_text += text[i].upper()

    #'i'-n mecatara sarqum ete nshan ka i-ic heto
    elif text[i] == 'i' and text[i + 1] in nshanner:
      new_text += text[i].upper()

    else:
      new_text += text[i]

  return new_text

# def main():
#   text = 'what time do i have to be there? what’s the address? this time i’ll try to be on time!' #input('Write sentences to capitalize: ')

#   return print(capitalize(text))

# if __name__ == '__main__':
#   main()



# Exercise 96: Does a String Represent an Integer?
def isInteger(text: str) -> int or bool:
  '''Identifies in given text integer availability and returns integer'''
  
  #ajic, dzaxic prabelner@ hanum enq
  clear_text = text.strip()
  digits_list = '0123456789π'
  plusminus = '+-'
  count_plus = clear_text.count('+')
  count_minus = clear_text.count('-')

  result = ''

     #stuguma +-ner@ vor 1-ic avel chlini u lini menak demic
  if (clear_text[0] in plusminus or clear_text[0] in digits_list) and (count_plus + count_minus) <= 1:
    for i in clear_text:
      if i in digits_list or clear_text[0] in plusminus:
        result += i
      else:
        return False
  else:
    return False

  return int(result)

# def main():
#   text = input('Enter a text: ')
#
#   print(isInteger(text))
#
# if __name__ == '__main__':
#   main()



# Exercise 97: Operator Precedence
def precedence(x: str) -> int:
    '''Returns precedence of a mathematical operator'''
    
    op_1 = '+-'     # return 1
    op_2 = '*/'     # return 2
    op_3 = '^'      # return 3
    op_0 = '%**//'  # return -1
    if x in op_0 + op_1 + op_2 + op_3:
       if x in op_1: return 1 
       elif x in op_2: return 2
       elif x in op_3: return 3
       elif x in op_0: return -1
    else:
       return 'Entered value is not operator!'
    
# def main():
#   x = input('Enter a operator: ')
#   result = precedence(x)
#   if result == 'Entered value is not operator!': 
#      return print(f'"{x}" is not operator')
#   else: 
#      return print(f'Precendence of "{x}" is {result}')

# if __name__ == '__main__':
#   main()



# Exercise 98: Is a Number Prime?
def isPrime(x: int) -> bool:
   '''Determines if given number is prime or not'''
   
   if x < 2:
      return False
   
   # a = 2
   # while a**2 <= x:
   #   if x % a == 0:
   #      return False
   #   a += 1
   # return True

   # for a in range(2, x//2+1):
   #      if x % a == 0:
   #          return False
   #  return True

# def main():
#   x = int(input('Enter a number: '))
#   print(isPrime(x))

# if __name__ == '__main__':
#   main()



# Exercise 99: Next Prime
def nextPrime(x: int) -> int:
   '''Finds next larger prime number'''
   
   # a = x + 1
   # while True:
   #     if isPrime(a):
   #         return a
   #    a += 1
   # return a


# def main():
#   x = int(input('Enter a number: '))
#   print(f'Next prime number is {nextPrime(x)}')

# if __name__ == '__main__':
#   main()



# Exercise 100: Random Password
from random import randint
def random_passwd() -> str:
  '''Generates random password with ASCII table 33-126 characters'''
  
  # x = ''
  # for i in range(33, 127):  # x-i mej lcnuma ascii 33 - 126 nisher@
  #    x += chr(i)
  #
  # passwd = ''
  # length = randint(7, 10)   #yntrum a patahakan erkarutyun 7-10 nish
  #
  # for i in range(length):   #generacia a anum password
  #    val = randint(1, len(x) - 1)
  #    passwd += x[val]
  # passwd = ''
  # for i in range(randint(7, 10)):
  #     passwd += chr(randint(33, 127))
  # return passwd

# def main():
#   print(random_passwd())
#
# if __name__ == '__main__':
#   main()



# Exercise 101: Random License Plate

# Xndri pahanj@ hayeci linelu hamar tox haykakan hamarner generacni, petakan u masnavor
# Ete hayeci-ic em xosum asa xi hayeren chem grum :D

from string import ascii_uppercase, digits
from random import choice

def random_licenseplate() -> str:
   '''Generates random Armenian license plate number for company or person'''
   
   tver_2 = choice(digits) + choice(digits)
   tver_3 = choice(digits) + choice(digits) + choice(digits)
   tarer = choice(ascii_uppercase) + choice(ascii_uppercase)

   if choice(digits[:2]) == '1':
      # hamarneri format - 00 XX 000
      person_numbers = tver_2 + ' ' + tarer + ' ' + tver_3
      return person_numbers
   else:
      # hamarneri format - 000 XX 00
      company_numbers = tver_3 + ' ' + tarer + ' ' + tver_2
      return company_numbers

# def main():
#   print(random_licenseplate())
#
# if __name__ == '__main__':
#   main()
