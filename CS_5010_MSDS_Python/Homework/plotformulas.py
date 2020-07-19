import matplotlib.pyplot as plt 
import numpy as np 
  
# Binary Search
x = np.linspace(-1, 5, 1000) 
y = (x * np.log(x)) + np.log(x)
# Sequential Search
x1 = np.linspace(-1, 5, 1000) 
y1 = x1

fig = plt.figure(figsize = (5, 5)) 

plt.plot(x, y, label='binary')  # Create the plot 
plt.plot(x1, y1, label='sequential') 
plt.grid(True)
plt.xlabel('items in list')
plt.ylabel('cost')
plt.show()  # Show the plot 