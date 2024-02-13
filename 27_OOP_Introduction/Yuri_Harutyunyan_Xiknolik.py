def iswin(l: list) -> bool:
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                    (0, 4, 8), (2, 4, 6)]

    for pattern in win_patterns:
        if l[pattern[0]] == l[pattern[1]] == l[pattern[2]] and l[pattern[0]] != ' ':
            return True
    return False


def update_boardview(b_list):
    boardview = f'''
 _______ _______ _______
|1      |2      |3      |
|   {b_list[0]}   |   {b_list[1]}   |   {b_list[2]}   |
|_______|_______|_______|
|4      |5      |6      |
|   {b_list[3]}   |   {b_list[4]}   |   {b_list[5]}   |
|_______|_______|_______|
|7      |8      |9      |
|   {b_list[6]}   |   {b_list[7]}   |   {b_list[8]}   |
|_______|_______|_______|

'''
    return print(boardview)


def main():
    player_1 = input('Enter player 1 name >> ')
    player_2 = input('Enter player 2 name >> ')

    b_list = [' ']*9

    update_boardview(b_list)

    while ' ' in b_list and not iswin(b_list):
        xik = int(input(f'{player_1}, your move >> '))
        while b_list[xik-1] != ' ':
            xik = int(input(f'{player_1}, Enter correct board number >> '))
        b_list[xik-1] = 'X'
        update_boardview(b_list)

        if iswin(b_list):
            print(f'{player_1} WON GAME!!')
            break

        if ' ' not in b_list:
            print("It's a DRAW!")
            break

        nolik = int(input(f'{player_2}, your move >> '))
        while b_list[nolik-1] != ' ':
            nolik = int(input(f'{player_2}, Enter correct board number >> '))
        b_list[nolik-1] = 'O'
        update_boardview(b_list)

        if iswin(b_list):
            print(f'{player_2} WON GAME!!')
            break

if __name__ == "__main__":
    main()










