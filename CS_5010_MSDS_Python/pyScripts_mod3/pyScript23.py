# File: pyScript23.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Creating a derived class (Inheritance) - another example

## Employee - Manager example


# *** BASE CLASS *** #
class Employee:
   def __init__(self, name, payRate):  # constructor
      self.name = name
      self.payRate = payRate

   def __str__(self):  # to-string method
      return self.name + ", " + str(self.payRate)

   def pay(self, hoursWorked):  # pay method, returns gross pay of employee
      return self.payRate * hoursWorked

# =======================================================
# *** DERIVED CLASS *** #
# Manager inherits from Employee, so add base class as an argument to Manager
class Manager(Employee):
   def __init__(self, name, payRate, isSalaried):  # constructor
      Employee.__init__(self, name, payRate) # call base-class constructor
      self.salaried = isSalaried

   def __str__(self):  # to-string method
      retStr = Employee.__str__(self) # call base class to-string method
      retStr += " salaried: " + str(self.salaried) # concat. to that salaried
      return retStr

   def pay(self, hoursWorked): # pay method for manager
      if self.salaried:
         return self.payRate
      else:  # hourly
         return self.payRate * hoursWorked


# =======================================================
		 
e1 = Employee("John Jones", 10.00) # create an employee (e1)
print(e1)
print("Gross pay: " + str(e1.pay(40))) # Pay for 40 hours ($10 * 40hrs)
print("")

m1 = Manager("Jane Smith", 1200, True) # create a manager (m1)
print(m1)
print("Gross pay: " + str(m1.pay(40))) # Salaried, so just $1200
print("")

m2 = Manager("Jim Brown", 20.00, False) # create a manager (m2)
print(m2)
print("Gross pay: " + str(m2.pay(40))) # Pay for 40 hours ($20 * 40hrs)