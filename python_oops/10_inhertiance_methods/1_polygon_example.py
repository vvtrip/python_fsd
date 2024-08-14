class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

    def describe(self):
        print(f"This polygon has {self.num_sides} sides and is {self.color} in color")


class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color):
        super().__init__(Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height

    def calc_area(self):
        return (1/2) * self.base * self.height  

class Square(Polygon):

    NUM_SIDES = 4

    def __init__(self, side_len, color):
        super().__init__(Square.NUM_SIDES, color)
        self.side_len = side_len

    def calc_area(self):
        return self.side_len**2


triangle = Triangle(4, 6, "Blue")
square = Square(4, "Green")

triangle.describe() #inherited method

square.describe() #inherited method


print(triangle.calc_area()) # same name but different implementation
print(square.calc_area()) # same name but different implementation