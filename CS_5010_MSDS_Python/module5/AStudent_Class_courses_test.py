# File: AStudent_Class_courses_test.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#    - Unit testing / debugging code
#    - Testing AStudent_Class.py  (the Student class)
#    - Testing if courses gets correct list of enrolled courses

# Copying enrollInCourse method for reference: 
#    [It should add an enrolled course to the courses list]
#    def enrollInCourse(self, cname): # Enroll in a course
#        courseName = cname
#        self.courses.append(courseName)
#        self.numCourses += 1 # increment the number of courses

## Note: the following is an example of ONE unit test 


import unittest
from AStudent_Class import *

class CoursesTestCase(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing courses list in AStudent_Class.py
    
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
                
            
if __name__ == '__main__':
    unittest.main()            