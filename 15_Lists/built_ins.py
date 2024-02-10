def my_min(sequence):
    minimum = sequence[0]
    for element in sequence:
        if element < minimum:
            minimum = element

    return minimum

def my_max(sequence):
    maximum = sequence[0]
    for element in sequence:
        if element > maximum:
            maximum = element

    return maximum

def my_sum(sequence):
    _sum = 0
    for element in sequence:
        _sum += element

    return _sum

def my_len(sequence):
    length_of_sequence = 0
    for _ in sequence:
        length_of_sequence += 1

    return length_of_sequence

def my_prod(sequence):
    product = 1

    for elem in sequence:
        product *= elem

    return product
