def is_strong_password(password: str) -> bool:
    """Password quality checker.

    :param password: Given password to check quality
    :return: True if password is strong else False
    """

    upper = lower = digit = False

    if 8 <= len(password) <= 10:
        for char in password:
            if char.isupper():
                upper = True
            elif char.islower():
                lower = True
            elif char.isdigit():
                digit = True

            if lower and digit and upper:
                return True
    return False


def main():
    pwd = input('Enter password: ')
    if is_strong_password(pwd):
        print('Password is strong.')
    else:
        print('Password is weak.')

if __name__ == '__main__':
    main()