def remove_even_values(dictionary):
    for key, value in dictionary.items():
        if value%2 == 0:
            del(dictionary[key])


my_dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

remove_even_values(my_dictionary)

# this will have runtime error because the same object is deleted from memory
# and is being considered for operation in the next iteration of the loop
# RuntimeError: dictionary changed size during iteration

# some built-in methods in Python can mutate objects.
# array.sort() will mutate the array, so sorted(array) could be used 
# in scenarios where mutation of original object is not desired