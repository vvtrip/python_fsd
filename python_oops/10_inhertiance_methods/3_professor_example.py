#type - 1 - no constructor in child class, 
# initilaised with same parameters of the parent class

class Professor1:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

class ScienceProfessor1(Professor1):

    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        super().greet_students()    
    
        
        
science_professor = ScienceProfessor1('rahul',36,'science')
science_professor.greet_students()

#type - 2 - local constructor with init call to parent constructor 

class Professor2:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

class ScienceProfessor2(Professor2):

    def __init__(self, name, age, course):
        super().__init__(name, age, course)

    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        super().greet_students()    
    
        
        
science_professor = ScienceProfessor2('rahul',36,'science')
science_professor.greet_students()



# type - 3 - constructor overloading by allowing no parameters during object creation
class Professor3:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

class ScienceProfessor3(Professor3):

    def __init__(self, name, age, course):
        super().__init__(name, age, course)

    # this init gets invoked in this example
    def __init__(self):
        pass

    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        super().greet_students()    
    
        
        
science_professor = ScienceProfessor3()
science_professor.greet_students()


# type - 4 - latest init gets invoked
class Professor4:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

class ScienceProfessor4(Professor4):

    
    def __init__(self):
        pass

    # this init gets invoked in this example
    def __init__(self, name, age, course):
        super().__init__(name, age, course)   

    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        super().greet_students()    
    
        
        
science_professor = ScienceProfessor4("rahul", 36, "physics")
science_professor.greet_students()

# The terms overwriting and overriding may sound and look very similar, but they are actually quite different.

# Overwriting means replacing existing code or data with new code or data.

# Overriding involves modifying the behavior of a method within a hierarchy. When a method is overridden, its new implementation takes precedence over previous implementations located higher in the hierarchy.

# 🚩 Knowing this difference is very important for choosing the correct term in the appropriate context.

# Method Overloading
# Method Overloading occurs when two methods of the same class have the same name but different parameters.

# When the methods are called, the version that is executed is determined by the number of arguments or their data types.



# ◼️ Python
# Python does not support method overloading. The closest thing to method overloading that we currently have in Python are default arguments, because you can call a method with a different number of arguments and use their default values. But this is not method overloading per se.



# ◼️ Java
# Other programming languages do support method overloading. One example is Java.

# In Java, you have to explicitly declare the data type of each argument, so the compiler can match the number, sequence, and data types of the arguments to the number, sequence, and data types of the formal parameters in each method to determine which one should be called.

# This is an example of method overloading in Java with two add() methods in the Test class:



# class Test {
 
#    public int add(int a, int b) { 
#        return a + b;
#    }
 
#    public int add(int a, int b, int c) {
#        return a + b + c;
#    }
# }
 
# class Main {
 
#    public static void main(String args[]) {
#        Test obj = new Test();
#        obj.add(10, 10);  # This will call the first method. Only two arguments
#        obj.add(20, 12, 5); # This will call the second method. Three arguments.
#    }
# }