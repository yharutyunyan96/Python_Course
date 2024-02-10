# empty = set()
# print(type(empty))

# s = {1,1,1,1,1,1,2}
# print(s)

# s1 = {'a', 'b', 'c', 'd', 'e'}
#  remove
# print(s1[0]) #TypeError
# s1.pop()
# s1.remove('w')
# s1.discard('w')

# add
# s1.update({1, 2})
# s1.add(4)

# copy
# s1_copy = s1.copy()
# print(s1)

# set methods
# s1 = {'a', 'b', 'c', 'd', 'e'}
# s2 = {'d', 'e', 'f', 'g', 'h'}

# intersection = s1.intersection(s2)
# intersection = s1 & s2
# s1.intersection_update(s2)
# print(intersection)
# print(s1)

# difference = s1.difference(s2)
# differnece = s1 - s2
# s1.difference_update(s2)
# print(difference)
# print(s1)

# symmetric_difference = s1.symmetric_difference(s2)
# symmetric_difference = s1 ^ s2
# s1.symmetric_difference_update(s2)
# print(symmetric_difference)
# print(s1)

# union = s1.union(s2)
# union = s1 | s2
# print(union)


# issuperset, issubset, isdisjoint
# s1 = {'a', 'b', 'c', 'd', 'e'}
# s2 = {'f', 'g'}

# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s1.isdisjoint(s2))


# set comprehension
# s = {i for i in range(1, 9) if i % 2 == 0}
# print(s)

letters = ['s', 'i']
words = 'This is a test of sets'.split()

only = [w for w in words if set(w).issuperset(set(letters))]
avoids = [w for w in words if set(w).isdisjoint(set(letters))]
print(only)
print(avoids)
