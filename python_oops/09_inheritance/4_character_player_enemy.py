class Character:

    def __init__(self, x, y, lives):
        self.x = x
        self.y = y
        self.lives = lives

class Player(Character):

    X = 0
    Y = 0
    INITIAL_NUM_LIVES = 10

    def __init__(self, score=0):
        super().__init__(Player.X, Player.Y, Player.INITIAL_NUM_LIVES)
        self.score = score

class Enemy(Character):

    def __init__(self, x=15, y=15, lives = 8, is_poisonous=False):
        super().__init__(x, y, lives)
        self.is_poisonous = is_poisonous

player = Player(5)

print("player stats")
print(player.x)
print(player.y)
print(player.lives)
print(player.score)


easy_enemy = Enemy(lives=1)

print("easy enemy stats")
print(easy_enemy.x)
print(easy_enemy.y)
print(easy_enemy.lives)
print(easy_enemy.is_poisonous)

hard_enemy = Enemy(lives=5, is_poisonous=True)

print("hard enemy stats")
print(hard_enemy.x)
print(hard_enemy.y)
print(hard_enemy.lives)
print(hard_enemy.is_poisonous)
