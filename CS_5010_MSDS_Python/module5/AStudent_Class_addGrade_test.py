#Module 5 Exercise: Python Unit Testing
#Kip McCharen 
#cam7cu

import unittest
from .AStudent_Class import AStudent


class AddGradeTestCase(unittest.TestCase): # inherit from unittest.TestCase

    # Unit testing addGrade() method in pyScript21_B.py

    def test_add_student(self):
        st1 = AStudent("Jimmy", "3993", 4, grades=[100,90,80,70], courses=["Physics", "Chemistry", "Data Science"])
        self.assertGreater(len(st1.grades),0)
        self.assertLess(len(st1.courses), st1.numCourses)

    def test_insert_grade(self): 
        st1 = AStudent("Jimmy", "3993", 4, grades=[100,90,80,70], courses=["Physics", "Chemistry", "Data Science"])
        st1.addGrade(100)
        self.assertEqual(len(st1.grades),5)

    def test_enrollInCourse(self):
        st1 = AStudent("Jimmy", "3993", 4, grades=[100,90,80,70], courses=["Physics", "Chemistry"])
        st1.enrollInCourse("Data Science")
        self.assertIn("Data Science", st1.courses)

if __name__ == '__main__':
    log_file = 'log_file.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)