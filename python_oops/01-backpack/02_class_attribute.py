class Backpack:

    # declaring a class attribute which is inititated for all instances of class
    max_num_of_items = 10

    def __init__(self, color, size):
        
            self.items = []
            self.color = color
            self.size = size
            print(self)

            
my_backpack = Backpack('red', 'medium')
print(my_backpack.max_num_of_items)

# we can access class attribute without creating an object as well
print(Backpack.max_num_of_items)