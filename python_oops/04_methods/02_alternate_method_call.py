# now we are passing a value for self.
# It's the first argument: the instance.
# In this example, we pass my_backpack, which is an instance of the Backpack class:
# Backpack.add_item(my_backpack, "Water")
# If we use this syntax, we need to pass it explicitly as the first argument 
# in the list of arguments.
# The value of self will not be assigned automatically because we are not using 
# dot notation, so the interpreter cannot know which instance is actually calling 
# the method if we do not specify it.

class Backpack:
 
    def __init__(self):
        self._items = []
	
    @property
    def items(self):
        return self._items
            
    def add_item(self, item):
        self._items.append(item)

my_mackpack = Backpack()
Backpack.add_item(my_mackpack, "water bottle")
print(my_mackpack.items)        