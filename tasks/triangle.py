import math


class triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def c(self):
        return math.sqrt(self.a**2 + self.b**2)

    def area(self):
        return (self.a * self.b) / 2

    def perimeter(self):
        return self.a + self.b + self.c()


a = int(input("a = "))
b = int(input("b = "))

tr = triangle(a, b)

print(f"C = {tr.c()}")
print(f"Area = {tr.area()}")
print(f"Perimeter = {tr.perimeter()}")
