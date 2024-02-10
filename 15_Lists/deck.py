from random import shuffle


def generate_deck() -> list:
    SUITS = ['s', 'h', 'd', 'c']
    VALUES = ['2', '3', '4', '5', '6', '7', '8',
              '9', '10', 'J', 'Q', 'K', 'A']

    deck = [value + suit for suit in SUITS for value in VALUES]

    return deck

def shuffle_deck(deck: list) -> None:
    # first_half = deck[:26]
    # second_half = deck[26:]
    #
    # shuffled_deck = []
    #
    # for i in range(len(first_half)):
    #     shuffled_deck.append(first_half[i])
    #     shuffled_deck.append(second_half[i])
    #
    #
    # return shuffled_deck
    shuffle(deck)




def deal(players: int, cards: int, deck: list) -> list:

    shuffle_deck(deck)

    hands = [[] for _ in range(players)]
    for i in range(cards):
        for j in range(players):
            card = deck.pop()
            hands[j] += [card]

    return hands


# deck = generate_deck()
# game = deal(36, 1, deck)
# print(game)