class Restaurant:
    def __init__(self):
        self.menu = []
        self.order = []

    def add_dish(self, dish):
        if dish not in self.menu:
            self.menu.append(dish)
            print(f'Блюдо "{dish}" добавлено в меню.')


    def remove_dish(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f'Блюдо "{dish}" удалено из меню.')


    def place_order(self, dishes):
        for dish in dishes:
            if dish in self.menu:
                self.order.append(dish)




restaurant = Restaurant()
restaurant.add_dish("Пицца")
restaurant.add_dish("Салат")
restaurant.place_order(["Пицца", "Суп"])
restaurant.remove_dish("Пицца")
