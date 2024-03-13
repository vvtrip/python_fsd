class Car:

    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_brand(self):
        print('in the brand getter')        
        return self._brand
    
    def set_brand(self, new_brand):
        print('in the brand setter')        
        #custom check for name to maintain integrity of the data to be set
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print('Invalid brand name')

    def get_year(self):
        print('in the year getter')        
        return self._year
    
    def set_year(self, new_year):
        print('in the year setter')        
        #custom check for name to maintain integrity of the data to be set
        if isinstance(new_year, int):
            self._year = new_year
        else:
            print('Invalid year')        

    brand = property(get_brand, set_brand)            
    year = property(get_year, set_year)

my_car = Car('Porsche', 2020)

try:
    print(my_car.brand) #this is like directly accessing/reaching out to get the attribute
except Exception as e:
    print(e)
finally:
    pass

#getter method serves the same purpose while mainting the limited access of the attribute
print(my_car.get_brand())

my_car.set_brand('Ferrari123')
print(my_car.get_brand())

my_car.set_brand('Ferrari')
print(my_car.get_brand())
print(f'My car {my_car.get_brand()} is of the year {my_car.get_year()}')
      
# because of the property function we can access the attribute directly
# the name of the property can be anything but for simplicity 
# it is given same as attribute name

my_car.brand = 'Laborghini'
my_car.year += 1

print(f'My car {my_car.brand} is of the year {my_car.year}')