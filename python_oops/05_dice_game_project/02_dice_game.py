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

my_die = Die()
print(my_die.value)

my_die.roll()
print(my_die.value)