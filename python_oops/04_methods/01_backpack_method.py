class Backpack:

    def __init__(self, color, size):
        self._items = []
        self._color = color
        self._size = size

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('please provide a valid item')
    
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print('This item is not in the backpack')
            return 0

    def has_item(self, item):
        return item in self._items

my_backpack = Backpack('red', 'medium')

print(my_backpack.items)

my_backpack.add_item('water bottle')
my_backpack.add_item('pencil')
my_backpack.add_item('box')

print(my_backpack.items)

my_backpack.remove_item('water bottle')

print(my_backpack.items)

print(my_backpack.has_item('pencil'))