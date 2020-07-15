# File: pyScript19
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Object-oriented programming (OOP) - Student Class
from functools import reduce

class Student:
    # fields: name, id, grades(a list)
    
    #Local variable
    #grades = [] # initially empty
    
    def __init__(self, name, id):  # constructor
        self.name = name
        self.id = id
        self.grades = []
        print(f"Student Added: {self.name}  |  ID # {self.id}")

    def __str__(self):
        return f"Student ID# {self.id} is named {self.name}, has {len(self.grades)} grades recorded, an average of {self.average()}"
    
    def addGrade(self, grade): # add the grade to the list of grades
        self.grades.append(grade)
    
    def addGrades(self, grades): # add the grade to the list of grades
        self.grades += grades

    def showGrades(self): # displaying the grades
        grds = '' # empty string
        for grade in self.grades: # Loop through grades list
            grds += str(grade) + ' '  # assign each grade to the string grds
        print(f"Grades: {grds}")
        return grds
    
    def average(self):
        avg = reduce(lambda x, y: x + y, self.grades) / len(self.grades)
        #print(f"this student's current average grade is {round(avg, 3)}")
        return round(avg, 2)
    
#==================================================
    
student1 = Student('Jones', '123')
student1.addGrades([88,72,100])
grades1 = student1.showGrades()
student1.average()
print(student1)
#print(str(student1.name) + ', ' + str(student1.id)) # Output: Jones, 123
# student1.addGrade(88)
# student1.addGrade(72)
# student1.addGrade(100)
#print("Grades: {student1.showGrades()}" + student1.showGrades()) # showing grades for student1

student3 = Student('Adalbert Frincke Hotopp', '456')
student3.addGrades([65,91,80])
grades3 = student3.showGrades()
student3.average()
#print(str(student1.name) + ', ' + str(student1.id)) # Output: Jones, 123
# student2.addGrade(65)
# student2.addGrade(91)
# student2.addGrade(80)
#print(f"Grades: {student1.showGrades()}") # showing grades for student1


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
s2 = Student('Clayton', '115')
#print(str(s2.name) + ', ' + str(s2.id)) 
s2.addGrade(85)
s2.addGrade(95)
s2.addGrade(99)
s2.showGrades()
s2.average()
#print("Grades: " + s2.showGrades())  # !!!
# =============================================================================

studentsDicts = [{'Name':'Betty Hemmings','ID':1735,'scores':[95,78,16,64]},
                {'Name':'James Hemmings','ID':1765,'scores':[50,7,68,89]},
                {'Name':'Sally Hemmings','ID':1773,'scores':[29,87,24,69]}]