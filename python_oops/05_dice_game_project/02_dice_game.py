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

class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("========================")
        print("Welcome to DiceGame")
        print("========================")

        while True:
            self.play_round()    

    def play_round(self):
        print("----- Welcome to new round -----")
        input(' Enter any key')
        
        player_val = self._player.roll_die()        
        computer_val = self._computer.roll_die() 

        if player_val > computer_val:
            print('You won')
            self._player.decrement_counter()
            self._computer.increment_counter()
        elif computer_val > player_val:
            print('Computer won. Train agaimn')
            self._player.increment_counter()
            self._computer.decrement_counter()
        else:
            print("it's a tie")

        print('your score',self._player.counter)
        print("computer's score", self._computer.counter)    

my_die = Die()
computer_die = Die()

my_player = Player(my_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

game.play()