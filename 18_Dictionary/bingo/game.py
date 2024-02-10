from time import sleep
from random import shuffle

from bingo_card import generate_card, show_card
from check_card import is_win

def change_position(card, number):
    for val in card.values():
        if number in val:
            val[val.index(number)] = 0

def game_main_loop(card: dict):
        box = list(range(1, 76))
        shuffle(box)

        print('Welcome to Bingo game, GOOD LUCK!')

        while not is_win(card):
            number = box.pop()
            print(f'Number is {number}')
            change_position(card, number)

            # sleep(2)
            show_card(card)

        print('Has winner!!')


def main():
    card = generate_card()
    game_main_loop(card)

if __name__ == '__main__':
    main()