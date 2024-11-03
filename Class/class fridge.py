class Fridge:
    def __init__(self, production, capacity, model):
        self.production = production
        self.capacity = capacity
        self.model_name = model
        self.is_open = False

    def open_door(self):
        if not self.is_open:
            self.is_open = True
            return f'The door of the {self.model_name} is opened'
        else:
            return f'The door of the {self.model_name} is already opened.'

    def close_door(self):
        if self.is_open:
            self.is_open = False
            return f'The door of the {self.model_name} is closed'
        else:
            return f'The door of the {self.model_name} is already closed.'

    def turn_on(self):
        return f'The {self.model_name} is now turned on'

    def __str__(self):
        return f'{self.production} {self.model_name}, capacity: {self.capacity} liters'

fridge1 = Fridge('ATLANT', 393, 'ХМ-4626-101-NL')
print(fridge1)
print(fridge1.turn_on())
print(fridge1.open_door())
print(fridge1.close_door())