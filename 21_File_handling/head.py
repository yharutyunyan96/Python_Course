import sys

try:
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        print(''.join(file.readlines()[:10]))
except IndexError:
    print('Filename must be provided as command line parameter.')
except FileNotFoundError as msg:
    print(msg)
    print(filename)