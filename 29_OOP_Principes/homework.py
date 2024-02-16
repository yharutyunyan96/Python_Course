class Tribute:
    def __init__(self, apartment, car, country_house):
        self.apartment = apartment
        self.car = car
        self.country_house = country_house


class Property(Tribute):
    def __init__(self, apartment, car, country_house):
        super().__init__(apartment, car, country_house)

    def Summa(self):
        return apartment / 1000 + car / 200 + country_house / 500


apartment = int(input('Enter the price of the apartment։ '))
car = int(input('Enter the price of the car: '))
country_house = int(input('Enter the price of the CountryHouse: '))
money = int(input('Enter your balance: '))
summa = Property(apartment, car, country_house).Summa()
if summa > money:
    print(f"Insufficient funds։Sorry, you cannot list your property։You need {(abs(summa-money))}")
else:
    print(f"Stayed with you {money-summa} price")
