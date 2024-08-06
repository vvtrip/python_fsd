# inheritance makes use of super class or parent class which has general features
# and is an abstract class. The child class or subclass inherits those features
# from parent class and may add more specific details inside it.
# Inheritance is based on DRY principle (Don't repeat yourself)

class Polygon:
    pass

class Triangle(Polygon):
    pass

class Square(Polygon):
    pass