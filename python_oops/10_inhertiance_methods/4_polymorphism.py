# Polymorphism is another fundamental pillar of Object-Oriented Programming.

# Polymorphism means that an object can take many forms.

# With polymorphism, we can use a single entity such as a function, operator or object, to represent different types in different situations.

# Polymorphism can be implemented through method overriding and method overloading (method overloading is not supported in Python per se).


# ◼️ Polymorphism with Built-in Operators
# A great example of polymorphism is the + operator.

# This operator acts differently based on the data type of the values it is operating with.

# For numbers, it acts as the addition operator:

# 5 + 6

# But with strings, it acts as a concatenation operator:

# "Hello" + "World"

# We use the same operator but the operations are different.

# The same principle can be applied to methods and functions, to act different based on the type of the value(s) they are working with.



# ◼️ Inheritance
# In Python, polymorphism can be implemented through inheritance when you override methods of the superclass.

# Here we have an example:

# First we have the classes File, PDFFile, and TextFile (they inherit from File):



class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension
 
    def open():
        print("Opening a generic file...")
 
 
class PDFFile(File):
 
    def __init__(self, name):
        File.__init__(self, name, ".pdf")
 
    def open(self):
        print("Opening a PDF File...")
 
 
class TextFile(File):
 
    def __init__(self, name):
        File.__init__(self, name, ".txt")
 
    def open(self):
        print("Opening a Text File...")


# Then we have this function:



def open_files(files):
    for file in files:
        file.open()


# If we create instances of these classes and include them in a list:



pdf1 = PDFFile("Brochure")
pdf2 = PDFFile("Course Advertising")
text1 = TextFile("List of Students")
 
files = [pdf1, text1, pdf2]


# We can call the function open_files passing this list as argument:



open_files(files)


# 💡 Tip: We are passing a list that with objects of different types and the code works correctly for all of them.

# This is because we know that all the classes have an .open() method defined, so the method of their corresponding class will be executed.

# This is an example of Polymorphism.

# Calling the same method on instances of different data types that have a method with the same name causes a different effect because the method is implemented differently in each class.

# This is the output:

# Opening a PDF File...
# Opening a Text File...
# Opening a PDF File..