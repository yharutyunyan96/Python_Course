# while loops
# import time
#
# pin = input('Enter Pin: ')
# retries = 3     # keep counter
#
# while pin != '1793':
#     retries = retries - 1   # retries -= 1
#     if retries == 0:
#         print('You are blocked 60 seconds.')
#         time.sleep(60)
#     print('Try again.')
#     pin = input('Enter Pin: ')


# infinity loop
# while True:
#     print('type Ctrl-C to stop me.')


# break statement
# n = int(input('Enter number: '))
# i = 2
# while i < n // 2:
#     if n % i == 0:
#         print(f"{i} * {n//i} = {n}")
#         break
#     i += 1
# else:
#     print(f"{n} is prime")


# continue statement
# while True:
#     pin = input('Enter Pin: ')
#     if pin != '1793':
#         print('Invalid Pin.')
#         continue
#     print('Welcome')
#     break


# i = 1
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)


# nested loops
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(f"{(i*j):4d}", end='')
#         j += 1
#     print()
#     i += 1


# ex.1
# num = int(input('Enter number: '))
# count = 0
# my_sum = 0
# evens_count = 0
# odds_count = 0
#
# while num != 0:
#     last = num % 10
#
#     if last % 2 == 0:
#         evens_count += 1
#     else:
#         odds_count += 1
#
#     num = num // 10
#     count = count + 1
#     my_sum = my_sum + last
#
# print(count)
# print(my_sum)
# print(evens_count)
# print(odds_count)

# ex. 8
# fibonacci series
# a, b = 0, 1
# n = int(input('Enter number: '))
# while a < n:
#     print(a, end=' ')
#     a, b = b, a+b

# ex.1
# n = int(input('>>> '))
# if n == 0:
#     print('First entered number must be not zero.')
# else:
#     my_sum = 0
#     count = 0
#     while n:
#         my_sum += n
#         count += 1
#         n = int(input('>>> '))
#
#     average = my_sum / count
#     print(average)
