class Backpack:
    
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_multiple_items(self, items):

        for item in items:
            self.add_items(item)

    def add_items(self, item):
        self._items.append(item)

my_backpack = Backpack()

my_backpack.add_multiple_items(['Bottle', 'Bag'])

print(my_backpack.items)

# Non-Public Methods
# To follow the Python naming conventions, to make a method "non-public", 
# you should add a leading underscore to its name, like this:

# def _add_items:

# Name Mangling
# Adding two underscores to the name of the method will trigger the 
# process of name mangling:

# def __add_items: