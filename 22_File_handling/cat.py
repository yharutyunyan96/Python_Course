import sys

files = sys.argv[1:]
if not files:
    sys.exit('No command line parameters.')
result = ''
for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            result += f.read()
    except Exception as e:
        print(f'{filename}: {e}')

print(result)