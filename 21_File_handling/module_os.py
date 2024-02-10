import os

file_name = 'sorted_dict.py'

abs_path = os.path.abspath('.')
abs_path = os.path.abspath('..')
# print(abs_path)

# file_path = os.path.join(abs_path, file_name)
# print(file_path)

files = os.listdir('..')
# print(files)

for file in os.listdir('..'):
    file_path = os.path.join(os.path.abspath('..'), file)
    if os.path.isdir(file_path):
        print(file_path, 'Directory')
    elif os.path.isfile(file_path):
        print(file, 'File')