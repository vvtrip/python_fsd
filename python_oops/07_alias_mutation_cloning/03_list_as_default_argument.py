# Common Bug: Be Careful with Mutable Data Types as Default Arguments

# ◼️ Please avoid using mutable data types (such as lists) as default arguments.
# Why?
# Default arguments are initialized when the methods are initially 
# interpreted by the Python interpreter, so there is only one copy 
# of each default argument in memory.
# Default arguments are not created every time you call the method. 
# Instead, they are created once when the program starts to run.

# ◼️ Lists as Default Arguments
# If you use a list as a default argument, the reference to the same 
# list will be reused for every method call.
# In the following code, you can see how we use an empty list as the 
# default argument for the clients parameter in the __init__() method.

# ◼️ You might expect this to work normally, creating an empty list 
# (a new object) every time you create an instance.
# But this is not what really happens...
# When we start adding elements to the list, you can see that the 
# two instances were modified (please see the example below):

class WaitingList:
	
    # The default argument is an empty list.
    def __init__(self, clients=[]):
        self.clients = clients
		
    def add_client(self, client):
        self.clients.append(client)

# Create the instances.		
waiting_list1 = WaitingList()
waiting_list2 = WaitingList()
 
# Add a client to the first waiting list.
waiting_list1.add_client("Jake")
 
# Both of them were modified!
print(waiting_list1.clients)
print(waiting_list2.clients)        

# ◼️ Behind the Scenes
# What truly happens behind the scenes is that when this line of code is executed: 
# self.clients.append(client)
# The new client is added to the same list, not to a different list for each instance.
# We can check that self.clients references the same list with the id() function.
# Notice how the ids are exactly the same in the two instances

class WaitingList:
	
    def __init__(self, clients=[]):
        self.clients = clients
        print("List id:", id(self.clients))
		
    def add_client(self, client):
        self.clients.append(client)
 
		
waiting_list1 = WaitingList()
waiting_list2 = WaitingList()

# ◼️ Solution
# A solution to this problem is to avoid using a list as a default argument, and use this instead:

class WaitingList:
	
    def __init__(self, clients=None):
        if clients is None:
            self.clients = []
        else:
            self.clients = clients
		
    def add_client(self, client):
        self.clients.append(client)


# None is used as the default argument, so you could omit the argument when you create the instance.
# If the value of clients is None, the attribute is initialized to an empty list.
# Otherwise, the value passed as argument is assigned.
# This will result in the behavior that we would expect:
waiting_list1 = WaitingList()
waiting_list2 = WaitingList()
 
waiting_list1.add_client("Jake")
 
waiting_list1.clients
waiting_list2.clients

# Now the instances reference two separate lists and modifying one does not modify the other.

print(waiting_list1.clients)
print(waiting_list2.clients)  