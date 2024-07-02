def remove_even_values(dictionary):
    for key, value in dictionary.copy().items(): # here it is iterating over copy of original dictionary
        if value%2 == 0:
            del(dictionary[key]) # here it is operating on original dictionary


my_dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

remove_even_values(my_dictionary)

print(my_dictionary)