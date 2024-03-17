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