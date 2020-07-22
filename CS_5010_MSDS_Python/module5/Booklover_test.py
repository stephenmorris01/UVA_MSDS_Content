import unittest
from .Booklover import BookLover

class BookLover_unit_test(unittest.TestCase): # inherit from unittest.TestCase
    
    bl5 = BookLover("Marsha", "mdavis@gmail.com", numBooks=2, favGenre="SciFi", bookLst=[("Dune", 4), ("Game of Thrones", 5), ("Hunger Games", 2)])
    
    def test_create_booklover(self):
        bl1 = BookLover("Marsha", "mdavis@gmail.com", numBooks=2, favGenre="SciFi", bookLst=[("Dune", 4), ("Game of Thrones", 5), ("Hunger Games", 2)])
        bl2 = BookLover("Jim", "jdavis@gmail.com", numBooks=0, favGenre="", bookLst=[])
        bl3 = BookLover("", "jimmy")
        self.assertEqual(str(bl1), "Name: Marsha | Email: mdavis@gmail.com | " \
            + "numBooks: 2 | favGenre: SciFi")

    def test_print_booklover(self):
        str_bl1 = str(bl1)


    def addbook(self):

    # def hasread(self):

    # def numbooksread(self):

    # def favbooks(self):


if __name__ == '__main__':
    log_file = 'log_file.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f)
       unittest.main(testRunner=runner)