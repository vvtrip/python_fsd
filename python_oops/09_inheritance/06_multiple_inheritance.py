# Multiple Inheritance

# In Multiple Inheritance, a class has more than one parent class.

# For example, if you are developing a Graphical User Interface 
# (GUI), a Button class could inherit from both the Rectangle class 
# (for style) and from the GUIEelement class (for functionality).

class Rectangle:
 
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
 
 
class GUIElement:
 
    def click(self):
        print("The object was clicked...")
 
 
class Button(Rectangle, GUIElement):
 
    def __init__(self, length, width, color, text):
        Rectangle.__init__(self, length, width, color)
        self.text = text
