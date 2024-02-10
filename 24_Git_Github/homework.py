# import sys

# sys.setrecursionlimit(10000)
# sys.set_int_max_str_digits(100000000000)
# print(10**123421)

# NATO = {
#     "A":"Alpha","B":"Bravo","C":"Charlie","E":"Echo",
#     "F":"Foxtrot","G":"Golf","H":"Hotel","I":"India",
#     "J":"Juliet","K":"Kilo","L":"lima","M":"Mike",
#     "N":"November","O":'Oscar',"P":"Papa","Q":"Quebec",
#     "R":"Romeo","S":"Sierra", "T":"Tango","U":"Uniform",
#     "V":"Viktor","W":"Whiskey","X":"Xray","Y":"Yankee","Z":"Zulu"
# }

# def encode(text: str) -> str:
#     if len(text) == 0:
#         return ''   # base case
    
#     if text[0] in NATO:
#         return NATO[text[0]] + ' ' + encode(text[1:])   # recursive case

# text = input('Enter text to encode: ').upper()

# result = encode(text)
# print(result)

# def isprime(x, a=2):
#     if x < 2:
#         return False
    
#     if x % a == 0:
#         return False
#     if a**2 > x:
#         return True
#     if x % a == 0:
#         return False
#     return isprime(x, a+1)

# print(isprime(13))

# def primefactors(user_input: int, factor=2) -> list:
#     """Return the prime factors of a number."""
#     if user_input < 2:
#         return []

#     if factor * factor > user_input:
#         return [user_input] if user_input > 1 else []

#     if user_input % factor == 0:
#         return [factor] + primefactors(user_input // factor, factor)
    
#     return primefactors(user_input, factor + 1)

# print(primefactors(80))


# n = 3
# ['((()))', '()()()', '(())()', '()(())', '(()())']