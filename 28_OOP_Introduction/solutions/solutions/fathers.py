class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
        else:
            print(f"Error: {self.name} is not old enough to be the parent of {child.name}.")

    def provide_information(self):
        info = f"Name: {self.name}, Age: {self.age}, Children: {[child.name for child in self.children]}"
        print(info)

    def calm_child(self, child):
        if child in self.children:
            child.calm = True
            print(f"{self.name} has calmed down {child.name}.")
        else:
            print(f"{child.name} is not a child of {self.name}.")

    def feed_child(self, child):
        if child in self.children:
            child.hungry = False
            print(f"{self.name} has fed {child.name}.")
        else:
            print(f"{child.name} is not a child of {self.name}.")


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True

    def provide_information(self):
        state_of_calm = "calm" if self.calm else "not calm"
        state_of_hunger = "not hungry" if not self.hungry else "hungry"
        info = f"Name: {self.name}, Age: {self.age}, State: {state_of_calm}, {state_of_hunger}"
        print(info)


parent = Parent("John", 40)
child1 = Child("Alice", 8)
child2 = Child("Bob", 5)

parent.add_child(child1)
parent.add_child(child2)

parent.provide_information()
child1.provide_information()
child2.provide_information()

parent.calm_child(child1)
parent.feed_child(child2)

child1.provide_information()
child2.provide_information()
