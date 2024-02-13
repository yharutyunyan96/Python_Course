class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, enemy):
        enemy.health -= 20
        print(f"{self.name} attacks! {enemy.name} now has {enemy.health} health points left.")

    def is_alive(self):
        return self.health > 0


def fight(warrior1, warrior2):
    while warrior1.is_alive() and warrior2.is_alive():
        warrior1.attack(warrior2)
        if warrior2.is_alive():
            warrior2.attack(warrior1)

    if warrior1.is_alive():
        print(f"{warrior1.name} has won the fight!")
    else:
        print(f"{warrior2.name} has won the fight!")


# Creating two warriors
warrior1 = Warrior("Warrior 1")
warrior2 = Warrior("Warrior 2")

# Starting the fight
fight(warrior1, warrior2)
