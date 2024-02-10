def is_prime(number: int) -> bool:
    for i in range(2, number//2):
        if number % i == 0:
            return False
    return True

def test(got, expected):
    # prefix = ' OK ' if got == expected else ' X '
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f"{prefix} Got: {repr(got)}, Expected: {repr(expected)}")

def main():
    test(is_prime(7), True)
    test(is_prime(12), False)
    test(is_prime(33), True)

if __name__ == '__main__':
    main()
    print(__name__)