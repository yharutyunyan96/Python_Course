def is_prime(number: int) -> bool:
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True



def primefactors(user_input: int) -> list:
    """Return the prime factors of a number."""
    factor = 2
    result = []

    while factor * factor <= user_input:
        if user_input % factor == 0:
            result.append(factor)
            user_input //= factor
        else:
            factor += 1

    if user_input > 1:
        result.append(user_input)

    return result


# Exercise 100: Random Password
from random import randint
def random_passwd() -> str:
    '''Generates random password with ASCII table 33-126 characters'''

    x = ''
    for i in range(33, 127):  # x-i mej lcnuma ascii 33 - 126 nisher@
       x += chr(i)

    passwd = ''
    length = randint(7, 10)   #yntrum a patahakan erkarutyun 7-10 nish

    for _ in range(length):   #generacia a anum password
       val = randint(1, len(x) - 1)
       passwd += x[val]

    return passwd

# def main():
#   print(random_passwd())

# if __name__ == '__main__':
#   main()



# Exercise 102: Check a Password
from string import ascii_uppercase, ascii_lowercase, digits
def passwd_quality(passwd: str) -> bool:
    '''Password quality checker.

    Returns True, if length is > 8 and contains at least
    - one uppercase
    - one lowercase
    - one number'''

    condition_1 = len(passwd) >= 8

    condition_2 = False   #one uppercase
    condition_3 = False   #one lowercase
    condition_4 = False   #one number

    if condition_1:
      for i in passwd:
        if i in ascii_uppercase:
          condition_2 = True
        elif i in ascii_lowercase:
          condition_3 = True
        elif i in digits:
          condition_4 = True
    else:
      return False

    return condition_2 and condition_3 and condition_4

# def main():
#   passwd = input('Enter password: ')
#   passwd_2 = input('Confirm password: ')

#   if passwd == passwd_2:
#     return print(passwd_quality(passwd))
#   else: 
#     return print('Passwords doesnt match.')

# if __name__ == '__main__':
#   main()



# Exercise 103: Random Good Password
def goodpasswd() -> str:
    '''Generates random good password in 8-10 characters'''

    attempts = 0
    passwd = ''

    while not passwd_quality(passwd):
      passwd = random_passwd()
      attempts += 1

    result = f'Generated password below \n{passwd}  \nNumber of attempts - {attempts}'
    return result

# def main():
#     return print(goodpasswd())

# if __name__ == '__main__':
#     main()



# Exercise 104: Hexadecimal and Decimal Digits
def int2hex(x: int) -> str:
  '''Coverts decimal to HEX number (limited in 0-15)'''
  
  if x in range(0, 16):
    hexnumbers = '_0123456789ABCDEF'
    result = hexnumbers[x]
    return result
  else:
    return 'ERROR, out of range'

def hex2int(hex: str) -> int:
  '''Converts HEX numbers to decimal (unlimited)'''
  
  converted = []
  
  #Converting letters A-F to numbers and adding all to list 'converted'
  for i in hex:  
    if i not in '0123456789ABCDEFabcdef':
      raise ValueError('Bad number')
    elif i.isdigit():
      converted.append(int(i))
    else:
      if i == 'A' or i == 'a': converted.append(10) 
      elif i == 'B' or i == 'b': converted.append(11) 
      elif i == 'C' or i == 'c': converted.append(12)
      elif i == 'D' or i == 'd': converted.append(13)
      elif i == 'E' or i == 'e': converted.append(14)
      elif i == 'F' or i == 'f': converted.append(15)
  
  result = 0
  length = len(converted)
  
  for i in range(0, length):
    x = converted[i]
    power = length - i - 1
    adding = x*(16**power)
    result += adding 
  
  return result

# def main():   #currently working for hex2int
#   user_input = input('Enter HEX number >> ')
#   result = hex2int(user_input)
#   return print(f'Decimal number for HEX {user_input} is {result}')

# if __name__ == '__main__':
#     main()


# Exercise 106: Days in a Month
def daysinmonth(month: int, year: int) -> int:
    '''Retruns the number of days in a month in a year.'''
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 0


# def main():
#     month = int(input('Enter a month (1-12): '))  
#     year = int(input('Enter a year: '))
#     days = daysinmonth(month, year)
#     print(f'There are {days} days in month {month} of year {year}.')


# if __name__ == '__main__':
#     main()




# Exercise 107: Reduce a Fraction to Lowest Terms    
def reducefraction(a: int, b: int):
    '''Reduces fraction to lower values\n 
    Example - 10/15 = 2/3'''
    
    if is_prime(a) or is_prime(b):
        return f'{a}/{b}'
    else:
        result1 = primefactors(a)
        result2 = primefactors(b)
        
        x = 1
        y = 1
        
        for num in result1:
            x *= num
        
        for num in result2:
            y *= num

        for num in result1:
            if num in result2:
                x //= num
                y //= num

        return f'{x}/{y}'


def main():
    print('a/b')
    a = int(input('Enter value of a: '))
    print(f'{a}/b')
    b = int(input('Enter value of b: '))
    print(f'Reduced fraction is {reducefraction(a, b)}')


if __name__ == '__main__':
    main()