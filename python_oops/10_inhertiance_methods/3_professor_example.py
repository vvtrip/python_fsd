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