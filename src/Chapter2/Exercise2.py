'''
Exercise 2
Here's  program that calculates the value of y for six different values of x:
    Quadratic function calculator
    '
    # Assume values of x
    
    x_values = [-1,1,2,3,4,5]
    
    for x in x_values:
        # Calculate the value of quadratic function
        y = x**2 + x*2 +1
        print('x={0} y{1}'.format(x,y))
    ' 
Your programming challenge is to enhance this program to create a graph of the
function. Try using at least 10 values for x instead of the 6 above. Calculate
the corresponding y values using the function and then create a graph using
these two sets of values.
'''

import random
import numpy
import matplotlib.pyplot as plt
import scipy.interpolate as inter

def plot(x,y):
    plt.scatter(x,y, marker='+')
    f = inter.interp1d(x, y,fill_value="extrapolate",kind='quadratic')
    plt.plot(numpy.linspace(0,100),f(numpy.linspace(0,100)))
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Quadratic Function')

def calc():
    x_data = [random.randint(0,100) for x in range(10)]
    y_data = [x**2 + x*2 +1 for x in x_data]
    plot(x_data,y_data)

calc()
plt.show()
