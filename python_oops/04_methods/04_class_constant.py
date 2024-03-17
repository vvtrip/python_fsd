class Circle:
    
    pi = 3.1416
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def find_area(self):
        return Circle.pi * (self.radius**2)

blue_circle = Circle(15, "Blue")
area = blue_circle.find_area()
print(area)