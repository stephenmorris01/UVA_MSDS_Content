# File: pyScript19
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Object-oriented programming (OOP) - Student Class

class Student:
    # fields: name, id, grades(a list)
    
    #Local variable
    grades = [] # initially empty
    
    def __init__(self, name, id):  # constructor
        self.name = name
        self.id = id
    
    def addGrade(self, grade): # add the grade to the list of grades
        self.grades.append(grade)
    
    def showGrades(self): # displaying the grades
        grds = '' # empty string
        for grade in self.grades: # Loop through grades list
            grds += str(grade) + ' '  # assign each grade to the string grds
        return grds
    
#==================================================
    
student1 = Student('Jones', '123')
print(str(student1.name) + ', ' + str(student1.id)) # Output: Jones, 123
student1.addGrade(88)
student1.addGrade(72)
student1.addGrade(100)
print("Grades: " + student1.showGrades()) # showing grades for student1
# print(student1) # Will NOT work, since we do not have a "to-string" (__str__) method
# Output of the above line will be a memory address like:
#      <__main__.Student object at 0x00000220B8611BE0>
#==================================================

# ** TO THINK ABOUT: **
# This is fine, however, what happens if you create a second Student object??
# Local ("global") variable grades (a list - which is a mutable object) will
# accumulate grades from ALL students... this behavior is not what we want. 
# Uncomment lines 46-51 below and see what happens.  How would you fix this?? 
# For now, the above file is fine for the above scenario. 

# =============================================================================
# s2 = Student('Clayton', '115')
# print(str(s2.name) + ', ' + str(s2.id)) 
# s2.addGrade(85)
# s2.addGrade(95)
# s2.addGrade(99)
# print("Grades: " + s2.showGrades())  # !!!
# =============================================================================
