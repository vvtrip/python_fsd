def remove_even_values(dictionary):
    for key, value in dictionary.copy().items(): # here it is iterating over copy of original dictionary
        if value%2 == 0:
            del(dictionary[key]) # here it is operating on original dictionary


my_dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

remove_even_values(my_dictionary)

print(my_dictionary)

x = (1,2,3)
y = x[:]
print(id(x))# same
print(id(y))

x = [1,2,3]
y = x[:]
print(id(x))# different
print(id(y))


# There is a reason why cloned tuples have the same id while cloned lists 
# have different ids. 
# Let's see...
# ◼️ Why?
# Tuples are immutable in Python, which means that they cannot be modified.
# Once you define a tuple, you cannot change the elements that are contained 
# directly within the tuple.
# That is why Python does not create a new tuple when you try to clone a tuple.
# Instead, it assigns a reference to the original tuple in memory to optimize memory usage.
# Think about it...
# The purpose of cloning is creating a copy of an object that you can modify without 
# mutating the original.
# But if we already have an immutable object that cannot be mutated, it makes sense to 
# save space and simply reuse the reference to the same object in memory.
# Interesting, right?
# In practice, we cannot really "clone" of a tuple. We can only assign a reference to 
# the original tuple to another variable.
