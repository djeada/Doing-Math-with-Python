'''
Exercise 2
According to the la w of large numbers, the average value of results over
multiple trials approaches the expected value as the number of trials
increases. Your challenge in this task is to verify the law when rolling a six-
sided die for the following number of trials: 100, 1000, 1,0000, 10,000, 
100,000, 500,000.
'''

import random

def average(x):
    rolls = [random.randint(1,6) for i in range(x)]
    return sum(rolls)/x

print('Expected value: 3.5')

numbers = [10, 100, 1000, 10000, 100000, 500000]

for x in numbers:
    print('Trials: {0} Trial average {1:.2f}'.format(x, average(x)))
