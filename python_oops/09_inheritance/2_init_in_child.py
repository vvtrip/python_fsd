class Polygon:
    
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

class Triangle(Polygon):
    #we can keep it constant since it won't change
    NUM_SIDES = 3
    
    def __init__(self, base, height, color):

        # we need to call the init of parent if the init method is also
        # present in the child class, the parameters are passed to the child init
        # in such a way that some of the parameters will be passed to parent init
        # (color) and child init(base, height)

        Polygon.__init__(self, Triangle.NUM_SIDES, color) 
        # self keyword is mandatory if calling parent constructor using classname

        # super() keyword could also be used instead of Polygon class, an example
        # super().__init__(Triangle.NUM_SIDES, color)
        # notice here self keyword is not passed but in case of Polygon class it
        # must be passed so that it would point the same 
        # child object as reference to parent
        
        # if we don't call the init method of parent class like above we get follwoing error:
        # AttributeError: 'Triangle' object has no attribute 'num_sides'
        
        self.base = base
        self.height = height

class Square(Polygon):
    pass

my_triangle = Triangle(5, 4, "blue")

print(my_triangle.num_sides)
print(my_triangle.base)
print(my_triangle.height)
print(my_triangle.color)



