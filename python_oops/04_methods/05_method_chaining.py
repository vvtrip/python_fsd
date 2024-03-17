class Pizza:
 
    def __init__(self):
        self.toppings = []
 
    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self
 
    def show_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize())


pizza = Pizza()
pizza.add_topping("mushrooms") \
    .add_topping("olives") \
    .add_topping("chicken") \
    .show_toppings()

print()
# we can wrap the code within parenthesis for readability
(pizza.add_topping("mushrooms")
    .add_topping("olives")
    .add_topping("chicken")
    .show_toppings())            