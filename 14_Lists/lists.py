# create empty list
# empty = []
# empty = list()
# print(type(empty))


# list can contain heterogeneous objects
# def f():
#     pass #Todo
    # ... # elipsis

# a, b, c = 6, 7, 8
# l = [5, 5.0, 'abc', True, [1, 2, 3], f, a, b, c]

# indexing, sliceing
# l = [1, 2, 'abc', [5, 6, 7]]
# pre_last = l[3][1]
# first_two_elems = l[:2]
# print(pre_last)
# print(first_two_elems)


# mutable data types vs immutable
# s = 'abcd'
# l = list(s)

# s[0] = 'g'    # TypeError
# l[0] = 'g'
# print(l)


# s1 = 'abc'
# s2 = 'abc'
# print(s1 == s2)
# print(s1 is s2)

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l2 = l1
# print(l1 == l2)
# print(l1 is l2)
# print(id(l1))
# print(id(l2))


# list methods
#adding
# l = ['a', 'b', 'c']

# l.append('d')
# l.insert(0, 'e')
# l[2:2] = 't'

# l2 = ['f', 'g']
# s = 'fghi'
# l.extend(l2)
# l.extend(s)
# l += ['y']
# print(l)

# removing
l = ['a', 'b', 'c']
# l.remove('a')
# first = l.pop(0)
# del l[0]
# l[0:2] = []
# l.clear()

# print(l)
# print(first)
# print(type(first))


# count, index
# l = ['a', 'b', 'c', 'a']
# idx_a = l.index('a', 1, 10)
# count_a = l.count('a')
# print(count_a)


# reverse, sort
# l = ['dg', 'cas', 'aadsga', 'asA', 'adda1']
# l.sort(key=len, reverse=True)
# l.reverse()
# print(l)

# copy
import copy

# l = ['a', 'b', 'c', ['x', 'y', 'z']]
# l_copy = l.copy()
# l_copy = l[:]
# l_copy = copy.deepcopy(l)

# l_copy[-1][-1] = 'e'
# print(l_copy)
# print(l)


# list comprehensions
# l = []
# for i in range(10):
#     if i % 2 == 0:
#         l.append(i)
#         # l += [i]
#     else:
#         l.append('odd')

# l = [i for i in range(10) if i % 2 == 0]
# l = [i if i % 2 == 0 else 'odd' for i in range(10)]
# print(l)


# nested list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# l = [i for row in matrix for i in row]
# l = []
# for row in matrix:
#     for i in row:
#         l.append(i)

# print(l)