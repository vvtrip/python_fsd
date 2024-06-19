print(id(15))

print(id("Hello, World!"))

print(id([1, 2, 3, 4]))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

# even though values are same, both are stored in different
# locations that's why IDs are different and there are 2 references
# to these two objects by 2 variables

# in each run the location of the object changes as the location is allotted
# only till the lifecycle of the object.

# From official documentation - 
# Id return the "identity" of an object. This is an integer which is guranteed to
# be unique and constant for an object during its lifetime. Two objects with non
# overlapping lifetimes may have the same id() value
 
print(id(a))
print(id(b))

b = a

# now the output will be same because b is poinitng to same address as a

print(id(a))
print(id(b))


class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items


my_backpack = Backpack()
your_backpack = Backpack()    
    
print(id(my_backpack))
print(id(your_backpack))