class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def speak(self, message):
        return f"{self.name} says: {message}"


class Parent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return super().__str__() + "(Родитель)"

    def __len__(self):
        return len(self.children)

    def __reversed__(self):
        return reversed(self.children)

    def raise_children(self):
        return f"{self.name} работает."


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return super().__str__() + " (ребенок)"

    def play(self):
        return f"{self.name} читает"

    def __add__(self, other):
        return f"{self.name} и {other.name} читают  вместе"


class Grandfather(Parent):
    def __str__(self):
        return super().__str__() + " (дедушка)"

    def tell_story(self):
        return f"{self.name} рассказывает историю"

class Grandmother(Parent):
    def __str__(self):
        return super().__str__() + " (бабушка)"

    def cook_pie(self):
        return f"{self.name} готовит пирог"


class Family:
    def __init__(self, family_name):
        self.family_name = family_name
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def __str__(self):
        return f"Family: {self.family_name}, Members: " + ', '.join(str(member) for member in self.members)



father = Parent("Коля", 55)
mother = Parent("Людмила", 52)
son = Child("Юра", 31)
daughter = Child("Яна", 27)
grandfather = Grandfather("Василий", 87)
grandmother = Grandmother("Анна", 86)


father.add_child(son)
father.add_child(daughter)
mother.add_child(son)
mother.add_child(daughter)


family = Family("Family")
family.add_member(father)
family.add_member(mother)
family.add_member(grandfather)
family.add_member(grandmother)
family.add_member(son)
family.add_member(daughter)


print(family)
print(grandfather.tell_story())
print(grandmother.cook_pie())
print(son.play())
print(father.raise_children())