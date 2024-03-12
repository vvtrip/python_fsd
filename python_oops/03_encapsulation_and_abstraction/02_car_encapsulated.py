class Car:

    def __init__(self, make, model, year):

        self.__make = make # name mangling
        self.__model_ = model # name mangling
        self._year = year  # recommended convention


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

print(my_car._Car__make)
print(my_car._Car__model_)
# There is no concept of private in python, rather a soft 
# non public concept is present and achieved through compliance 
# with convention. It is used to avoid accessing some attributes 
# outside of class.

# Name Mangling is a special case of non public attribute where two 
# leading underscore or an additional lagging underscore is added to 
# attribute within class. outside of the class the attribute can still 
# be accessed but by even complex naming convention of _Classname__attribute. 
# Thus inceasing the complexity of using the attribute.

# It decreases the readability and ease of testing, thus only a single 
# leading underscore is recommended to be added before an attribute by convention

# two leading and two trailing underscore do not make name mangling 
# rather it is a convention for magic function like __init__