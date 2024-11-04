class Person:
    def __init__(self, name, last_name, age, phone_number):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.is_standing = False

    def stand_up(self):
        if not self.is_standing:
            self.is_standing = True
            return f'{self.name} {self.last_name} встает'
        else:
            return f'{self.name} {self.last_name} уже стоит'

    def sit_down(self):
        if self.is_standing:
            self.is_standing = False
            return f'{self.name} {self.last_name} садится'
        else:
            return f'{self.name} {self.last_name} уже сидит'

    def __str__(self):
        return f'{self.name} {self.last_name}, {self.age} years old, Phone: {self.phone_number}'


person1 = Person('Яна', 'Уманцева', 27, '+375292793139')
print(person1)
print(person1.stand_up())
print(person1.sit_down())