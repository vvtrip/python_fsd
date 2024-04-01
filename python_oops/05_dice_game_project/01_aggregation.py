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


# Aggregation is a "has a" relationship.

# An instance of class B has an instance of class A 
# but they can both exist independently.

# If the program removes the instance of class B, the 
# instance of class A can still exist on its own.

# Implementation

# To implement this in our code, we usually pass 
# an instance of a class as an argument to create an 
# instance of another class.