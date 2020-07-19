from random import triangular # For student grade RNG

# Define student class
class Student:
    # fields: name, sid, grades (list)
    
    # Changes for exercise below
    # --------------------------
    def __init__(self, name, sid, grades=[]):
        # if 'grades' in locals():
        #     del grades
        self.name = name
        self.sid = sid
        self.grades = grades
            
    def __str__(self):
        return f"Name: {self.name}, ID: {self.sid}, Grades: {self.show_grades()}"
    
    def average(self):
        try: 
            return 'Average Grade: ' + str(sum(self.grades) / len(self.grades))
        except ZeroDivisionError:
            print('No grades entered for this student!')
        except TypeError:
            print('Please re-enter the grades as numbers!')
    # --------------------------
    # Changes for exercise above
            
    def add_grade(self, grade):
        return self.grades.append(grade)
    
    def show_grades(self):
        grds = ''
        for grade in self.grades: 
            grds += str(grade) + ' '
        return grds

# Define students (cast as dictionary for compactness)
students = {'Terry': '007zyx', 'Tina': '008ab', 'Tom': '009c'}

# Initialize list to capture output
student_output = []

# Iterate and print student attributes
for key, value in students.items():

    # Generates 5 random grades (65-100) and adds them while creating student
    grades = [round(triangular(65, 100)) for i in range(5)]
    s = Student(key, value, grades)
 
    # Generates 5 random grades (65-100) and individually adds them to the student
    grades2 = [round(triangular(65, 100)) for i in range(5)]
    for g in grades2:
        s.add_grade(g)
    print('\n---------- New Student entry ----------\n')
    print(s)
    print(s.show_grades())
    print(s.average())
    student_output.append(s)

# Delete final student
del s

