a = 25700
b = 25700

print(id(a))
print(id(b))
print(a is b) # True

# above code returns true(surprisingly) because python by default allocates single 
# location for a range of numbers (from -5 to 256) to optimise memory usage
# here we can see it returns true for numbers outside this range as well.
# This is due to various versions across development environments like vscode, pycharm etc
# where this range is increased.

#--------------------------------------------------------------

# similar is the case with strings, since strings are immutable, 
# python provides reference to 
# single location of the string object

a = 'HI'
b  = 'HI'

print(a is b)

# this is called string interning

# The behavior of string interning can be different if
# you use the interactive console or if you run a Python
# script, based on how the code is optimized behind the scenes when the program runs.

# Different environments have different levels of optimization.

# The process can also vary between different versions of Python.