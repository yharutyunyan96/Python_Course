import builtins
import sys

# print(dir(builtins))

# command line parameters
# my_args = sys.argv
# print(my_args)
def fibo(n): return n if n <= 1 else fibo(n-1) + fibo(n-2)

# try:
#     n = int(sys.argv[1])
#     result = fibo(n)
#     print(result)
# except (IndexError, TypeError):
#     print('Parameters must be provided in command line.')
# except ValueError as error:
#     print(error)
#     print('Arguments must be a integer')
# finally:
#     print('Finally block always will be work.')


# try:
#     file = open('document.txt', 'r', encoding='utf-8')
#     print(file.read())
# except FileNotFoundError as error:
#     print(error)
#     print('Creating file.')
#     file = open('document.txt', 'w', encoding='utf-8')
#     lines = [str(i) + '\n' for i in range(1, 21)]
#     file.writelines(lines)
# finally:
#     file.close()
#     print('File is closed.')


# class MyError(BaseException):
#     pass
#
# raise MyError('ERRROR')