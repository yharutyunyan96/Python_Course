from functions import var

def count_it(string: str) -> dict:
    import math
    return {int(number): string.count(number) for number in string}


# s = '12454267869764543148635762413'
# result = count_it(s)
# print(result)

print(var)