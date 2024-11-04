class House:
    def __init__(self, floors, area, rooms):
        self.floors = floors
        self.area = area
        self.rooms = rooms

    def calculate(self, price):
       return self.area * price

    def __str__(self):
        return f'Дом с {self.floors} этажами, площадью {self.area} м² и {self.rooms} комнатами'



house1 = House(2, 120, 5)
print(house1)

price = 1000
price1 = house1.calculate(price)
print(f'Стоимость дома: {price1} рублей')