# x = 1
#
# if x:
#     y = 2
#
# print(y)


# num = -5
#
# if num > 0:
#     print('Num is positive.')
#     if num > 5:
#         print('Num is greater then five.')
#         if num % 2 == 0:
#             print('Num is even.')
#         else:
#             print('Num is odd.')
#     elif num == 5:
#         print('Num is five')
#     else:
#         print('Num is lesser than five')
# elif num == 0:
#     print('Num is zero')
# else:
#     print('Num is negative')


# match statements

# language = input('Enter language: ')
#
# match language:
#     case 'Python' | 'Java' | 'PHP':
#         print('Backend')
#     case 'HTML' | 'CSS' | 'JS':
#         print('FrontEnd')
#     case _:
#         print('Unknown language')


# language = input('Enter language: ')
#
# if language == 'Python' or language == 'PHP':
#     print('Backend')
# elif language in 'HTMLCSS':
#     print('FrontEnd')
# else:
#     print('Unknown language')


# response = 404
#
# match response:
#     case 200 | 203 | 204:
#         print('Ok')
#     case 400 | 404 | 406:
#         print('Page not found.')
