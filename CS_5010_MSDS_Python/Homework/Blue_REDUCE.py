from functools import reduce

def startup():
   """Per submission instructions. Ensure at the top of your Python file you include:"""
   print(r"##In-Class Assignment 3: Map, Filter, Reduce)##",'\n')
   print(r"##Reduce examples##")
   blue_reduce_team = {'alz9cb': 'Andrew Zazzera','maw3as': 'Annie Williams','bd6fr': 'Buckley Dowdle','dv6bq': 'David Vann','hbf3k': 'Hannah Frederick','js8hh': 'Joon Soh','jm8ux': 'Jordan Machita','kn3gs': 'Krissy North','mo2cr': "Maureen O'Shea",'na5zn': 'Nikki Aaron','fwb4cx': 'Will Blickle'}

   print("Team: ",[b for b in blue_reduce_team.values()], '\n')

####IGNORE ME NOTHING TO SEE HERE######
#not required, but extra tidbits
def add_next_val(x, _): 
   """Given an unused iterable as second value, instead of adding to an accumulating list, only update the x values"""
   return [x[1],x[0]+x[1]]

def print_funct_info_and_output(func):
   """Decorator to print function details before running it, then print its outcome."""
   def wrapper(*args, **kwargs):
      print('\n')
      print("##",func.__name__.upper(),"##:   ", str(func.__doc__).strip())
      print("Inputs: ", args)
      print("Result: ", func(*args, **kwargs))
   wrapper.__name__ = func.__name__
   wrapper.__doc__ = func.__doc__
   return wrapper

def accept_int(val):
   """Only accept an integer, otherwise say no. """
   if isinstance(val, int):
      return val
   else:
      raise TypeError
#######################################

#Example A: Concatenate strings with a space
@print_funct_info_and_output
def concat_strings(list_of_strings, concatenator=" "):
   """If you're tired of ' '.join() why not try concat_strings? Reduce adds concatenator in-between each value."""
   return reduce(lambda x, y: x + concatenator + y, list_of_strings)

#Example B: Apply factorial function to input number in one line
@print_funct_info_and_output
def factorial(n):
   """Calculate factorial value for given int. Reduce cumulatively generates the factorial value."""
   return reduce(lambda x, y: x*y, range(1,accept_int(n)+1))

#Example C: 
@print_funct_info_and_output
def fibonacci(nth_value):
   """Produce the nth value of the Fibonacci sequence. Reduce does not accumulate values, only finds nth value requested. """
#  output pair       function to use  iterator (value not used)    starting pair
   reduced_fib = reduce(add_next_val, range(accept_int(nth_value)), [0,1])
   return reduced_fib[0]

if __name__ == "__main__":
   startup()
   fibdoc = str(fibonacci.__doc__).split(" ")
   concat_strings(fibdoc, "|||||")
   factorial(5)
   fibonacci(10)