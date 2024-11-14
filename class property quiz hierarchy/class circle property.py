import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    def area(self):
        return math.pi * (self.radius ** 2)


c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area()}")

c.radius = 10
print(f"New Radius: {c.radius}")
print(f"New Area: {c.area()}")

