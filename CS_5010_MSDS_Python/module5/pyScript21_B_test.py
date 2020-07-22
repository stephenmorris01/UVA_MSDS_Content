import unittest
from .pyScript21_B import AStudent

class AddGradeTestCase(unittest.TestCase): # inherit from unittest.TestCase

    # Unit testing addGrade() method in pyScript21_B.py

    def test_is_addGrade_inserting_into_grades(self): #(example of 1 unit test)

        # Is addGrade() method successfully adding each grade to grades list?
        # Set up:
        student1 = AStudent('Clayton', '5010', 0) # create instance
        student1.grades = []
        student1.addGrade(90) # add a few grades
        student1.addGrade(80)
        student1.addGrade(100)
        print(student1.grades)
        # Test: (using assertEqual() method)
        self.assertEqual(student1.grades, [90,80,100]) # grades == [90,80,100]?
    
    def test_is_addGrade_inserting_into_grades2(self):
        student1 = AStudent('Nada', '5010', 0, grades=[])
        student1.addGrade(90) # add a few grades
        student1.addGrade(80)
        student1.addGrade(100)


    def test_is_courses_working_correctly(self):
        # Are enrolled courses being correctly added to courses list?

        # Set up
        studentJ = AStudent('Colin', '5010', 0) # create instance
        studentJ.enrollInCourse("CS5010")
        studentJ.enrollInCourse("CS5050")
        studentJ.enrollInCourse("CS5777")
        print("What's in courses list?  " + str(studentJ.courses))
        
        # Test
        # Does the list of courses contain  ['CS5010', 'CS5050', 'CS5777']?
        self.assertEqual(studentJ.courses, ['CS5010', 'CS5050', 'CS5777']) 

class EnrollInTestCase(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing enrollInCourse() method in AStudent_Class.py
    
    def test_is_numCoursincremented_correctly(self):
        # Is enrollInCourse() method successfully incrementing the
        # numCourses attribute of the Student object 

        # Set up
        student1 = AStudent('Katherine', '5010', 0) # create instance
        student1.enrollInCourse("CS5010")
        student1.enrollInCourse("CS5050")
        student1.enrollInCourse("CS5777")
        print(student1.courses)
        print(student1.numCourses)
        
        # Test
        self.assertEqual(student1.numCourses, 3) # should be 3
        # Uncomment the following assert statement (and comment the 
        # one above) for an example of what you might see if a test fails
        # Artificially causing the assert statement to fail: 
        #self.assertEqual(student1.numCourses, 4)
                          
if __name__ == '__main__':
    unittest.main()        