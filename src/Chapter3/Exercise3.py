'''
Exercise 3
For this challenge, download the following data as a CSV file from 
http://quandl.com/WORLDBANK/US_SP_POP_TOTL/: the total population of the 
United States at the end of each year for the years 1960 to 2012. Then,
calculate the mean, median, variance, and standard deviation of the 
difference in population over the years and create a graph showing these 
differences.

'''

import matplotlib.pyplot as plt
from collections import Counter
import csv
import re
 
def read_data(filename):
    with open(filename) as file:
        numbers = [(int(x[0]), int(x[1])) for x in csv.reader(file,delimiter=';') if re.search(r'\d+.?\d*', x[0]) and re.search(r'\d+.?\d*', x[1])]
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

def plot(x,y):
    plt.plot(x,y, marker='+')
    plt.xlabel('Year')
    plt.ylabel('Budget')
    plt.title('Budget vs Year')
    plt.show()

numbers = read_data('mydata.csv')
difference = [numbers[i][1]-numbers[i-1][1] for i in range(1, len(numbers))]
budget = [x[1] for x in numbers]
year = [x[0] for x in numbers]

plot(year, budget)

print('Mean: ', calculate_mean(difference))
print('Median: ', calculate_median(difference))
print('Mode: ', calculate_mode(difference))
print('Variance: ', calculate_variance(difference))
