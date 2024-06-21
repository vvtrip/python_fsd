# alias is when we assign a mutable object to a new variable
# such that making changes in new variable modifies Value
# of the old variable as well as both are pointing to same address

a = [1,2,3,4]
b = a #this is called aliasing, b is alias of a
print(a)
print(b)
print(a is b)

b[0] = 15

print(a is b)
print(a)
print(b)


a = 'hi'
# since the reference of variable a is changed from old address
# holding value [1,2,3,4] to new address with value 'yes'
# the old address will be deleted from memory with automatic 
# garbage collection

b = a
print(a)
print(b)
print(a is b)

print(id(a))
print(id(b))

b = 'hello'

print(a)
print(b)
print(a is b)

print(id(a))
print(id(b))


# advantage of mutable objects - efficient memory management - low cost
# disadvantage - cahnces of bugs in case of aliasing

# immutable objects - int, float, tuple, string, boolean
# advantage - chances of bugs are removed even in case of aliasing since new objects are created
# disadvantage - adds up memory cost if some modification required on the object, since a new object
# is required to be created 

a = (1,2,3,4)
print(a)
print(id(a))
#if we have to insert 7 in between 2 and 3, it is not possible on a tuple directly
# so need to make a new object 

a = a[:2] + (7,) + a[-2:]
print(a)
print(id(a)) # old object is deletd from memory and new objects with more
# space(since an extra element is present) is created