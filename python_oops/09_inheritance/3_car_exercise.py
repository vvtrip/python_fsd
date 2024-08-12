class Vehicle:
    
    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed  # In Km/h
        self.fuel_type = fuel_type

class Car(Vehicle):
    
    default_speed = 40
    
    def __init__(self, color, speed, fuel_type, num_doors, is_electric, default_speed = default_speed):
    
        Vehicle.__init__(self, color, speed, fuel_type)
    
        self.num_doors = num_doors
        self.is_electric = is_electric
        self.default_speed = default_speed
        
my_car = Car("Blue", 50, "Diesel", 4, False)

print(my_car.color)
print(my_car.speed)
print(my_car.fuel_type)
print(my_car.num_doors)
print(my_car.is_electric)
print(my_car.default_speed)