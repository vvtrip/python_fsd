class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self._year = year


my_car = Car('Hyundai', 'i10', 2018)
# we can update the object attribute outside of class
# but following gives error as year is made non public 
# in the class
try:
    print(my_car.year)
except Exception as e:
    print(e)
finally:
    pass        
# gives AttributeError: 'Car' object has no attribute 'year'. Did you mean: '_year'?

# even thoguh we can access it throgh my_car._year we shouldn't do it by convention
# as there is no private keyword in python, it is responsibility of developer
# to have the understanding of convention

my_car.year= 2020
print(my_car.year)

# above line of code is error free as it creates new attribute called year
# which is different from _year

# __year can also be created and the technique is called name mangling
# but is supposed to be used in special cases