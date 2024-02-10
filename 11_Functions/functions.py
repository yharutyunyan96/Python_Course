# functions

# defining functions
def fibonacci(n: int) -> None:
    """Print Fibonacci series up to n."""

    cur_value, next_value = 0, 1

    while cur_value < n:
        print(cur_value, end=' ')
        cur_value, next_value = next_value, cur_value + next_value


# calling functions
# result = fibonacci(400)
# print()
# print(result + 10)

# def fibonacci(n: int) -> list:
#     """Return  Fibonacci series containing on list up to n."""
#
#     result = []
#     cur_value, next_value = 0, 1
#
#     while cur_value < n:
#         result += [cur_value]
#         cur_value, next_value = next_value, cur_value + next_value
#
#     return result


# doc, annotations
# print(fibonacci.__doc__)
# print(fibonacci.__annotations__)


# f100 = fibonacci(100)
# f1000 = fibonacci(1000)
# print(f100)
# print(f1000)

# link
# f = fibonacci
# print(f)
# print(type(f))
# f_500 = f(500)
# print(f_500)
# print(f is fibonacci)

# garbage collector
# x = 7
# y = 7
# x = 10
# y = 11

