'''
Exercise 4
Let's say we want to calculate the observation at percentile p:
    1. In ascending order, sort the given list of numbers, which we might call
    data.
    2. Calculate 
        i = frac{np}{100}+0.5,
    where n is the number of items in data.
    3. If i is an integer, data[i] is the number corresponding to percentile p.
    4. If i is not an integer, set k equal to the integral part of i and f
    equal to the fraction part of i. The number (1-f)*data[k] + f*data[k+1] is
    the nuber at percentile p.
    
Using this approach, write a program that will take a set of numbers in a file
and display the number that corresponds to a specific percentile supplied as an
input to the program.
'''

import re
import math

def read_numbers(filename):
    with open(filename) as file:
        numbers = [float(x) for x in file if re.search(r'\d+.?\d*', x)]
    return numbers

def percentile(N, percent, key=lambda x:x):
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    return key(N[int(f)])*(c-k) + key(N[int(c)])*(k-f)

numbers = read_numbers('mydata.txt')
numbers.sort()
print(percentile(numbers,float(input('Enter the percentile: '))))
