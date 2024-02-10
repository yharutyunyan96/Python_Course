# string

# single quotes
# text = 'I'm a programmer'     # SyntaxError
# text = 'I\'m a programmer'
# text = "I'm a programmer"


# double quotes
# text = "He said "ok""         # SyntaxError
# text = "He said \"ok\""
# text = 'He said "ok"'
# print(text)


'''Python is Fun'''

# long_text = """Python
# is
# Fun"""
#
# print(long_text)


# path = 'C:User\test\pycharmProjects'
# path = r'C:User\test\pycharmProjects'
# print(path)


# string formatting
#concatenation
# text = '5 ' + 'Iphones ' + 'price: ' + '$' + '4999.00'

#
# quantity = int(input('Enter quantity: '))
# product = input('Enter product: ')
# price = float(input('Enter price of product: '))
# total = price * quantity

# text = '%05i %s price: $%.2f'%(quantity, product, total)
# text = '%5d %s price: $%.2f'%(5, 'Iphone', 4999)

# text = '{} {} price: ${}'.format(
#     quantity,
#     product,
#     total
# )


# q = int(input('Enter quantity: '))
# prod = input('Enter product: ')
# p = float(input('Enter price of product: '))
# t = p * q
#
# text = '{quantity} {product} price: ${total}'.format(
#     quantity=q,
#     product=prod,
#     total=t
# )
# print(text)


# f-string  Use Python 3.6 +
# quantity = int(input('Enter quantity: '))
# product = input('Enter product: ')
# price = float(input('Enter price of product: '))
# total = price * quantity
#
# text = f'{quantity:05d} {product:->10} price: ${total:.2f}'
# print(text)


# intro for loops
print(f"+{'+':-^19}+")
print(f"|{'index': ^9}|{'char':^9}|")
print(f"+{'+':-^19}+")
for ascii_index in range(97, 123):
    print(f"|{ascii_index: ^9}|{chr(ascii_index): ^9}|")
print(f"+{'+':-^19}+")