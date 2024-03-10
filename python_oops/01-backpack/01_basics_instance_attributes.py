# Below is a class header. 
# Class names are as singular nouns
# and written in capital camelcase

class Backpack:

    # declaring a class attribute which is inititated for all instances of class
    max_num_of_items = 10

    # If the name of a parameter clashes with a keyword, you should add a trailing underscore to the parameter.
    # For example:
    # def __init__(self, description, type_):
    
    # __init__ is the constructor which is called automatically upon object creation
    # self keyword is a reference to the current instance of the class
    def __init__(self, color, size):
        
        # self.items indicates the assignment of instance attribute
        # since a bagpack is initially empty, it is assigned an empty list
            self.items = []
            # color and size are parameters passed through the objects
            # and assigned to the instance attribute of color and size
            self.color = color
            self.size = size

            # we did not pass a value for self in the arguments list (at least not explicitly), but the code worked correctly.
            # Why did we not write something like this?
            # my_backpack = Backpack(<value_for_self>, 'red', 'medium')
            # The answer is that we do not need to.
            # Let's check if self already has a value.
            # If we add a line of code to the __init__() method to print the value of self, this is what we get:
            # <__main__.Backpack object at 0x00000197411C0490>

            print(self)

            
my_backpack = Backpack('red', 'medium')
print(my_backpack)
# prints <__main__.Backpack object at 0x00000197411C0490>
# which is same as output of print(self)

# None is an object itself, like you can see right here 
# when we check if it is an instance of object:
# isinstance(None, object) # True
# None is also the only value of the NoneType data type. 
# If we print the value returned by type(None)The output is <class 'NoneType'>

# You can delete an instance attribute with the keyword del
# ex - del my_backpack.color
try:
    del my_backpack.color
    print(my_backpack.color)
except Exception as e:    
    print(e)
finally:
     pass    
# prints AttributeError: 'Backpack' object has no attribute 'color'

your_backpack = Backpack('black', 'large')
# We can use delattr (a built-in Python function) to delete 
# attributes dynamically, based on the value of a variable.
attributes = ['color', 'size']
for attr in attributes:
      delattr(your_backpack, attr)

try:
    print(your_backpack.color)
except Exception as e:    
    print(e)
finally:
     pass

try:
    print(your_backpack.size)
except Exception as e:    
    print(e)
finally:
     pass

# prints
# <__main__.Backpack object at 0x000001FD779ABFD0>
# <__main__.Backpack object at 0x000001FD779ABFD0>
# 'Backpack' object has no attribute 'color'
# <__main__.Backpack object at 0x000001FD779ABF40>
# 'Backpack' object has no attribute 'color'
# 'Backpack' object has no attribute 'size'