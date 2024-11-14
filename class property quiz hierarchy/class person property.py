class Person:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
         self._age = new_age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
          self._height = new_height


p = Person("Yana", 27, 157)
print(p.name)
print(p.age)
print(p.height)

p.age = 25
p.height = 175
print(p.age)
print(p.height)

p.name = "Maria"
print(p.name)