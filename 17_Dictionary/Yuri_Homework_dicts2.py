'''------------------|  DICT EXERCICES  |------------------'''
'''---------------|18/01/2024 - 20/01/2024|----------------'''

# Exercise 136: Reverse Lookup
def reverseLookup(dicti: dict, value) -> list:
    '''Return list of keys that have values of given value'''
    listik = [key for key, val in dicti.items() if val == value]
    return listik


# def main():
#     heraxos_dict = {
#         'Samsung':    15,
#         'Google':     5,
#         'Blackberry': 8,
#         'Realme':     15,
#         'Iphone':     10,
#         'Nokia':      10,
#         'Vivo':       5,
#         'Xiaomi':     35,
#         'HP':         4,
#         'Huawei':     6,
#         'Dorado':     1,
#         'LG':         10}
#     value = 10
#     print(reverseLookup(heraxos_dict, value))

    
# if __name__ == '__main__':
#     main()



# Exercise 137: Two Dice Simulation
from random import randint
def dice():
    
    # totallist = list(range(2, 13))
    dicti = {n: 0 for n in range(2, 13)}
    for _ in range(1000):
        dice_1 = randint(1, 6)
        dice_2 = randint(1, 6) 
        x = dice_1 + dice_2
        dicti[x] += 1
    dicti = {key: value/10 for key, value in dicti.items()}
    return dicti


# def main():
#     print("{:<8} {:<14}".format("Total", "Simulated"))
#     print("{:<8} {:>9}".format("", "Percent"))
#     for key, value in dice().items():
#         print("{:>5} {:>12.2f}".format(key, value))


# if __name__ == '__main__':
#     main()



# Exercise 138: Text Messaging
from string import ascii_lowercase
user_input = 'Hello, World!' #input('Write messege').lower()
user_input = user_input.lower()

dicti = {
    1: '.,?!:',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: ' ',
}

output = ''
for tar in user_input:
    for key, val in dicti.items():
        if tar in val:
            n = val.find(tar) + 1
            output += str(key) * n
            break

# print(output)



# Exercise 139: Morse Code
# dicti = {
#     'A': '.-',   'J': '.---', 'S': '...',   '1': '.----',
#     'B': '-...', 'K': '-.-',  'T': '-',     '2': '..---',
#     'C': '-.-.', 'L': '.-..', 'U': '..-',   '3': '...--',
#     'D': '-..',  'M': '--',   'V': '...-',  '4': '....-',
#     'E': '.',    'N': '-.',   'W': '.--',   '5': '.....',
#     'F': '..-.', 'O': '---',  'X': '-..-',  '6': '-....',
#     'G': '--.',  'P': '.--.', 'Y': '-.--',  '7': '--...',
#     'H': '....', 'Q': '--.-', 'Z': '--..',  '8': '---..',
#     'I': '..',   'R': '.-.',  '0': '-----', '9': '----.'}

# user_input = 'Hello World!' #input('Write messege: ')
# user_input = user_input.upper()
# morse_code = ''

# for tar in user_input:
#     if tar in dicti:
#         morse_code += dicti[tar] + ' '

# print(morse_code)



# Exercise 140: Postal Codes
# dicti = {
#     'Newfoundland':          'A',
#     'Nova Scotia':           'B',
#     'Prince Edward Island':  'C',
#     'New Brunswick':         'E',
#     'Quebec':                'GHJ',
#     'Ontario':               'KLMNP',
#     'Manitoba':              'R',
#     'Saskatchewan':          'S',
#     'Alberta':               'T',
#     'British Columbia':      'V',
#     'Nunavut':               'X',
#     'Northwest Territories': 'X',
#     'Yukon':                 'Y'
# }
# valid_letters = ''
# for tar in dicti.values():
#     valid_letters += tar

# user_input = 'X0j' #input('Enter postal code: ')

# payman = user_input[0].isdigit() or user_input[0].islower() or user_input[0] not in valid_letters or not user_input[1].isdigit()

# if payman: 
#     print('Invalid postal code.')
# else:
#     taracqlist = []
#     taracq = ''
#     for key, value in dicti.items():
#         if user_input[0] in value:
#             taracqlist.append(key)
#     if len(taracqlist) > 1:
#         for i in range(len(taracqlist)):
#             if i == 0:
#                 taracq += taracqlist[i]
#             else:
#                 taracq += ' or ' +  taracqlist[i]
#     else:
#         taracq = taracqlist[0]
#     if user_input[1] == '0': second = 'rural' 
#     else: second = 'urban' 

#     print(f'Postal code is for a {second} adress in {taracq}.')



# Exercise 141: Write out Numbers in English
def num_to_words(num: int) -> str:
    '''Return word implementation of nums 0-999'''
    if num < 0 or num > 999:
        return f'{num} not supported yet'
    
    x1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
          6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    x2 = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 
          60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    harurner = num // 100 * 100
    taser = (num % 100) // 10 * 10
    tver = num % 10
    result = ''

    if harurner == 0:
        pass
    else:
        a = harurner // 100
        for key, val in x1.items():
            if a == key:
                result += val + ' hundred '
                break

    if taser == 0:
            pass
    else:
        for key, val in x2.items():
            if taser == key:
                result += val + ' '
                break

    if tver == 0:
            pass
    else:
        for key, val in x1.items():
            if tver == key:
                result += val
                break

    return result if result else 'zero'


if __name__ == '__main__':
    num = int(input('Enter number 1-999 >> '))
    print(num_to_words(num))



# Exercise 142: Unique Characters
# user_input = input('Write something: ')
# unique = len(set(user_input))
# print(f'{unique} unique characters')



# Exercise 143: Anagrams
# user_input1 = 'evil' #input('Enter first word >> ')
# user_input2 = 'live' #input('Enter second word >> ')

# list1 = sorted([i for i in user_input1])
# list2 = sorted([i for i in user_input2])

# print(list1 == list2)



# Exercise 144: Anagrams Again - # capitalization and spacing are ignored
# user_input1 = 'I am a weakish speller' #input('Enter first something >> ')
# user_input2 = 'William Shakespeare' #input('Enter second something >> ')

# list1 = sorted([i.lower() for i in user_input1 if i != ' '])
# list2 = sorted([i.lower() for i in user_input2 if i != ' '])

# print(list1 == list2)



# Exercise 145: Scrabble™ Score
dicti = {# points - letters
           1:       ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
           2:       ['D', 'G'],
           3:       ['B', 'C', 'M', 'P'],
           4:       ['F', 'H', 'V', 'W', 'Y'],
           5:       ['K'],
           8:       ['J', 'X'],
           10:      ['Q', 'Z']}

user_input = input('Enter a word: ')
x = user_input.upper()

score = 0
for tar in x:
    for key, val in dicti.items():
        if tar in val:
            score += key

# print(score)