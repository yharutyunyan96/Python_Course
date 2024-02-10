'''------------------|  DICT EXERCICES  |------------------'''
'''---------------|21/01/2024 - 23/01/2024|----------------'''

# Exercise 146 - 148:
from random import shuffle
from time import sleep
from random import sample


def create_card() -> dict:
    '''Creates BINGO loto card, returns cards in dict'''
    
    b_list = sample(range(1, 16), 5)
    i_list = sample(range(16, 30), 5)
    n_list = sample(range(31, 45), 5)
    g_list = sample(range(46, 60), 5)
    o_list = sample(range(61, 75), 5)

    carddict = {
        'B': b_list,
        'I': i_list,
        'N': n_list,
        'G': g_list,
        'O': o_list
        }
    return carddict


def display_card(cards: dict) -> None:
    '''Prints BINGO loto card'''
    
    print('|-------------------------|')
    print('|  B    I    N    G    O  |')
    print('|-------------------------|')
    for b, i, n, g, o in zip(*cards.values()):
        print(f'| {b:2}   {i:2}   {n:2}   {g:2}   {o:2}  |')
    print(' -------------------------')




def random_numlist() -> list:
    '''Creates lists of random numbers in 1-75'''
    
    numlist = list(range(1, 76))
    shuffle(numlist)
    return numlist


def is_win(card: dict) -> bool:
    '''LOTO CARD IS WINNER OR NOT'''
    
    l = list(card.values())

    for i in range(5): 
           #VERTICAL              #HORIZONAL
        if len(set(l[i])) == 1 or l[0][i] == l[1][i] == l[2][i] == l[3][i] == l[4][i]:
            return True
    
    #DIAGONAL
    diag1 = l[0][0] == l[1][1] == l[2][2] == l[3][3] == l[4][4]
    diag2 = l[0][4] == l[1][3] == l[2][2] == l[3][1] == l[4][0]
    return diag1 or diag2
  

def maingamerun():
    '''Run BINGO game'''
    
    cards = create_card()
    park = random_numlist()
    
    print('WELCOME TO BRAK LOTO\n')
    sleep(2)
    print('This is your card\n')
    sleep(1)
    display_card(cards)
    print('\n')
    sleep(3)
    
    while not is_win(cards):
        num = park.pop(0)
        print(f'Number is: {num}')
        print(f'Numbers left: {len(park)}\n')
        
        for values in cards.values():
            if num in values:
                values[values.index(num)] = 0
        
        display_card(cards)
        print()
        sleep(1.5)
        
    print('GAME OVER')

if __name__ == '__main__':
    maingamerun()
