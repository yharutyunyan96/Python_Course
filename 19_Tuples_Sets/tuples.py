# create tuple

# empty = ()
# empty = tuple()
# print(type(empty))

# single = (1,)
# single = 1,
# print(type(single))

# t = (1, 2, 3, 4)
# t = 1, 2, 3, 4
# u = t, ('a', 'b', 'c')
# z = dict(tuple(zip(t, ('a', 'b'))))
# print(z)
# print(len(u))


# iterate over tuple
# t = 1, 'a', [1, 2, 3], 'b', True
# t[2][0] = 8888
# print(t)
# t[0] = 1
# for elem in t:
#     print(elem)


# unpacking
# t = 'a', 'b', 'c', 'd', 'e', 'f'
# a, *b, c = t
# print(a)
# print(b)
# print(c)


# coordinates = (0, 1)
# coordinates_list = [0, 1]
# print(coordinates.__sizeof__())
# print(coordinates_list.__sizeof__())


# tuple methods
# t = 'a', 'b', 'c', 'a', 'd'
# print(t.index('a', 2, 10))
# print(t.count('a'))
# first_half = t[:len(t)//2]
# print(first_half)

