# In Python, the == operator checks if two objects have the same values but it 
# does not check if they are the same object in memory. This is very different.

class Dog:
	
    def __init__(self, age):
        self.age = age
 
		
my_dog = Dog(5)
your_dog = Dog(5)
 
print(my_dog == your_dog)


# The comparison operator doesn't return True, even if their instance attributes have the same value.
# Why is this?


# Objects created from user-defined classes have to meet two conditions for 
# the expression obj1 == obj2 to evaluate to True.
# Condition 1
# They have to refer to the same object (x is y has to evaluate to True).
# Condition 2
# The expression hash(x) == hash(y) has to be True. The hash() function maps 
# the object to a unique integer.
# This is why comparing an object from a user-defined class to itself using the == operator returns True:

class Dog:
	
    def __init__(self, age):
        self.age = age
 
		
my_dog = Dog(5)
your_dog = Dog(5)
 
print(my_dog == your_dog)  # False
print(my_dog == my_dog)  # True
print(your_dog == your_dog)  # True
print(your_dog == my_dog)  # False

# The values returned by hash() are not equal for the two objects:

print(hash(my_dog))
-2143773140
print(hash(your_dog))
3710489

# When the hash values are different:
# The expression hash(a) == hash(b) will be False.
# The expression (a is b) and (hash(a) == hash(b)) evaluates to False, so a == b evaluate to False.
# This is what happens behind the scenes when you compare two 
# instances of a user-defined class with the == operator.

a = [1,2,3,4]
b = [1,2,3,4]

print(a is b) # False
print(a==b) # True

b = a

print(a is b) # True
print(a==b) # True
