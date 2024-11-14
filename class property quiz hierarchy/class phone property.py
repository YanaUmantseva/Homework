class Phone:
    def __init__(self, model, color, price):
        self._model = model
        self._color = color
        self._price = price

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    def discount(self, discount1):
        discount_amount = self.price * (discount1 / 100)
        return self.price - discount_amount


phone = Phone("iPhone 14", "purple", 1100)
print(f"Model: {phone.model}")
print(f"Color: {phone.color}")
print(f"Price: {phone.price}")


discounted_price = phone.discount(20)
print(f"Discounted Price: {discounted_price}")


phone.color = "white"
phone.price = 1000
print(f"Updated Color: {phone.color}")
print(f"Updated Price: {phone.price}")

