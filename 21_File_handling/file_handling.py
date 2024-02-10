# file handling
# open(filename, mode, encoding)

# open('example.txt', 'x')

# file = open('example.txt', 'w')
# file.write('Text\n')
# file.write('Test\n')
# file.close()


# file = open('example.txt', 'a', encoding='utf-8')
# file.write('բարև\n')
# file.close()


f = open('example.txt', 'r', encoding='utf-8')

# for line in f:
#     print(line)

# all_file = f.read()
# all_file = f.read(10)
# print(all_file)

# first_line = f.readline()
# second_line = f.readline(3)
# #
# print(first_line)
# print(second_line)


# all_lines = f.readlines()
# print(all_lines)

# lines = [str(i) + '\n' for i in range(1, 21)]
# file = open('example.txt', 'w', encoding='utf-8')
# file.writelines(lines)
# file.close()


# context manager
# with open('example.txt', 'a', encoding='utf-8') as file:
#     file.write('hello\n')

