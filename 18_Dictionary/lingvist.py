# def lingvist(s):
#     # return {char: s.count(char) for char in s}
#     d = {}
#     for i in range(len(s)):
#         if s[i] not in d:
#             count = 1
#             for j in range(i+1, len(s)):
#                 if s[i] == s[j]:
#                     count += 1
#             d[s[i]] = count
#         else:
#             continue
#     return d
#
# d = lingvist('aabcdsas')
# print(d)