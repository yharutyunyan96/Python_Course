class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {self.age}\n"

class Parent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.childs = []

    def __str__(self):
        return super().__str__() + f"Childs: {self.childs}\n"

    def add_child(self, child):
        self.childs.append(child)


class Citizen(Parent, Person):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    def __str__(self):
        return super().__str__() + f"Country: {self.country}\n"


citizen = Citizen('Alex', 25, 'USA')
print(citizen)

print(Citizen.__mro__)  # method resolution order
