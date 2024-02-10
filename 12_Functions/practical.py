# Exercise 69: Admission Price
# guest_age = 0
# price = 0
# guest_quantity = 1
#
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


# ex.88 median of three numbers
def median(a, b, c):
    # if a < b < c or c < b < a: return b
    # elif b < a < c or c < a < b: return a
    # else: return c
    #
    # return sorted([a, b, c])[1]

    # l = [a, b, c]
    # return sum(l) - min(l) - max(l)

    if a in range(b, c+1) or a in range(c, b+1): return a
    elif b in range(a, c+1) or b in range(c, a+1): return b
    else: return c

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))
# med = median(a, b, c)
# print(med)

# ex. 95
import string

def text_to_upper(s: string) -> string:
    """
    :param s: The given text
    :return: Converted text
    """
    changed_s = ''
    for i in range(len(s)):
        if i == 0:
            changed_s += s[i].upper()
        elif s[i] == 'i' and s[i-1] == ' ' and (s[i+1] == ' ' or s[i+1] in string.punctuation):
            changed_s += s[i].upper()
        elif s[i-2] in '.?!' and i - 2 > 0:
            changed_s += s[i].upper()
        else:
            changed_s += s[i]
    return changed_s

# text = "what time do i have to be there? what's the address? this time i'll try to be on time!"
# res = "What time do I have to be there? What's the address? This time I'll try to be on time!"
# changed_text = text_to_upper(text)
# print(changed_text == res)


def precedence(operator):
    return 1 if operator in '+-' else 2 if operator in '/*' else 3 if operator == '^' else -1

# print(precedence('?'))