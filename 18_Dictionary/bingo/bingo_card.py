from random import sample


def generate_card() -> dict:
    """Generate bingo card"""

    card = {
        'B': list(sample(range(1, 15), k=5)),
        'I': list(sample(range(16, 30), k=5)),
        'N': list(sample(range(31, 45), k=5)),
        'G': list(sample(range(46, 60), k=5)),
        'O': list(sample(range(61, 75), k=5)),

    }

    return card


def show_card(card: dict) -> None:
    for char in card:
        print(f"{char:>5}", end='')

    print()
    for i in range(len(card)):
        for val in card.values():
            print(f'{val[i]:>5}', end='')
        print()

def main():
    card = generate_card()
    show_card(card)

if __name__ == '__main__':
    main()