class Polygon:
    
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

class Triangle(Polygon):
    pass

class Square(Polygon):
    pass

# this calls the constructor or __init__ function of the base class if the 
# __init__ function is not defined in the dervied class
my_triangle = Triangle(3, "blue")

print(my_triangle.num_sides)
print(my_triangle.color)



