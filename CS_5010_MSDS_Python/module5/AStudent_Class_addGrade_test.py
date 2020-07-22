import unittest
from .AStudent_Class import AStudent

class AddGradeTestCase(unittest.TestCase): # inherit from unittest.TestCase

    # Unit testing addGrade() method in pyScript21_B.py

    def test_is_addGrade_inserting_into_grades(self): #(example of 1 unit test)

    def test_enrollInCourse(self):

    def test_showGrades(self):

    def test_str_output(self):

    def test_avg(self):

    
# Directions: This assignment involves writing a small unit test.
# Using the AStudent class in AStudent_Class.py, write two (2) unit tests.
# The first unit test should test if the addGrade(..) method is working properly.
# The second unit test can test any other aspect of the program.
 
# Notes:
 
# Create a new Python file called AStudent_Class_addGrade_test.py. You can write both unit tests in this file.
# Use an assertEqual() method (or other as appropriate).
# Run your unit tests to check that no errors are reported.
# Show your output in the notebook (or save your output in a text file, e.g., inClass_unittests_Out.txt).
if __name__ == '__main__':
    log_file = 'log_file.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f)
       unittest.main(testRunner=runner)