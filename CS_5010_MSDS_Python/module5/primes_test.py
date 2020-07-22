# File: primes_test.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Unit testing / debugging code
#    - Testing  primes.py
#    - Testing  is_prime() method 
#       The print_next_prime() method calls is_prime() method so it is
#       important to test the is_prime() method thoroughly
#    - Testing print_next_primt() method, which is the primary method

# import unittest and the is_prime() method from the file primes.py
import unittest
#--------------------------------------------------#
# Uncomment ONE of the three options below         #
#--------------------------------------------------#
from primes import is_prime, print_next_prime
#from primes_fail1 import is_prime, print_next_prime
#from primes_fail2 import is_prime, print_next_prime
#--------------------------------------------------#

# Unit testing is_prime() method:

class PrimesTestCase(unittest.TestCase): # inherit from unittest.TestCase
    # The following are unit tests to test primes.py, in particular
    # testing is_prime() method
    
    def test_is_five_prime(self):
        # Is five (5) successfully determined to be a prime?
        # using assertTrue()
        self.assertTrue(is_prime(5)) # call method with 5, expect True
        
    def test_is_seven_prime(self):
        # Is seven (7) successfully determined to be a prime?
        # using assertEqual(), Asking, do actual and expected values match?
        self.assertEqual(is_prime(7), True) # ACTUAL value, EXPECTED value
        
    def test_is_four_non_prime(self):
        # Is four (4) correctly determined not to be prime?
        # Note, can add an optional message argument to the assert call
        
        # If this test had failed, the message would have been printed 
        # to the console, giving *additional information* to whoever ran 
        # the test
        self.assertFalse(is_prime(4), msg='Four is not prime!')
        
    def test_is_zero_not_prime(self):
        # Test edge cases ==> 0, 
        # since by definition, prime numbers must be *greater than one*
        self.assertFalse(is_prime(0))
        
    def test_negative_number(self):
        # Is a negative number correctly determined not to be prime?
        # Here, we decide to check all numbers from -1 .. -9
        
        # Calling a test method in a loop is perfectly valid
        # since multiple (related) calls to assert methods 
        # are allowed in a single test
        for index in range(-1, -10, -1): # range -1 to -9
            #self.assertFalse(is_prime(index))
            self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))
            # Adding the message will help us determine which of the tests failed
            
            
if __name__ == '__main__':
    unittest.main()
