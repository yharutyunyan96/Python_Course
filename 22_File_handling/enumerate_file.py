input_file = input('Enter input filename: ')
output_file = input('Enter output file name: ')

with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
    output_file.writelines([f'{i+1}: {line}' for i, line in enumerate(input_file.readlines())])
    
    
# for i, text in enumerate(('a', 'b', 'c','d'), 1):
#     print(i, text)
