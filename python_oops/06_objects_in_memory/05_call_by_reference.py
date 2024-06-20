# python passes objects by references in function calls

my_list = [6, 2, 8, 2]


def print_data(seq):
    print("Inside the function:", id(seq))
    for elem in range(len(seq)):
        seq[elem] = seq[elem]*2

print("Outside the function, original list:", id(my_list), my_list)
print_data(my_list)
print("after function", my_list)


# copy method can be used to create duplicate of existing object
# without any implication of modification on new object over old object 
print()
my_list = [6, 2, 8, 2]
new_list = my_list.copy()

print("Outside the function, original list:", id(my_list), my_list)
print_data(new_list)
print("after function, original list", my_list)
print("after function, new list", id(new_list), new_list)
