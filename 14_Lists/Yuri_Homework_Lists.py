'''LIST EXERCICES'''
'''11/01/2024 - 12/01/2024'''

# Exercise 110: Sorted Order
# a = None
# listik = []
# while a != 0:
#     a = int(input('Enter a number to store in list: '))
#     if a != 0: 
#         listik.append(a)

# sorted_list = sorted(listik)
# print('\nSorted list below')

# for val in sorted_list:
#     print(val)



# Exercise 111: Reverse Order
# a = None
# listik = []
# while a != 0:
#     a = int(input('Enter a number to store in list ("0" to exit): '))
#     if a != 0: 
#         listik.append(a)

# listik.reverse()
# print('\nReversed list below')

# for val in listik:
#     print(val)



# Exercise 112: Remove Outliers
'''LUCUM 1 - list -> sort list -> new sorted list'''
def remove_outliers_sort(list: list, n: int) -> list:
    '''Removes n largest and n smallest values from list
    param: list - given list
    param: n    - number of items to remove
    Returns sorted copy of list'''

    #stugum enq vor hanvox elementneri qanak@ shat chlini u list@ minimum 4 element unena
    if len(list) >= 4 and n > 0 and len(list) > n * 2 + 1:  
        new_list = sorted(list)     # sorted new list
        new_list = new_list[n:-n]   # patrast a
        return new_list
    else:
        raise ValueError('Invalid length of list or slice number')


# def main():
#     listik = [3,2,1, 1245, -25154, -244, 1254]
#     n = 2
#     new_list = remove_outliers_sort(listik, n)
#     print(f'Old list below\n{listik}')
#     print(f'New list below\n{new_list}')


# if __name__ == '__main__':
#     main()


'''LUCUM 2 - list -> new list'''
def remove_outliers(list: list, n: int) -> list:
    '''Removes n largest and n smallest values from list
    param: list - given list
    param: n    - number of items to remove
    Returns copy of list'''

    #stugum enq vor hanvox elementneri qanak@ shat chlini u list@ minimum 4 element unena
    if len(list) >= 4 and n > 0 and len(list) > n * 2 + 1:  
        new_list = list.copy()
        for _ in range(n):
            new_list.remove(max(new_list))
            new_list.remove(min(new_list))
        return new_list
    else:
        raise ValueError('Invalid length of list or slice number')


# def main():
#     listik = [3,2,1, 1245, -25154, -244, 1254]
#     n = 2
#     new_list = remove_outliers(listik, n)
#     print(f'Old list below\n{listik}')
#     print(f'New list below\n{new_list}')


# if __name__ == '__main__':
#     main()



# Exercise 113: Avoiding Duplicates
# a = None
# listik = []
# while a != '':
#     a = input('(leave blank to exit) >>> : ')
#     if a != '' and a not in listik: 
#         listik.append(a)

# print('\nHere is the list')

# for val in listik:
#     print(val)



# Exercise 114: Negatives, Zeros and Positives
# l_negative = []
# l_zeroes = []
# l_positive = []

# while True:
#     a = input('Enter numbers (blank to exit): ')
#     if a == '': 
#         break
#     elif float(a) < 0:
#         l_negative.append(int(a))
#     elif float(a) == 0:
#         l_zeroes.append(int(a))
#     elif float(a) > 0:
#         l_positive.append(int(a))

# result = l_negative + l_zeroes + l_positive
# print('\nNegatives, Zeros and Positives list below')
# print(result)



# Exercise 115: List of Proper Divisors
def proper_divisors(n: int) -> list:
    '''Returns positive 'n' number's proper divisors'''
    
    result = [1]  #1-@ misht mejna 
    for i in range(2, n//2 + 1):
        if n % i == 0:
            result.append(i)
    return result


# def main():
#     n = int(input('Enter a positive number: '))
#     result = proper_divisors(n)
#     print(result)


# if __name__ == '__main__':
#     main()



# Exercise 116: Perfect Numbers
def perfectnumber(n: int) -> bool:
    ''''n' number perfect or not\n
    a number is perfect when the sum of all of the proper divisors of n is equal to n'''
    
    return sum(proper_divisors(n)) == n
         

# def main():  
#     '''identifies and returns perfect number in range: 1 - 10,000'''
    
#     numberslist = []
#     for i in range(1, 10001):
#         if perfectnumber(i):
#             numberslist.append(i)
    
#     return print(numberslist)


# if __name__ == '__main__':
#     main()



# Exercise 117: Only the Words
from string import punctuation
from tarfile import LENGTH_NAME
def onlywordslist(text: str) -> list:
    '''Receives text and returns list of that text words'''
    punct = punctuation + ' '
    listik = []
    bar = ''
 
    for val in text:
        if val not in punct:
            bar += val
        elif len(bar) > 0:
            listik.append(bar)
            bar = ''

    if bar != '':
        listik.append(bar)

    return listik
    
# def main():  
#     text = "Contractions include: don’t, isn’t, and wouldn’t." #input('Write please: ')
#     return print(onlywordslist(text))


# if __name__ == '__main__':
#     main()



# Exercise 118: Word by Word Palindromes
def wordpalindromes(text: str) -> bool:
    '''Checking whether or not the entered string is a word by word palindrome'''
    
    #Converting string into word by word list
    listik = onlywordslist(text)
    #poqratar enq sarqum vor hamematenq elementner@
    listik = [word.lower() for word in listik]
    #reverse enq anum elementner@
    copy_list = listik[::-1]
    
    return listik == copy_list


# def main():  
#     text = "Information school graduate seeks graduate school information"
#     #text = input('Write please: ')
#     return print(wordpalindromes(text))


# if __name__ == '__main__':
#     main()



# Exercise 119: Below and Above Average

# Es 2 funkcianer@ sirunacnelu hamara vor int-i depqum int lcni listi mej, floati depqum float
def is_valid_float(s):
    try:
        _ = float(s)
        return True
    except ValueError:
        return False
    
def is_valid_int(s):
    try:
        _ = int(s)
        return True
    except ValueError:
        return False
    
# num_list = []

# while True:
#     user_input = input('Write numbers (leave blank to quit): ')
#     if user_input == '':
#         break
#     elif not is_valid_float(user_input):
#         user_input = input('Write number!!!! (leave blank to quit): ') 
#     else:
#         if is_valid_int(user_input):
#             num_list.append(int(user_input))
#         else:
#             num_list.append(float(user_input))

# average = sum(num_list) / len(num_list)
# num_list.sort()
# poqrlist = [val for val in num_list if val <= average]
# meclist = [val for val in num_list if val > average]

# print(f'\nAverage of numbers is: {average}')
# print(f'\nBelow average list:\n {poqrlist}')
# print(f'\nAbove average list:\n {meclist}')



# Exercise 120: Formatting a List
def listformatting(x: list) -> str:
    '''Read exercise 120 to understand it'''
    
    lenght = len(x)
    result = ''

    if lenght == 1:
        return x[0]
    elif lenght == 2:
        return x[0] + ' and ' + x[1]
    elif lenght >= 3:
        for i in range(lenght):
            if i < lenght-2:
                result += x[i] + ', '
            elif i == lenght-2:
                result += x[i] + ' and '
            else:
                result += x[i]
        return result
                

# def main():  
#     x = ['apples', 'bananas', 'mandarines', 'sujuxs', 'lemons']
#     #listik = input('Write please: ')
#     return print(listformatting(x))


# if __name__ == '__main__':
#     main()
    


# Exercise 121: Random Lottery Numbers
# from random import randint
# listik = []
# start, end = 1, 49


# for i in range(1, 7):
#     val = randint(start, end)
#     #duplicate checking
#     while True:
#         if val in listik:
#             val = randint(start, end)
#             continue
#         else:
#             listik.append(val)
#             break

# listik.sort()
    
# print(f'Lottery numbers: {listik}')
    


# Exercise 122: Pig Latin
# user_input = 'computer think office algoritm' #input('Write to translate text: ')

# # computer -> omputercay
# # think -> inkthay
# # office -> officeway

# a = 'bcdfghjklmnpqrstvwxyz'
# b = 'aeiou'

# #naxadasutyun@ list enq sarqum
# listik = onlywordslist((user_input))
# newstart = ''
# newend = ''
# result = ''

# for val in listik:
#     if val[0] in a:
#         newend += val[0]
#         for i in range(1, len(val)):
#             if val[i] in a:
#                 newend += val[i]
#             else:
#                 newstart += val[i:]
#                 break
#         result += newstart + newend + 'ay '
#         newstart = ''
#         newend = ''
#     else:
#         result += val + 'way '
        
# print(result)