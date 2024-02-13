import random

class House:
    def __init__(self):
        self.food = 50
        self.money = 0


class Human:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.satiety += 10
            print(f"{self.name} ate. Satiety: {self.satiety}, Food left: {self.house.food}")
        else:
            print(f"{self.name} has no food to eat.")

    def work(self):
        self.satiety -= 10
        self.house.money += 10
        print(f"{self.name} worked. Satiety: {self.satiety}, Money earned: {self.house.money}")

    def play(self):
        self.satiety -= 10
        print(f"{self.name} played. Satiety: {self.satiety}")

    def go_to_store(self):
        if self.house.money >= 20:
            self.house.money -= 20
            self.house.food += 20
            print(f"{self.name} went to the store. Money left: {self.house.money}, Food bought: {self.house.food}")
        else:
            print(f"{self.name} doesn't have enough money to buy food.")

    def live_one_day(self):
        roll = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_to_store()
        elif self.house.money < 50:
            self.work()
        elif roll == 1:
            self.work()
        elif roll == 2:
            self.eat()
        else:
            self.play()

        if self.satiety <= 0:
            print(f"{self.name} has died of hunger.")
            return False

        return True


# Creating a shared house and two people living in it
shared_house = House()
artyom = Human("Artyom", shared_house)
alex = Human("Alex", shared_house)

# Simulating 365 days
for day in range(1, 366):
    print(f"Day {day}")
    if not artyom.live_one_day():
        break
    if not alex.live_one_day():
        break

# Final state of the house and inhabitants
print("\nFinal State:")
artyom.eat()
alex.eat()
print(f"House: Food {shared_house.food}, Money {shared_house.money}")


