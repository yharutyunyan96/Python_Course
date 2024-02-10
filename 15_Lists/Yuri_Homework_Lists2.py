'''LIST EXERCICES'''
'''13/01/2024 - 15/01/2024'''

from string import punctuation

# Exercise 123 - i hamar a
def onlywordslist(text: str) -> list:
    '''Receives text and returns list of that text words'''
    listik = []
    bar = ''
    for val in text:
        if val != ' ':
            bar += val
        elif len(bar) > 0:
            listik.append(bar)
            bar = ''
    if bar != '':
        listik.append(bar)
    return listik


# Exercise 123: Pig Latin Improved
# user_input = 'Computer, think office Algoritm!' #input('Write to translate text: ')

# a = 'bcdfghjklmnpqrstvwxyz' + 'bcdfghjklmnpqrstvwxyz'.upper()
# b = 'aeiou' + 'aeiou'.upper()

# #naxadasutyun@ list enq sarqum
# listik = onlywordslist((user_input))

# newstart = ''
# newend = ''
# punct = ''
# result = ''
# mecatar = False

# for val in listik:
#     upperidx = []
#     for i in range(len(val)):
#         if val[i] in punctuation:
#             punct += val[i]

#     if val[0] in a:
#         if val[0].isupper():
#             newend += val[0].lower()
#             mecatar = True 
#         else:
#             newend += val[0]

#         for i in range(1, len(val)):
#             if val[i] in a:
#                 newend += val[i]
#             elif val[i] in b:
#                 if punct == '':
#                     newstart += val[i:]
#                     break
#                 else:
#                     newstart += val[i:-(len(punct))]
#                     break

#         result += newstart + newend + 'ay' + punct + ' '
#         if mecatar: result = result[0].upper() + result[1:]
#         newstart = ''
#         newend = ''
#         punct = ''
#         mecatar = False
#     else:
#         if punct == '':
#             result += val[:] + 'way' + punct + ' '
#         else:
#             result += val[:-(len(punct))] + 'way' + punct + ' '

# print(result)



# Exercise 124: Line of Best Fit
# x_list = []  
# y_list = []  
# while True:  # stanum enq cordinater@, qanak@ u lcnum listi mej
#     x = input('Enter x cordinate (blank to quit):  ')
#     if x != '':
#         x_list.append(float(x))
#     else:
#         break
#     y = input('Enter y cordinate: ')
#     y_list.append(float(y))

# lenght = len(x_list)

# # mijin tvabanakan x, y
# x_avg = sum(x_list) / lenght
# y_avg = sum(y_list) / lenght

# # x - x mijin, y - y mijin 
# x_mijin = [i - x_avg for i in x_list]
# y_mijin = [i - y_avg for i in y_list]

# x_y = sum([x * y for x, y in zip(x_mijin, y_mijin)])
# qaraksuix = sum([i * i for i in x_mijin])

# m = x_y / qaraksuix
# b = y_avg - m * x_avg

# print(f'\n y = {m:.2f}x + {b:.2f}')



# Exercise 125: Shuffling a Deck of Cards
from random import randint


def createDeck() -> list:
    '''Creates cards deck in 52'''
    mast = ['s', 'h', 'd', 'c']
    qar = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    kalod = [x + y for x in qar for y in mast]
    return kalod


def shuffle(kalod: list):
    '''Shuffles deck'''
    x = []
    
    while kalod:
        x.append(kalod.pop(randint(0, len(kalod)-1)))
        
    return x


# if __name__ == '__main__':
#     print(shuffle(createDeck()))



# Exercise 126: Dealing Hands of Cards

def deal(cards: list, cardsperplayer: int, playernum: int) -> list:
    '''Deals cards per player number and cards per player'''
    
    lriv = [[] for i in range(playernum)]
    
    for _ in range(cardsperplayer):
        for mard in lriv:
            mard.append(cards.pop(randint(0, len(cards)-1)))

    lriv.append(cards)
    return lriv 


# def main():
#     cards = shuffle(createDeck())
#     cardsperplayer = 6
#     playernum = 4
#     x = deal(cards, cardsperplayer, playernum)
    
#     for i in range(playernum):
#         print(f'Hand {i+1} cards - {x[i]}')
#     print(f'\nRemaining cards - {x[-1]}')
    

# if __name__ == '__main__':
#     main()



# Exercise 127: Is a List already in Sorted Order?
def sortedlistornot(listik: list) -> bool:
    '''Determines given list is sorted or not'''
    
    first = listik[0]
    listik.pop(0)

    for tiv in listik:
        if tiv > first:
            first = tiv
        else:
            return False
    return True


# def main():
#     x = None
#     listik = []
#     while x != '':
#         x = input('Enter numbers (blank to exit) >>> ')
#         if x != '':
#             listik.append(float(x))
            
#     print(sortedlistornot(listik))
#     print(listik)


# if __name__ == '__main__':
#     main()