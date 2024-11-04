class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        return f'The engine of the {self.year} {self.make} {self.model} is started'
    def __str__(self):
        return f'{self.year} {self.make} {self.model} in {self.color}'

car1 = Car ('Audi' , 'A7', 2022, 'black')
print(car1)
print(car1.start())
