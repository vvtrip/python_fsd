class Car:

    def __init__(self, brand, color, model):
        self._brand = brand
        self._color = color
        self._model = model

    @property
    def brand(self):
        return self._brand

    @property
    def color(self):
        return self._color

    @property
    def model(self):
        return self._model

    def show_info(self):
        print('brand', self.brand)
        print('color', self.color)
        print('model', self.model)

class Person:

    def __init__(self, name, age, gender, car):
        self._name = name
        self._age = age
        self._gender = gender
        self._car = car
    
    @property
    def car(self):
        return self._car
    
    def show_car_info(self):
        print('brand', self.car.brand)
        print('color', self.car.color)
        print('model', self.car.model)


car_c = Car('audi', 'black', 'R8')
per_p = Person('ram', 22, 'male', car_c) 

print(per_p.car.show_info())
print()
print(per_p.show_car_info())

# Aggregation
# Aggregation is a "has a" relationship.

# An instance of class B has an instance of class A 
# but they can both exist independently.

# If the program removes the instance of class B, the 
# instance of class A can still exist on its own.

# Implementation

# To implement this in our code, we usually pass 
# an instance of a class as an argument to create an 
# instance of another class.

# ---------------------------------------------------------

# Composition
# In composition, a composed object cannot exist without the 
# object that contains it.

# For example, let's say that conceptually, an Engine instance 
# cannot exist without its Car instance in a given program. If 
# we remove the Car instance from the program, the Engine 
# instance associated to the car should be removed as well.

# Implementation

# To implement this in our code, this would involve creating the 
# instance of the composed object inside the object that contains it.

# This way, when the "container" object is removed from the program, 
# the composed object is removed as well.

# class Die:
 
#     def __init__(self, value):
#         self.value = value
 
 
# class Player:
 
#     def __init__(self):
#         # Create the instance of Die 
#         # inside the instance of Player.
#         # This Die instance cannot exist without 
#         # the Player instance that contains it. 
#         self.die = Die(5)
 
        
# my_player = Player()