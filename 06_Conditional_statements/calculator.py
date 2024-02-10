from math import sqrt, pi


# Simple calculator
# a = float(input('Enter first number > '))
# operator = input('Enter operator [ + / - * ] > ')
# b = float(input('Enter second number > '))

# if operator == '+': print(a + b)
# elif operator == '-': print(a - b)
# elif operator == '*': print(a * b)
# elif operator == '/': print(a / b)
# else: print('Unknown operator')

# match operator:
#     case '+': print(a + b)
#     case '-': print(a - b)
#     case '*': print(a * b)
#     case '/': print(a / b)
#     case _: print('Unknown operator')


# pythonic calculator ))
# print(eval(input('Enter statement: ')))



# Calculator
main_menu = '''1. Numeric
2. Geometric
3. Temperature'''

print('Simple Calculator'.center(50, '-'))
print('_'*50)
print(main_menu)

user_choice = input('Select > ')

if user_choice == '1':
    a = float(input('Enter first number > '))
    operator = input('Enter operator [ + / - * ] > ')
    b = float(input('Enter second number > '))

    if operator == '+': print(a + b)
    elif operator == '-': print(a - b)
    elif operator == '*': print(a * b)
    elif operator == '/': print(a / b)
    else: print('Unknown operator')

elif user_choice == '2':
    geometric_menu = "1. Rectangle\n2. Triangle\n3. Circle\n"
    user_choice = input(geometric_menu + 'Select > ')

    if user_choice == '1':
        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))

        area = round(a * b, 2)
        print(area, 'm^2')
    elif user_choice == '2':
        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))
        c = float(input('Enter third side: '))

        p = (a + b + c) / 2
        area = round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)    # formula Herona

        print(area, 'm^2')
    elif user_choice == '3':
        radius = float(input('Enter radius of circle: '))
        area = round(pi * radius ** 2, 2)
        print(area, 'm^2')
    else:
        print('Please enter 1 or 2 or 3')
elif user_choice == '3':
    temperature_menu = '1. Celsius to Fahrenheit\n2. Fahrenheit to celsius\n'
    user_choice = input(temperature_menu + 'Select > ')

    if user_choice == '1':
        celsius = float(input('Enter temperature in celsius: '))
        fahrenheit = round(celsius * (9 / 5) + 32, 2)

        print(fahrenheit, 'F')
    elif user_choice == '2':
        fahrenheit = float(input('Enter temperature in fahrenheit: '))
        celsius = round((fahrenheit - 32) * (5 / 9), 2)

        print(celsius, 'C')
    else:
        print('Please enter 1 or 2')
else:
    print('Please enter 1 or 2 or 3')