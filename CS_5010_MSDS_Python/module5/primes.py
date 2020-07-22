# File: primes.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Unit testing / debugging code
#    - Using primes example

#class Primes:
    
def is_prime(number):
    # Return True if *number* is prime
    if number < 0:  # Negative numbers are not prime
        return False

    if number in (0, 1):  # The numbers 0 and 1 are not prime
        return False

    # Above two if-statements could be replaced by following single if-statement
    # However, above two if-statements are kept for clarity for this example
    #if number <= 1:
    #    return False

    for element in range(2, number):  # Checking numbers 2 and higher
        if number % element == 0:
            return False
        
    return True  # Otherwise... return True, the number IS a prime

# ======================================================
def print_next_prime(number):
    # Print the closest prime number larger than *number*
    # Returns a single numerical value 
    index = number
    while True:
        index += 1
        if is_prime(index):
            return index

# Testing / Usage:
inputvalue = 3 # To change input, change it here 
res = print_next_prime(inputvalue)
print('Closest prime number to ' + str(inputvalue) + ' is: ' , end='')
print(res)