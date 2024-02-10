import random
import time

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def __str__(self):
        return self.name

    def attack(self, enemy):
        if isinstance(enemy, Warrior):
            enemy.health -= 20
            print(f"{enemy} attacked by {self.name}")
            print(f"{self.name}: {self.health} | {enemy.name}: {enemy.health}")


def game_main_loop(player1, player2):
    players = [player1, player2]


    while player1.health and player2.health:
        attacker, enemy = random.sample(players, k=2)
        attacker.attack(enemy)
        time.sleep(1)

    winner = player1 if player1.health else player2

    print(f'Winner {winner}')
    print('Game over')


def main():
    player1 = Warrior('Subzero')
    player2 = Warrior('Scorpio')
    game_main_loop(player1, player2)

if __name__ == '__main__':
    main()