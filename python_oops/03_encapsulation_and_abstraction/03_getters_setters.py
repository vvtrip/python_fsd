class Car:

    def __init__(self, brand, year):
        self._brand = brand
        self.year = year

    def get_brand(self):
        return self._brand
    
    def set_brand(self, new_brand):
        
        #custom check for name to maintain integrity of the data to be set
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print('Invalid brand name')

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