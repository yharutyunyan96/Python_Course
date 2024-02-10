class Family:
    def __init__(self, surname, balance):
        self.surname = surname
        self.balance = balance
        self.have_a_house = False

    def earn_money(self, amount):
        self.balance += amount
        print(f'Current balance is: {self.balance}')

    def buy_house(self, house_price, discount=0):
        house_price = house_price - (house_price * discount / 100)
        if self.balance >= house_price:
            self.balance -= house_price
            self.have_a_house = True
            print(f'House is purchased\nCurrent balance ${self.balance}')
        else:
            print(f"You don't have enough money, you are shorter {house_price - self.balance}"
                  "Go earn money!!!")


family = Family('Smith', 500000)

if not family.have_a_house:
    family.buy_house(1000000)
    if not family.have_a_house:
        family.earn_money(400000)
        family.buy_house(1000000, discount=10)