from string import ascii_lowercase

message = input('Enter message: ')
shift = int(input('Enter shift: '))
alphabet = ascii_lowercase * 2

code = ''

for letter in message:
    code += alphabet[alphabet.index(letter) + shift]

print(code)