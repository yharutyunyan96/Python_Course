import time
from random import sample, choice

text = "Hello World!"

for char in text:
    print(char)
    if char == ' ':
        about_break = "'break' statement will be stop the loop"
        about_continue = "'continue' statement will be disable current iteration"
        # about iteration: one working step of the loop
        action = input(about_break + '\n' + about_continue + '\nEnter > ').lower()
        if action in 'continue' or action in 'yes' or action == '1':
            continue
        elif action in 'break' or action in 'nope' or action == '0':
            break
        else:
            print('System access blocked for 60 seconds')
            for second in range(60, 0, -1):
                time.sleep(1)
                print(f"{second} seconds left")
else:
    nicknames = ['Putin', 'Pashinyan', 'Aliev', 'Sahakashvili']
    combs = ['Paper', 'Rock', 'Scissors']
    player_name, pc_name = sample(nicknames, k=2)
    player_points = pc_points = 0
    while True:
        player_choice = input('Rock, Paper, Scissors ? ').capitalize()
        pc_choice = choice(combs)
        print(f"{player_name}: {player_choice} | {pc_choice}: {pc_name}")
        if player_choice not in combs:
            continue
        elif player_choice == pc_choice:
            print("No one. Lets try again!")
            continue
        match (player_choice, pc_choice):
            case ('Rock', 'Scissors') | ('Paper', 'Rock') | ('Scissors', 'Paper'):
                player_points += 1
                print(f"{repr(player_name)} Win")
                print(f"{player_name}: {player_points} | {pc_name}: {pc_points}")
            case _:
                pc_points += 1
                print(f"{repr(pc_name)} Win")
                print(f"{player_name}: {player_points} | {pc_name}: {pc_points}")
        if player_points == 3 or pc_points == 3:
            winner = pc_name if pc_points == 3 else player_name
            print(f'{winner} Win')
            if input('Dou you want to exit: [y/n]\n').lower() == 'y':
                print('Game Over!'.center(50))
                break
            else:
                pc_points = player_points = 0