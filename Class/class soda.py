class Soda:
    def __init__(self, cooking_ingredient):
        self.cooking_ingredient  = cooking_ingredient

    def show_my_drink(self):
        if self.cooking_ingredient :
            return f'Газировка и {self.cooking_ingredient }'
        else:
            return 'Обычная газировка'


soda1 = Soda('лимон')
print(soda1.show_my_drink())
