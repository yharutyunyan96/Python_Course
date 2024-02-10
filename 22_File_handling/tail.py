import sys

if len(sys.argv) != 2:
    sys.exit('File name must be provided as command line parameter.')
    
try:
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        last_ten_lines = ''.join(file.readlines()[-10:])
        print(last_ten_lines)
except FileNotFoundError:
    print('Unknown file.')
except IndexError:
    print('File name must be provided as command line parameter.')