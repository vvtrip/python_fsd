# Important Tip: Immutable doesn't mean that its elements are immutable
# Immutable objects can contain mutable objects.
# For example, we could have a list inside a tuple.
# These mutable objects can be modified even if their containers cannot be modified.


# ◼️ Example
# Here is an example that illustrates this. We have this initial list:
my_list = ([1, 2, 3], "abc", 56)
# If we try to change an element of the tuple, we get an error because 
# tuples are immutable objects:
# TypeError: 'tuple' object does not support item assignment
# But if we go even deeper and we try to modify the elements of an element 
# of the tuple that is mutable, we will not get any errors.
# Here we are changing the second element first element in the tuple (the list). 
# We are replacing the number 2 of the list [1, 2, 3] by the number 4 ([1, 4, 3]).

my_list[0][1] = 4 
print(my_list)

# 🚩 The key takeaway is that choosing an immutable "container" object 
# (e.g a tuple) does not really "protect" the elements themselves from 
# change if they are mutable (e.g lists).

# ◼️ Shallow Copy
# When you create a shallow copy of an object, you are creating a new object in memory (a new reference).
# However, the elements of the main object will still point to the same objects.
# Let's illustrate this.
# List Example
# If we have a tuple that contains a list (a mutable object) and we create a clone of the tuple, like this:


a = ([0, 6, 2], "Hello", 56)
b = a[:]

# We might think that this will be the result: 
# two independent objects with a different list object in each one them.

# But this is not what really happens.
# The tuple only contains a reference to the list object, not to the list object itself.
# The other objects are stored as references as well.

# So if you modify the list contained in the tuple that is referenced by b, like this:

b[0][0] = -1

# You are actually modifying the list in memory, so both tuples are affected since 
# they only contain a reference to the list:

# That is why the list was modified in both tuples, even if that was not our 
# initial intention. In the following code, you can see the output immediately 
# below each line of code because the code ran in the interactive Python shell.

# >>> a
# ([-1, 6, 2], 'Hello', 56)
# >>> b
# ([-1, 6, 2], 'Hello', 56)

# ⚠️ You should be really careful with this because it can cause bugs.

# This is another example with the .copy() method that you can call on dictionaries:

# >>> a = {"Nora": ["055-452-322", "Washington Ave."], "Gino": ["006-545", "5th Avenue"]}
# >>> b = a.copy()
 
# >>> a
# {'Nora': ['055-452-322', 'Washington Ave.'], 'Gino': ['006-545', '5th Avenue']}
# >>> b
# {'Nora': ['055-452-322', 'Washington Ave.'], 'Gino': ['006-545', '5th Avenue']}
 
# # If you modify an element of the list
# >>> b["Nora"][0] = "56"
 
# # They are both affected. The original and the copy.
# >>> b
# {'Nora': ['56', 'Washington Ave.'], 'Gino': ['006-545', '5th Avenue']}
# >>> a
# {'Nora': ['56', 'Washington Ave.'], 'Gino': ['006-545', '5th Avenue']}

# IMPORTANT
# According to the Python Documentation:
# Shallow copies of dictionaries can be made using dict.copy(), 
# and of lists by assigning a slice of the entire list, for example, copied_list = original_list[:].

# The copy Module
# You can also use the copy module to create a shallow copy. 
# To do this, you would just need to import the module with import 
# copy at the top of your script, like this:

# >>> import copy
 
# >>> a = ([5, 2, 6, 2], "Welcome", 67)
# >>> b = copy.copy(a)
# >>> b[0][0] = -1
 
# # They are both modified
# >>> a
# ([-1, 2, 6, 2], 'Welcome', 67)
# >>> b
# ([-1, 2, 6, 2], 'Welcome', 67)

# ◼️ Deep Copy
# With a deep copy, in addition to creating a copy of the "container" 
# object, you also create a copy of each one of the elements that are contained in the object.

# This diagram illustrates what would happen in the previous example 
# if we created a deep copy of the tuple. A new copy of the list would be created for the new copy of the tuple.

# If you modify the list, you will not any affect other names or objects that reference them because they will be new copies.

# To perform a deep copy, you should use the copy module, like this:

# >>> import copy
# >>> a = ([5, 2, 6, 2], "Welcome")
# >>> b = copy.deepcopy(a)
# >>> b[0][0] = -1
 
# # Changing the list in b did not affect the list in a
# >>> a
# ([5, 2, 6, 2], 'Welcome')
# >>> b
# ([-1, 2, 6, 2], 'Welcome')

# 💡 Tip: Shallow and Deep copies have unique advantages and disadvantages.