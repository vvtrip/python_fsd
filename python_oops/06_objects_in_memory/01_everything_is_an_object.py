
print(object)

print(isinstance(5, object))

print(isinstance([1, 5, 2, 6], object))

print(isinstance((1, 5, 2, 6), object))

print(isinstance("Hello, World!", object))

print(isinstance({"a": 5, "b": 6}, object))

print(isinstance(False, object))

print(isinstance(True, object))

def f(x):
    return x * 2
    

print(isinstance(f, object))

class Movie:

    def __init__(self, title):
        self.title = title

#even a class itself an object!
print(isinstance(Movie, object))

# reference is a name that refers to the location(address) in memory
# of the object
# ex-  variables, attributes and items are all examples of references
# variables in python store references to object in memory

# programs keep track of how many "references" to the objects exist

# when there are no references left to an object in the program
# then the object is deleted from memory, this is called 
# Garbage collection. It is done automatically to improve memory usage
# and optimise the efficiency of the program

# ----------------------------------------------------

# There is a very subtle difference between an object and an instance. 
# In most cases, you will see them being used interchangeably.

# An object is a conceptual representation of an entity, while an instance 
# is the actual implementation this entity in the program.

# For example, a House object is the conceptual representation of a house 
# in code while a house instance is the actual implementation of a house.