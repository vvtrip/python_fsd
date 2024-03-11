class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year


my_car = Car('Hyundai', 'i10', 2018)
# we can update the object attribute outside of class
my_car.year = 2020

print(my_car.year)

# If we have to avoid this assignment to achieve encapsulation
# ,i.e., bind data(parameters) and actions(methods) inside the class, 
# then we can follow convention of adding underscore as a prefix to object attribute.
# The ultimate purpose is information hiding and disallowing problematic 
# changes to the state by preventing direct access to the data of object

# developers may want only certain data to be visible to the outside world
# so getters and setters are methods used for this purpose

