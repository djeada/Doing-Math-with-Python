'''
Exercise 2
Implement a statistics calulator that takes a list of numbers in the file
mydata.txt and then calculates and prints the mean, median, mode, variance, and
standard deviation using the functions we wrote earlier in this chapter.
'''

import re

def read_numbers(filename):
    with open(filename) as file:
        numbers = [float(x) for x in file if re.search(r'\d+.?\d*', x)]
    return numbers

def calculate_mean(x):
    return sum(x)/len(x)

def calculate_median(x):
    sortedLst = sorted(x)
    N = len(x)
    
    if N % 2:
        return x[int((N-1)/2)]
    else:
        return(x[int((N-1)/2)] + x[int((N-1)/2)+1])/2

def calculate_mode(x):
    return max(set(x), key=x.count)
    
def find_differences(x):
    mean = calculate_mean(x)
    return [xi - mean for xi in x]

def calculate_variance(x):
    diff = find_differences(x)
    squared_diff = [xi**2 for xi in diff]
    sum_squared_diff = sum(squared_diff)    
    return sum_squared_diff/len(x)

numbers = read_numbers('mydata.txt')
print('Mean: ', calculate_mean(numbers))
print('Median: ', calculate_median(numbers))
print('Mode: ', calculate_mode(numbers))
print('Variance: ', calculate_variance(numbers))
