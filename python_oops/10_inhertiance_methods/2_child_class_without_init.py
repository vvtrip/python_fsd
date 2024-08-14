class Triangle():

    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def calc_area(self):
        print((1/2) * self.base * self.height)

class RightAngleTriangle(Triangle):

    def display_area(self):
        print("Right angle triangle")

        super().calc_area() # parent init called without passing the base, height, it already passed the reference
        # above line could also be written as Triangle.calc_area(self) and it would pass child calss reference through self keyword

rat = RightAngleTriangle(5, 6)

rat.display_area()