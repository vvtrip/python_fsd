class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
            self._price = price

    price = property(get_price, set_price)

    def get_size(self):
        return self._size

    def set_size(self, size):
        if size in ["small", "medium", "large"]:
            self._size = size

    size = property(get_size, set_size)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if isinstance(brand, str) and brand:
            self._brand = brand

    brand = property(get_brand, set_brand)


class BouncyBallDec:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    # this is the getter method
    @property
    def price(self):
        return self._price
	
    # this is the setter method and uses name_of_the_property.setter
    # as the convention
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price

    @property
    def size(self):
        return self._size
	
    @size.setter
    def size(self, new_size):
        if new_size in ["small", "medium", "large"]:
            self._size = new_size
        else:
            print('size is not valid')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand:
            self._brand = new_brand

bb = BouncyBall(10, 'small', 'abc')
print(bb.brand)
bb.brand = 'xyz'
print(bb.brand)

bbd = BouncyBallDec(10, 'small', 'abc')
print(bbd.size)
bbd.size = 'xtralarge'
print(bbd.size)
# You do not necessarily have to add getters and setters 
# for all your non-public attributes. The decision of whether 
# or not to include a getter and/or a setter should be taken 
# after a careful analysis.

# If the attribute is only intended to be used and updated 
# within the class, and you cannot foresee any possible scenarios 
# where you might need to access or update the attribute on an 
# instance, you could omit them.            