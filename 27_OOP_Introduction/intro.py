# store info about user
user = ('Alex', 25, False)

user = ['Alex', 25, False]

user = {
    'name': 'Alex',
    'age': 25,
    'is_banned': False
}

# creating class
class User:
    # constructor method
    def __init__(self, fullname, age):
        self.name, self.surname = fullname.split()
        self.age = age
        self.is_banned = False

    def show_info(self):    # method
        print(f"Name: {self.name}\tAge: {self.age}\tIs banned: {self.is_banned}")

# creating instance of class
user1 = User('Alex Smith', 25)
user2 = User('Bob Johnson', 30)

# print(user1.is_banned)
# user2.is_banned = True
# print(user2.is_banned)

# print(user1.name)
# print(user2.surname)

user1.show_info()
user2.show_info()

print(user1.__dict__)
print(user1.surname)