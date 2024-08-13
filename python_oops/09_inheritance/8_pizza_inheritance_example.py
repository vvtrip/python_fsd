class Pizza:
    
    def __init__(self, size, toppings, price, rating):
        self.size = size  # "Small", "Medium", or "Large"
        self.toppings = toppings  # A list of toppings
        self.price = price
        self.rating = rating  # On a scale from 1 to 5

# Write your code below:
class Margherita(Pizza):
    
    def __init__(self, size, toppings, price, rating, has_extra_cheese):
        super().__init__(size, toppings, price, rating)
        self.has_extra_cheese = has_extra_cheese

class Marinara(Pizza):
    
    def __init__(self, size, toppings, price, rating, has_extra_oregano):
        super().__init__(size, toppings, price, rating)
        self.has_extra_oregano = has_extra_oregano

size, toppings, price, rating =  'L', 'tomato', '10$', 4
has_extra_cheese = True
has_extra_oregano = False
margherita = Margherita(size, toppings, price, rating, has_extra_cheese)
marinara = Marinara(size, toppings, price, rating, has_extra_oregano)
