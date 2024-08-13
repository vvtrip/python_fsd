#  Multilevel Inheritance
# we can create more complex hierarchies with multiple levels.

# This is called Multilevel Inheritance.

# Here we have an example of a hierarchy with three different 
#  levels. Notice how we go from the most general concept (Vehicle) 
#  to the most specific concepts (Car and Truck).

class Vehicle:
    pass
 
class LandVehicle(Vehicle):
    pass
 
class Car(LandVehicle):
    pass
 
class Truck(LandVehicle):
    pass