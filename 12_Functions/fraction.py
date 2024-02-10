# ex107
# կրճատել կոտորակի համարիշն ու հայտարարը

def reduce_fraction(a, b):
    # list_1 = [i for i in range(1, a + 1) if a % i == 0]
    # list_2 = [i for i in range(1, b + 1) if b % i == 0]
    # return str(a // max(set(list_1) & set(list_2))) + '/' + str(b // max(set(list_1) & set(list_2)))


    minimum = a if a < b else b
    i = minimum
    if a == minimum:
        return b
    else:
        return a
    while i:

        if a % i == 0 and b % i == 0:
            return f'{a//i}/{b//i}'
        i -= 1
    return f'{a}/{b}'

    # for i in range(minimum, )



if __name__ == '__main__':
    a = float(input('Write down a numerator. '))
    b = float(input('Write down a denominator. '))
    result = reduce_fraction(a, b)
    print(result)
