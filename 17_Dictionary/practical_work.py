# ex.4
# store = {
#     'iphone': 999,
#     'ipad': 1999,
#     'macbook': 2999,
#     'imac': 3999
# }
#
#
# for product, price in store.items():
#     print(f"{product:^10}: {price:>10}$")
#
#
#
# while product_name := input('Enter product: ').split():
#     quantity = int(input('Enter quantity: '))
#
#     # total = store[product_name] * quantity
#     total = store.get(product_name, 0) * quantity
#     print(total, '$')
#
# product_name, quantity = input('Enter product name and quantity seperated by a space: ').split()
# print(product_name, int(quantity))


# ex.8
def is_poly(text: str) -> bool:
    # d = {letter: text.count(letter) for letter in text}
    #
    # return len([value for value in d.values() if value % 2 != 0]) <= 1

    d = dict()

    for letter in text:
        d[letter] = text.count(letter)

    l = []
    for value in d.values():
        if value % 2 != 0:
            l.append(value)

    length = len(l)

    if length > 1:
        return False
    return True



# s = 'abcd'
# l = list(s)
# new = ''.join(l)
# print(new)


# l = ['a', 'b', 'c']
# s = ''.join(l)
# print(s)




# ex.137
from random import randint

def dice() -> None:
    sums = list(range(2, 13))
    data = dict.fromkeys(sums, 0)

    for _ in range(100000):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        dices = dice1 + dice2
        data[dices] += 1

    data = {key: value / 1000 for key, value in data.items()}
#
    l = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    print(f"{'Исход':>5}{'Процент симуляции':>5}{'Ожидаемый процент':>5}")
    for i, key, value in enumerate(data.items()):
        print(f"{i:>5}{key:>5}{l[i]:>5}")


dice()