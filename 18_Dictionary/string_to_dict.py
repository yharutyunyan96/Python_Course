# s = 'a,2,b,5,c,8,a,4,e,11'
# l = [int(i) if i.isdigit() else i for i in s.split(',')]
#
# d = {}
# for i in range(0, len(l), 2):
#     if l[i] in d:
#         d[l[i]] += l[i+1]
#     else:
#         d[l[i]] = l[i+1]

# print(d)
# digits = []
# alphas = []
# for char in s.split(','):
#     if char.isdigit():
#         char = int(char)
#         digits.append(char)
#     else:
#         alphas.append(char)
# print(digits)
# print(alphas)

# d = dict(zip(alphas, digits))
# print(d)

# s = 'a,2,b,5,c,8,a,4,e,11'
# s = s.split(',')
# dict_1 = {}
# for i in range(0, len(s), 2):
#     if s[i] in dict_1:
#         dict_1[s[i]] += int(s[i + 1])
#     else:
#         dict_1[s[i]] = int(s[i + 1])

# print(dict_1)