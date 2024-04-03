import random


class Die:

    def __init__(self):        
        self._value = None #initialzing as None because we want to have a unrolled die in start

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return self._value

class Player:

    def __init__(self, die, is_computer=False):
        #if not sure whether to make attributes public or non public, always choose non public
        #as recommended by python style guide
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter
    
    def roll_die(self):
        self._die.roll()

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1


my_die = Die()
player = Player(my_die, is_computer=False)
print(my_die.value) #None

my_die.roll() #same value for below 2 prints
print(my_die.value) 
print(player.die.value)

player.roll_die() #same value for below 2 prints
print(my_die.value)
print(player.die.value)

