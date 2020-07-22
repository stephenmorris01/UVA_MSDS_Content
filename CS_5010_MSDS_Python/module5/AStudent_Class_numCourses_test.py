# File: AStudent_Class_numCourses_test.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#    - Unit testing / debugging code
#    - Testing AStudent_Class.py  (the Student class)
#    - Testing enrollInCourse() method in AStudent class to see
#      if the "numCourses" attribute is correctly incremented

# Copying enrollInCourse method for reference:
#    def enrollInCourse(self, cname): # Enroll in a course
#        courseName = cname
#        self.courses.append(courseName)
#        self.numCourses += 1 # increment the number of courses

## Note: the following is an example of ONE unit test 


import unittest
from AStudent_Class import *

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