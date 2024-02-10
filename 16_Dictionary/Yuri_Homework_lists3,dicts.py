'''LIST EXERCICES'''
'''17/01/2024 - 18/01/2024'''

# Exercise 128: Count the Elements
def countRange(listik: list, min: float, max: float) -> int:
    '''Determine and return the number of elements in list that are greater than or equal min and max'''

    qanak = 0
    for tiv in listik:
        if min <= tiv <= max:
            qanak += 1
    return qanak


# def main():
#     listik = [-0.151, -842, 15, 20, 3, 4, 5, 6, 8, 9, 10]
#     minimum = 5.15
#     maximum = 10.001
#     print(countRange(listik, minimum, maximum))


# if __name__ == '__main__':
#     main()



# Exercise 129: Tokenizing a String
def tokenList(s: str) -> list:
    '''Returns list of tokens in given mathematical expression string "s"'''
    
    nshanner = ['+', '-', '*', '/', '^', '(', ')']
    listik = []
    lenn = len(s)
    i = 0
    x = ''
    
    while i < lenn:
        if s[i] in nshanner:
            listik.append(s[i])
            i += 1
        elif s[i] == ' ':
            i += 1
        elif s[i].isdigit():
            while i < lenn and s[i].isdigit():
                x += s[i]
                i += 1
            listik.append(x)
            x = ''
                
    return listik


# def main():
#     user_input = '100 + 500 + (1 / 1)' #input('Enter mathematical expression: ')
#     print(tokenList(user_input))


# if __name__ == '__main__':
#     main()



'''------------------|  DICT EXERCICES  |------------------'''

# Задание 1. Песни — 2
# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83}

# qanak = i = int(input('How many songs? '))
# jamanak = 0
# while i > 0:
#     anun = input(f'Enter name of the song {qanak - i + 1}: ')
#     i -= 1
#     jamanak += violator_songs[anun]

# print(f'Total time of songs - {jamanak} minutes')



# Задание 2. Криптовалюта
# import pprint
# data = {"address": "0x544444444444",
    
# "ETH": {"balance": 444,
# "totalIn": 444,
# "totalOut": 4},
    
# "count_txs": 2,
    
# "tokens": [
# {"fst_token_info": 
# {"address": "0x44444",
# "name": "fdf",
# "decimals": 0,
# "symbol": "dsfdsf",
# "total_supply": "3228562189",
# "owner": "0x44444",
# "last_updated": 1519022607901,
# "issuances_count": 0,
# "holders_count": 137528,
# "price": False},
 
# "balance": 5000,
# "totalIn": 0,
# "total_out": 0},
    
# {"sec_token_info": {
# "address": "0x44444",
# "name": "ggg",
# "decimals": "2",
# "symbol": "fff",
# "total_supply": "250000000000",
# "owner": "0x44444",
# "last_updated": 1520452201,
# "issuances_count": 0,
# "holders_count": 20707,
# "price": False
# },
# "balance": 500,
# "totalIn": 0,
# "total_out": 0
# }
# ]
# }

#1
# keys = data.keys()
# values = data.values()
# #2
# data['ETH']['total_diff'] = 100
# #3
# data['tokens'][0]['fst_token_info']['name'] = 'doge'
# #4
# del data['tokens'][0]['total_out'], data['tokens'][1]['total_out']
# data['tokens'][0]['total_out'] = data['tokens'][1]['total_out'] = data['ETH']['total_diff']
# #5
# data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

# pprint.pprint(data)



# Задание 3. Товары
goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',}

store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
}

obshi_gin = 0
qanak = 0
mek = 0

for key in goods:
    x = goods[key]

    print(f'{key}:')

    for i in range(len(store[x])):
        obshi_gin += store[x][i]['quantity'] * store[x][i]['price']
        qanak += store[x][i]['quantity']

    print(f'{qanak} hat, obshi gin {obshi_gin}')
    obshi_gin = 0
    qanak = 0