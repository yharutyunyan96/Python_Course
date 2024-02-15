class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Parent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)


class Citizen(Parent, Person):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country


citizen = Citizen('Alex', 25, 'USA')

print(citizen.country)
citizen.add_child('Bob')
print(citizen.childs)

print(citizen.__dict__)