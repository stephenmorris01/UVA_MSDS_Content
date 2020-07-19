# File: pyScript22.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Creating a derived class (Inheritance)

## Working with inheritance
# Used to implement is-a relationships between objects (e.g. car is-a vehicle)
# Concepts:
# - Base class (e.g. vehicle or employee) having certain set of attributes and 
#   behaviors

# - Derived class (e.g. car or manager) that inherits from the base class
#   It inherits the attributes and behaviors that are defined for the base
#   class and then adds *extra* functionality to the derived class (specifics)
#   e.g. vehicle - something that has wheels; car - (specific) has four wheels

# ===============================================================

## Example: Shape/Rectangle [Shape=base class; Rectangle=derived class]

# *** BASE CLASS *** #
class Shape:
   def __init__(self, xcor, ycor):  # constructor
      self.x = xcor
      self.y = ycor

   def __str__(self):  # to-string method
      return 'x: ' + str(self.x) + ' y: ' + str(self.y)

   def move(self, x1, y1):
      print(f"moved by {x1},{y1}")
      self.x = self.x + x1  # move x-axis
      self.y = self.y + y1  # move y-axis
      
# *** DERIVED CLASS *** #
class Rectangle(Shape):  # put the base class as an argument to derived class
   def __init__(self, xcor, ycor, width, height):  # Note all the attributes
      Shape.__init__(self, xcor, ycor) # Call the base class constructor
      self.width = width    # handle 'local' fields/attributes: width/height
      self.height = height

   def __str__(self):
      retStr = Shape.__str__(self) # Call to-string of base class (Shape)
      retStr += ' width: ' + str(self.width) + ' height: ' + str(self.height)
      return retStr
      
   def area(self):
       recArea = self.width * self.height
       return recArea
       

rec = Rectangle(5,10,8,9) # rec is created with x,y,w,h attributes
print(rec) # Calls to-string methods to print out
rec.move(10,12)  # Calling a method "move" in base class (Shape)
print(rec)
print("Area of rectangle is: " + str(rec.area()))
print("")

rec2 = Rectangle(10, 25, 8, 3) # create second rectangle
print(rec2)
print("Area of rectangle is: " + str(rec2.area()))
      
